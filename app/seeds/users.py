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

    dummy6 = User(
        username='1', email='1@aa.io', password='password')
    dummy7 = User(
        username='2', email='2@aa.io', password='password')
    dummy8 = User(
        username='3', email='3@aa.io', password='password')
    dummy9 = User(
        username='4', email='4@aa.io', password='password')
    dummy10 = User(
        username='5', email='5@aa.io', password='password')
    dummy11 = User(
        username='6', email='7@aa.io', password='password')

    user701 = User(
        username='happyHug', email='happyhug@aa.io', password='password')
    user702 = User(
        username='dreamTrue', email='dreamtrue@aa.io', password='password')
    user703 = User(
        username='joyHealth', email='joyhealth@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(tim)
    db.session.add(angelina)
    db.session.add(dummy6)
    db.session.add(dummy7)
    db.session.add(dummy8)
    db.session.add(dummy9)
    db.session.add(dummy10)
    db.session.add(dummy11)
    db.session.add(user701)
    db.session.add(user702)
    db.session.add(user703)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
