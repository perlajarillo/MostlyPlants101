from flask import Flask, render_template, url_for, request, redirect, flash
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Ingredient, Bowl, Bowl_Ingredient, User
import random
import string
from flask import session as login_session
import httplib2
import json
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response
import requests
import config
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Bowls 101"


engine = create_engine('sqlite:///bowls101.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Defining decorated view for authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash("Please login into your account and try again")
            return redirect('/login')
    return decorated_function


# Defining decorated view for authorization
def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = getUserID(login_session['email'])
        bowl_user_id = getBowlUserID(kwargs['bowl_id'])
        if user_id == bowl_user_id:
            return f(*args, **kwargs)
        else:
            return render_template("no-authorized.html")
    return decorated_function


# Connect using Google credentials
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    t = credentials.access_token
    url = 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % t
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_a_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_a_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('User is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    # set session variables with the user info
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    print(login_session['username'])
    # See if the user exist, if it does not create it
    uid = getUserID(data['email'])
    if not uid:
        uid = createUser(login_session)
    login_session['user_id'] = uid
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;'
    output += '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print("done!")
    return output


# Disconnect from Google
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is %s', access_token)
    print('User name is: ')
    print(login_session['username'])
    a_token = login_session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % a_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Performs logout
@app.route('/disconnect')
def disconnect():
    gdisconnect()
    flash("You have successfully been logged out.")
    return redirect(url_for('showIndex'))


# JSON APIs dislay Bowls created
@app.route('/bowls/JSON')
def bowlsJSON():
    if 'username' not in login_session:
        return redirect('/login')
    bowls_ingredients = session.query(Bowl_Ingredient).all()
    return jsonify(BowlsIngredients=[i.serialize for i in bowls_ingredients])


# Route for index
@app.route('/')
@app.route('/bowls101')
def showIndex():
    return render_template("index.html")


# Create a new bowl
@app.route('/makebowl', methods=['GET', 'POST'])
@login_required
def makebowl():
    user_id = getUserID(login_session['email'])
    if request.method == 'POST':
        f = request.form
        newBowl = Bowl(
            name=f['bowl_name'], user_id=user_id, type=f['type'])
        session.add(newBowl)
        session.commit()
        bowl_id = newBowl.id
        for key in f.keys():
            for value in f.getlist(key):
                if ((key != 'bowl_name') and (key != 'type')):
                    newIngredientBowl = Bowl_Ingredient(
                        bowl_id=bowl_id, ingredient_id=value)
                    session.add(newIngredientBowl)
                    session.commit()
        flash('%s Successfully Created' % newBowl.name)
        return redirect(url_for('userHome'))
    else:
        ingredients = session.query(Ingredient).all()
        return render_template("makeBowl.html", ingredients=ingredients)


# Edit a bowl
@app.route('/editbowl/<int:bowl_id>', methods=['GET', 'POST'])
@login_required
@auth_required
def editbowl(bowl_id):
    bData = session.query(Bowl).filter_by(id=bowl_id).one()
    bowls_ingredients = session.query(
        Bowl_Ingredient).filter_by(bowl_id=bowl_id).all()
    if request.method == 'POST':
        f = request.form
        bData.name = f['bowl_name']
        bData.type = f['type']
        session.add(bData)
        session.commit()
        # Delete previous ingredients so we can add the new selected, if any
        query = "DELETE FROM Bowl_Ingredient WHERE bowl_id=:bowl_id"
        session.execute(query, {"bowl_id": bowl_id})
        session.commit()
        for key in f.keys():
            for value in f.getlist(key):
                if ((key != 'bowl_name') and (key != 'type')):
                    newIngredientBowl = Bowl_Ingredient(
                        bowl_id=bowl_id, ingredient_id=value)
                    session.add(newIngredientBowl)
                    session.commit()
        flash('%s Successfully Updated' % bData.name)
        return redirect(url_for('userHome'))
    else:
        # Creating a list that contains the bowl's ingredients ids
        b = []
        for i in bowls_ingredients:
            b.append(i.ingredient_id)
        # Performing queries to get ingredients by category
        i = session.query(Ingredient).all()
        return render_template("editBowl.html", ingr=i, bowlsIn=b, bData=bData)


# Delete a bowl
@app.route('/deletebowl/<int:bowl_id>', methods=['GET', 'POST'])
@login_required
@auth_required
def deletebowl(bowl_id):
    bowlData = session.query(Bowl).filter_by(id=bowl_id).one()
    if request.method == 'POST':
        # Bowl's ingredients will be deleted in cascade, as defined in model
        session.delete(bowlData)
        session.commit()
        flash('%s Successfully Deleted' % bowlData.name)
        return redirect(url_for('userHome'))
    else:
        return render_template("deleteBowl.html", bowlData=bowlData)


# Route for user home, this is the page the user will be redirected after login
@app.route('/bowls101/userhome')
@login_required
def userHome():
    # Getting user id
    user_id = getUserID(login_session['email'])
    # Getting the bowls created by the user, if any
    usersBowls = session.query(Bowl).filter_by(user_id=user_id).all()
    return render_template("userHome.html", usersBowls=usersBowls)


# Shows the login page to start authentication
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    id = config.client_id
    return render_template('login.html', STATE=state, client_id=id)


# User Helper Functions

# Create a user
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# Get user data
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# Get user id
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except NoResultFound:
        return None


# Get bowl user id
def getBowlUserID(bowl_id):
    try:
        bowl = session.query(Bowl).filter_by(id=bowl_id).one()
        return bowl.user_id
    except NoResultFound:
        return None


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
