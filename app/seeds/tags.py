from app.models import db, Tag


# Adds tags
def seed_tags():
    jamiTag1 = Tag(
    name="BEVERAGE", recipeId=21)
    jamiTag2 = Tag(
        name="WINE", recipeId=21)
    jamiTag3 = Tag(
        name="BEVERAGE", recipeId=22)
    jamiTag4 = Tag(
        name="CHOCOLATE", recipeId=22)
    jamiTag5 = Tag(
        name="DESSERT", recipeId=23)
    jamiTag6 = Tag(
        name="ICE CREAM", recipeId=23)
    jamiTag7 = Tag(
        name="DESSERT", recipeId=24)
    jamiTag8 = Tag(
        name="APPLE", recipeId=24)
    jamiTag9 = Tag(
        name="APPETIZER", recipeId=25)
    jamiTag10 = Tag(
        name="CHEESE", recipeId=25)
    jamiTag11 = Tag(
        name="APPETIZER", recipeId=26)
    jamiTag12 = Tag(
        name="EGGS", recipeId=26)
    jamiTag13 = Tag(
        name="ENTREE", recipeId=27)
    jamiTag14 = Tag(
        name="TUNA", recipeId=27)
    jamiTag15 = Tag(
        name="ENTREE", recipeId=28)
    jamiTag16 = Tag(
        name="BURGER", recipeId=28)
    jamiTag17 = Tag(
        name="SNACK", recipeId=29)
    jamiTag18 = Tag(
        name="TOMATO", recipeId=29)
    jamiTag19 = Tag(
        name="SNACK", recipeId=30)
    jamiTag20 = Tag(
        name="PLASTIC", recipeId=30)

    db.session.add(jamiTag1)
    db.session.add(jamiTag2)
    db.session.add(jamiTag3)
    db.session.add(jamiTag4)
    db.session.add(jamiTag5)
    db.session.add(jamiTag6)
    db.session.add(jamiTag7)
    db.session.add(jamiTag8)
    db.session.add(jamiTag9)
    db.session.add(jamiTag10)
    db.session.add(jamiTag11)
    db.session.add(jamiTag12)
    db.session.add(jamiTag13)
    db.session.add(jamiTag14)
    db.session.add(jamiTag15)
    db.session.add(jamiTag16)
    db.session.add(jamiTag17)
    db.session.add(jamiTag18)
    db.session.add(jamiTag19)
    db.session.add(jamiTag20)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()
