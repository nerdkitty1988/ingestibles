from app.models import db, Instruction


# Adds instructions
def seed_instructions():
    instruction1 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FT8/D0US/KUGYA4VW/FT8D0USKUGYA4VW.jpg?auto=webp&frame=1&fit=bounds&md=5208bb94e2aa9bdb2a68c7040b057950", stepTitle="Prepare the Meat", directions="This is a large piece of meat I'm working with and we need to do a little trick to season it properly from the inside. let's cut about 10 slices into the meat. Make sure you don't cut all the way through, the bottom has to stay intact.")
    instruction2 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FNX/H9CS/KUGYA4VX/FNXH9CSKUGYA4VX.jpg?auto=webp&frame=1&fit=bounds&md=9917f5f930438cb067714d99790465ac", stepTitle="Season the Meat", directions="Let's make the marinade first. simply mix 3-4 tbsp olive oil, 2 tsp red paprika, 1 tsp salt, 1 tbsp whole grain mustard, 3 tbsp soy sauce, 1 tbsp dijon mustard and 1 tsp pepper in a small bowl or cup. Then place the pork collar into a deep baking dish, pour the marinade over it and use your hands to properly coat the meat with the marinade.")
    instruction3 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FBS/GORU/KUGYA4VY/FBSGORUKUGYA4VY.jpg?auto=webp&frame=1&fit=bounds&md=26fe32d2f4e596829cb94efa4f117c35", stepTitle="Onion Base Now", directions="Remove the seasoned meat from the dish for a bit. Roughly chop/cut 5-6 smaller onions and add them to the baking dish. Spread them out evenly, to form a nice layer.")
    instruction4 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FXM/HUKY/KUGYA4VZ/FXMHUKYKUGYA4VZ.jpg?auto=webp&frame=1&fit=bounds&md=c7a92090d9566f2c8d5788304007034e", stepTitle="Time for the Bacon", directions="Place the meat back into the baking dish and insert a slice of smoked bacon into every cut that you have made previously. To make this dish more fragrant, season it with Italian seasonings. Secure the ends with a couple of toothpicks, so the meat doesn't 'open' too much while baking.")
    instruction5 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FEK/K17R/KUGYA4W0/FEKK17RKUGYA4W0.jpg?auto=webp&frame=1&fit=bounds&md=6caf43a787cf567688e3b56479d614bd", stepTitle="Time to Bake", directions="Cover the baking dish with aluminum foil and bake in the oven at 200-220C or 400-425F for about 90 minutes.")
    instruction6 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FOC/KKU2/KUGYA4W1/FOCKKU2KUGYA4W1.jpg?auto=webp&frame=1&fit=bounds&md=5f83fb387b7edc4234e2aa54beb28f4d", stepTitle="Time to Add Potatoes & Carrots", directions="""90 minutes later, the meat should be quite soft. Make a fork test, it should slide in easily. If it's not the case, give it 20 more minutes.

        Now cut a few carrots into bigger chunks and drop them into the baking dish, nicely around the meat. Next come the potatoes, place them over the carrots all over the meat again. Make sure to fill all the empty space. Season the potatoes with some olive oil, salt and pepper.

        Put the baking dish back into the oven, this time without the foil cover. Give it 45 or so more minutes so the potatoes bake fully too.""")
    instruction7 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/F03/WHTR/KUGYA4W3/F03WHTRKUGYA4W3.jpg?auto=webp&frame=1&fit=bounds&md=0dad81c5b5018bf27c0f18752e09adb4", stepTitle="We Are Done", directions="Once the meat is tender and potatoes catch some nice golden brown color, we are done and it's time to serve.")
    instruction8 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FKM/OLJI/KUGYA4W7/FKMOLJIKUGYA4W7.jpg?auto=webp&frame=1&fit=bounds&md=c9e64bde0b7c49942a95c294d18f7c71", stepTitle="Serving Time", directions="""Slice the meat now, go through the cuts we have made at the beginning. I like to use everything from the dish, including the onions and carrots, plus the potatoes of course. There is a lot of juices and drippings in the baking dish, make sure to use them! Pour a few tablespoons of this liquid goodness over the meat and potatoes.

        Thanks for reading,

        Matej.""")
    instruction9 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FDF/MOD6/KU9T4UR0/FDFMOD6KU9T4UR0.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=8677f6cfe5157c122a6e796133c93b06", stepTitle="Prep the Veggies", directions="Cut up the mushrooms, onions and jalapenos. The mushrooms and onions should be roughly the same size - at about a quarter-inch cubes. And the jalapenos should be about half of that.")
    instruction10 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FKC/ACN8/KU9T4UQV/FKCACN8KU9T4UQV.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=c86a342b05b91181b32ef1b29611f2d3", stepTitle="Cook the Meat", directions="In a large sauce pan over medium-high heat, add oil, onions and garlic. Cook for 3 minutes then add ground beef, red pepper flakes, salt, and jalapenos. Cook until no longer pink. Now is also a good time to get that griddle heating up to medium-high heat.")
    instruction11 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FLR/XB6L/KU9T4UQW/FLRXB6LKU9T4UQW.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=099d6a2c39ca108d13e51381b155f140", stepTitle="Make the Sauce", directions="Combine sauce ingredients in a bowl.")
    instruction12 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FNH/6O33/KU9T4UQY/FNH6O33KU9T4UQY.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=5d0dd38eaba6b1ae75e3c9d5971c438a", stepTitle="Build the Patty Melts", directions="""Build the sandwich – start with a slice of bread spread with sauce, add a slice of cheese, a portion of meat mixture, a slice of cheese, and a slice of bread. (See photo in post)

        I strongly suggest making all of the sandwiches before you start putting them on the griddle. This way everyone gets hot food at the same time.""")
    instruction13 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/F8L/5AL2/KU9T4UQU/F8L5AL2KU9T4UQU.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=3cdac686865097343273c576be3d7134", stepTitle="Get Cooking!", directions="Cook on griddle for 5 minutes on each side. Slice on the diagonal and serve up.")


    db.session.add(instruction1)
    db.session.add(instruction2)
    db.session.add(instruction3)
    db.session.add(instruction4)
    db.session.add(instruction5)
    db.session.add(instruction6)
    db.session.add(instruction7)
    db.session.add(instruction8)
    db.session.add(instruction9)
    db.session.add(instruction10)
    db.session.add(instruction11)
    db.session.add(instruction12)
    db.session.add(instruction13)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the instructions table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()
