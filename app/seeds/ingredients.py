from app.models import db, Ingredient


# Adds ingredients
def seed_ingredients():
    ingredient701 = Ingredient(
        recipeId=1,
        info="700mL bottle of vodka")
    ingredient702 = Ingredient(
        recipeId=1,
        info="2 stalks of lemongrass")
    ingredient703 = Ingredient(
        recipeId=1,
        info="1 thumb of galangal")
    ingredient704 = Ingredient(
        recipeId=1,
        info="1 or 2 makrut / kaffir lime leaves")
    ingredient705 = Ingredient(
        recipeId=1,
        info="1 clove of garlic")
    ingredient706 = Ingredient(
        recipeId=1,
        info="1 large shallot")
    ingredient707 = Ingredient(
        recipeId=1,
        info="1 small ripe tomato")
    ingredient708 = Ingredient(
        recipeId=1,
        info="1+ chili pepper")
    ingredient709 = Ingredient(
        recipeId=1,
        info="a small bunch of coriander stalks")
    ingredient710 = Ingredient(
        recipeId=1,
        info="1 wedge of lime")
    


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
