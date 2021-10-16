from app.models import db, Media


# Adds media
def seed_media():
    media1 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=1)
    
    media2 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FQV/RSDM/KU5IVJLY/FQVRSDMKU5IVJLY.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=c3ac97bb305aef7f3067ee77bc5d4575', recipeId=2)

    media3 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FOQ/XQTD/KUCXRRGA/FOQXQTDKUCXRRGA.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=2ecbf4b4788ee2f144956420f7ef6eba', recipeId=3)

    media4 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=4)
    
    media5 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FOQ/XQTD/KUCXRRGA/FOQXQTDKUCXRRGA.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=2ecbf4b4788ee2f144956420f7ef6eba', recipeId=5)
    
    media6 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=6)
    
    media7 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=7)
    
    media8 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FQV/RSDM/KU5IVJLY/FQVRSDMKU5IVJLY.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=c3ac97bb305aef7f3067ee77bc5d4575', recipeId=8)
    
    media9 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=9)
    
    media10 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FQV/RSDM/KU5IVJLY/FQVRSDMKU5IVJLY.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=c3ac97bb305aef7f3067ee77bc5d4575', recipeId=10)
    media11 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=11)
    media12 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FQV/RSDM/KU5IVJLY/FQVRSDMKU5IVJLY.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=c3ac97bb305aef7f3067ee77bc5d4575', recipeId=12)
    media13 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=1)
    media14 = Media(
        mediaUrl='https://ingestiblesapp.s3.amazonaws.com/90cad61efc1d4d51be16043ad995f93f.mp4', recipeId=1)
    media15 = Media(
        mediaUrl='https://ingestiblesapp.s3.amazonaws.com/90cad61efc1d4d51be16043ad995f93f.mp4', recipeId=1)
    media16 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=1)
    media17 = Media(
        mediaUrl='https://ingestiblesapp.s3.amazonaws.com/90cad61efc1d4d51be16043ad995f93f.mp4', recipeId=3)
    media18 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=3)
    


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
