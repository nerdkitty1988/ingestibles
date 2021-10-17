from app.models import db, Recipe


# Adds recipes
def seed_recipes():
    recipe701 = Recipe(
        title='Tom Yum Vodka', description="""I think by now, Thailand's famous Tom Yum Goong (hot and sour prawn soup) is a household name around the world. But this is more than just a soup. Tom yum's hot, spicy, sour, packed-with-herbs flavour is used in everything from potato chips to instant noodles.

So I had a stroke of genius.

Why not use this flavour to turn plain old vodka into a masterpiece?

The delicious, aromatic herbs give this drink a unique scent that you just can't find anywhere else, and chili and garlic a little some fire.

The best part?

It's so easy to make, you can have this recipe done in just 5 minutes today. And tomorrow, you can reap the reward of a delicious, sophisticated little beverage.""", authorId=1, ingredientPhoto='https://content.instructables.com/ORIG/FZ2/8QSC/KTPSYXDD/FZ28QSCKTPSYXDD.jpg?auto=webp&frame=1&width=552&height=1024&fit=bounds&md=f596ae9807c182a3b39b52ae88ce2df0')

    recipe702 = Recipe(
        title='Frozen Strawberry Lemonade Slushies', 
        description="""This has been a very hot summer so far. For this Water Instructable, I decided I wanted to make a refreshing drink made with 4 cups of water and some of my favorite ingredients. Nothing tastes better than to sit back with an icy cold drink to cool you. And fresh lemonade traditionally can be such a special summertime treat! To make it even better, I decided to freeze the water to make frozen lemonade slushies. Then I thought to add some strawberries and how about some mint from my garden too? I had my idea of the perfect summer frozen drink! It was so very tasty and definitely hit the spot that I wanted to hit!! You can make it too by following these steps. """,
        authorId=2, 
        ingredientPhoto='https://content.instructables.com/ORIG/FE3/5PBQ/KR4X9504/FE35PBQKR4X9504.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=62676314745e3eafcf31d0ca8b292949')
    
    recipe703 = Recipe(
        title='Halloween Themed Chocoflan',
        description="""Warning!!!!!!!

The following recipe contains eggs and cocoa, if you are allergic to these please DO NOT do this recipe. If you do not like chocolate cake you can always replace it with any other type of cake.

Also, this recipe has medium to hard difficulty so please try at your own risk""",
        authorId=3, 
        ingredientPhoto='https://content.instructables.com/ORIG/F5G/AEY8/GYLZWZN3/F5GAEY8GYLZWZN3.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=f52c991a7c3b58d95dccd3b4549217cb')
    

    recipe704 = Recipe(
        title="Spirited Away Cake: No Face's Feast", description="""Hello!

If you've ever watched Hayao Miyazaki's award winning film "Spirited Away,' you might recall a certain food scene. In it, No-Face, a spirit, ravenously consumes pounds of delicious food in front of his hosts. Miyazaki is such a master with animated food I felt compelled to make a cake honoring such a fun scene.

Be warned though, this is not an easy cake! It took me wayyy to long to finish inbetween work and school. If anyone wants to re-create this, I have suggestions on each step to make the process a little easier. :)

Enough rambling, onto the cake!

(no-face drawing by Valentina Hramov)""", authorId=1, ingredientPhoto='https://content.instructables.com/ORIG/F4Z/QCJZ/KSUD6CY1/F4ZQCJZKSUD6CY1.png?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=5c5f098b41d393dd081793ba7c1d3b6f')

    recipe705 = Recipe(
        title='RECIPE |MANDARIN AVOCADO SALAD', description="""Spring is finally here! With 15 degree weather, I am forcing myself to believe that spring is here to stay even after that random snow storm we had last week. With Spring, comes warmer weather and cooler dishes like this Mandarin Avocado Salad. I've been trying to get back into my salad routine to cure my skin issues. After all, you are what you eat.

In the past year, my skin has rewound back to my teenage years when acne haunted me. I had awful cystic acne where I would get nasty volcano-like zits on my forehead, nose or chin. I was lucky in the fact that I didn't get a zillion red blemishes all over my face but life decided to be fair by giving me exactly that all over forehead along with little white bumps. At first I thought I wasn't cleaning off my makeup as well as I should, even though I would triple cleanse! (Yes triple cleanse with 3 different types of cleanser. Don't worry I've reduced that down to 2 cleansers now so I don't dry out my skin). Then I thought maybe there is too much oil in my diet but that wasn't it either. I swapped up my skin regime multiple times to figure out what was going wrong. I searched high and low for the answer and I finally figured it out. I found this YouTuber who explained that it was an fungal infection underneath my skin, hence the numerous white bumps that would turn into red little blemishes. The cause for the infection was an influx of yeast and sugars from white carbohydrates in my diet. It makes sense as I've been eating a lot more white carbs to replace my meat intake. Now don't get me wrong, not everyone will experience these same symptoms because every one is different. So please don't be convinced that you need to lower your carb intake and increase your meat intake. But I really needed to force myself to eat more whole grains not just white breads/pastas which is common sense. I am not just a fan of the taste in whole grains? Long story, short: I've returned back to eating more greens, fruits, and replacing white carbs with whole grain ones. So far, so good. My skin is clearing day by day!

So if you're also experiencing some skin issues, first think about what you eat. Do some research and try to understand what the cause is. I would say that 80% of our skin issues are based on our diet. Then to assist with the healing, look into active oils or serums that will speed up the healing process. But just remember you can apply all the serums in the world but if you eat garbage, it will still reflect on your skin. As they say, "Beauty comes from within."
Anyway I hope you guys give this salad a shot. It's one of my favourites and I used to eat it daily before my wedding and I remember having glowing clear skin! It's filled with Vitamin C, Folate, and antioxidants which fight the skin-villains. Easy, quick to make and wonderful for the new Spring season. In this recipe, I'm using the Super Greens salad box by Organic Girl which you can find at major Canadian grocers. If you do end up making this recipe, take a picture of it, tag @christieathome on Instagram and it may be featured. If you're not on Instagram please share this recipe with your family and friends!

Disclaimer: I am not sponsored by the companies listed in this post.""", authorId=4, ingredientPhoto='https://content.instructables.com/ORIG/FCA/QAOF/J1QP0HWE/FCAQAOFJ1QP0HWE.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=ccb44c5e51c5e090a32132fff232b14b')


    recipe706 = Recipe(
        title='Parmesan Baked Olives - Easy Appetizer!',
        description=""" a crunchy shell of parmesan cheese filled with olives - doesn't that sound delicious?

- it certainly is!

Spoil your guests with this impressive, but easy to make fingerfood.

comes great with a glass of red wine or just as a snack for itself.

Only a few ingredients, about 30 minutes of your time

and your taste buds will be thrilled! - that's a promise!""",
        authorId=5,
        ingredientPhoto='https://content.instructables.com/ORIG/F5Z/EL5C/KNRGTACH/F5ZEL5CKNRGTACH.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=4812535626cf3fcdd6cd4e099bd9d907')
    
    recipe707 = Recipe(
        title='Grilled Ribeye With Mint Vinaigrette',
        description="""In this recipe you will be making a very good mint vinaigrette to enjoy with your grilled ribeye. I mean has mint, oil and vinegar ever been a bad combo? No! If you think that that is a great combo, start making this recipe right away and I know you will like it.""",
        authorId=12,
        ingredientPhoto='https://content.instructables.com/ORIG/FE9/4KFH/KQGMRBRN/FE94KFHKQGMRBRN.jpg?auto=webp&frame=1&width=678&height=1024&fit=bounds&md=a5e1e68c5bff75ce68995f2919a5c6ab')

    recipe708 = Recipe(
        title='Rigatoni With Sausage, Spinach, & Goat Cheese',
        description="""This creamy, tangy, and delicious Rigatoni with Sausage, Spinach, and Goat Cheese dish will quickly become a family favorite. This recipe has basic ingredients, but it turns into magic when the melted goat cheese brings them together. The whole meal can come together very quickly, so it’s great for a last-minute dinner. """,
        authorId=13,
        ingredientPhoto='https://content.instructables.com/ORIG/FJ8/DQLK/KKWL8KF2/FJ8DQLKKKWL8KF2.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=91c503cc91fba32a95d95a07bee4f7e9')

    recipe709 = Recipe(
        title='Best Ever Chocolate Chip Cookie Recipe',
        description="""The winning cookies taste like they came from a high-end bakery, I'm not even kidding you. But you can make them yourself - it's easy!

I tell you this, Instructables fans, I hesitated to share the results of this experiment with you. It is now one of the most potent tools in my recipe belt, and I have secretly entertained fantasies of launching my own bakery, based on the inspiration provided by this recipe alone. But alas, I already have an awesome job here at Instructables HQ, and it would be criminal of me to keep this secret to myself.

If you follow this recipe, you'll soon be known wide and far for your amazing chocolate chip cookie skills, and will be called upon to provide them at every function. I recommend making up a huge batch and storing them in the freezer. What could be better than surprising your guests with freshly-baked, bakery-quality chocolate chip cookies in fifteen minutes?

Nothing. That's what.""",
        authorId=14,
        ingredientPhoto='https://content.instructables.com/ORIG/FXM/0GPY/GD2J2URC/FXM0GPYGD2J2URC.jpg?auto=webp&frame=1&width=915&height=1024&fit=bounds&md=6aec64dc29532b4fd4810099d4c97778')

    recipe710 = Recipe(
        title='No Bake Halloween Bat Snack',
        description="""Bats! You can cut chocolate wafer cookies in half and stick them into pretty much anything and they'll look like bats. This is a super fast treat that requires no cooking- a 10 minute snack.

The first version I made used chocolate graham crackers but then I tried Keebler Deluxe Fudge covered graham crackers and they're just as delicious, though a little less “healthy”. """,
        authorId=12,
        ingredientPhoto='https://content.instructables.com/ORIG/FOH/QCA0/IUHMTP3R/FOHQCA0IUHMTP3R.jpg?auto=webp&frame=1&width=653&height=1024&fit=bounds&md=b48342912ebeca0f08111a50b3f38c7d')

    
    db.session.add(recipe701)
    db.session.add(recipe702)
    db.session.add(recipe703)
    db.session.add(recipe704)
    db.session.add(recipe705)
    db.session.add(recipe706)
    db.session.add(recipe707)
    db.session.add(recipe708)
    db.session.add(recipe709)
    db.session.add(recipe710)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()
