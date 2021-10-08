from app.models import db, Comment


# Adds comments
def seed_comments():
    comment1 = Comment(
        userId=1, comment='Are these low sodium?')
    comment2 = Comment(
        userId=3, comment='You can substitute some of the ingredients for the lower sodium variety, but this recipe itself is not low sodium.')
    comment3 = Comment(
        userId=1, comment='Ok thank you!')
    comment4 = Comment(
        userId=2, comment='I use the low soium soy sauce as a replacement for the soy sauce.  It only makes a small difference in taste.')
    comment5 = Comment(
        userId=1, comment='Awesome!  I will try that!')


    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the comments table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
