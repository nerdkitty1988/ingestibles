from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', biography='I am a demo user!', profilePic='https://www.enigmatixmedia.com/public/pics/demo.png')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', biography='I love food of all kinds, but my favorite seems to be good country cooking!', profilePic='https://www.slantmagazine.com/wp-content/uploads/2006/02/marnie.jpg')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', biography='French cuisine really tickles my pickle!', profilePic='https://www.thehistorymakers.org/sites/default/files/Steele_Bobbie_wm.png')
    tim = User(
        username='tim', email='tim@aa.io', password='password', biography='If it is healthy, I will try it.', profilePic='https://media.npr.org/assets/img/2018/04/17/npr_84364431_full_vert-ba5ff3e9efe3084b63ae9d7cafc5dd409a73bd51-s300-c85.jpg')
    angelina = User(
        username='angelina', email='angelina@aa.io', password='password', biography='Pumpkin spice time has arrived!', profilePic='https://southblueprint.com/wp-content/uploads/2020/10/ECC21D0A-778A-48B1-BF16-DF1B1C5199FA-53CE2E76-1575-42DA-94CA-17B4D54DC155-900x600.jpg')


    #Jami
    user301 = User(
        username='fake_Emeril', email='nottheemeril@aa.io', password='Password1!', biography='I like Emeril.  I am not Emeril.  But I love to throw spice on my food and say "WHAM!"', profilePic='https://food.fnr.sndimg.com/content/dam/images/food/editorial/talent/emeril-lagasse/emeril-lagasse.jpg.rend.hgtvcom.336.336.suffix/1371587262156.jpeg')
    user302 = User(
        username='elvisLives', email='uhuhuh@aa.io', password='Password1!', biography='I like to eat.  I do not like to cook.  Hoping to find some easy recipes on here like my famous peanut butter, banana, bacon sandwich.', profilePic='https://hips.hearstapps.com/esq.h-cdn.co/assets/16/33/1471374259-elvis-presley-wallpaper-1280-x-960.jpeg')
    user303 = User(
        username='fancy21', email='skyeyes@aa.io', password='Password1!', biography='Pumpkin spice time has arrived!', profilePic='https://image.shutterstock.com/mosaic_250/614404/1543602947/stock-photo-skin-care-woman-with-beauty-face-touching-healthy-facial-skin-portrait-beautiful-smiling-asian-1543602947.jpg')


    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(tim)
    db.session.add(angelina)
    db.session.add(user301)
    db.session.add(user302)
    db.session.add(user303)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
