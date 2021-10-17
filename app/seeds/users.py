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


    #Johnny
    user501 = User(
        username='morbidstork', email='morbid@stork.com', password='password', biography="I am a multifaceted artist, Renaissance Man and World Traveller. I am often misinterpreted and questioned for my lifestyle and my artistic methods and endeavors. Inspired by the dark aspects in life and the nature of life/death, I have been attacking the world with an avalanche of obscure and macabre art, scripts, video, literature, music, and photography.", profilePic='https://media-cldnry.s-nbcnews.com/image/upload/MSNBC/Components/Video/201709/sq_juggalorally_170917_copy.jpg')
    user502 = User(
        username='ragefilledkitten', email='rage@kitten.com', password='password', biography="Appearing at Lollapalooza III in Philadelphia, Rage create a silent protest against censorship by standing naked on stage for 15 minutes without singing or playing a note. Each band member has duct tape across his mouth and a letter scrawled on his chest, spelling out 'P-M-R-C.'", profilePic='https://siouxsielaw.files.wordpress.com/2010/02/black-cat.jpg')
    user503 = User(
        username='emotionalturtle', email='emotional@turtle.com', password='password', biography="Yertle was once a king of a pond that is on a far-away Island of Sala-ma-son. The pond he ruled over had everything the other turtles needed such as food, and warm water and the turtles were very happy until Yertle became ungrateful about the throne he sits due to it being low and he thought that if he could make it higher he would be a great ruler of all he can see so he called 9 of the turtles who serve him, to attention. ", profilePic="https://i1.sndcdn.com/artworks-000011487677-pdp5ep-t500x500.jpg")


    #Meitong
    user701 = User(
        username='happyHug', email='happyhug@aa.io', password='password', biography='I love food!')
    user702 = User(
        username='dreamTrue', email='dreamtrue@aa.io', password='password', biography='Cooking is my favorite!')
    user703 = User(
        username='joyHealth', email='joyhealth@aa.io', password='password', profilePic='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeGZMvntM86MXW_ddi6psTHg9z0hAB4LVA_w&usqp=CAU')



    #Darren
    user901 = User(
        username='passionatepolarbear', email='passionate@polarbear.com', password='password', biography="I am sad polar bear, and I am lonely. I want to have friends. Follow me as I try to find a friend to play with.", profilePic='https://i.pinimg.com/236x/b0/84/c2/b084c279dc3ff4e598ee0ffa0cd50c71--baby-polar-bears-oso-polar.jpg')
    user902 = User(
        username='sexyhorse', email='sexy@horse.com', password='password', biography="I am Frederik the Great, a rare Friesian horse living in Arkansas, and I have more than 39,000 followers on my Facebook fan page.", profilePic='https://clearspan.files.wordpress.com/2013/10/famous-horses.png')
    user903 = User(
        username='rickroll', email='rick@roll.com', password='password', biography="We're no strangers to love. You know the rules and so do I. A full commitment's what I'm thinking of. You wouldn't get this from any other guy. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you", profilePic='https://cdn.vox-cdn.com/thumbor/7BMHi-0CALa3odBFMD-MJK9Ye4Y=/0x44:1268x889/1200x800/filters:focal(0x44:1268x889)/cdn.vox-cdn.com/uploads/chorus_image/image/47684009/Screenshot_2014-07-19_15.24.57.0.png')





    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(tim)
    db.session.add(angelina)

    db.session.add(user301)
    db.session.add(user302)
    db.session.add(user303)

    db.session.add(user501)
    db.session.add(user502)
    db.session.add(user503)

    db.session.add(user701)
    db.session.add(user702)
    db.session.add(user703)

    db.session.add(user901)
    db.session.add(user902)
    db.session.add(user903)



    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
