from app.models import db, Ingredient


# Adds ingredients
def seed_ingredients():
    ingredient1 = Ingredient(
        recipeId=1,
        info="1.5-2kg (3-4lbs) piece of pork neck (collar)")
    ingredient2 = Ingredient(
        recipeId=1,
        info="5-6 onions")
    ingredient3 = Ingredient(
        recipeId=1,
        info="4-5 carrots")
    ingredient4 = Ingredient(
        recipeId=1,
        info="10 slices of bacon")
    ingredient5 = Ingredient(
        recipeId=1,
        info="1.5kg (3lbs) small potatoes")
    ingredient6 = Ingredient(
        recipeId=1,
        info="3-4 tbsp olive oil")
    ingredient7 = Ingredient(
        recipeId=1,
        info="1 cup dark beer")
    ingredient8 = Ingredient(
        recipeId=1,
        info="2 tsp red paprika")
    ingredient9 = Ingredient(
        recipeId=1,
        info="1 tsp salt")
    ingredient10 = Ingredient(
        recipeId=1,
        info="1 tbsp whole grain mustard")
    ingredient11 = Ingredient(
        recipeId=1,
        info="3 tbsp soy sauce")
    ingredient12 = Ingredient(
        recipeId=1,
        info="1 tbsp dijon mustard")
    ingredient13 = Ingredient(
        recipeId=1,
        info="11 tsp pepper")
    ingredient14 = Ingredient(
        recipeId=1,
        info="Italian seasoning")
    ingredient15 = Ingredient(
        recipeId=2,
        info="16 slices Buttermilk Bread")
    ingredient16 = Ingredient(
        recipeId=2,
        info="16 slices Swiss Cheese")
    ingredient17 = Ingredient(
        recipeId=2,
        info="1½ lb Ground Beef")
    ingredient18 = Ingredient(
        recipeId=2,
        info="2 tbsp Avocado Oil")
    ingredient19 = Ingredient(
        recipeId=2,
        info="½ White Onion, diced")
    ingredient20 = Ingredient(
        recipeId=2,
        info="4 Garlic Cloves, minced")
    ingredient21 = Ingredient(
        recipeId=2,
        info="1 cup Mushrooms, chopped")
    ingredient22 = Ingredient(
        recipeId=2,
        info="1 Jalapeno, diced")
    ingredient23 = Ingredient(
        recipeId=2,
        info="1 tsp Salt")
    ingredient24 = Ingredient(
        recipeId=2,
        info="1 tsp Red Pepper Flakes")
    ingredient25 = Ingredient(
        recipeId=2,
        info="1 cup Mayo")
    ingredient26 = Ingredient(
        recipeId=2,
        info="½ cup Ketchup")
    ingredient27 = Ingredient(
        recipeId=2,
        info="¼ cup Sweet Relish")



    db.session.add(ingredient1)
    db.session.add(ingredient2)
    db.session.add(ingredient3)
    db.session.add(ingredient4)
    db.session.add(ingredient5)
    db.session.add(ingredient6)
    db.session.add(ingredient7)
    db.session.add(ingredient8)
    db.session.add(ingredient9)
    db.session.add(ingredient10)
    db.session.add(ingredient11)
    db.session.add(ingredient12)
    db.session.add(ingredient13)
    db.session.add(ingredient14)
    db.session.add(ingredient15)
    db.session.add(ingredient16)
    db.session.add(ingredient17)
    db.session.add(ingredient18)
    db.session.add(ingredient19)
    db.session.add(ingredient20)
    db.session.add(ingredient21)
    db.session.add(ingredient22)
    db.session.add(ingredient23)
    db.session.add(ingredient24)
    db.session.add(ingredient25)
    db.session.add(ingredient26)
    db.session.add(ingredient27)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the ingredients table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
