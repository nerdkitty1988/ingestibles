from app.models import db, Media


# Adds media
def seed_media():
    media701 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FPX/23L1/KTPSYXG9/FPX23L1KTPSYXG9.jpg?auto=webp&frame=1&width=563&height=1024&fit=bounds&md=619106ddb4dd497a0a2cff236eba5b69', recipeId=1)
    media702 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FK6/1EKB/KTPSYXH4/FK61EKBKTPSYXH4.jpg?auto=webp&frame=1&width=396&height=1024&fit=bounds&md=6355eec22ad47682d075aff4d45f5959', recipeId=1)
    
    media7 = Media(
        mediaUrl='', recipeId=1)
    


    db.session.add(media1)
    db.session.add(media2)
    db.session.add(media3)
    db.session.add(media4)
    db.session.add(media5)
    db.session.add(media6)
    db.session.add(media7)
    db.session.add(media8)
    db.session.add(media9)
    db.session.add(media10)
    db.session.add(media11)
    db.session.add(media12)
    db.session.add(media13)
    db.session.add(media14)
    db.session.add(media15)
    db.session.add(media16)
    db.session.add(media17)
    db.session.add(media18)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_media():
    db.session.execute('TRUNCATE media RESTART IDENTITY CASCADE;')
    db.session.commit()
