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
# 1. Spinach, lettuce, arugula, spring greens
greens = Preparation(preparation="Remove any damaged outer leaves. Cleaned them with cold water to remove any dirt on the leaves. Chop big leaves as you desired. Remove the excess of water and place the greens in a salad bowl.")
session.add(greens)
session.commit()

# 2. Kale, collard greens
specialGreens = Preparation(
    preparation="Remove any damaged outer leaves. Cleaned them with cold water to remove any dirt on the leaves. Fold the leaves in half with the stem at the crease, and cut or tear the stem off. Remove the excess of water and place the greens in a salad bowl. Optional for a smoother flavor: Whisk some olive oil and salt. Massage until the leaves starts to soften and wilt, 2 to 3 minutes.")
session.add(specialGreens)
session.commit()

# 3. Beans, chickpeas, garbanzo beans
beans = Preparation(
    preparation="Prepare in advance: Sort and rinse under running water. Quick preparation method: Boil into 8 cups of water for around 2 minutes. Remove from heat; cover with a lid and let stand 1 hour. Drain water and rinse. Cooking after preparing:  Add 8 cups of salted water and bring to boil. Reduce heat and simmer with partial cover for 2 to 3 hours until tender. Stir occasionally.")
session.add(beans)
session.commit()

# 4. for raw vegetables
vegetables = Preparation(preparation="Chop into small pieces")
session.add(vegetables)
session.commit()

# 5. for herbs
herbs = Preparation(preparation="Cut into very small pieces")
session.add(vegetables)
session.commit()

# 6. for dressing
dressing = Preparation(
    preparation="Gradually drizzle along the side of the bowl.")
session.add(dressing)
session.commit()

# 7. for no cooking requirement ingredients like almonds, cheese,
nocooking = Preparation(
    preparation="Add to the bowl the rest of the ingredients.")
session.add(nocooking)
session.commit()

# 8. for vegetables or soft beans that can't be ate raw
steam = Preparation(
    preparation="Add in boiling water, turn the heat off and leave rest for 5 minutes.")
session.add(steam)
session.commit()

# 9. Grilled. For vegetables that are better grilled than raw or steam
grilled = Preparation(
    preparation="Chop in small pieces and grilled in a pan.")
session.add(grilled)
session.commit()


# bases
#  (name, origin, phase, calories, carbs, fat, protein, portionSize, preparation)
# portions are in cups, fat, carbs and protein in grams (g)
ingredient1 = Ingredient(name="Spinach", origin="vegetable", phase="base",
                         calories=7.0, carbs=1.1, fat=0.1, protein=0.9, portionSize=1, preparation=1)
session.add(ingredient1)
session.commit()

ingredient2 = Ingredient(name="Lettuce", origin="vegetable", phase="base",
                         calories=5, carbs=1.0, fat=0.1, protein=0.5, portionSize=1, preparation=1)
session.add(ingredient2)
session.commit()

ingredient3 = Ingredient(name="Kale", origin="vegetable", phase="base",
                         calories=33,  carbs=5.9, fat=0.6, protein=2.9, portionSize=1, preparation=2)
session.add(ingredient3)
session.commit()

ingredient4 = Ingredient(name="Arugula", origin="vegetable", phase="base",
                         calories=5, carbs=0.7, fat=0.1, protein=0.5, portionSize=1, preparation=1)
session.add(ingredient4)
session.commit()


# vegetables and fruits

ingredient5 = Ingredient(name="Broccoli", origin="vegetable", phase="v&f",
                         calories=15, carbs=3, fat=0.2, protein=1.3, portionSize=0.5, preparation=4)
session.add(ingredient5)
session.commit()

ingredient6 = Ingredient(name="Carrots", origin="vegetable", phase="v&f",
                         calories=26, carbs=6.1, fat=0.2, protein=0.6, portionSize=0.5, preparation=4)
session.add(ingredient6)
session.commit()

ingredient7 = Ingredient(name="Peas", origin="vegetable", phase="v&f",
                         calories=99, carbs=17, fat=0.7, protein=7.1, portionSize=0.5, preparation=8)
session.add(ingredient7)
session.commit()

ingredient8 = Ingredient(name="Celery", origin="vegetable", phase="v&f",
                         calories=8, carbs=1.5, fat=0.1, protein=0.3, portionSize=0.5, preparation=4)
session.add(ingredient8)
session.commit()

ingredient9 = Ingredient(name="Corn", origin="vegetable", phase="v&f", calories=53,
                         carbs=10.5, fat=0.8, protein=2.3, portionSize=0.5, preparation=8)
session.add(ingredient9)
session.commit()

ingredient10 = Ingredient(name="Asparagus", origin="vegetable", phase="v&f",
                          calories=33, carbs=4.5, fat=1.3, protein=2.5, portionSize=0.5, preparation=9)
session.add(ingredient10)
session.commit()

ingredient11 = Ingredient(name="Grapes", origin="fruit", phase="v&f", calories=31,
                          carbs=7.9, fat=0.2, protein=0.3, portionSize=0.5, preparation=7)
session.add(ingredient11)
session.commit()

ingredient12 = Ingredient(name="Strawberry", origin="fruit", phase="v&f",
                          calories=24, carbs=5.8, fat=0.2, protein=0.5, portionSize=0.5, preparation=7)
session.add(ingredient12)
session.commit()

ingredient13 = Ingredient(name="Dried Crawnberry", origin="fruit", phase="v&f",
                          calories=92, carbs=24.7, fat=0.4, protein=0, portionSize=0.25, preparation=7)
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

ingredient19 = Ingredient(name="Peanuts", origin="nut", phase="texture",
                          calories=160, carbs=4.6, fat=14, protein=7, portionSize=0.25, preparation=7)
session.add(ingredient19)
session.commit()

ingredient20 = Ingredient(name="Almonds", origin="nut", phase="texture", calories=207,
                          carbs=7.7, fat=17.8, protein=7.6, portionSize=0.25, preparation=7)
session.add(ingredient20)
session.commit()

ingredient21 = Ingredient(name="Pecans", origin="nut", phase="texture", calories=188,
                          carbs=3.8, fat=19.6, protein=2.5, portionSize=0.25, preparation=7)
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


# Saltiness

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
