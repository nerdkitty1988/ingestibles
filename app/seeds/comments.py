from app.models import db, Comment


# Adds comments
def seed_comments():
    comment701 = Comment(
        recipeId=1,
        userId=2, comment="Oh that's an interesting combination! I'd try it :)")
    comment702 = Comment(
        recipeId=1,
        userId=1, comment='Please do so. I hope you love it.')
    comment703 = Comment(
        recipeId=1,
        userId=5, comment='Is it very strong?')

    comment704 = Comment(
        recipeId=2,
        userId=1, comment="Love it!")
    comment705 = Comment(
        recipeId=2,
        userId=5, comment='Awesome!  I will try that!')

    comment706 = Comment(
        recipeId=3,
        userId=1, comment="Halloween~~")
    comment707 = Comment(
        recipeId=3,
        userId=12, comment='Is it very sweet?')

    comment708 = Comment(
        recipeId=4,
        userId=12, comment="If you were within 100 miles of me I'd buy one from you!")
    comment709 = Comment(
        recipeId=4,
        userId=13, comment='Really well done! Bravo!')
    comment710 = Comment(
        recipeId=4,
        userId=7, comment='This is aaaaaaamazing. Wow! :D')

    comment711 = Comment(
        recipeId=5,
        userId=8, comment="I like avocado! Definitely gonna try it.")
    comment712 = Comment(
        recipeId=5,
        userId=14, comment='So simple but healthy')

    comment713 = Comment(
        recipeId=6,
        userId=2, comment='These sound fun and tasty!')
    comment714 = Comment(
        recipeId=6,
        userId=3, comment='The combination sounds interesting')
    comment715 = Comment(
        recipeId=6,
        userId=4, comment='Cheese is my favorite')

    comment716 = Comment(
        recipeId=7,
        userId=11, comment='Nice job!')
    comment717 = Comment(
        recipeId=7,
        userId=10, comment='I need that dish for my dinner!')

    comment718 = Comment(
        recipeId=8,
        userId=4, comment='Yeah~ Creamy pasta~')
    
    comment719 = Comment(
        recipeId=9,
        userId=1, comment='I will definitely try your recipe')

    comment720 = Comment(
        recipeId=10,
        userId=1, comment='Wow! So cute, and easy steps!')

    db.session.add(comment701)
    db.session.add(comment702)
    db.session.add(comment703)
    db.session.add(comment704)
    db.session.add(comment705)
    db.session.add(comment706)
    db.session.add(comment707)
    db.session.add(comment708)
    db.session.add(comment709)
    db.session.add(comment710)
    db.session.add(comment711)
    db.session.add(comment712)
    db.session.add(comment713)
    db.session.add(comment714)
    db.session.add(comment715)
    db.session.add(comment716)
    db.session.add(comment717)
    db.session.add(comment718)
    db.session.add(comment719)
    db.session.add(comment720)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the comments table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
