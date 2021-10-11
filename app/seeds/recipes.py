from app.models import db, Recipe


# Adds recipes
def seed_recipes():
    recipe1 = Recipe(
        title='No-Bake Chocolate Cheesecake With Kit Kats', description="In this Instructable, I will show you how to make a no-bake chocolate cheesecake with Kit Kats from scratch. This easy cheesecake recipe is so awesome and doesn't have any eggs in it. If you love chocolate and you love cheesecake you have got to try this. It has four amazing layers, oreo cookie bottom crust, chocolate cheesecake filling, chocolate ganache on top of that, and then whipped cream and mini-chocolate chips. All surrounded by a layer of Kit Kats. A chocolate lover's dream cake. If I can do it, you can do it. Let's get started!", authorId=1)
    recipe2 = Recipe(
        title="Spirited Away Cake: No Face's Feast", description="""Hello!

If you've ever watched Hayao Miyazaki's award winning film "Spirited Away,' you might recall a certain food scene. In it, No-Face, a spirit, ravenously consumes pounds of delicious food in front of his hosts. Miyazaki is such a master with animated food I felt compelled to make a cake honoring such a fun scene.

Be warned though, this is not an easy cake! It took me wayyy to long to finish inbetween work and school. If anyone wants to re-create this, I have suggestions on each step to make the process a little easier. :)

Enough rambling, onto the cake!

(no-face drawing by Valentina Hramov)""", authorId=2)
    recipe3 = Recipe(
        title='HEALTHY VEGAN CREAMY MANGO TART NO-BAKE', description="""
        If you’re looking for a healthy dessert✨that tastes delicious😋, is easy to make, and will appeal to all eaters at the table, then this 🌱Vegan & Gluten Free Creamy Mango tart is for you!

This tart has a creamy 🥭mango-cashews filling with a 🥥coconut-almond crust.

Mango is:

A low-calorie fruit that is high in fibre 😀.
A good source of immune-boosting nutrients like Vitamins A and C.
A good source of antioxidants.
It’s a no-bake tart that anybody can master, and I’ll show you all the steps below.""", authorId=1)
    recipe4 = Recipe(
        title="3 Cheese ‘N Bacon Breakfast Cupcakes", description="I made a recipe similar to these unusual cupcakes years ago for a brunch. Everyone loved them and I decided that they would be perfect for the Instructables Cheese Speed Challenge! They feature 3 kinds of cheese....shredded cheddar, ricotta and cream cheese. These cheesy sweet and savory breakfast cupcakes are fun to make, fun to serve, fun to look at and fun to eat!", authorId=1)
    recipe5 = Recipe(
        title='Tom Yum Vodka', description="""I think by now, Thailand's famous Tom Yum Goong (hot and sour prawn soup) is a household name around the world. But this is more than just a soup. Tom yum's hot, spicy, sour, packed-with-herbs flavour is used in everything from potato chips to instant noodles.

So I had a stroke of genius.

Why not use this flavour to turn plain old vodka into a masterpiece?

The delicious, aromatic herbs give this drink a unique scent that you just can't find anywhere else, and chili and garlic a little some fire.

The best part?

It's so easy to make, you can have this recipe done in just 5 minutes today. And tomorrow, you can reap the reward of a delicious, sophisticated little beverage.""", authorId=1)
    recipe6 = Recipe(
        title='Halloween/ Harvest Chocolate Bark', description="""What did the dog say to make the squirrel run up the tree?... " Bark! Bark! Bark! "

Okay, I know that was pretty bad, but I promise you these are really, really good! They also make a great midday snack, or a nice little treat for family, friends, and co-workers.

Prep time: 30- 35 minutes""", authorId=2)
    recipe7 = Recipe(
        title='Homemade Twix Bars', description="""In this Instructable, I will show you how to make copycat Twix Bars at home. This homemade Twix candy bars recipe is so awesome and really easy to make. If you are a fan of Twix cookie bars you will love these homemade Twix. I love copycat recipes, and this is one of my favorites. If I can do it, you can do it. Let's get started!

Don't forget to follow me and check out my other Instructables.

Follow the easy steps below or watch the video tutorial or do both! :)""", authorId=2)
    recipe8 = Recipe(
        title='Rigatoni With Sausage, Spinach, & Goat Cheese', description='This creamy, tangy, and delicious Rigatoni with Sausage, Spinach, and Goat Cheese dish will quickly become a family favorite. This recipe has basic ingredients, but it turns into magic when the melted goat cheese brings them together. The whole meal can come together very quickly, so it’s great for a last-minute dinner.', authorId=3)
    recipe9 = Recipe(
        title='Skillet Ravioli Lasagna', description="""This one pot meal is the perfect dinner for a busy weeknight. It comes together easily, is extra tasty, and best of all the clean-up is super quick!

I love a good lasagna, but sometimes the effort seems like too much – this Skillet Ravioli Lasagna is a great alternative and really packs in the flavour of a traditional lasagna.

Note: This meal serves 6, so feel free to divide the recipe in half for a smaller portion or if you are concerned it won’t fit in your pan. It does require a large pan with high sides.""", authorId=3)
    recipe10 = Recipe(
        title='Five Bean Salad', description="""Who wants to cook in the summer, right? So what can we eat? Oh! Legumes!

Protein, fiber, vitamins and minerals!

Very healthy stuff! Combine a few of them and they are very colorful too.

This is a great salad for a summer barbecue. Or just eaten by itself because its packed with flavor. Also this salad is easy peasy especially if your just buying all the beans precooked in jars or cans. If you live in the Americas you will be extremely lucky to have at your disposal a limitless variety of beans or, as they are called in some parts, frijoles So go ahead and find a nice variety of beans to put in your salad, Hey! you might even make a Six Bean Salad but that would be an entirely different instructable""", authorId=4)
    recipe11 = Recipe(
        title='RECIPE |MANDARIN AVOCADO SALAD', description="""Spring is finally here! With 15 degree weather, I am forcing myself to believe that spring is here to stay even after that random snow storm we had last week. With Spring, comes warmer weather and cooler dishes like this Mandarin Avocado Salad. I've been trying to get back into my salad routine to cure my skin issues. After all, you are what you eat.

In the past year, my skin has rewound back to my teenage years when acne haunted me. I had awful cystic acne where I would get nasty volcano-like zits on my forehead, nose or chin. I was lucky in the fact that I didn't get a zillion red blemishes all over my face but life decided to be fair by giving me exactly that all over forehead along with little white bumps. At first I thought I wasn't cleaning off my makeup as well as I should, even though I would triple cleanse! (Yes triple cleanse with 3 different types of cleanser. Don't worry I've reduced that down to 2 cleansers now so I don't dry out my skin). Then I thought maybe there is too much oil in my diet but that wasn't it either. I swapped up my skin regime multiple times to figure out what was going wrong. I searched high and low for the answer and I finally figured it out. I found this YouTuber who explained that it was an fungal infection underneath my skin, hence the numerous white bumps that would turn into red little blemishes. The cause for the infection was an influx of yeast and sugars from white carbohydrates in my diet. It makes sense as I've been eating a lot more white carbs to replace my meat intake. Now don't get me wrong, not everyone will experience these same symptoms because every one is different. So please don't be convinced that you need to lower your carb intake and increase your meat intake. But I really needed to force myself to eat more whole grains not just white breads/pastas which is common sense. I am not just a fan of the taste in whole grains? Long story, short: I've returned back to eating more greens, fruits, and replacing white carbs with whole grain ones. So far, so good. My skin is clearing day by day!

So if you're also experiencing some skin issues, first think about what you eat. Do some research and try to understand what the cause is. I would say that 80% of our skin issues are based on our diet. Then to assist with the healing, look into active oils or serums that will speed up the healing process. But just remember you can apply all the serums in the world but if you eat garbage, it will still reflect on your skin. As they say, "Beauty comes from within."
Anyway I hope you guys give this salad a shot. It's one of my favourites and I used to eat it daily before my wedding and I remember having glowing clear skin! It's filled with Vitamin C, Folate, and antioxidants which fight the skin-villains. Easy, quick to make and wonderful for the new Spring season. In this recipe, I'm using the Super Greens salad box by Organic Girl which you can find at major Canadian grocers. If you do end up making this recipe, take a picture of it, tag @christieathome on Instagram and it may be featured. If you're not on Instagram please share this recipe with your family and friends!

Disclaimer: I am not sponsored by the companies listed in this post.""", authorId=5)
    recipe12 = Recipe(
        title='Sous Vide Smoked Brisket', description="""I love a well prepared smoked brisket, Southwestern-style. But, this is not your normal low and slow brisket. This brisket take around 52 hours to prepare and it is absolutely 100% worth the time.

It is juicy, soft, has a perfect smoke ring, brown/black crust and is really tasty.

And yes, I know my American friends, you are most probably laughing at this, but try it, you might just never look back again!!

You see, I do not have a proper smoke house to do this low and slow. What I do have is a Sous Vide stick. And boy, that Sous Vide works well.

If you do not know what a Sous Vide stick is, it is simply an immersion cooker. Google it and you will see what it looks like.

The basic idea is you vacuum seal your meat, place it in a water bath and set the Sous Vide stick to a very specific temperature for the cut of meat you are preparing and walla, perfect meat!!!""", authorId=5)

    db.session.add(recipe1)
    db.session.add(recipe2)
    db.session.add(recipe3)
    db.session.add(recipe4)
    db.session.add(recipe5)
    db.session.add(recipe6)
    db.session.add(recipe7)
    db.session.add(recipe8)
    db.session.add(recipe9)
    db.session.add(recipe10)
    db.session.add(recipe11)
    db.session.add(recipe12)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()
