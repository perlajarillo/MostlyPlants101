from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Ingredient, Base, Preparation
import config

db_string = config.db_credentials_string
engine = create_engine(db_string)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
# Preparations
# Spinach, lettuce, arugula, spring greens
greens = Preparation(preparation="Remove any damaged outer leaves. Cleaned them with cold water to remove any dirt on the leaves. Chop big leaves as you desired. Remove the excess of water and place the greens in a salad bowl.")
session.add(greens)
session.commit()

# Kale, collard greens
specialGreens = Preparation(
    preparation="Remove any damaged outer leaves. Cleaned them with cold water to remove any dirt on the leaves. Fold the leaves in half with the stem at the crease, and cut or tear the stem off. Remove the excess of water and place the greens in a salad bowl. Optional for a smoother flavor: Whisk some olive oil and salt. Massage until the leaves starts to soften and wilt, 2 to 3 minutes.")
session.add(specialGreens)
session.commit()

# Beans, chickpeas, garbanzo beans
beans = Preparation(
    preparation="Prepare in advance: Sort and rinse under running water. Quick preparation method: Boil into 8 cups of water for around 2 minutes. Remove from heat; cover with a lid and let stand 1 hour. Drain water and rinse. Cooking after preparing:  Add 8 cups of salted water and bring to boil. Reduce heat and simmer with partial cover for 2 to 3 hours until tender. Stir occasionally.")
session.add(beans)
session.commit()

# for vegetables
vegetables = Preparation(preparation="Chop into small pieces")
session.add(vegetables)
session.commit()

# for herbs
herbs = Preparation(preparation="Cut into very small pieces")
session.add(vegetables)
session.commit()

# for dressing
dressing = Preparation(
    preparation="Gradually drizzle along the side of the bowl.")
session.add(dressing)
session.commit()

# for no cooking requirement ingredients like almonds, cheese,
nocooking = Preparation(
    preparation="Add to the bowl the rest of the ingredients.")
session.add(dressing)
session.commit()

# bases
ingredient1 = Ingredient(name="Spinach", origin="vegetable", phase="base")
session.add(ingredient1)
session.commit()

ingredient2 = Ingredient(name="Lettuce", origin="vegetable", phase="base")
session.add(ingredient2)
session.commit()

ingredient3 = Ingredient(name="Kale", origin="vegetable", phase="base")
session.add(ingredient3)
session.commit()

ingredient4 = Ingredient(name="Arugula", origin="vegetable", phase="base")
session.add(ingredient4)
session.commit()


# vegetables and fruits

ingredient5 = Ingredient(name="Broccoli", origin="vegetable", phase="v&f")
session.add(ingredient5)
session.commit()

ingredient6 = Ingredient(name="Carrots", origin="vegetable", phase="v&f")
session.add(ingredient6)
session.commit()

ingredient7 = Ingredient(name="Peas", origin="vegetable", phase="v&f")
session.add(ingredient7)
session.commit()

ingredient8 = Ingredient(name="Celery", origin="vegetable", phase="v&f")
session.add(ingredient8)
session.commit()

ingredient9 = Ingredient(name="Corn", origin="vegetable", phase="v&f")
session.add(ingredient9)
session.commit()

ingredient10 = Ingredient(name="Asparagus", origin="vegetable", phase="v&f")
session.add(ingredient10)
session.commit()

ingredient11 = Ingredient(name="Grapes", origin="fruit", phase="v&f")
session.add(ingredient11)
session.commit()

ingredient12 = Ingredient(name="Strawberry", origin="fruit", phase="v&f")
session.add(ingredient12)
session.commit()

ingredient13 = Ingredient(name="Dried Crawnberry", origin="fruit", phase="v&f")
session.add(ingredient13)
session.commit()


# Texture

ingredient14 = Ingredient(name="Quinoa", origin="vegetable", phase="texture")
session.add(ingredient14)
session.commit()

ingredient15 = Ingredient(name="Barley", origin="grain", phase="texture")
session.add(ingredient15)
session.commit()

ingredient16 = Ingredient(name="Couscous", origin="grain", phase="texture")
session.add(ingredient16)
session.commit()

ingredient17 = Ingredient(name="Pasta", origin="grain", phase="texture")
session.add(ingredient17)
session.commit()

ingredient18 = Ingredient(name="Rice", origin="grain", phase="texture")
session.add(ingredient18)
session.commit()

ingredient19 = Ingredient(name="Peanuts", origin="nut", phase="texture")
session.add(ingredient19)
session.commit()

ingredient20 = Ingredient(name="Almonds", origin="nut", phase="texture")
session.add(ingredient20)
session.commit()

ingredient21 = Ingredient(name="Pecans", origin="nut", phase="texture")
session.add(ingredient21)
session.commit()

# Protein

ingredient22 = Ingredient(name="Hard boiled egg",
                          origin="animal", phase="protein")
session.add(ingredient22)
session.commit()

ingredient23 = Ingredient(name="Turkey", origin="animal", phase="protein")
session.add(ingredient23)
session.commit()

ingredient24 = Ingredient(name="Beans", origin="grain", phase="protein")
session.add(ingredient24)
session.commit()

ingredient25 = Ingredient(name="Chickpeas", origin="grain", phase="protein")
session.add(ingredient25)
session.commit()

ingredient26 = Ingredient(name="Lentils", origin="grain", phase="protein")
session.add(ingredient26)
session.commit()

ingredient27 = Ingredient(
    name="Grilled meat", origin="animal", phase="protein")
session.add(ingredient27)
session.commit()

ingredient28 = Ingredient(name="Roasted chicken",
                          origin="animal", phase="protein")
session.add(ingredient28)
session.commit()

ingredient29 = Ingredient(name="Smoked fish", origin="animal", phase="protein")
session.add(ingredient29)
session.commit()


# Satiness

ingredient30 = Ingredient(
    name="Feta cheese", origin="animal", phase="saltiness")
session.add(ingredient30)
session.commit()

ingredient31 = Ingredient(
    name="Fresh cheese", origin="animal", phase="saltiness")
session.add(ingredient31)
session.commit()

ingredient32 = Ingredient(name="Olives", origin="vegetable", phase="saltiness")
session.add(ingredient32)
session.commit()

ingredient33 = Ingredient(name="Capers", origin="vegetable", phase="saltiness")
session.add(ingredient33)
session.commit()


# Herb

ingredient34 = Ingredient(name="Chives", origin="vegetable", phase="smoot")
session.add(ingredient34)
session.commit()

ingredient35 = Ingredient(name="Basil", origin="vegetable", phase="smoot")
session.add(ingredient35)
session.commit()

ingredient36 = Ingredient(name="Cilantro", origin="vegetable", phase="smoot")
session.add(ingredient36)
session.commit()

ingredient37 = Ingredient(name="Parsley", origin="vegetable", phase="smoot")
session.add(ingredient37)
session.commit()


# Sharpen

ingredient38 = Ingredient(name="Cucumber", origin="vegetable", phase="sharpen")
session.add(ingredient38)
session.commit()

ingredient39 = Ingredient(name="Pepeers", origin="vegetable", phase="sharpen")
session.add(ingredient39)
session.commit()


ingredient40 = Ingredient(name="Pickles", origin="vegetable", phase="sharpen")
session.add(ingredient40)
session.commit()


# Dreesing


ingredient41 = Ingredient(
    name="Vinaigrette", origin="vegetable", phase="dressing")
session.add(ingredient41)
session.commit()

ingredient42 = Ingredient(name="Yogurt dressing",
                          origin="animal", phase="dressing")
session.add(ingredient42)
session.commit()

print "Ingredients added"
