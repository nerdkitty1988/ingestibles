from app.models import db, Media


# Adds media
def seed_media():
    jamiMedia1 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FLL/JYUH/KN8W3MU5/FLLJYUHKN8W3MU5.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=2c3a9a67ad4372bba2ebfa7fe98ca5e6', recipeId=21)
    jamiMedia2 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FXH/M5OU/KN8W3QX0/FXHM5OUKN8W3QX0.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d70f5f185890ada9d14b085096a64cf2', recipeId=21)
    jamiMedia3 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F1O/HLA9/KN8W3UMO/F1OHLA9KN8W3UMO.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=4eff9057a122178afbe52218e1660cbf', recipeId=21)
    jamiMedia4 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FDD/D90A/KN8W3YLR/FDDD90AKN8W3YLR.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=28ea0bb55fc079c8e2257835b193afe0', recipeId=21)
    jamiMedia5 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F9X/O3LG/KIKA4K08/F9XO3LGKIKA4K08.png?auto=webp&frame=1&width=933&fit=bounds&md=3879e9346b30b85c513038eac4c435f1', recipeId=22)
    jamiMedia6 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FZ5/JK2Q/KIKA4K02/FZ5JK2QKIKA4K02.png?auto=webp&frame=1&width=400&fit=bounds&md=6ad949a89730fcb964c195e83e2999cb', recipeId=22)
    jamiMedia7 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F4I/0CRX/KIKA4JZU/F4I0CRXKIKA4JZU.png?auto=webp&frame=1&width=400&fit=bounds&md=f6573a420a7485fed6ac71fe2ab5bf31', recipeId=22)
    jamiMedia8 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FP2/SKGJ/KIKA4JZW/FP2SKGJKIKA4JZW.png?auto=webp&frame=1&fit=bounds&md=51b3acad72f01884590f5458792684c3', recipeId=22)
    jamiMedia9 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F43/423B/KQCCFWQ0/F43423BKQCCFWQ0.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=9387b32ea6cc3167bb94156f635f46a6', recipeId=23)
    jamiMedia10 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FF6/RO6L/KQ57CO8F/FF6RO6LKQ57CO8F.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=5b34dbedeca3ba61073fbedfc57bebfe', recipeId=23)
    jamiMedia11 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FHU/76WK/KQ57CO84/FHU76WKKQ57CO84.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=860e812b91318a0b34fc16488314e65e', recipeId=23)
    jamiMedia12 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FDZ/Y6IE/KQ57CP1P/FDZY6IEKQ57CP1P.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=43b30bcaef18846b343ac68de17bf6ab', recipeId=23)
    jamiMedia13 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FG5/OBDL/KNG1B6DK/FG5OBDLKNG1B6DK.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=bb646e2bb222387898a36d947099cc9b', recipeId=24)
    jamiMedia14 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FOD/L6S3/KNG1B6DJ/FODL6S3KNG1B6DJ.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=affa06ff996b834e79956a78c910ad81', recipeId=24)
    jamiMedia15 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FNV/SUYD/KNG1B6DG/FNVSUYDKNG1B6DG.jpg?auto=webp&frame=1&crop=2:3&width=400&height=1024&fit=bounds&md=ed7d531f2f44634ecebec6b16e7cca4b', recipeId=24)
    jamiMedia16 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FWJ/S2R6/KNG1BIF7/FWJS2R6KNG1BIF7.jpg?auto=webp&frame=1&crop=2:3&width=400&height=1024&fit=bounds&md=ad49d9de391320122018c01b7f544461', recipeId=24)
    jamiMedia17 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F66/1C1G/KNYM1BA5/F661C1GKNYM1BA5.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=bda8ff1f44650bc1efb2027af66d0fe1', recipeId=25)
    jamiMedia18 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FCD/QBC9/KNYM0P6Y/FCDQBC9KNYM0P6Y.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=3a8170fa6b0ceb7a95393a23d13c2b77', recipeId=25)
    jamiMedia19 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FLB/3N3L/KNYM0P71/FLB3N3LKNYM0P71.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=47b1bbb12b9db4a7832ed19dcb21afcc', recipeId=25)
    jamiMedia20 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FV5/8479/KN36CAIL/FV58479KN36CAIL.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=b3e17aea915e988dd7d7a5f1065ef76b', recipeId=26)
    jamiMedia21 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F8I/1LE7/KN36CAGG/F8I1LE7KN36CAGG.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=a6dfd4b65d04e11b578f01a0fb7a5b06', recipeId=26)
    jamiMedia22 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FEV/28M9/KFZEJGHF/FEV28M9KFZEJGHF.png?auto=webp&frame=1&width=547&height=1024&fit=bounds&md=c1746224bc20b2e31ca2a84b15e1fc6a', recipeId=27)
    jamiMedia23 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FV4/5D0B/KFZEJGHD/FV45D0BKFZEJGHD.png?auto=webp&frame=1&width=411&fit=bounds&md=2c1239043615a1e5f3096adc6803fedf', recipeId=27)
    jamiMedia24 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FA2/L6Y4/KFZEJGH5/FA2L6Y4KFZEJGH5.png?auto=webp&frame=1&width=411&fit=bounds&md=f0b7f1b1232d02d1cb03e50c01fafe91', recipeId=27)
    jamiMedia25 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F68/6RHR/KA9N94GK/F686RHRKA9N94GK.png?auto=webp&frame=1&width=560&fit=bounds&md=0359917175c53e054ef3106313fbd758', recipeId=28)
    jamiMedia26 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FD6/3Q24/KAB2MMQG/FD63Q24KAB2MMQG.png?auto=webp&frame=1&width=525&fit=bounds&md=8ca511cabaea6ffd2ce17ad7c460eb8c', recipeId=28)
    jamiMedia27 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F55/PHJY/KQQMU1SN/F55PHJYKQQMU1SN.jpg?auto=webp&frame=1&width=1020&height=1024&fit=bounds&md=b2716a4fb8e8e8d4c6667c0ae6a9b9b1', recipeId=29)
    jamiMedia28 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FBM/QOOJ/KQQMU1R9/FBMQOOJKQQMU1R9.jpg?auto=webp&frame=1&width=822&height=1024&fit=bounds&md=73f3e5e86f9755c5eafeabd7a700c415', recipeId=29)
    jamiMedia29 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FC5/VVYH/JGGTFXAO/FC5VVYHJGGTFXAO.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=a57c985c088b7772385045d164f5a8f8', recipeId=30)
    jamiMedia30 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F2O/G5JV/JGGTFXDF/F2OG5JVJGGTFXDF.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d2bc80c1ad36b6c72ba1141c68add379', recipeId=30)
    jamiMedia31 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FVB/UAMU/JGGTG035/FVBUAMUJGGTG035.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=0bc4a49bc526e42f8267571d1ca39fef', recipeId=30)



    db.session.add(jamiMedia1)
    db.session.add(jamiMedia2)
    db.session.add(jamiMedia3)
    db.session.add(jamiMedia4)
    db.session.add(jamiMedia5)
    db.session.add(jamiMedia6)
    db.session.add(jamiMedia7)
    db.session.add(jamiMedia8)
    db.session.add(jamiMedia9)
    db.session.add(jamiMedia10)
    db.session.add(jamiMedia11)
    db.session.add(jamiMedia12)
    db.session.add(jamiMedia13)
    db.session.add(jamiMedia14)
    db.session.add(jamiMedia15)
    db.session.add(jamiMedia16)
    db.session.add(jamiMedia17)
    db.session.add(jamiMedia18)
    db.session.add(jamiMedia19)
    db.session.add(jamiMedia20)
    db.session.add(jamiMedia21)
    db.session.add(jamiMedia22)
    db.session.add(jamiMedia23)
    db.session.add(jamiMedia24)
    db.session.add(jamiMedia25)
    db.session.add(jamiMedia26)
    db.session.add(jamiMedia27)
    db.session.add(jamiMedia28)
    db.session.add(jamiMedia29)
    db.session.add(jamiMedia30)
    db.session.add(jamiMedia31)
    db.session.add(jamiMedia14)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_media():
    db.session.execute('TRUNCATE media RESTART IDENTITY CASCADE;')
    db.session.commit()
