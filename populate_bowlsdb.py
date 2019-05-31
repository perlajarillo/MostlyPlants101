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
session.add(herbs)
session.commit()


# 6. for no cooking requirement ingredients like almonds, cheese,
nocooking = Preparation(
    preparation="Measure and add to the bowl.")
session.add(nocooking)
session.commit()

# 7. for vegetables or soft beans that can't be ate raw
steam = Preparation(
    preparation="Add in boiling water, turn the heat off and leave rest for 5 minutes.")
session.add(steam)
session.commit()

# 8. Grilled. For vegetables that are better grilled than raw or steam
grilled = Preparation(
    preparation="Chop in small pieces and grill them in a pan.")
session.add(grilled)
session.commit()

# 9. Grilled meat. For fish, beef, pork or chicken
grilledMeat = Preparation(
    preparation="Prepare a grill for high heat and place a wire rack on one side (you can also use a pan instead a grill). While you are waiting for the grill (pan) to be ready, poor some seasoning of your preference over the meat. Once the grill is ready, place it in the rack and grill until marks appear around the edges. Flip to grill the other side and repeat the procedure. When it's well cook chop in pieces.")
session.add(grilledMeat)
session.commit()

# 10. Quinoa
quinoa = Preparation(preparation="If you have cooked quinoa add it to the bowl. If you have uncooked quinoa: Rinse and drain quinoa in cold water before cooking. For every cup of quinoa add 2 cups of water in a saucepan and bring to a boil. Reduce to a simmer, cover and cook until all water is absorbed, for about 10 to 15 minutes. Let it cool and use the suggested portion to make your bowl.")
session.add(quinoa)
session.commit()

# 11. Hard boiled eggs
eggs = Preparation(
    preparation="Place eggs in saucepan large enough to hold them in single layer. Add cold water to cover eggs by 1 inch. Bring to boil. Remove from the burner and cover pan. Let the eggs stand in hot water for 12 minutes. Drain and cool completely under cold running water. Peel and chop in cubes or slides.")
session.add(eggs)
session.commit()

# 12. Lentils
lentils = Preparation(
    preparation="Rinse lentils with fresh water. Cook on a stovetop, using 3 cups of water for every cup of lentils. Bring to a boil, cover tightly, reduce heat and simmer until they are tender (15-20 minutes). Remove the excess of liquid. Messure the suggested portion and add to the bowl.")
session.add(lentils)
session.commit()

# 13. Barley
barley = Preparation(
    preparation="Rinse barley with fresh water. Bring to boil using 2 cups of water for every cup of barley. Reduce heat to a simmer. Cook, covered, until tender and most of the liquid has been absorbed (40-50 minutes). Messure the suggested portion and add to the bowl.")
session.add(barley)
session.commit()

# 14. Couscous
couscous = Preparation(preparation="If you have cooked couscous add it to the bowl. If you have uncooked couscous: Rinse and drain in cold water before cooking. For every cup of couscous add 1 1/2 cups of water in a saucepan and bring to a boil. Reduce to a simmer, cover and cook until all water is absorbed, for about 5 to 10 minutes. Let it cool and use the suggested portion to make your bowl.")
session.add(couscous)
session.commit()

# 15. Pasta
pasta = Preparation(preparation="In a large pot bring 4 quarts of water to rolling boil. Add content of pasta package to boiling water. Boil for the time suggested in the package, usually around 10 minutes. Remove from heat and drain well. Let it cool and use the suggested portion to make your bowl.")
session.add(pasta)
session.commit()

# 16. Rice
rice = Preparation(preparation="Pour water into a large pot, use 1 3/4 cups of water per every cup of rice. Add rice to boiling water. Stir once to separate any clumps. Cover the pot and let rice simmer for about 18 minutes. Remove from heat and allow the rice to steam for another 5 minutes. Let it cool and use the suggested portion to make your bowl.")
session.add(rice)
session.commit()

# 17. for tofu, cheese, avocado
tofu = Preparation(preparation="Chop into cubes.")
session.add(tofu)
session.commit()

# 18. for dressing (always keep at the buttom)
dressing = Preparation(
    preparation="Gradually drizzle along the side of the bowl over the other ingredients.")
session.add(dressing)
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
                         calories=50, carbs=8.5, fat=0.35, protein=3.55, portionSize=0.25, preparation=7)
session.add(ingredient7)
session.commit()

ingredient8 = Ingredient(name="Celery", origin="vegetable", phase="v&f",
                         calories=8, carbs=1.5, fat=0.1, protein=0.3, portionSize=0.5, preparation=4)
session.add(ingredient8)
session.commit()

ingredient9 = Ingredient(name="Corn", origin="vegetable", phase="v&f", calories=53,
                         carbs=5.25, fat=0.4, protein=1.15, portionSize=0.25, preparation=7)
session.add(ingredient9)
session.commit()

ingredient10 = Ingredient(name="Asparagus", origin="vegetable", phase="v&f",
                          calories=33, carbs=4.5, fat=1.3, protein=2.5, portionSize=0.5, preparation=8)
session.add(ingredient10)
session.commit()

ingredient11 = Ingredient(name="Grapes", origin="fruit", phase="v&f", calories=31,
                          carbs=3.95, fat=0.1, protein=0.15, portionSize=0.25, preparation=6)
session.add(ingredient11)
session.commit()

ingredient12 = Ingredient(name="Strawberry", origin="fruit", phase="v&f",
                          calories=12, carbs=2.9, fat=0.1, protein=0.25, portionSize=0.25, preparation=4)
session.add(ingredient12)
session.commit()

ingredient13 = Ingredient(name="Dried Cranberries", origin="fruit", phase="v&f",
                          calories=92, carbs=24.7, fat=0.4, protein=0, portionSize=0.25, preparation=6)
session.add(ingredient13)
session.commit()


# Texture

ingredient14 = Ingredient(name="Quinoa", origin="vegetable", phase="texture",
                          calories=160, carbs=30, fat=2.5, protein=6, portionSize=0.25, preparation=10)
session.add(ingredient14)
session.commit()

ingredient15 = Ingredient(name="Barley", origin="grain", phase="texture",
                          calories=162.5, carbs=33.75, fat=1.05, protein=5.75, portionSize=0.25, preparation=13)
session.add(ingredient15)
session.commit()

ingredient16 = Ingredient(name="Couscous", origin="grain", phase="texture", calories=44,
                          carbs=9, fat=0.1, protein=1.5, portionSize=0.25, preparation=14)
session.add(ingredient16)
session.commit()

ingredient17 = Ingredient(name="Pasta", origin="grain", phase="texture", calories=140,
                          carbs=29.33, fat=0.3, protein=4.6, portionSize=0.5, preparation=15)
session.add(ingredient17)
session.commit()

ingredient18 = Ingredient(name="Rice", origin="grain", phase="texture", calories=103,
                          carbs=22.5, fat=0.2, protein=2.15, portionSize=0.5, preparation=16)
session.add(ingredient18)
session.commit()

ingredient19 = Ingredient(name="Peanuts", origin="nut", phase="texture",
                          calories=160, carbs=4.6, fat=14, protein=7, portionSize=0.25, preparation=6)
session.add(ingredient19)
session.commit()

ingredient20 = Ingredient(name="Almonds", origin="nut", phase="texture", calories=207,
                          carbs=7.7, fat=17.8, protein=7.6, portionSize=0.25, preparation=6)
session.add(ingredient20)
session.commit()

ingredient21 = Ingredient(name="Pecans", origin="nut", phase="texture", calories=188,
                          carbs=3.8, fat=19.6, protein=2.5, portionSize=0.25, preparation=6)
session.add(ingredient21)
session.commit()

# Protein

ingredient22 = Ingredient(name="Hard boiled egg",
                          origin="animal", phase="protein",  calories=105.5,
                          carbs=0.75, fat=7, protein=8.5, portionSize=0.5, preparation=11)
session.add(ingredient22)
session.commit()

ingredient23 = Ingredient(name="Grill Turkey Breast",
                          origin="animal", phase="protein", calories=189, carbs=0, fat=7, protein=29, portionSize=0.5, preparation=9)
session.add(ingredient23)
session.commit()

ingredient24 = Ingredient(name="Beans", origin="grain",
                          phase="protein", calories=110, carbs=19, fat=1, protein=7, portionSize=0.5, preparation=3)
session.add(ingredient24)
session.commit()

ingredient25 = Ingredient(name="Chickpeas", origin="grain", phase="protein",
                          calories=184, carbs=32, fat=3.2, protein=9.6, portionSize=0.25, preparation=3)
session.add(ingredient25)
session.commit()

ingredient26 = Ingredient(name="Lentils",
                          origin="grain", phase="protein", calories=115, carbs=20, fat=0.4, protein=9, portionSize=0.5, preparation=12)
session.add(ingredient26)
session.commit()

ingredient27 = Ingredient(
    name="Grilled beef", origin="animal", phase="protein", calories=157, carbs=17.9, fat=5.3, protein=9.3, portionSize=0.5, preparation=9)
session.add(ingredient27)
session.commit()

ingredient28 = Ingredient(name="Grilled chicken breast",
                          origin="animal", phase="protein", calories=100, carbs=1, fat=2, protein=22, portionSize=0.5, preparation=9)
session.add(ingredient28)
session.commit()

ingredient29 = Ingredient(name="Grilled salmon",
                          origin="animal", phase="protein", calories=170, carbs=0, fat=11, protein=24, portionSize=0.5, preparation=9)
session.add(ingredient29)
session.commit()


# Saltiness

ingredient30 = Ingredient(
    name="Feta cheese", origin="animal", phase="saltiness", calories=70, carbs=3, fat=5, protein=4, portionSize=0.25, preparation=6)
session.add(ingredient30)
session.commit()

ingredient31 = Ingredient(
    name="Grated parmesan cheese", origin="animal", phase="saltiness", calories=54, carbs=0.5, fat=3.6, protein=4.8, portionSize=0.125, preparation=6)
session.add(ingredient31)
session.commit()

ingredient32 = Ingredient(name="Black Olives", origin="vegetable", phase="saltiness",
                          calories=25, carbs=1, fat=2, protein=0, portionSize=0.125, preparation=6)
session.add(ingredient32)
session.commit()

ingredient33 = Ingredient(name="Capers", origin="vegetable", phase="saltiness",
                          calories=4, carbs=0.8, fat=0.1, protein=0.4, portionSize=0.125, preparation=6)
session.add(ingredient33)
session.commit()


# Herb

ingredient34 = Ingredient(name="Chives", origin="vegetable", phase="smoot",
                          calories=1, carbs=0, fat=0, protein=0, portionSize=0.125, preparation=5)
session.add(ingredient34)
session.commit()

ingredient35 = Ingredient(name="Basil", origin="vegetable", phase="smoot",
                          calories=1, carbs=0.1, fat=0, protein=0.2, portionSize=0.125, preparation=5)
session.add(ingredient35)
session.commit()

ingredient36 = Ingredient(name="Cilantro", origin="vegetable", phase="smoot",
                          calories=0, carbs=0, fat=0, protein=0, portionSize=0.125, preparation=5)
session.add(ingredient36)
session.commit()

ingredient37 = Ingredient(name="Parsley", origin="vegetable", phase="smoot",
                          calories=3, carbs=0.5, fat=0.1, protein=0.2, portionSize=0.125, preparation=5)
session.add(ingredient37)
session.commit()


# Sharpen

ingredient38 = Ingredient(name="Cucumber", origin="vegetable", phase="sharpen",
                          calories=8, carbs=2, fat=0, protein=0, portionSize=0.5, preparation=4)
session.add(ingredient38)
session.commit()

ingredient39 = Ingredient(name="Peppers", origin="vegetable", phase="sharpen",
                          calories=30, carbs=7, fat=0.2, protein=1.5, portionSize=0.5, preparation=4)
session.add(ingredient39)
session.commit()


ingredient40 = Ingredient(name="Pickled cucumbers", origin="vegetable", phase="sharpen",
                          calories=8, carbs=1.75, fat=0.15, protein=0.25, portionSize=0.5, preparation=4)
session.add(ingredient40)
session.commit()


# Dreesing


ingredient41 = Ingredient(
    name="Balsamic Vinaigrette Dressing", origin="vegetable", phase="dressing", calories=71, carbs=3.6, fat=6.2, protein=0.1, portionSize=0.125, preparation=18)
session.add(ingredient41)
session.commit()

ingredient42 = Ingredient(name="Yogurt dressing",
                          origin="animal", phase="dressing", calories=128, carbs=3, fat=12, protein=2, portionSize=0.125, preparation=18)
session.add(ingredient42)
session.commit()

ingredient43 = Ingredient(name="Tofu",
                          origin="vegetable", phase="protein", calories=94, carbs=2.3, fat=6, protein=10, portionSize=0.5, preparation=17)
session.add(ingredient43)
session.commit()

ingredient44 = Ingredient(name="Tomato", origin="vegetable", phase="v&f",
                          calories=18, carbs=3.9, fat=0.2, protein=0.9, portionSize=0.5, preparation=4)
session.add(ingredient44)
session.commit()

ingredient45 = Ingredient(name="Zucchini", origin="vegetable", phase="v&f",
                          calories=9, carbs=1.52, fat=0, protein=0.7, portionSize=0.5, preparation=4)
session.add(ingredient45)
session.commit()

ingredient46 = Ingredient(name="Avocado", origin="vegetable", phase="v&f",
                          calories=58.5, carbs=3, fat=5.25, protein=0.72, portionSize=0.25, preparation=17)
session.add(ingredient46)
session.commit()

ingredient47 = Ingredient(name="Radish", origin="vegetable", phase="sharpen",
                          calories=4.5, carbs=1, fat=0.05, protein=0.2, portionSize=0.25, preparation=4)
session.add(ingredient47)
session.commit()

print "Ingredients added"
