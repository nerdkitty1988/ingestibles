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

    tag705 = Tag(
        name="Beverage", recipeId=2)
    tag706 = Tag(
        name="strawberry", recipeId=2)
    tag707 = Tag(
        name="Lemonade", recipeId=2)
    tag708 = Tag(
        name="Slushies", recipeId=2)
    
    tag709 = Tag(
        name="cake", recipeId=3)
    tag710 = Tag(
        name="chocolate", recipeId=3)
    tag711 = Tag(
        name="dessert", recipeId=3)

    tag712 = Tag(
        name="cake", recipeId=4)
    tag713 = Tag(
        name="dessert", recipeId=4)
    
    tag714 = Tag(
        name="appetizer", recipeId=5)
    tag715 = Tag(
        name="salad", recipeId=5)
    tag716 = Tag(
        name="avocado", recipeId=5)

    tag717 = Tag(
        name="appetizer", recipeId=6)
    tag718 = Tag(
        name="Olives", recipeId=6)
    tag719 = Tag(
        name="cheese", recipeId=6)
    
    tag720 = Tag(
        name="entree", recipeId=7)
    tag721 = Tag(
        name="steak", recipeId=7)
    tag722 = Tag(
        name="beef", recipeId=7)
    tag723 = Tag(
        name="grill", recipeId=7)
    
    tag724 = Tag(
        name="entree", recipeId=8)
    tag725 = Tag(
        name="pasta", recipeId=8)
    tag726 = Tag(
        name="italian", recipeId=8)
    tag727 = Tag(
        name="Sausage", recipeId=8)

    tag728 = Tag(
        name="snack", recipeId=9)
    tag729 = Tag(
        name="cookie", recipeId=9)

    tag730 = Tag(
        name="snack", recipeId=10)
    tag731 = Tag(
        name="cookie", recipeId=10)

    db.session.add(tag701)
    db.session.add(tag702)
    db.session.add(tag703)
    db.session.add(tag704)
    db.session.add(tag705)
    db.session.add(tag706)
    db.session.add(tag707)
    db.session.add(tag708)
    db.session.add(tag709)
    db.session.add(tag710)
    db.session.add(tag711)
    db.session.add(tag712)
    db.session.add(tag713)
    db.session.add(tag714)
    db.session.add(tag715)
    db.session.add(tag716)
    db.session.add(tag717)
    db.session.add(tag718)
    db.session.add(tag719)
    db.session.add(tag720)
    db.session.add(tag721)
    db.session.add(tag722)
    db.session.add(tag723)
    db.session.add(tag724)
    db.session.add(tag725)
    db.session.add(tag726)
    db.session.add(tag727)
    db.session.add(tag728)
    db.session.add(tag729)
    db.session.add(tag730)
    db.session.add(tag731)
    

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()
