# Mostly Plants 101

Author: Perla Jarillo

## About

Mostly Plants 101 promotes healthy alimentation. The first part of this app is the module Bowls 101 that teach the basics to make balanced bowls in 8 steps.

## Dependencies and resources:

In order to run this app it is important for you to have the next dependencies and resources set in your computer.

### Linux machine.

If you don't want to install Linux in your computer you can install VirtualBox and Vagrant. Also, a Vagrant file is provided in this repository (see instructions bellow to install).

- VirtualBox. Download [here](https://www.virtualbox.org/wiki/Downloads)
- Clic [here](https://www.virtualbox.org/manual/ch02.html#installation_windows) to see the installation instructions for Windows
- Or [here](https://www.virtualbox.org/manual/ch02.html#installation-mac) if you have Mac OS X Hosts

- Vagrant. You can get it [here](https://www.vagrantup.com/downloads.html)

### Python 2.7 or superior.

As you will be working with a VM you may have already Python installed. But if you don't:

    a. Windows and Mac: Install it from python.org: https://www.python.org/downloads/
    b. Mac (with Homebrew): In the terminal, run brew install python3
    c. Debian/Ubuntu/Mint: In the terminal, run sudo apt-get install python3

### Libraries

Once you have Vagrant installed, you will need to install [sqlalchemy](https://www.sqlalchemy.org/), [httplib2](https://pypi.org/project/httplib2/), [oauth2client](https://oauth2client.readthedocs.io/en/latest/) and [flask_httpauth](https://flask-httpauth.readthedocs.io/en/latest/). Continue reading for more information.

## Installation

The first step is to clone this repository in your local machine and then, open a terminal and cd into the project directory. Then follow this steps:

### 1. run the command `vagrant up`

This will download and install vagrant if you are using a Virtual Machine. If you are under a Linux SO this will not be necessary.

### 2. run the command `vagrant ssh`

This will perform the log in to the installed Linux VM. After the log in is completed, type `cd /vagrant` in your terminal.

### 3. Install the libraries:

- httplib2. It is HTTP client library
  `sudo pip install httplib2`

- oauth2client. Makes it easy to interact with OAuth2-protected resources
  `sudo pip install oauth2client`

- Flask-HTTPAuth. It is a simple extension that simplifies the use of HTTP authentication with Flask routes.
  `sudo pip install flask_httpauth`

- SQLAlchemy. It is the Python SQL toolkit and Object Relational Mapper.
  `sudo pip install sqlalchemy`

### 4. Create the database:

The repository contains a file named model.py that contains the database model. From your terminal type:

`python model.py`

### 5. Populate the database

The app requires information that has been saved for your convenience in populate_bowlsdb.py.
To populate the database type from your terminal:

`python populate_bowlsdb.py`

### 6. Create yor Google keys

Mostly Plants 101 uses OAuth 2.0 to Access Google APIs. If you don't have a key or need more information visit [Google Developers Console ](https://console.developers.google.com/).Once you have your key generated download it and save it inside the repository under the name **client_secrets.json**. That file has not been uploaded in this repository for safety.

### 7. Configure the environment

You will also need to create a file named config.py and set client_id variable with your google client id as follows:

`client_id="your-clientid-goes-here"`

Also, you will need to set the db_credentials_string with the database URL to connect with your database server. 

`db_credentials_string = "your-database-URL"`

If you want to know more about database URL for engine configuration see  [Engine Configuration — SQLAlchemy 1.3 Documentation](https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql).

### 8. Start the application

Once you have all the dependencies and database ready, start the application by typing:

`python bowls101.py`

## How to use Mostly Plants 101

To start creating bowls, log in into the app using your Google credentials. You will be redirected after some seconds to your principal page, where you can start interacting with the app: create, modify, delete a bowl. The bowls has been separated by categories: vegan, vegetarian and contains meat.

## Contributor Guidelines

If you're looking for a place to start contributing code, check out the list of issues that are labeled as **help wanted**. The process to contribute in this repository is:

1. Comment on the issue that you're going to be working on it. This will help me to avoid work duplication.
2. Fork the repository.
3. Start coding.
4. Make a PR when you are ready.
5. I will review your contribution and ask for any necessary changes and/or approve and merge.

## Development Notes

Mostly Plants 101 has been powered by Bootstrap. The styles are inspired in [this](https://startbootstrap.com/template-overviews/agency) template.

## Credits

Photos by Anna Pelzer, Dan Gold, Edgar Castrejon, Ella Olsson, Jez Timms,
Kai Pilger, Mariana Medvedeva, Milada Vigerova, rawpixel, Tom Hermans and Jose Aragones on
[Unsplash](https://unsplash.com/)
