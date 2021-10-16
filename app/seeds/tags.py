from app.models import db, Tag


# Adds tags
def seed_tags():
    tag701 = Tag(
        name="Beverage", recipeId=1)
    tag702 = Tag(
        name="Vodka", recipeId=1)
    tag703 = Tag(
        name="Ginger", recipeId=1)
    tag704 = Tag(
        name="Alcoholic drink", recipeId=1)
    

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
