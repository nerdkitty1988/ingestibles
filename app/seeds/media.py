from app.models import db, Media


# Adds media
def seed_media():
    media701 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FPX/23L1/KTPSYXG9/FPX23L1KTPSYXG9.jpg?auto=webp&frame=1&width=563&height=1024&fit=bounds&md=619106ddb4dd497a0a2cff236eba5b69', recipeId=1)
    media702 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FK6/1EKB/KTPSYXH4/FK61EKBKTPSYXH4.jpg?auto=webp&frame=1&width=396&height=1024&fit=bounds&md=6355eec22ad47682d075aff4d45f5959', recipeId=1)
    
    media703 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FK2/SID1/KR4X94WT/FK2SID1KR4X94WT.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=4ff089b752e0d18edd34929c4e657e6f', recipeId=2)

    media704 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FQV/RSDM/KU5IVJLY/FQVRSDMKU5IVJLY.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=c3ac97bb305aef7f3067ee77bc5d4575', recipeId=3)

    media705 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FKG/HYRL/KSUD6GJG/FKGHYRLKSUD6GJG.png?auto=webp&frame=1&width=632&height=1024&fit=bounds&md=7e2b8de316945a23b06ca1629df55cce', recipeId=4)
    media706 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FIV/SK5J/KSN82IJF/FIVSK5JKSN82IJF.jpg?auto=webp&frame=1&width=247&height=1024&fit=bounds&md=d1559835ddc029026dc950dacfa07552', recipeId=4)
    media707 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FZK/W86V/KSONIGFZ/FZKW86VKSONIGFZ.png?auto=webp&frame=1&width=247&height=1024&fit=bounds&md=e27628b316d1f2e2e0112c537ddfa5e1', recipeId=4)

    
    media708 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F2Y/3FF3/J1QP0HWD/F2Y3FF3J1QP0HWD.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=fa27ecd9f7aa0ac4d42873309e1abe81', recipeId=5)



    media709 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FED/DVP1/KNRGV0DF/FEDDVP1KNRGV0DF.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=436c8eac45d9a98ba0f62d892127799b', recipeId=6)
    media710 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F53/AEBM/KNRGUUUB/F53AEBMKNRGUUUB.jpg?auto=webp&frame=1&width=233&height=1024&fit=bounds&md=0dc1e53a1943eb6a7a48152b195d7ffb', recipeId=6)


    
    media711 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F0Z/U1RJ/KQGMRBUA/F0ZU1RJKQGMRBUA.jpg?auto=webp&frame=1&width=874&height=1024&fit=bounds&md=ffef0afa22a5dba342e3227016c65991', recipeId=7)
    media712 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FZI/YLMS/KQGMRBUB/FZIYLMSKQGMRBUB.jpg?auto=webp&frame=1&width=326&height=1024&fit=bounds&md=bd78d0e2e97a53b004f769473a50686b', recipeId=7)
    media713 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FMK/GEP0/KQGMRBTZ/FMKGEP0KQGMRBTZ.jpg?auto=webp&frame=1&width=326&height=1024&fit=bounds&md=6a790537b59db3b18c2f0f9f9056b50b', recipeId=7)



    media714 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FVU/8OW3/KKWL8KF3/FVU8OW3KKWL8KF3.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=fe3ba40124d51f1a3cb87b46b175c900', recipeId=8)
    
    media715 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FD3/A29G/GD2JKDVX/FD3A29GGD2JKDVX.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=473b941f1783a0156c26dd969c6ceb9c', recipeId=9)

    media716 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FZM/A5AR/IUHMTRO5/FZMA5ARIUHMTRO5.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=91a31f58bf923808118f4b54a303dc3f', recipeId=10)
    media717 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FJA/9F3T/IUHMTP3Q/FJA9F3TIUHMTP3Q.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=7af9fa915eb0cb131ddc5d28b9328fca', recipeId=10)


    db.session.add(media701)
    db.session.add(media702)
    db.session.add(media703)
    db.session.add(media704)
    db.session.add(media705)
    db.session.add(media706)
    db.session.add(media707)
    db.session.add(media708)
    db.session.add(media709)
    db.session.add(media710)
    db.session.add(media711)
    db.session.add(media712)
    db.session.add(media713)
    db.session.add(media714)
    db.session.add(media715)
    db.session.add(media716)
    db.session.add(media717)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_media():
    db.session.execute('TRUNCATE media RESTART IDENTITY CASCADE;')
    db.session.commit()
