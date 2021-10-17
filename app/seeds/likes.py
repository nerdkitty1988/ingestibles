from app.models import db, Like


# Adds like
def seed_likes():
    like701 = Like(
        userId=1, recipeId=1)
    like702 = Like(
        userId=1, recipeId=2)
    like703 = Like(
        userId=1, recipeId=5)
    like704 = Like(
        userId=1, recipeId=6)
    like705 = Like(
        userId=1, recipeId=8)
    like706 = Like(
        userId=1, recipeId=9)
    
    like707 = Like(
        userId=3, recipeId=1)
    like708 = Like(
        userId=12, recipeId=1)
    like709 = Like(
        userId=6, recipeId=1)
    like710 = Like(
        userId=9, recipeId=1)
    like711 = Like(
        userId=10, recipeId=1)
    like712 = Like(
        userId=11, recipeId=1)

    like713 = Like(
        userId=2, recipeId=2)
    like714 = Like(
        userId=8, recipeId=2)
    like715 = Like(
        userId=12, recipeId=2)
    like716 = Like(
        userId=13, recipeId=2)
    like717 = Like(
        userId=14, recipeId=2)

    like718 = Like(
        userId=5, recipeId=3)
    like719 = Like(
        userId=13, recipeId=3)
    like720 = Like(
        userId=12, recipeId=3)

    like721 = Like(
        userId=6, recipeId=4)
    like722 = Like(
        userId=7, recipeId=4)

    like723 = Like(
        userId=12, recipeId=5)
    like724 = Like(
        userId=2, recipeId=5)
    
    like725 = Like(
        userId=3, recipeId=6)
    like726 = Like(
        userId=4, recipeId=6)
    like727 = Like(
        userId=5, recipeId=6)

    like728 = Like(
        userId=5, recipeId=7)

    like729 = Like(
        userId=4, recipeId=8)

    like730 = Like(
        userId=2, recipeId=9)
    like731 = Like(
        userId=5, recipeId=9)

    like732 = Like(
        userId=3, recipeId=10)
    like733 = Like(
        userId=5, recipeId=10)


    db.session.add(like701)
    db.session.add(like702)
    db.session.add(like703)
    db.session.add(like704)
    db.session.add(like705)
    db.session.add(like706)
    db.session.add(like707)
    db.session.add(like708)
    db.session.add(like709)
    db.session.add(like710)
    db.session.add(like711)
    db.session.add(like712)
    db.session.add(like713)
    db.session.add(like714)
    db.session.add(like715)
    db.session.add(like716)
    db.session.add(like717)
    db.session.add(like718)
    db.session.add(like719)
    db.session.add(like720)
    db.session.add(like721)
    db.session.add(like722)
    db.session.add(like723)
    db.session.add(like724)
    db.session.add(like725)
    db.session.add(like726)
    db.session.add(like727)
    db.session.add(like728)
    db.session.add(like729)
    db.session.add(like730)
    db.session.add(like731)
    db.session.add(like732)
    db.session.add(like733)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_likes():
    db.session.execute('TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
