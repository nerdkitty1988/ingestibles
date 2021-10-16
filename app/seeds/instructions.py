from app.models import db, Instruction


# Adds instructions
def seed_instructions():
    instruction701 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/F0T/WZ6N/KTPSYXFI/F0TWZ6NKTPSYXFI.jpg?auto=webp&frame=1&width=523&height=1024&fit=bounds&md=9187be258aa7fa893dfc549851593b69",
        stepTitle="Prepare the Bottle",
        directions='''To start, you need a bottle that's big enough to hold 700mL of vodka plus all the things you will put inside. I used a 1 liter bottle that I had at home.

        If you don't have a good bottle to use, don't worry!

        You can pour your vodka into a pitcher and then only pour back what you can fit in the bottle.''')
    instruction702 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FUB/97EF/KTPSYXDA/FUB97EFKTPSYXDA.jpg?auto=webp&frame=1&width=558&height=1024&fit=bounds&md=531891c2eaada968b471e0488c91daad",
        stepTitle="Add Your Herbs",
        directions='''Now it's time to add the herbs.

This means add the galangal, lemongrass, tomato, chili, shallot, garlic, coriander, makrut leaf, and lime. This is the flavour of tom yum!

All you have to do is slice or smash everything to help release the flavours and so you can jam it into the bottle. I used my wooden pestle like a club, but you can use the side of a heavy knife, or karate.

Galangal - This is a root in the ginger family that smells amazing. In Thailand we use it in everything! If you can't find it fresh, DON'T use ginger because it will taste too weird. You can find dried galangal online and soak it in hot water to make it like new again!

Makrut lime leaf - This is also called kaffir lime leaf and you can usually find it frozen or dried. Frozen is better. Tear the leaf up to release its incredible scent!

Lemongrass - You can just use the softer, paler low part of the stem for a milder tste, or the leaves as well for something much stronger.

Shallot - I roasted my shallot over a burner first then peeled it and sliced it up. This gave the drink a slight smoky flavour, but it also tastes good raw.

Chilis - Put in as many as you want. One or two goes a long way, but it depends how hot you like it!
        ''')
    instruction703 = Instruction(
        recipeId=1,
        imageUrl="https://content.instructables.com/ORIG/FL2/ML9I/KTPSYXEC/FL2ML9IKTPSYXEC.jpg?auto=webp&frame=1&width=396&height=1024&fit=bounds&md=331b4c208276426bf5d7199473ac5d69",
        stepTitle="Add the Vodka and Wait...",
        directions='''...but not long.

Go ahead and pour the vodka into the bigger bottle, or back from your pitcher into the original bottle, whichever you used.

Now put it in a dark place so that light doesn't dull the colours or the flavour.

You'll be surprised - after just one day your tom yum vodka will taste and especially smell great!

When it's ready, you can keep it in the refrigerator in this bottle with all the herbs inside because they are so pretty. Or you can pour just the alcohol back into the original vodka bottle and it will last a lot longer.

I think you can sip this vodka all on its own, but you can also mix it to make drinks like the best bloody mary ever.

It looks great when you serve it to your friends with all the herbs still inside, especially with some Thai food.

Thanks and I hope you enjoy my recipe!
        ''')


    instruction701 = Instruction(
        recipeId=1,
        imageUrl="",
        stepTitle="",
        directions='''''')
    instruction701 = Instruction(
        recipeId=1,
        imageUrl="",
        stepTitle="",
        directions='''''')
    instruction701 = Instruction(
        recipeId=1,
        imageUrl="",
        stepTitle="",
        directions='''''')
    instruction701 = Instruction(
        recipeId=1,
        imageUrl="",
        stepTitle="",
        directions='''''')
   


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
