from app.models import db, Like


# Adds like
def seed_likes():
    like1 = Like(
        userId=1, recipeId=1)

    like2 = Like(
        userId=3, recipeId=2)

    like3 = Like(
        userId=1, recipeId=3)

    like4 = Like(
        userId=2, recipeId=4)

    like5 = Like(
        userId=1, recipeId=5)

    like6 = Like(
        userId=1, recipeId=6)

    like7 = Like(
        userId=1, recipeId=7)

    like8 = Like(
        userId=5, recipeId=8)

    like9 = Like(
        userId=1, recipeId=9)

    like10 = Like(
        userId=1, recipeId=10)
    like11 = Like(
        userId=1, recipeId=11)
    like12 = Like(
        userId=1, recipeId=12)
    like13 = Like(
        userId=3, recipeId=1)

    db.session.add(like1)
    db.session.add(like2)
    db.session.add(like3)
    db.session.add(like4)
    db.session.add(like5)
    db.session.add(like6)
    db.session.add(like7)
    db.session.add(like8)
    db.session.add(like9)
    db.session.add(like10)
    db.session.add(like11)
    db.session.add(like12)
    db.session.add(like13)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_likes():
    db.session.execute('TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
