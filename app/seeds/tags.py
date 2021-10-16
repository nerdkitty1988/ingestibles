from app.models import db, Tag


# Adds tags
def seed_tags():
    tag1 = Tag(
        name="CAKE", recipeId=1)
    tag13 = Tag(
        name="Snack", recipeId=1)
    tag14 = Tag(
        name="Appetizer", recipeId=1)
    tag2 = Tag(
        name="Dessert", recipeId=2)
    tag3 = Tag(
        name="Entree", recipeId=3)
    tag4 = Tag(
        name="Beverage", recipeId=4)
    tag15 = Tag(
        name="CUPCAKE", recipeId=4)
    tag5 = Tag(
        name="DRINK", recipeId=5)
    tag6 = Tag(
        name="CANDY", recipeId=6)
    tag7 = Tag(
        name="CANDY", recipeId=7)
    tag8 = Tag(
        name="PASTA", recipeId=8)
    tag9 = Tag(
        name="PASTA", recipeId=9)
    tag10 = Tag(
        name="SALAD", recipeId=10)
    tag11 = Tag(
        name="SALAD", recipeId=11)
    tag12 = Tag(
        name="BBQ", recipeId=12)

    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.add(tag4)
    db.session.add(tag5)
    db.session.add(tag6)
    db.session.add(tag7)
    db.session.add(tag8)
    db.session.add(tag9)
    db.session.add(tag10)
    db.session.add(tag11)
    db.session.add(tag12)
    db.session.add(tag13)
    db.session.add(tag14)
    db.session.add(tag15)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()
