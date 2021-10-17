from app.models import db, Instruction


# Adds instructions
def seed_instructions():
    jamiInstruction1 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FSA/3CUS/KN8W3OI0/FSA3CUSKN8W3OI0.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=56a6ec8de5a7f05b68e33474d636d7b5",
        stepTitle="The Tomatoes",
        directions="During the summer I'm too busy to make soup and sauce. So I freeze a lot of my tomatoes. I cut out the core and remove any blemishes. Even large cracks are no problem, just slice out the bad and freeze the rest. No blanching required. Leave the skin on as well. Its easy to keep up with the crop this way. The beets in the picture are for the soup, not the wine. Though they could add a unique color I'm sure.")
    jamiInstruction2 = Instruction(
        recipeId=19,
        imageUrl="",
        stepTitle="Step 2: Skin Removal",
        directions="The skin is easy to remove when the tomato is frozen. You run a bit of lukewarm water over it, and the skin lets go. Keeping the tomato frozen is key to not loosing the meat with the skin.")
    jamiInstruction3 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/F9H/UI6K/KN8W3QJC/F9HUI6KKN8W3QJC.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=07f3614e3efb526ee7024b05ac3bed85",
        stepTitle="Compost the Skins",
        directions="These are the skins from 40 liters of tomatoes. I don't plan on using them in my fermentation, so they just go into the compost.")
    jamiInstruction4 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/F76/IJ08/KN8W3QJD/F76IJ08KN8W3QJD.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=fc76cfa90fb2713e1edf0d87859efabe",
        stepTitle="Collect Liquid",
        directions="It will take a few days for the tomatoes to thaw. Once they do, they create lots of watery juice. To make soup, I don't want all this extra liquid. To boil it down is a waste of energy. Rather than tossing it out, I'm going to convert it into an amazing wine. I use a sieve spoon and large measuring cup to separate the solids from the juice.")
    jamiInstruction5 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FS4/5IWE/KNABJT3W/FS45IWEKNABJT3W.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=1a5c522fe6eeae7d0f3a09e3080f0ca7",
        stepTitle="The Hydrometer",
        directions="I use the potential alcohol scale when adding sugar. I want an 11% wine. I use the specific gravity to determine when the fermentation is done. When it reaches 0.990 the fermentation is done.")
    jamiInstruction6 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FLB/HXV6/KN8W3QX1/FLBHXV6KN8W3QX1.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=dfae2a67bef5c3bada5acb5641b4791d",
        stepTitle="Get the Specific Gravity Right",
        directions="This step is important. To get the alcohol content you want, you'll have to add sugar. I fill the pot and bring it to a boil. I dissolve two cups of sugar and let it cool till the next morning. When I check my possible alcohol, it registers 11%. Now I know how much sugar is required for each pot to create my juice. I boil each pot of juice to kill any wild yeasts as well as adding sugar. If the alcohol level is to low, I would dissolve more sugar and add it. If to high, I would make a new pot with less. It's not rocket science. There is an entire pail to work with so there are lots of chances to make adjustments.")
    jamiInstruction7 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FDK/ME6V/KN8W3REK/FDKME6VKN8W3REK.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=3abd6acc916d8af8875b973c296d7e5f",
        stepTitle="Prep the Yeast",
        directions="After the juice has cooled to room temperature, its time to get the fermentation started. I'm using Lalvin 1118 but I would have preferred Lalvin 1116. I find it to be a much gentler yeast. It works slower and makes a smoother wine. Due to COVID 19 I found it hard to find supplies in my area. I'm sure this will be fine though.  In a small bowl add 1/4 cup of warm water, slightly warmer than body temperature. Add the yeast and stir it around until it sinks into the liquid. In about 15 minutes it will come alive and start bubbling and foaming. This is when I pour in some of the juice. I leave it for another 15 minutes or so. These pics give a good idea of how the process works. If the yeast is expired it won't work, and you'll need to buy more. Always check the best before date when you buy it.")
    jamiInstruction8 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FAS/6SYV/KN8W3REJ/FAS6SYVKN8W3REJ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=3ce7d5b3e92c00d3b5c5021679b51486",
        stepTitle="Pitch the Yeast",
        directions="The juice must be put into a carboy before you pitch the yeast. A siphon hose is the easiest way to do this. Now that the yeast culture is working well, its time to add it into the carboy. Once the yeast culture is added, install an air lock. That's it, now you wait.")
    jamiInstruction9 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FNK/GCYF/KN8W3T80/FNKGCYFKN8W3T80.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=2c9d03af64a4a14de2aa866e581828d4",
        stepTitle="AAAAHHGH!!!",
        directions="Wow! I guess the yeast is working well. Glad I wrapped the towel around the base of the carboy")
    jamiInstruction10 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FEJ/1WR3/KN8W3TJB/FEJ1WR3KN8W3TJB.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=01b6d442784acedb3100a30386f35859",
        stepTitle="Create Some Air Space",
        directions="This should have been done earlier. Make sure you leave enough space at the beginning to avoid a mess. This will involve a gallon jug and another air lock. I knew this, but I was rushing yesterday and neglected to do it.")
    jamiInstruction11 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FDR/KMXU/KN8W3TT3/FDRKMXUKN8W3TT3.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=18e9755ea361fe5fd14632ca5b4ba7f6",
        stepTitle="Day 3",
        directions="This is day 3. The color is changing and bubbling isn't as vigorous.")
    jamiInstruction12 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FMV/987E/KN8W3TTK/FMV987EKN8W3TTK.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=da858f1e7b635f45762516dbbaab51b3",
        stepTitle="Day 7",
        directions="On day 7 the fermentation has pretty much stopped. The specific gravity is down to 0.990 so I think it's tome to kill it off and start the clearing. I crush and add 5 campden tablets to the carboy. I also pour in contents of the gallon jug. I use a piece of paper and a hammer to crush the tablets. Then pour the powder in. You can use the potassium metabisulphite powder, but the tablets make it easier to measure.")
    jamiInstruction13 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FSH/YUFI/KN8W3UMI/FSHYUFIKN8W3UMI.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=519e241a2b224b5e360e9577727bad75",
        stepTitle="Day 12",
        directions="I let the wine sit for 5 days. Now I'll siphon it over to a new clean carboy. I'll add 5 more crushed campden tablets to sterilize and neutralize the oxygen introduced while siphoning. Then replace the air lock.")
    jamiInstruction14 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/F2G/XUBR/KN8W3V78/F2GXUBRKN8W3V78.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=fad65e7fcca43bc740ffae7c53c854ab",
        stepTitle="Day 15 Filter Time",
        directions="Rather than wait for the wine to clear naturally, I'm going to filter it. I set up my filter machine, and a bucket with a few gallons of water sterilized with potassium metabisulphite. This will be used to clean my hoses, and soak my filter pads.")
    jamiInstruction15 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FT9/4BSA/KN8W3VQ6/FT94BSAKN8W3VQ6.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=445db3522da076322fe522853be0edc9",
        stepTitle="Sterilize",
        directions="I will soak the hoses, filter pads and brackets to sterilize them.")
    jamiInstruction16 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FN9/4PK3/KN8W3VZ2/FN94PK3KN8W3VZ2.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=8e49ec910800255fb6426a34ff2c8b2f",
        stepTitle="Assemble the Filter",
        directions="I now assemble the filter.")
    jamiInstruction17 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FPG/CNZ0/KN8W3W4D/FPGCNZ0KN8W3W4D.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=d5c1fd9a57e4c65363e333083a1ee698",
        stepTitle="Run the Filter",
        directions="To charge the filter, I circulate the sterile water mixture first. Then I transfer the siphon hose into the wine. I run the filter until wine comes out the exit hose. Then I transfer the exit hose to the empty carboy. I added a clamp to my filter. In the past I found it would leak around the edges without it.")
    jamiInstruction18 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FL5/X5TP/KN8W3XKC/FL5X5TPKN8W3XKC.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=a3001f09df4b3cd97e276b03a7e8d021",
        stepTitle="Filter With #1 Filter",
        directions="I filter the carboy with the #1 filter to remove the largest particles. As you can see the wine is still cloudy. The sediment left is from the past 3 days. I'll wash it out while #2 filters soak.")
    jamiInstruction19 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FMA/TJIM/KN8W3YKB/FMATJIMKN8W3YKB.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=7fdd56ec392b11468c341691b0664b8e",
        stepTitle="Soak Filter #2",
        directions="The #2 is a finer filter. I soak it and then swap out the #1's then continue filtering.")
    jamiInstruction20 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FOR/PWQ9/KN8W3YKD/FORPWQ9KN8W3YKD.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=a90178aa6d4422aea81738ee645c4343",
        stepTitle="Filter #2",
        directions="As you can see the wine is much clearer this round. No need to clean the carboy this time. But another filtration is needed.")
    jamiInstruction21 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FN2/5HPR/KN8W3ZVW/FN25HPRKN8W3ZVW.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=50694bc4fa1c818efd55e55229f4a304",
        stepTitle="Filter #3",
        directions="Filter #3 does a nice job of clearing this wine up to a crystal clear amber nectar.")
    jamiInstruction22 = Instruction(
        recipeId=19,
        imageUrl="https://content.instructables.com/ORIG/FLF/K7AS/KN8W40KX/FLFK7ASKN8W40KX.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=95c3d2bda526b17458782a704e8bbd61",
        stepTitle="Oh Yeah!",
        directions="Filtering is kind of cheating the process. It allows you to take a lot of waiting and siphoning out of the process. It could take a few months to achieve this kind of clarity. But you don't need a fancy filter to get there. Just patience. Wine also seasons with age. Although young wine like this is perfectly good to drink, you will want to stash a few bottles away for a year or two so you can enjoy a more interesting flavor profile.  If you have any questions don't hesitate to ask.  Cheers!")
    jamiInstruction23 = Instruction(
        recipeId=20,
        imageUrl="https://content.instructables.com/ORIG/FVK/VKT4/KNABJRMM/FVKVKT4KNABJRMM.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=49d185084ec84c04bda26032a133076d",
        stepTitle="Enjoy!",
        directions="This wine is quite nice. No one would ever guess it was made with tomatoes.")
    jamiInstruction24 = Instruction(
        recipeId=20,
        imageUrl="https://content.instructables.com/ORIG/FZ5/JK2Q/KIKA4K02/FZ5JK2QKIKA4K02.png?auto=webp&frame=1&width=400&fit=bounds&md=6ad949a89730fcb964c195e83e2999cb",
        stepTitle="Prep",
        directions="Start by prepping your milk. Mix 3/4 cup whole milk with 3/4 cup goat milk.  Put a little bit of your milk in a separate bowl and mix in 1 tbsp corn starch. Set this aside for later.  Now chop up your dark chocolate (so it melts easier).")
    jamiInstruction25 = Instruction(
        recipeId=20,
        imageUrl="https://content.instructables.com/ORIG/FBY/PDBB/KIKA4JZT/FBYPDBBKIKA4JZT.png?auto=webp&frame=1&width=400&fit=bounds&md=9b89836f25b267acbfa194c8206b0c58",
        stepTitle="Cook",
        directions="Over medium heat, mix your dark chocolate with a bit of your milk and stir till the chocolate is melted. Add in the rest of the milk, the corn starch mixture, 1/2 pod vanilla bean, 1 tbsp cocoa powder, 3 tbsp honey, 3 anise pods, and a pinch of salt.  Stir constantly until it reaches a thickness you like.")
    jamiInstruction26 = Instruction(
        recipeId=20,
        imageUrl="https://content.instructables.com/ORIG/FKX/MK13/KIKA4JZV/FKXMK13KIKA4JZV.png?auto=webp&frame=1&width=933&fit=bounds&md=d258a2fd268e12a33419cae0b087a209",
        stepTitle="Icing a Cup",
        directions="Take some white chocolate, and melt it down till its melted, but not too runny.  Grab your favorite drinking cup and glaze the rim with the white chocolate.")
    jamiInstruction27 = Instruction(
        recipeId=20,
        imageUrl="https://content.instructables.com/ORIG/FAV/NFH8/KIKA4JZY/FAVNFH8KIKA4JZY.png?auto=webp&frame=1&width=400&fit=bounds&md=2c3670dd36641e39d049a31ecea16221",
        stepTitle="Pour and Garnish",
        directions="Pour your hot chocolate into your cup. Garnish with whip cream and then top with some ancho chili.")
    jamiInstruction28 = Instruction(
        recipeId=20,
        imageUrl="https://content.instructables.com/ORIG/F65/IMP7/KIKA4JZZ/F65IMP7KIKA4JZZ.png?auto=webp&frame=1&width=933&fit=bounds&md=fff7c1f2b6f615dfe2520c1a27b56928",
        stepTitle="Enjoy!",
        directions="That's it! Easy! Delicious!  Now enjoy! The flavors in the hot chocolate, mixed with the ancho chili, blended with the white chocolate that melts as you drink the hot chocolate, all come together into one amazing cup of hot chocolate!")
    jamiInstruction29 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/FY6/30Y6/KQ57CNZ0/FY630Y6KQ57CNZ0.jpg?auto=webp&frame=1&width=300&height=1024&fit=bounds&md=b40d8f6568bccbb28b9164c3a16de02f",
        stepTitle="Make the Brownie Bases",
        directions="Place the chocolate, butter and caster sugar in a microwave safe bowl and heat in the microwave for 30 second bursts, stirring in between each burst until fully melted.  To add the eggs place them in a bowl and add a few spoons of the warm brownie mixture to the eggs and mix together then add it to the chocolate mixture. This helps to 'temper the eggs' to stop them from cooking if the mixture is too hot.  Then add the vanilla bean, bi-carb soda, salt and cocoa powder (sifted) and mix until it all comes together.")
    jamiInstruction30 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/F3H/J4A6/KQ57CO68/F3HJ4A6KQ57CO68.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e9ac6617af2a3ffd24951d157028a337",
        stepTitle="Bake the Brownies",
        directions="For these brownies you want to have a specific thickness so that all the ice cream fits into your pan. I am using a 20cm x 20cm x 5cm (8inch x 8 inch x 2 inch) square baking tin.  Then take 2 sheets of baking paper and cut them into long rectangles so that they can cross over each other in the pan. This will help lift out the brownies and ice cream sandwiches from the pan later.  Pour 1 and 1/3 cup of the brownie mixture into the brownie tin and spread it around the pan, then drag the knife through the mixture to even it out and remove any bubbles. Then place a square of baking paper over the top of the brownie mixture and this will help it bake evenly.  Preheat the oven to 170 degrees Celsius (340 degrees Fahrenheit) and bake for between 15-17 minutes.  When the brownies come out, while they are still hot press a tea towel over the top to make the brownie more dense and to even it out. Then let them cool for 15 minutes, remove the brownie from the pan and repeat this process to bake the other half of your ice cream sandwiches.  When they are both done place them in the freezer to cool while you make your ice cream.")
    jamiInstruction31 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/FOQ/AJZB/KQ57CO6V/FOQAJZBKQ57CO6V.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=a35d6023f5c91f1f7bade29e08240113",
        stepTitle="Make the Ice Cream",
        directions="To make the ice cream place your thickened cream and vanilla bean into a large bowl of a stand mixer with a whisk attachment on high until it reaches firm peaks (approx 90 seconds). Then add the cold sweetened condensed milk and salt and beat on high for a few minutes until light and fluffy with firm peaks.")
    jamiInstruction32 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/F39/C4Q8/KQ57CP0P/F39C4Q8KQ57CP0P.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=80637ed9d25186dd021053349ec53283",
        stepTitle="Colour the Ice Cream",
        directions="Separate the ice cream evenly into 5 separate bowls (roughly 1 and 1/3 cup each) and add food colouring until you reach a depth of colour you are happy with. Making red, yellow, green, blue and purple.  **Then place each colour in a separate piping or ziplock bag. To make this easier you can place the bag in a mug and stretch the bag over the mug. This helps keep the bag open while you pour in the ice cream.  I find putting it in the bags helpful for layering the ice cream later (you will see what i mean).")
    jamiInstruction33 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/FQC/C45Z/KQ57CPW9/FQCC45ZKQ57CPW9.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=b95566b46b2d2a0223c4f4ef47ba26c4",
        stepTitle="Layering the Ice Cream",
        directions="Take the brownies out of the freezer, making sure that it is cold before adding the ice cream (otherwise it may melt).  Start by piping the purple ice cream layer on the bottom brownie. By piping the ice cream across the brownie you can see the thickness of the layer and try to keep it more even. Then with a butter knife lightly run in along the pan in one direction then perpendicular at 90 degrees to 'cross-hatch' the ice cream. this helps to make it even and remove any air bubbles.  Then repeat the same piping and knife technique with the rest of the colours in the order of blue, green, yellow and red. ** You will see that the amount of ice cream and the thickness of brownies is made exactly for this pan. if you make your brownies too thick the ice cream may overflow out f the pan.  Then add the top layer of brownie on top of the ice cream roughly in the middle over the brownie base to line them up to top off the sandwich.  Then cover with glad wrap and place into the freezer for a minimum of 8 hours (i typically leave in the freezer over night or the day before i need them)")
    jamiInstruction34 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/FW1/NYE3/KQ57CQQL/FW1NYE3KQ57CQQL.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=efbd353d9b0f536029ed3e42f1ef52cb",
        stepTitle="Cut the Ice Cream Sandwiches",
        directions="Take the ice cream sandwiches out of the freezer and pull them out of the pan. Then run a hot knife under water and cut the sandwich in half. Make sure to run the knife under hot water in between each cut to make sure the colour stays beautiful and vibrant!  Then cut them into smaller bits to whatever size you like. Either 8 large slices or 16 smaller squares.  These are very rich so it might be better to make smaller ice cream sandwiches. Then individually wrap them in glad wrap and store in the freezer in a large zip lock bag for up to a month.")
    jamiInstruction35 = Instruction(
        recipeId=22,
        imageUrl="https://content.instructables.com/ORIG/FVA/3W9N/KNG1BIDT/FVA3W9NKNG1BIDT.jpg?auto=webp&frame=1&width=831&height=1024&fit=bounds&md=a05f6d84bed0bdebbaeb7db2462393d9",
        stepTitle="Prepare the Apples",
        directions="Cut apples into quarters and remove the seeds and cores.  Using cheese grater slicer, slice all apples as evenly as possible. They should all be uniformly thin.  Mix a good amount of food dye to 2 tablespoons of rose water and 2 cups of boiling water. Add to apples and Immediately cover and let sit for 20 minutes. Apples should be pliable.  Once apples are soft, lay them out on paper towels and pat dry.")
    jamiInstruction36 = Instruction(
        recipeId=22,
        imageUrl="https://content.instructables.com/ORIG/FFY/S117/KNG1B6DI/FFYS117KNG1B6DI.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=53f26c578b1f542eefa337907e8e6f58",
        stepTitle="Prepare the Pastry",
        directions="Cut puff pastry sheets into strips. If using Pepperidge Farms puff pastry sheets, one sheet will make 6 roses. Keep as cold as possible. It will be easier to handle.  Brush strips with melted butter, sprinkle with cinnamon and sugar, and add almond paste if you desire. You can substitute almond paste for jam.  Place apples on puff pastry. I used 8 slices per rose, but all apples are created different.  Fold the bottom half of pasty over the apples.  Brush the pastry again with a bit of butter, and sprinkle cinnamon and sugar.  Roll up to create a rose.  At this time, adjust the pedals to make it bloom and place in the fridge while you create the others.")
    jamiInstruction37 = Instruction(
        recipeId=22,
        imageUrl="https://content.instructables.com/ORIG/F3Q/PS2Y/KNG1B6DL/F3QPS2YKNG1B6DL.jpg?auto=webp&frame=1&crop=2:3&width=400&height=1024&fit=bounds&md=ff92092675748fa31ce6a3eb879ab8d8",
        stepTitle="Paint",
        directions="Once all roses are completed, Mix a teaspoon of vodka with food dye to create edible paints. Paint the base and inside of the rose. You don’t want any visible pasty showing. The bottom can be left unpainted.  Place all rolls in the refrigerator for 15 minutes.  Spray cupcake pan and add the Mourning buns.  Brush apples with lightly beaten egg wash  Bake at 400°F for 35 - 40 minutes. Lightly place tin foil on the apples during the last 15 minuets if cooking  Let cool and Enjoy.")
    jamiInstruction38 = Instruction(
        recipeId=23,
        imageUrl="https://content.instructables.com/ORIG/FWD/AII5/KNYM0P7Q/FWDAII5KNYM0P7Q.jpg?auto=webp&frame=1&crop=3:2&width=301&height=1024&fit=bounds&md=95021644262cad1a7b5b2cd4c4d2ee3a",
        stepTitle="Squeeze the Whey From the Curds",
        directions="Place a colander over your large bowl and lay 2 thin layers of cheesecloth over the colander. Pour 1lb of cottage cheese on your cheesecloth and squeeze your whey out. Squeeze as much whey as you can because the whey can cause crazy splattering when you fry your nuggets.Remember liquid and oil don't mix!!  Once your curds feel relatively dry, transfer them into a different bowl together with your other shredded cheese. Reserve the whey as you will using it to make the thick cheese sauce.  If you wish, you can add a few handful of chopped pepperoni. If you are a vegetarian, you can omit the meat altogether.  ")
    jamiInstruction39 = Instruction(
        recipeId=23,
        imageUrl="https://content.instructables.com/ORIG/FV9/CE36/KNYM0P8W/FV9CE36KNYM0P8W.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=cd2feeb3e6b20a6bda63930c418d060e",
        stepTitle="Make Your Cheese Sauce",
        directions="You will need about 1/2 cup of whey that you reserved earlier.  Place 1/2 a cup of whey into a small saucepot and heat on your stove at medium heat, or a microwave, until it is warmed up. Place five slices of American cheese inside your warm whey and reheat it again until the cheese is warm and melting. Use a whisk and whisk up the mixture until it resembles a thick cheese sauce .  Once thicken, remove from heat and let it cool down completely. It must be completely cool or it will melt the other cheeses. I place them in the freezer to hasten the cooling, ensure to whisk it occasionally.")
    jamiInstruction40 = Instruction(
        recipeId=23,
        imageUrl="https://content.instructables.com/ORIG/FZC/TD4F/KNYM0PA8/FZCTD4FKNYM0PA8.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=7467597723e6eca85a241225a1f6c713",
        stepTitle="Make the Nugget Filling",
        directions="First, mix in your cornstarch into your cooled cheese sauce. If you wish you can add a tablespoon of cayenne pepper for some heat. Then gradually add in your cheese sauce into your bowl of mixed cheeses. So slowly add them as you go.  Your filling should not be too runny, it should be able to hold it's shape despite looking shaggy and lumpy.")
    jamiInstruction41 = Instruction(
        recipeId=23,
        imageUrl="https://content.instructables.com/ORIG/FZY/J6PZ/KNYM0PC6/FZYJ6PZKNYM0PC6.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=99859d8480128547eda3bd28e9e92b76",
        stepTitle="Shape Them",
        directions="Using clean and dry hands, shape them into your desired shape. It can be as little or as big as you want. Tho I highly recommend you don't go any bigger than 2 inches as it will not cook and melt the cheese thoroughly while frying. Smaller is better.  Place them on a tray or a plate lined with parchment paper to prevent sticking.  Once complete, place them in the freezer for 5-10 minutes until firm and slightly harden. It doesn't have to freeze completely, just firm enough to work with.")
    jamiInstruction42 = Instruction(
        recipeId=23,
        imageUrl="https://content.instructables.com/ORIG/F8I/59HO/KNYM0PEF/F8I59HOKNYM0PEF.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=339170b3a3a0248fc8e3dff3d1ed4659",
        stepTitle="Breading Station",
        directions="Dredge your harden nugget into the flour. Followed by the egg wash coating and then to your breadcrumb mixture.  Repeat until you complete all of them.")
    jamiInstruction43 = Instruction(
        recipeId=23,
        imageUrl="https://content.instructables.com/ORIG/FVB/70F6/KNYM0PI2/FVB70F6KNYM0PI2.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=314f6a86ed82d8415fc843b424240b42",
        stepTitle="Fry Your Cold Nuggets",
        directions="Once the nuggets are cold and firmed up, you have a choice to either fry them immediately or neatly place them in freezer-safe bags for future use.  TO FRY:  In a medium pot or oil fryer, heat enough oil to deep fry them.  Heat your oil to about 300-325 degrees Fahrenheit.  Any lower, and your nuggets will sit in oil and get overly greasy.  Too hot, you risk burning your breadcrumbs even before getting a chance to thoroughly melt your cottage cheese.  Fry the nuggets within that temperature range, about 2 big nuggets at a time. Do not overcrowd your fryer. Fry them for approximately 3 minutes on each side. 6-10 minutes total.You want to fry them long enough that you give the cottage cheese time to melt properly and turn creamy, if not you be left with a very lumpy nugget.  Once fried, transfer them to a wire rack to drain off any excess dripping oil.  Serve immediately while hot.")
    jamiInstruction44 = Instruction(
        recipeId=24,
        imageUrl="https://content.instructables.com/ORIG/FRJ/QMEA/KN36CAG6/FRJQMEAKN36CAG6.jpg?auto=webp&frame=1&width=284&height=1024&fit=bounds&md=78e5419ea1f19ab3c4f8a02a997d4945",
        stepTitle="Cook Eggs",
        directions="Some people boil their eggs in a pot  Others even cook them in an Instant Pot(pressure cooker)  I have an egg cooker, and love it. I actually have two; this one is a little bigger and can do 10 eggs at once.  You place the eggs in the indentations, pierce the egg top with provided spike, add varying water amount to achieve soft to hard(it also poaches and cooks omelets), turn on and that's it. It automatically shuts off when water is gone.  I like to put them in a bowl of cold water, and place into fridge. This stops them from cooking any further.  I like medium-boiled for deviled eggs.  Peeling eggs  Tap eggs gently on a hard surface, all around the egg. Carefully pull away the egg shell. I would also recommend pulling away the thin membrane if you plan on dying them. Color comes out more consistent.  Slice eggs exactly in half, lengthwise.  Place yolks in a bowl, this will be used in the filling recipe.  Try to remove all of the yolk, as some left behind will also affect the dyeing process.")
    jamiInstruction45 = Instruction(
        recipeId=24,
        imageUrl="https://content.instructables.com/ORIG/F0G/0NIJ/KN36CAGF/F0G0NIJKN36CAGF.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=ee33fc41714e46a90adb7c78eecab14c",
        stepTitle="Dye Egg Whites",
        directions="Get 4 small bowls, glass or ceramic is best.  Add 10 drops of each color to each bowl, for purple 5 red and 5 blue.  Add 1 Tbsp of white vinegar, stirring, add enough water to fill bowl halfway. Stir.  Add 4-6 egg halves to each bowl. The eggs should be submerged; add more water if necessary.  Gently stir the eggs around. Do this occasionally, every few minutes.  For a light pastel, 5-10 minutes should be good(they will dry a little darker than they initially appear)  For a saturated color, it may take up to 30 minutes.  While waiting, let's make the filling....")
    jamiInstruction46 = Instruction(
        recipeId=24,
        imageUrl="https://content.instructables.com/ORIG/F3E/YPEB/KN36CAGY/F3EYPEBKN36CAGY.jpg?auto=webp&frame=1&width=300&height=1024&fit=bounds&md=edbe0f4e22546f03d32dcb46d2e3c9cc",
        stepTitle="Puree Chickpeas",
        directions="Besides just the yolks and mayo/mustard, you'll also add chickpeas and... vodka!  If you don't want the vodka thing, you can also use pre-made hummus instead. : )  First puree the chickpeas. I used a magic bullet. There is not enough moisture in the chickpeas, so you need 2 oz of liquid, or vodka to produce a creamy puree.")
    jamiInstruction47 = Instruction(
        recipeId=24,
        imageUrl="https://content.instructables.com/ORIG/FIY/VIT0/KN36CAH5/FIYVIT0KN36CAH5.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=e4206d6d8ffffdd2d91a6eafeb28588b",
        stepTitle="Make Egg Filling",
        directions="Mash up egg yolks. A pastry blender or two folks works well.  To that add 1/4 cup of mayo. I used Primal Kitchen's chipotle lime.  Add 2 Tbsp of Dijon mustard  And add two pinches of salt  Combine thoroughly")
    jamiInstruction48 = Instruction(
        recipeId=24,
        imageUrl="https://content.instructables.com/ORIG/FXK/5TIY/KN36CAHP/FXK5TIYKN36CAHP.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=dccbd52b84b71e840286ca85ba265721",
        stepTitle="Combine Mixtures, Add Kimchi, Chill",
        directions="Now combine the chickpea and the yolk mixtures  Some people add pickles to deviled eggs, I thought mild kimchi would be nice, and extra nutritious.  Chop the kimchi so that all the strands are small bits  Add to filling  If you need to put in fridge because you are doing this ahead of when you need them, place saran wrap over the mixture, touching it, and secure around bowl.  Eggs should be nice and dark at this point...")
    jamiInstruction49 = Instruction(
        recipeId=24,
        imageUrl="https://content.instructables.com/ORIG/FV5/8479/KN36CAIL/FV58479KN36CAIL.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=b3e17aea915e988dd7d7a5f1065ef76b",
        stepTitle="Dry Eggs and Fil",
        directions="Allow the excess water from the eggs to be absorbed by a couple of paper towels.  I did this the night before, so I also covered with saran and put them in the fridge. No problems, dyed looked just the same.  You should not make the deviled eggs too far ahead of when you'll be serving them to your guests. Best to fill the bottoms with the filling no more than one hour before serving, then pop in fridge for 1/2 hour.  You want to put something on the serving plate so the eggs won't slide around.  I used shredded coconut. (You can save it after, no reason to throw away, though I did put it in the fridge)  It looked beautiful and did the trick!  For a final detail I sprinkled chipotle chili powder on top.  Looks like paprika but gives a tiny kick.  My family loved them, and these would be a big hit at a spring-themed party.  Now that you know how easy it is to dye the whites, inspiration abounds! You could adapt these for any season or holiday, changing up the color schemes to fit.")
    jamiInstruction50 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/FP0/VTXD/KFZEJGHN/FP0VTXDKFZEJGHN.png?auto=webp&frame=1&width=301&fit=bounds&md=bb173449736f8e8eb8fccbdc25e2048d",
        stepTitle="Making the Tuna Mousse",
        directions="Put 400gr of tuna, a handful of washed and squeezed salted capers, 7 pitted olives and 3-4 anchovy fillets in a mixer. Mix everything together until you get something like the fourth photo.")
    jamiInstruction51 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/F2N/FEMO/KFZEJGHX/F2NFEMOKFZEJGHX.png?auto=webp&frame=1&width=383&fit=bounds&md=21e5cada6ce7a31ed890849214575195",
        stepTitle="Adding Potatoes",
        directions="I prefer not to blend the potatoes. Instead, I crush them with a fork, but you can use a potato masher if you like. When you're done, add a pinch of salt (not too much, because the tuna condiment is pretty salty already!), then mix it with the tuna mousse using a fork or a spatula. If you want and you like, you can add a few more capers in this step.")
    jamiInstruction52 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/F4O/BCWD/KFZEJGI7/F4OBCWDKFZEJGI7.png?auto=webp&frame=1&width=404&fit=bounds&md=8d86b5424e5bb85685371a0223751d0f",
        stepTitle="Getting Hands Dirty!",
        directions="What you have to do now is to free your imagination! Put the dough on a plate and try shaping it like a fish. I suggest you to moisten your hands, so the surface will turn out smoother. If you want, you can also use a straight knife to shape the fish even better :)")
    jamiInstruction53 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/FD6/1AC4/KFZEJGIP/FD61AC4KFZEJGIP.png?auto=webp&frame=1&width=296&fit=bounds&md=bbf5a7067a57cdc6d2cf648c6647ac45",
        stepTitle="Adding Mayonnaise Glaze",
        directions="It is now time to cover the fish with mayonnaise! You don't have to make a shiny surface, because we'll be covering it with more decoration!")
    jamiInstruction54 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/FD9/R34H/KFZEJGGA/FD9R34HKFZEJGGA.png?auto=webp&frame=1&width=388&fit=bounds&md=2460eb5dad6c9d98982778c746398f02",
        stepTitle="More Mayo Decoration!",
        directions="Using a tube of mayonnaise, we can now highlight the shape of the fish and make a few more decorations. I suggest you to cover the side too, using the tip of a knife to join each 'strip' of mayo.")
    jamiInstruction55 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/FYG/3KLQ/KFZEJGGS/FYG3KLQKFZEJGGS.png?auto=webp&frame=1&crop=3:2&width=394&fit=bounds&md=0fcf04b7155aabfd55a6dea1107731df",
        stepTitle="Adding Peppers and Olives",
        directions="It is now time to add pickled peppers and olives to further decorate the fish. Cut them to the appropriate shapes in order to fit them inside the mayo scales you made in the previous step.")
    jamiInstruction56 = Instruction(
        recipeId=25,
        imageUrl="https://content.instructables.com/ORIG/FOE/H72C/KFZEJGHE/FOEH72CKFZEJGHE.png?auto=webp&frame=1&width=789&fit=bounds&md=5a040e379a97428e9b9cabb26280f72a",
        stepTitle="Done!",
        directions="Your fish-shaped potato mash and tuna is finished! Time to finally eat it! Mmmmh, delicious!!!  I hope you had fun following this recipe, let me know if you make your own :)")
    jamiInstruction57 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/FHV/WCVP/KAB2MKY8/FHVWCVPKAB2MKY8.png?auto=webp&frame=1&fit=bounds&md=6c2a8ac7f32fcfca87b6d08aba39bbc9",
        stepTitle="Bake the Brioche Buns",
        directions="Using a stand mixer with the whisk attachment, whisk the milk, butter, sugar and yeast. Add eggs and whisk until combined.  Change out the whisk for the dough hook. Add the flour and salt and mix on low-medium for 8-10 minutes. The dough should appear sticky, soft and smooth but come away from the bowl.  Cover the bowl with cling wrap and place in a warm area. Let the dough rise for 1-2 hours or until doubled in size. Once risen, punch the dough to deflate.  Lightly flour your work space and scrape out the dough. Divide into 8 pieces and shape each one into buns by rolling into balls.  On a large baking tray lined with baking paper, arrange the buns, making sure none are touching. Cover with a towel and let rise again in a warm area for 30 minutes to an hour or until they've risen and puffed up a little.  Use this time to preheat the oven to 200°C/400°F.  Before placing in the oven, whisk together the yolk with 1 tsp of water and brush over the tops of the buns. Sprinkle on the sesame seeds if using.  Bake for 15 minutes or until golden. Let the buns cool on a rack before assembling burgers.")
    jamiInstruction58 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/FHS/J1ED/KA9N97IN/FHSJ1EDKA9N97IN.png?auto=webp&frame=1&width=600&fit=bounds&md=e0c67709a9f51cb1e0892c7bccef8f62",
        stepTitle="Make the Burger Sauce",
        directions="Mix all the ingredients together in a small bowl.  Either serve immediately or spoon into a jar and place in the fridge for at least an hour for the flavours to work their magic.")
    jamiInstruction59 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/F7E/ICZE/KA9N985H/F7EICZEKA9N985H.png?auto=webp&frame=1&width=600&fit=bounds&md=a37be3524bdb1d998790986bb4a6b66c",
        stepTitle="Pickle the Onion",
        directions="Thinly slice the red onion.  Combine the vinegar, water, salt and sugar in a small bowl.  Scrunch the onion slices in your hand before transferring to the bowl and mixing all together.  Allow to rest for 30 minutes before serving.")
    jamiInstruction60 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/FCW/IKPB/KA9N98B4/FCWIKPBKA9N98B4.png?auto=webp&frame=1&width=400&fit=bounds&md=5f9e659b60fdeeef5e1d09c3e9619313",
        stepTitle="Make the Beef Patties",
        directions="Divide the mince into 4 portions. Without handling the beef too much, shape each portion into plump balls. Try not to take too long doing this as the more you shape them, the tougher they will be.  Generously sprinkle salt and pepper onto both sides of the balls.  Using a large fry pan on medium high, heat a drizzle of oil.  Once the oil is hot, place all the balls in the fry pan. Using a burger press or potato masher, press down on each patty until thin. The patties won't be perfectly round, but the craggily bits that form will get crispy and give the patty extra texture and flavour.  Fry on one side for about 3-4 minutes before flipping. The second side should take 2-3 minutes to cook.  In the last 30 seconds, place a slice of cheese on top of each patty and let it melt.  Once cooked, rest patties on a plate for a few minutes before assembling the burgers (or add straight to the bun and eat immediately for a super juicy burger)")
    jamiInstruction61 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/FC6/DF2A/KAB2MG2T/FC6DF2AKAB2MG2T.png?auto=webp&frame=1&fit=bounds&md=9409c148711bba3a0105cb33dac405f4",
        stepTitle="Assemble the Burger",
        directions="As a frequent burger maker, I feel I have somewhat perfected the art of assembling a burger that prevents spillage of the filling and soaking of the bun. The above order of ingredients is my own personal favourite method of assembly, but really, it doesn't matter that much. Burgers aren't fancy French pastries that require strict measurements and steps, so go ahead and just build that burger. You know it's going to be good regardless!")
    jamiInstruction62 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/FZQ/81F0/KAB2MHTG/FZQ81F0KAB2MHTG.png?auto=webp&frame=1&fit=bounds&md=476a53b82f40b10afd80853fe0d4c1f5",
        stepTitle="Bake the French Fries",
        directions="Peel all the potatoes and then slice into wedges or medium sized strips  Place all the cut potatoes in a large bowl and add enough water to cover them. Soak the potatoes for 20 minutes (Soaking gets rid of some of the starch and results in crispier fries).  While you wait for the potatoes to soak, preheat the oven to 200°C/400°F and line two large baking trays with baking paper.  Once soaked, rinse the potatoes and thoroughly dry them by patting them down with a tea towel.  Transfer to the large bowl and drizzle a generous amount of oil and a good sprinkling of salt and pepper. Use your hands to mix everything up and ensure all the potatoes are covered in oil.  Spread the fries over the two baking trays, making sure to leave space between each one for maximum crispiness.  Bake in the oven for 25-35 minutes or until golden and crunchy. Don't forget to take them out about halfway through to flip as this ensures even browning of the fries.  Before serving, toss the fries in more salt or any other seasonings of choice.")
    jamiInstruction63 = Instruction(
        recipeId=26,
        imageUrl="https://content.instructables.com/ORIG/FRY/JA3V/KAB2MITG/FRYJA3VKAB2MITG.png?auto=webp&frame=1&fit=bounds&md=065dd9cdedcddaf35edb795def78bbb5",
        stepTitle="Blend the Chocolate Milkshake",
        directions="In the jug of a milkshake maker or blender, add the milk, ice-cream and a large drizzle of chocolate syrup.  Blend until there are no more lumps and the milkshake is frothy.  In your serving glass, drizzle the chocolate syrup all around the inside before pouring the milkshake in.  Top with a squirt of whipped cream and a maraschino cherry (or two).")
    jamiInstruction64 = Instruction(
        recipeId=27,
        imageUrl="",
        stepTitle="Preparing the Tomatoes",
        directions="")
    jamiInstruction65 = Instruction(
        recipeId=27,
        imageUrl="https://content.instructables.com/ORIG/F9Y/1R5V/KQQMU1KN/F9Y1R5VKQQMU1KN.jpg?auto=webp&frame=1&width=580&height=1024&fit=bounds&md=5e0397a6b3c7b5604e84f1ae4a121c1e",
        stepTitle="Preparing the Tomatoes",
        directions="Preheat the oven to 400°F or 200°C  Rinse and dry the tomatoes.  Slice off the top of each to make a lid and set these to one side.  Using a teaspoon, carefully remove the inside of each tomato,  Place the tomato shells onto a buttered heat-proof dish.")
    jamiInstruction66 = Instruction(
        recipeId=27,
        imageUrl="https://content.instructables.com/ORIG/FI7/HX87/KQQMU1QP/FI7HX87KQQMU1QP.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=818964d932768762dd21d961c96531c2",
        stepTitle="Preparing the Filling",
        directions="Sauté the red onion until it begins to soften. Add the chopped interior of the tomato and let this simmer briskly until it loses most of its liquid.  Split the skins of the sausage and add the meat to the pan and cook these until the sausage meat has browned and the sauce has thickened.  Add the herbs and mix well.")
    jamiInstruction67 = Instruction(
        recipeId=27,
        imageUrl="https://content.instructables.com/ORIG/F3L/WJZB/KQQMU1RA/F3LWJZBKQQMU1RA.jpg?auto=webp&frame=1&crop=3:2&width=378&height=1024&fit=bounds&md=c7a06bddf218a546e6ba745563b5d7a3",
        stepTitle="Filling, Cooking, Enjoying!",
        directions="Using a teaspoon stuff each tomato with the filling.  Put a 'lid' onto each tomato.  Place in the oven for 10 minutes or until the cherry tomatoes are cooked.  Allow them to cool slightly if you are taking them straight to the table. Tomatoes hold their heat too well!  Enjoy!")
    jamiInstruction68 = Instruction(
        recipeId=28,
        imageUrl="https://content.instructables.com/ORIG/FPV/HIBT/JGGTG029/FPVHIBTJGGTG029.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=1f457af2ae142af8cae32f8ef6e58360",
        stepTitle="Boil",
        directions="Mix the water and agar in a pot, bring it to a boil, and let it boil for 30 seconds. Take the pot off the heat, and let the bubbles escape. Skim off any foam from the top.  Let the liquid cool till it stops steaming. This will make it easier to coat the parchment paper evenly. Pour the liquid onto a baking sheet with parchment paper and quickly tilt it to distribute the liquid in an even, thin layer.  Set the baking sheet aside, and let the plastic dry for at least 24 hours or more.  NOTE: I have tried both pouring the plastic onto aluminum foil and directly onto a plate, and neither worked as the plastic stuck. Parchment paper is the way to go.")
    jamiInstruction69 = Instruction(
        recipeId=28,
        imageUrl="https://content.instructables.com/ORIG/FFV/WL3Y/JGGTFX58/FFVWL3YJGGTFX58.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=865231e593d5a699ce1ac2693d8118e3",
        stepTitle="Cut",
        directions="When the plastic is completely dry, it should peel off easily. Carefully remove it from the parchment paper. Trim the edges, and cut the plastic into appropriately sized squares.")
    jamiInstruction70 = Instruction(
        recipeId=28,
        imageUrl="https://content.instructables.com/ORIG/FR6/FRG9/JGGTFZRA/FR6FRG9JGGTFZRA.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=45f3aa01a378c6d1fd8ff4bece07b975",
        stepTitle="Fill",
        directions="Put your desired filling (I used trail mix) onto one half of a piece of plastic, and check to see that the other half can be folded over to close the pocket.  Brush some water around the edges of one half of the plastic, and fold over the other half, pressing on the edges to adhere. If the edges do not adhere very well, try folding the edges to secure the filling better.  Let the seams dry for half an hour before packing and enjoying the little pouches.")
    jamiInstruction71 = Instruction(
        recipeId=28,
        imageUrl="https://content.instructables.com/ORIG/FLK/356K/JGGTFXAM/FLK356KJGGTFXAM.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=f88b571bb1447090f138c92c08d1cc88",
        stepTitle="Verdict",
        directions="VERDICT:  Taste: I think these trail mix pouches actually taste quite good, even though they challenge the sensory experience of eating trail mix a bit. The first impression is that you are stuffing, well, plastic in your mouth, and the plastic can have a very slight salty flavor from the agar, but as soon as you start chewing, the plastic disappears, and you get all the goodness from the trail mix. If you really think about it, the edible plastic adds a slight, chewy gummy-bear texture in the background, but it goes perfectly with the dried fruit.  Durability: The plastic holds up pretty well to scrunching, even though it may rip in areas that are very thin. However, the seams are a bit fragile and can easily open so that trail mix falls out. Also, the plastic is sensitive to humidity. So I probably wouldn't stuff these goodie bags in the kids' pockets if I knew they were going to play in the rain or stick their hands in the pocket a thousand times to feel if the treat is still there (even though I think I might actually slip one of these in my own pocket, hmmm, but for the kids, maybe put it as a surprise in the sack lunch for school). I think the best way to store and carry these plastic pockets with trail mix would be in a real food-grade plastic bag or container.  I hope you liked this instructable! If you did, please vote for me in the Science of Cooking contest and Pocket-Sized contest. Thank you! Also, if you try this out, please share the result and any modifications in the comments!")

    instruction50101 = Instruction(
        recipeId=11,
        imageUrl="https://content.instructables.com/ORIG/FLR/R3EN/IBM254HX/FLRR3ENIBM254HX.jpg?auto=webp&frame=1&fit=bounds&md=423007502182c04a377df3c7240a85e7", stepTitle="Dice the Tomatoes", directions="""
            Start with a large Roma tomato.

            Use a sharp knife to slice the tomato lengthwise into quarters.

            Use your knife and remove the seeds from each tomato quarter.

            Take each tomato quarter and slice it lengthwise into at least five strips.

            Rotate the sliced tomato quarter horizontally and cut the strips into a dice.

            Repeat for all of the tomatoes :)

            For this recipe I used three large Roma tomatoes.
        """)
    instruction50102 = Instruction(
        recipeId=11,
        imageUrl="https://content.instructables.com/ORIG/F9C/HB5S/IBM250ND/F9CHB5SIBM250ND.jpg?auto=webp&frame=1&fit=bounds&md=6c87d6389a05d75e0c74619a3de9e472", stepTitle="Prepare the Bruschetta Mix", directions="""
            This part is really easy!

            Placed your diced tomatoes into a bowl.

            Add two tablespoons of extra virgin olive oil.

            Add three tablespoons of shredded Parmesan cheese.

            Add three tablespoons of diced/shredded cilantro.

            Add 1 teaspoon of garlic powder or two teaspoons of diced roasted garlic

            Mix everything up with a spoon and smile!

            Note: Traditional bruschetta uses fresh basil instead of cilantro. We used cilantro since we had a "bunch" on hand for the guacamole.
        """)
    instruction50103 = Instruction(
        recipeId=11,
        imageUrl="https://content.instructables.com/ORIG/FZY/1NJK/IBM250PI/FZY1NJKIBM250PI.jpg?auto=webp&frame=1&fit=bounds&md=790d9aa6830bd08df050af69d1d6b65d", stepTitle="Prepare the Guacamole", directions="""
            This is another really easy step!

            Slice open two avocados and use a spoon to scoop the fruit away from the skin.

            Place the avocado into a bowl and remove the big seeds!

            To the avocados add the following:

                Juice of two fresh limes
                3 tablespoons diced/shredded cilantro
                1 teaspoon kosher salt
                1 teaspoon garlic powder
                1/4 teaspoon cayenne pepper
                Now mash it all together until smooth!

            Note: Traditional guacamole would also include a small diced red onion. I don't like raw onions so I don't add them to my guacamole!
        """)
    instruction50104 = Instruction(
        recipeId=11,
        imageUrl="https://content.instructables.com/ORIG/FLJ/75ZH/IBM250PJ/FLJ75ZHIBM250PJ.jpg?auto=webp&frame=1&fit=bounds&md=86b352d519127646d69c517db940ad67", stepTitle="Toast the Bread and Assemble", directions="""
            Slice a loaf of French bread on a diagonal for bite sized toasts.

            Brush each side of the bread with olive oil.

            The olive oil adds flavor and helps the bread look beautiful after toasting!

            Toast the bread on your grill over High heat.

            Do your toasting with the lid up and pay attention! It is easy to go from "beautifully toasted" to "burnt to a crisp".

            Depending upon your grill you will need to toast for about three minutes per side.

            You could also do this in the oven using the broiler. You know...just in case it's raining or something :)

            Remove the toasted bread from the grill.

            Spread a layer of the fresh guacamole onto the toast.

            Pile the fresh bruschetta on top of the guacamole.

            Take a big bite and smile!

            I hope you enjoyed this Instructable! I would appreciate any votes you are willing to provide!
        """)

    instruction50201 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FT8/D0US/KUGYA4VW/FT8D0USKUGYA4VW.jpg?auto=webp&frame=1&fit=bounds&md=5208bb94e2aa9bdb2a68c7040b057950", stepTitle="Prepare the Meat", directions="This is a large piece of meat I'm working with and we need to do a little trick to season it properly from the inside. let's cut about 10 slices into the meat. Make sure you don't cut all the way through, the bottom has to stay intact.")
    instruction50202 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FNX/H9CS/KUGYA4VX/FNXH9CSKUGYA4VX.jpg?auto=webp&frame=1&fit=bounds&md=9917f5f930438cb067714d99790465ac", stepTitle="Season the Meat", directions="Let's make the marinade first. simply mix 3-4 tbsp olive oil, 2 tsp red paprika, 1 tsp salt, 1 tbsp whole grain mustard, 3 tbsp soy sauce, 1 tbsp dijon mustard and 1 tsp pepper in a small bowl or cup. Then place the pork collar into a deep baking dish, pour the marinade over it and use your hands to properly coat the meat with the marinade.")
    instruction50203 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FBS/GORU/KUGYA4VY/FBSGORUKUGYA4VY.jpg?auto=webp&frame=1&fit=bounds&md=26fe32d2f4e596829cb94efa4f117c35", stepTitle="Onion Base Now", directions="Remove the seasoned meat from the dish for a bit. Roughly chop/cut 5-6 smaller onions and add them to the baking dish. Spread them out evenly, to form a nice layer.")
    instruction50204 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FXM/HUKY/KUGYA4VZ/FXMHUKYKUGYA4VZ.jpg?auto=webp&frame=1&fit=bounds&md=c7a92090d9566f2c8d5788304007034e", stepTitle="Time for the Bacon", directions="Place the meat back into the baking dish and insert a slice of smoked bacon into every cut that you have made previously. To make this dish more fragrant, season it with Italian seasonings. Secure the ends with a couple of toothpicks, so the meat doesn't 'open' too much while baking.")
    instruction50205 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FEK/K17R/KUGYA4W0/FEKK17RKUGYA4W0.jpg?auto=webp&frame=1&fit=bounds&md=6caf43a787cf567688e3b56479d614bd", stepTitle="Time to Bake", directions="Cover the baking dish with aluminum foil and bake in the oven at 200-220C or 400-425F for about 90 minutes.")
    instruction50206 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FOC/KKU2/KUGYA4W1/FOCKKU2KUGYA4W1.jpg?auto=webp&frame=1&fit=bounds&md=5f83fb387b7edc4234e2aa54beb28f4d", stepTitle="Time to Add Potatoes & Carrots", directions="""90 minutes later, the meat should be quite soft. Make a fork test, it should slide in easily. If it's not the case, give it 20 more minutes.
        """)
    instruction50207 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/F03/WHTR/KUGYA4W3/F03WHTRKUGYA4W3.jpg?auto=webp&frame=1&fit=bounds&md=0dad81c5b5018bf27c0f18752e09adb4", stepTitle="We Are Done", directions="Once the meat is tender and potatoes catch some nice golden brown color, we are done and it's time to serve.")
    instruction50208 = Instruction(
        recipeId=12,
        imageUrl="https://content.instructables.com/ORIG/FKM/OLJI/KUGYA4W7/FKMOLJIKUGYA4W7.jpg?auto=webp&frame=1&fit=bounds&md=c9e64bde0b7c49942a95c294d18f7c71", stepTitle="Serving Time", directions="""Slice the meat now, go through the cuts we have made at the beginning. I like to use everything from the dish, including the onions and carrots, plus the potatoes of course. There is a lot of juices and drippings in the baking dish, make sure to use them! Pour a few tablespoons of this liquid goodness over the meat and potatoes.

        Thanks for reading,

        Matej.""")
    instruction50301 = Instruction(
        recipeId=13,
        imageUrl="https://content.instructables.com/ORIG/FM5/Y8BG/IJRFGQNY/FM5Y8BGIJRFGQNY.jpg?auto=webp&frame=1&fit=bounds&md=1531abdddefa403cc4a0ff1f2ebc9557", stepTitle="Melt the Chocolate", directions="""
            Melt the chocolate in the top of a double boiler, or by placing it in a heatproof bowl and microwaving in 15-second blasts until the chocolate is mostly melted. Once the chocolate is mostly melted, stir it gently; the remaining bits should melt in the residual heat. Let the melted chocolate cool for 5-10 minutes. While it cools, line the inside of six small bowls with plastic wrap, pressing the plastic wrap in as smoothly as you can to smoothe it into the shape of the bowl (a few small wrinkles are OK). Use enough plastic wrap so that it slightly hangs over the sides, which will make removal easier later. If you don’t have six bowls for molding, this is ok: you can make the chocolate bowls a few at a time and re-use the same molding bowls.
        """)
    instruction50302 = Instruction(
        recipeId=13,
        imageUrl="https://content.instructables.com/ORIG/FX7/NQSM/IJRFGPRT/FX7NQSMIJRFGPRT.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=433e62a28bd07e5aaf1b8666f32fc135", stepTitle="Brush the Chocolate on the Plastic", directions="""
            Using either your small spatula or pastry brush, spread a thin and even layer of chocolate inside of the plastic wrap lining each of the molding bowls, taking special attention to spread the chocolate on the sides. Don’t go too nuts: you’ll put a second layer of chocolate in the bowls, so only use about ½ of the melted chocolate for this step. Once you’ve put a layer of chocolate in each plastic-lined bowl, place them in the refrigerator for about 10 minutes. This will help them “set”.
        """)
    instruction50303 = Instruction(
        recipeId=13,
        imageUrl="https://content.instructables.com/ORIG/FXZ/3XSR/IJRFGPQ6/FXZ3XSRIJRFGPQ6.jpg?auto=webp&frame=1&fit=bounds&md=6196c58008ddb60275b9de218c705de4", stepTitle="Add Another Layer of Chocolate and Chill", directions="""
            After 10 minutes, remove each bowl unit from the refrigerator. The initial layer of chocolate should be firm and look slightly matte. Brush the inside of each bowl with another layer of chocolate, once again giving special attention to the sides of each bowl.Return the molding bowls to the refrigerator, and let them set for 10-15 minutes. Remove from the refrigerator, and use the plastic wrap overhanging the sides to pull out the chocolate bowl from the molding bowl. As gently as possible, peel the plastic wrap off. It should come off very easily, and you will be left with chocolate bowls. Keep the bowls in the refrigerator, covered in plastic, until ready to fill. When ready, gently unsold the plastic and fill.
        """)

    instruction50401 = Instruction(
        recipeId=14,
        imageUrl="https://content.instructables.com/ORIG/FIA/3ZLR/INPE8NHN/FIA3ZLRINPE8NHN.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e9577c8b6237a94e0b24ae6b651edee0", stepTitle="Slice the Spice", directions="""
            With a knife, cut your peppers into pieces. I cut the habaneros in half and sliced the jalapeno.

            If you will be using dried peppers, you don’t need to cut them.
        """)
    instruction50402 = Instruction(
        recipeId=14,
        imageUrl="https://content.instructables.com/ORIG/FZS/II0X/INPE8SZQ/FZSII0XINPE8SZQ.jpg?auto=webp&frame=1&width=1024&fit=bounds&md=34b9a13020b4e29cbd31b584b852da05", stepTitle="Hot Water", directions="""
            1. Place the peppers into a jar or mug and then pour in 1 cup of boiling hot water.
            2. Wait for the water to cool.
            3. When the water has reached room temperature, it should be spicy and ready to use.
            Don’t sniff the water, it might make your nose cry.

            You only really need ½ a cup of water to make a batch of gummies, but it’s always good to have extra just in case you spill or want to make a second batch.
        """)
    instruction50403 = Instruction(
        recipeId=14,
        imageUrl="https://content.instructables.com/ORIG/FZG/A30A/INPE8NHV/FZGA30AINPE8NHV.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=a773a8d42b584eb5620337586e92ddeb", stepTitle="Mix", directions="""
            1. Measure out 1/2 cup of spicy water into a microwavable measuring glass.
            2. Microwave for 2 minutes.
            3. Remove from microwave.
            4. Stir in in 2 tbsp sugar.
            5. Stir in 1/2 tsp Kool-Aid mix.
            6. Stir in 2 packets of unflavored gelatin.
            7. If a lot of gelatin is left undissolved, microwave the mixture for 30 seconds and stir again.
            8. Scoop out any chunks of gelatin that may be floating on top.
        """)
    instruction50404 = Instruction(
        recipeId=14,
        imageUrl="https://content.instructables.com/ORIG/FAJ/XTK5/INPE8NHS/FAJXTK5INPE8NHS.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=fda7b8d8e2e9bb2c89cc285dbaf6d993", stepTitle="Pour and Wait", directions="""
            1. Pour the mixture into a candy mold.
            2. Place in refrigerator for an hour or so to set, or in the freezer for 20 minutes, or just leave them out at room temperature for a few hours.
            3. Once they've solidified, you can remove them from mold and enjoy.
            I don’t know how to quantitatively measure the spiciness of each of the gummies I made using the different peppers. So, I’ll just let you know how many peppers I put per cup of water and I’ll try to describe the spice level.

            2 Habaneros, 1 cup Water: (mixed with Orange Kool-Aid) Spiciest of the three. Has a bite to it, but doesn’t set your mouth on fire. Wouldn’t want to pop a whole one into my mouth, but if I did it wouldn’t be terrible. Best enjoyed squirrel-style, (in tiny bites over a longer period of time). Could eat more than one but would rather have something less spicy.

            1 Jalapeno, 1 cup Water: (mixed with Green Apple Kool-Aid) Moderately spicy. Just enough spice it give it a kick. The heat isn’t overpowering and doesn’t distract from the overall flavor of the gummy. Green Apple Kool-Aid adds a sour taste which made this gummy sweet, sour and spicy. Strange, yet tasty.

            5 Dried Japanese Chili Peppers, 1 cup Water: (mixed with Cherry Kool-Aid) Spice is barely noticeable, would feed these to a child.
        """)

    instruction50501 = Instruction(
        recipeId=15,
        imageUrl="https://content.instructables.com/ORIG/FY2/SR4E/HIGFJMJH/FY2SR4EHIGFJMJH.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=bbb60be5c2992da2089e03d9ec95d27b", stepTitle="The Aroma Base", directions="""
            the following instructions will be for one drink!

            with a sharp knife, peel away some slices of the lemon zest and put them in a longdrink glass. (be carefull not to cut the white part of the lemon, as it is bitter)
            add one twig of fresh mint.

            crush the lemon and the mint with a muddler or something similar. this will make the aromas and essential oils come out.
        """)
    instruction50502 = Instruction(
        recipeId=15,
        imageUrl="https://content.instructables.com/ORIG/FC0/A2SU/HIGFJMJW/FC0A2SUHIGFJMJW.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=587c8897b9225d8995085315a15f4033", stepTitle="Gin & Juice & Gingerale", directions="""
            put 3 cubes of ice in the glass and add 4 cl (40 ml) of gin.

            add a dash of blackcurrant juice (you can also leave that out if you don't have any)

            fill the rest of the glass half with cranberry juice and half with ginger ale.
        """)
    instruction50503 = Instruction(
        recipeId=15,
        imageUrl="https://content.instructables.com/ORIG/FG8/5PB2/HIGFFXAT/FG85PB2HIGFFXAT.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=17c34506d600aff806170d56a097b46e", stepTitle="Enjoy!", directions="""
            add a slice of lemon for decoration and enjoy your drink!
        """)

    instruction50601 = Instruction(
        recipeId=16,
        imageUrl="https://content.instructables.com/ORIG/FFE/41L1/H8AZCSWT/FFE41L1H8AZCSWT.jpg?auto=webp&frame=1&fit=bounds&md=d84fed2a6e3087367289fbe9ae2a5a00", stepTitle="Mixing It Up", directions="""
            TIPS
            - Cabbage is the key "crunch" factor here so dice to your preference.
            - Mix a teaspoon of salt into the chopped lettuce; the salt will help extract excess water, which can be poured out after a few minutes of sitting.

            Now mix all of the ingredients up in a large bowl until even.

            Time: 2 minutes

            TIP
            - Start by making only 10 at a time and increase as you get quick at making them.
            - Microwave a spoonful of the mix for about 45 seconds or until it's cooked. Then add salt, pepper, and/or soy sauce according to your preference.
        """)
    instruction50602 = Instruction(
        recipeId=16,
        imageUrl="https://content.instructables.com/ORIG/FQK/V1VP/H8AZCT74/FQKV1VPH8AZCT74.jpg?auto=webp&frame=1&fit=bounds&md=539bf0eaa0a57149ee1e60a981dde4a6", stepTitle="Forming the Gyozas", directions="""
            Time: about 2 minutes to make 10 gyozas

            - Place a gyoza wrapper in your hand and then a small spoonful of the filling in the center of the wrapper.
            - Wet a finger tip and draw a quick half-circle ring inside the edge of the gyoza wrapper (basically around the filling).
            - Pick up and pinch together the wet edge and its opposite edge at the center (right above the filling). Then pinch a little more to either side, leaving the two ends open.

            TIP
            Cover unused wrappers with a clean kitchen towel to keep them from drying.
        """)
    instruction50603 = Instruction(
        recipeId=16,
        imageUrl="https://content.instructables.com/ORIG/FF9/1AM3/H7W5Z2ZL/FF91AM3H7W5Z2ZL.jpg?auto=webp&frame=1&fit=bounds&md=a15e96f46e6208d18749d8cfb6e56cf8", stepTitle="Cooking Them!", directions="""
            Time: about 10 minutes

            - Lightly oil the pan and put it on medium heat until it's warm (don't overheat or the oil will start to splatter).
            - Place 10 gyozas in the pan next to each other. The gyozas should sizzle a bit as you place them in the pan.
            - When the gyozas' bottoms form a slight, golden brown coating, pour enough water until it's about 1/2 inch deep. Then cover the pan with the lid and open once in a while to let the steam out.
            - When almost all of the water is gone, use the spatula to "work" the sticky gyozas off the pan. The bottom of the gyozas should be covered in more brown spots but are still crispy. Try to keep them together!

            TIPS
            - Sprinkle some water on the "pasty white" portions of the gyoza wrappers. This will help make the gyozas more presentable when they're done cooking.
            - Can't finish all 50 gyozas? You can put the uncooked gyozas in the freezer until you need them. Then just defrost them and cook them as you would normally! (It's OK if they're stuck together.)
        """)
    instruction50604 = Instruction(
        recipeId=16,
        imageUrl="https://content.instructables.com/ORIG/FK7/W7XI/H7UQQYNQ/FK7W7XIH7UQQYNQ.jpg?auto=webp&frame=1&fit=bounds&md=abcebf706fecd1a93d416e51c9521fdc", stepTitle="Eating and Serving Your Work of Art", directions="""
            Congratulations! You've made your very own gyozas! Now try different ingredients such as:

          - Corn
          - Peas
          - Shitake mushrooms
          - Chicken/beef/shrimp
          - Tofu (this can be a bit harder to work with, so I'd suggest using firm tofu)

          Enjoy!

          TIP
          Add some chopped garlic and a tiny bit of sesame oil into the soy sauce.
        """)

    instruction50701 = Instruction(
        recipeId=17,
        imageUrl="https://content.instructables.com/ORIG/FCR/TYKG/KKZG04FO/FCRTYKGKKZG04FO.jpg?auto=webp&frame=1&fit=bounds&md=5067fa1b9fb2de85be18c891bdd3878b", stepTitle="Marinating Chicken", directions="""
            For Marinating the chicken, mix the following ingredients:

            Here I have taken 1 Kilogram of chicken (with bone) and marinated it by adding:

            1 cup fresh thick curd.
            2-3 tablespoon ginger garlic paste.
            Add salt as per taste.
            1 teaspoon turmeric powder.
            2 teaspoon red chili powder.
            Mix everything well and keep it aside for 30-40 minutes.

            pro tip:

            The more time you marinate the chicken, more juicy and flavorful the meat will be. 30 minutes is enough though.
        """)
    instruction50702 = Instruction(
        recipeId=17,
        imageUrl="https://content.instructables.com/ORIG/FKN/6XGC/KKZG04FU/FKN6XGCKKZG04FU.jpg?auto=webp&frame=1&fit=bounds&md=45db907e1b55821ce7de1d4679b512b0", stepTitle="Preparation", directions="""
            While the chicken is marinating lets prep everything required for this recipe

            - Finely slice 1 medium sized onion.
            - Grind 1 medium sized onion.
            - Finely Chop 2 tomatoes.
            - Cut 2 small sized potatoes in small cubes.
        """)
    instruction50703 = Instruction(
        recipeId=17,
        imageUrl="https://content.instructables.com/ORIG/F8A/WP8T/KKZG04EQ/F8AWP8TKKZG04EQ.jpg?auto=webp&frame=1&fit=bounds&md=df47bb27a489d4c5a7d0c932e52b414b", stepTitle="Curry Making", directions="""
            Take a pan and heat 4-5 tablespoon oil (vegetable oil or mustard oil). Here I am using mustard oil because here in India it is said that nonveg tastes better when cooked with mustard oil.
            Add all the whole spices (bay leaf, black peppercorn, black cardamom, green cardamom, cinnamon stick, cloves) to the hot oil and sauté is for a min.
            Then add the sliced onions and sauté.
            cook the onions till they are slightly golden brown.
            Once the onions turn brown add the grinded onion paste and cook it for 5 minutes
            Add chopped tomatoes and cook till oil separates.
        """)
    instruction50704 = Instruction(
        recipeId=17,
        imageUrl="https://content.instructables.com/ORIG/FY8/NZJD/KKZG04EW/FY8NZJDKKZG04EW.jpg?auto=webp&frame=1&fit=bounds&md=852f5635cdc4c5fb2d6c474a6a05d1d6", stepTitle="Adding Spices", directions="""
            Adding spices is a spicy affair, specially if you are sensitive to spices, be careful with these since this is a Indian dish, it is medium spicy !

            Add the following spices:

            - 2-3 tablespoon of red chili powder.
            - 1 tablespoon of turmeric powder.
            - 2 tablespoon of coriander cumin powder.
            - Add salt as per taste.
            - 2-3 tablespoon of chicken masala.
            Mix all the ingredients and cook for about 3-4 mins.
        """)
    instruction50705 = Instruction(
        recipeId=17,
        imageUrl="https://content.instructables.com/ORIG/FZ5/ZHK7/KKZG04ES/FZ5ZHK7KKZG04ES.jpg?auto=webp&frame=1&fit=bounds&md=0ff46f4e0808a1c81d3b063b16501809", stepTitle="Cooking Chicken", directions="""
            - Once the spices are added and oil separates, we can now directly add our marinated chicken.
            - Mix the chicken well.
            - Cover and let the chicken cook for 15 minutes.
            -  Take the lid off, Add the potatoes and mix everything well.
            - Add 2 cups of water.
            - Cover it and let it cook for 10 more minutes.
            Yummy chicken curry is ready!

            There is one optional step that you can follow to make the curry taste even better.
        """)
    instruction50706 = Instruction(
        recipeId=17,
        imageUrl="https://content.instructables.com/ORIG/FVU/X3M4/KKZG04FT/FVUX3M4KKZG04FT.jpg?auto=webp&frame=1&fit=bounds&md=347246c24ae06e81f939b42733a0726c", stepTitle="Optional Step", directions="""
            This is a optional step, but following this step will make the chicken curry even more tasty.

            - Heat a small pan.
            - Add 1 tablespoon of oil.
            - Once the oil is hot add 1 teaspoon of cumin seeds. Let it pop.
            - Then Add 2 tablespoon of chopped ginger and cook it for a min.
            - Add 7-9 curry leaves and turn off the flame.
            - add this mixture to the chicken curry.
            Tada! Chicken curry is ready. Garnish with fresh coriander leaves, Serve hot with rice/ roti and Enjoy.

            If you found this recipe useful, vote for us in one pot challenge! thank you for reading.
        """)

    instruction50801 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/F2G/Z2IB/KRWGGM0J/F2GZ2IBKRWGGM0J.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=f833406bac42070a5212c1cbd6a6fd14", stepTitle="Pomegranate Seeds", directions="""
            1. Cut pomegranate and remove the pomegranate seeds.
            2. We need about 3/4 cup of pomegranate seeds to extract the juice.
        """)
    instruction50802 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/FVX/1571/KRWGGLT4/FVX1571KRWGGLT4.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=0f2341542ab64bb276c8d94b31c9714f", stepTitle="Extract Juice", directions="""
            1. Take a mixer/grinder, and grind 3/4th cup of pomegranate seeds.
            2. Strain the juice with the help of a strainer and a spoon.
            3. Keep this juice aside.
        """)
    instruction50803 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/FQ3/MUKJ/KRWGGLT3/FQ3MUKJKRWGGLT3.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=9b83f6e6c5d7ee77367ce487248db537", stepTitle="Prep Pomegranate Juice", directions="""
            1. Add about 1 tablespoon of sugar ( You can adjust according to your taste). I like Ice-cream semi-sweet.
            2. If you are using whipping cream 1 tablespoon is enough as whipping cream already has sugar.
            3. If you're using heavy cream, add 2-4 tablespoon of sugar.
            4. Mix sugar and juice till the sugar is dissolved completely.
            5. To that add 3 tablespoon of milk powder and mix well.
            6. Keep this mixture aside.
        """)
    instruction50804 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/F08/VBM8/KRWGGLRO/F08VBM8KRWGGLRO.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=6b7dfe2c3c932f3152f5bfd2e9eb6d5a", stepTitle="Whip the Cream", directions="""
            1. Take 1 cup of whipping cream or heavy cream in a big bowl.
            2. Start beating it with a beater or a whisk till you get super-soft peaks.
            3. Don't beat till you get stiff peaks. We want soft peaks for making ice-cream.
        """)
    instruction50805 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/FLU/6PGR/KRWGGLRN/FLU6PGRKRWGGLRN.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=55043c4282100209d8058bf69ce556d5", stepTitle="Adding Prepared Pomegranate Juice", directions="""
            1. To the whipped cream, gradually add the pomegranate juice.
            2. Add little by little and mix well with a spatula.
            3. Don't overmix.
            4. Mix till the whipped cream and pomegranate juice are perfectly combined.
        """)
    instruction50806 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/F4N/7NV7/KRWGGM0R/F4N7NV7KRWGGM0R.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=0e6640f52d24aa21bdce9891ec45ebdd", stepTitle="Add Food Color (Optional)", directions="""
            1. For a bit of color, add 1-2 drops of red food color.
            2. Mix everything well.
        """)
    instruction50807 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/FSK/ZSNW/KRWGGM1L/FSKZSNWKRWGGM1L.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=52b758a452c0bf2d0274d8892be8fdf5", stepTitle="SET the Ice-cream", directions="""
            1. Transfer this cream mixture to a freezer safe container.
            2. Top with some pomegranate seeds.
            3. Cover it.
            4. Let it set in the freezer for about 6-8 hours (Best overnight).
        """)
    instruction50808 = Instruction(
        recipeId=18,
        imageUrl="https://content.instructables.com/ORIG/FX8/JTQG/KRXX5VJB/FX8JTQGKRXX5VJB.jpg?auto=webp&frame=1&fit=bounds&md=641770878fe6c93d95e9e7cbde67c7aa", stepTitle="Ready", directions="""
            Our Pomegranate Ice-cream is absolutely ready to delight our taste buds!

            Scoop out your Ice-cream and Garnish it with some more Pomegranate seeds . This gives a nice crunch to the Ice-cream. Making this requires less than 30 minutes. Best when you wanna eat something sweet and cool. Make this and Enjoy with your family! I hope you like the recipe. I Hope you enjoy eating it more than you enjoyed making it! It definitely tastes better than the one you find in Ice-cream stores. It looks so tempting and creamy. Do try this recipe and tell me in the comments how it was. I promise you are gonna love it. Also please follow me on Instagram @thelockdowncheff. Thank you for reading.
        """)

    instruction90101 = Instruction(
        recipeId=29,
        imageUrl="https://content.instructables.com/ORIG/F4U/I07S/KNG1CRSJ/F4UI07SKNG1CRSJ.png?auto=webp&frame=1&width=1024&fit=bounds&md=e7f745475b7ba2a001be1f2ac423280d", stepTitle="Garlic and Tomato", directions="""
            Heat butter in a pan until melted, add garlic and cook on a medium heat couple minutes until aromatic.

            Add chopped tomato and cook few minutes more.
        """)
    instruction90102 = Instruction(
        recipeId=29,
        imageUrl="https://content.instructables.com/ORIG/F5N/MTZY/KNG1CRSK/F5NMTZYKNG1CRSK.png?auto=webp&frame=1&width=1024&fit=bounds&md=d9746d4b70b1ac661498a0dfc083ca72", stepTitle="Cheese, Starch and Cream", directions="""
            Add shredded cheese to the pan, then corn starch.
            Stir everything with a spatula. Cook until cheese starts to melt.

            Turn the heat to low and add room temperature full fat cream.

            Stir, cooking until smooth.
        """)
    instruction90103 = Instruction(
        recipeId=29,
        imageUrl="https://content.instructables.com/ORIG/FDA/LYW0/KNG1CRSM/FDALYW0KNG1CRSM.png?auto=webp&frame=1&width=1024&fit=bounds&md=1e31e0f026085d2ced9eacc824bb2b7c", stepTitle="Spice It Up", directions="""
            Add spices and marinated chili. You can chop fresh one, but it will be less spicy.

            Add parsley or cilantro, stir and cook few minutes.
        """)
    instruction90104 = Instruction(
        recipeId=29,
        imageUrl="https://content.instructables.com/ORIG/FFB/FNUC/KNG1CRT0/FFBFNUCKNG1CRT0.png?auto=webp&frame=1&width=1024&fit=bounds&md=66d5cba8bc3f2ff7a6cd818d0292bf74", stepTitle="Let It Cool and Enjoy!", directions="""
            We served our Chile con queso warm in heat-proof dish with tortilla chips on the side.

            Also sprinkle chili flake on top, if you wish.

            Enjoy!
        """)

    instruction90201 = Instruction(
        recipeId=30,
        imageUrl="https://content.instructables.com/ORIG/FPJ/R33A/HIXPVTQE/FPJR33AHIXPVTQE.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=7e77b6630845483aab0ea21fedfa076e", stepTitle="Blend and Enjoy!", directions="""
            Combine all ingredients in a high speed blender and pulse until combined. If too thick, add more liquid to thin the consistency. Garnish with a wedge of watermelon and a sprig of mint.

            For more delicious and easy recipes, check out my blog: www.kitchencandid.com
        """)

    instruction90301 = Instruction(
        recipeId=31,
        imageUrl="https://content.instructables.com/ORIG/F3W/WF6G/KQTHRAPD/F3WWF6GKQTHRAPD.jpg?auto=webp&frame=1&fit=bounds&md=2fbd50640ea62cc716544f17af9dda74", stepTitle="Cut Paneer Into Rectangular Cubes", directions="""
            Take a big block of Paneer.
            Cut it into medium sized rectangular cubes.
            Don't cut it too thin because we have to put it into a wooden skewer.
            Our Paneer cubes are ready.
        """)
    instruction90302 = Instruction(
        recipeId=31,
        imageUrl="https://content.instructables.com/ORIG/F8F/NMEJ/KQTHRAOR/F8FNMEJKQTHRAOR.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=c9dee75c443e27c79d71f60e6a831933", stepTitle="Marination", directions="""
            Take the paneer cubes from last step in a bowl, to that add the following:

            1. 1 tablespoon of ginger garlic paste.
            2. 1 tablespoon of soy sauce
            3. 1 tablespoon of chili sauce
            4. 1 tablespoon of schezwan sauce
            5. 1 tablespoon of tomato sauce/ketchup
            6. Salt as per taste
            7. 1/2 teaspoon of black pepper powder
            8. 1/2 teaspoon of kashmiri red chili powder
            Mix everything well carefully. Our marination is ready. Keep this marination aside for 1 hour (Minimum 30 mins).
        """)
    instruction90303 = Instruction(
        recipeId=31,
        imageUrl="https://content.instructables.com/ORIG/F3U/IJGE/KQTHRANG/F3UIJGEKQTHRANG.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=0eb888376c3384e3f74d00a77b79a247", stepTitle="Preparing Coating Slurry for Frying Paneer", directions="""
            In a glass take:

            - 2 Tablespoon of all purpose flour.
            - 1 Tablespoon of corn flour.
            - Salt as per taste.
            - 1/4 cup of water.
            - Mix this well, make a semi liquid paste.
            Our slurry is ready.
        """)
    instruction90304 = Instruction(
        recipeId=31,
        imageUrl="https://content.instructables.com/ORIG/F02/OA5Y/KQTHRAOP/F02OA5YKQTHRAOP.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=936fa1bc04dfb379999e7845ab1f8ed2", stepTitle="Assembling and Frying Paneer", directions="""
            - Take the marinated paneer cubes and thread onto metal or bamboo skewers. I'm using Bamboo Skewers.
            - Heat a pan, Add some oil.
            - Dip the marinated paneer into the slurry we made and fry them on the pan. (You can shallow fry or deep fry the paneer as per your liking.)
            - Fry for 1-2 mins on each side till it is nice golden brown and ready.
            - Our fried Paneer is ready.
            Keep this aside and start preparing the sauce.
        """)
    instruction90305 = Instruction(
        recipeId=31,
        imageUrl="https://content.instructables.com/ORIG/F2Q/2917/KQUX6RS1/F2Q2917KQUX6RS1.jpg?auto=webp&frame=1&fit=bounds&md=0ac4dc8b718428345af62c4f0f19cdf1", stepTitle="Preparing Sauce", directions="""
            In the same pan:

            - Add 3 tablespoon of oil.
            - Add 2-3 Tablespoon of finely chopped garlic.
            - 1 medium sized onion finely chopped
            - 2 green chilies finely chopped
            - Fry them Nicely till they're nice golden.
            - Add the left over marinate and the following sauces.
                - 1 Tablespoon of chili sauce
                - 1 tablespoon of soy sauce
                - 1 tablespoon of schezwan sauce
                - 1 tablespoon of tomato sauce/ketchup.
            - Mix everything well and let the sauces cook for a min.
            - Add a pinch of orange food color (optional).
            - Add some water and let it cook for another minute.
            - In 1/2th cup of water, Add 1 tablespoon of corn flour and make a slurry.
            - Add this slurry to the pan and mix well. Make sure that there are no lumps.
            - Let it cook .Keep stirring. After a minute our sauce will be is ready.
            - Add the fried Paneer to the sauces and coat them well carefully.
        """)
    instruction90306 = Instruction(
        recipeId=31,
        imageUrl="https://content.instructables.com/ORIG/F2T/N6OX/KQUX6RWX/F2TN6OXKQUX6RWX.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e3d9f1c597c55e8cecf0a4811c1471ed", stepTitle="Ready!", directions="""
            Tadaa! Our Paneer satay is ready. Serve it on a plate and put the sauce all over the paneer sticks. Garnish it with some green spring onions. Enjoy!

            I hope you like the recipe. You can use boneless chicken in place of paneer, the recipe will be the same. I Hope you enjoy eating it more than you enjoyed making it! It definitely tastes better than the one you find in restaurants. It was looking so tempting and yummy. Do try this recipe and tell me in the comments how it was. I promise you are gonna love it. Also please follow me on Instagram @thelockdowncheff.

            Thank you for reading.
        """)

    instruction90401 = Instruction(
        recipeId=32,
        imageUrl="https://content.instructables.com/ORIG/F9K/OW1L/HSYO27VI/F9KOW1LHSYO27VI.jpg?auto=webp&frame=1&fit=bounds&md=c3b79f3ea52b322b4d5e13f4869ef7b5", stepTitle="Prepping Mexican Style Chicken", directions="""
            Tip #1 Mexican food is all about improv

            Dice the chicken and set aside. Now heat a dash of vegetable oil in a skillet on medium heat, add garlic and let sit for a minute or so.  Add the diced chicken and cook thoroughly.  Once chicken is cook through add diced onions and green peppers.  Cover and let the onions and green soften. Add about a 1/4 cup of water to the skillet. Now time to add your spices(Cumin, garlic powder, paprika, chili powder, salt, pepper, etc)…I can’t tell you exact amounts to add of each, but you be the judge.  Add the spices I listed in the ingredients section at your discretion (Add this point if you like spicy foods then add you favorite hot sauce to the chicken). Lower the heat and let simmer until use.
        """)
    instruction90402 = Instruction(
        recipeId=32,
        imageUrl="https://content.instructables.com/ORIG/FB1/RXZ4/HSYO278D/FB1RXZ4HSYO278D.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=332e45c6ce6400fd18014c59e667afa5", stepTitle="Prepping Vegetables", directions="""
            Tip #2 Make as much as you like, You like onions well then add more onions!

            Now time to prep your vegetables!  Dice your red onions, garlic, and tomatoes and set aside in separate bowls.  Now chop your cilantro and basil (Set aside separately).
        """)
    instruction90403 = Instruction(
        recipeId=32,
        imageUrl="https://content.instructables.com/ORIG/F2X/Y2EB/HSYO2798/F2XY2EBHSYO2798.jpg?auto=webp&frame=1&fit=bounds&md=d578210bd7806b7dc14ff9c57622f14f", stepTitle="Prep Guacamole and Salsas", directions="""
            Now open your avocados, remove the seed and mash up into bowl until smooth.  Incorporate in a portion of your prepared garlic, red onions, cilantro, a squeeze of lime, and a dash of sugar…Mix it up! Taste and add more lime or sugar depending on flavor.  This is your guacamole! Next we prep our corn and tomato salsas. Open your can of corn and drain out the liquid.  Place in small bowl and mix in basil and red onions.  Set aside.  To make your tomato salsa take the diced tomatoes mix in red onions, cilantro, and cumin…that’s all there is to it. Set it aside.
        """)
    instruction90404 = Instruction(
        recipeId=32,
        imageUrl="https://content.instructables.com/ORIG/FM0/EGYV/HSYO27HG/FM0EGYVHSYO27HG.jpg?auto=webp&frame=1&fit=bounds&md=366cd5e0b244b75edef231070dbe40a7", stepTitle="Dos Capas Assembly", directions="""
            Tip #3 Clean as you go…makes for less cleaning afterwards

            Time to Assemble! Preheat oven to 350 and a skilllet on medium heat.  Place hard shells into oven and bake until hot, while they are baking heat up small soft tortillas on each side until bubbles start to form.  Now take soft shell and place hard shell into it then begin to load with ingredients.  Start with cheese, chicken, corn salsa, tomato salsa, lettuce, hot sauce, sour cream, and guacamole.  If you would like to get your soft shell to stick to hard shell you can put the guac inbetween the shells =) Sneakyyyy eh?
        """)
    instruction90405 = Instruction(
        recipeId=32,
        imageUrl="https://content.instructables.com/ORIG/F6G/FYYI/HSYO27KH/F6GFYYIHSYO27KH.jpg?auto=webp&frame=1&fit=bounds&md=1884901f85792b07a29318d91f058d00", stepTitle="Suggestions", directions="""
            Pick a nice sauce to go on top of each dish. I prefer maybe garlic and herb, or a chipotle ranch.

            For more Mexican flavor add some fresh cilantro on top on any dish.

            Serve with a white wine, corona, or if your feeling a bit ambitious maybe a strawberry patron margarita.
        """)

    instruction90501 = Instruction(
        recipeId=33,
        imageUrl="https://content.instructables.com/ORIG/FLP/JQ21/HJKBZ8DC/FLPJQ21HJKBZ8DC.jpg?auto=webp&frame=1&fit=bounds&md=218fd73a7b41682e00797b36ebc5d9e8", stepTitle="Step 1", directions="""
            1.Take condensed milk (250 ml ) [if you don't have it boil 1 litre full -cream milk until it gets 1/4 to its quantity in a saucepan.]
            2.cool it down for half an hour
        """)
    instruction90502 = Instruction(
        recipeId=33,
        imageUrl="https://content.instructables.com/ORIG/FZO/5XFO/HJKBZ8DK/FZO5XFOHJKBZ8DK.jpg?auto=webp&frame=1&fit=bounds&md=64ed7c3e739820b662dd4aa1c77d0610", stepTitle="Step 2", directions="""
            1. take 1 cup milk
            2. add 1 teaspoon of fennel seeds and 4 to 5 cardomom in the milk.
            3. Then boil the milk for upto 10 min at sim flame.      [ it adds flavour and aroma of these to milk so make sure flame is at sim ]
            4. After it pour the boil milk into grinder.
            5. Add 1 teaspoon gulkand and 1 teaspoon of fennel seeds to grinder.
            6. Grind the mixture well.
            7.  Take a bowl and pour the mixture from fine mesh strainer and gently shake the strainer to extract all the juices from the remaining extract.
            8.Now take this flavored milk and cool it down for 30 min. in fridge
        """)
    instruction90503 = Instruction(
        recipeId=33,
        imageUrl="https://content.instructables.com/ORIG/FD6/EAPF/HJKBZ8H0/FD6EAPFHJKBZ8H0.jpg?auto=webp&frame=1&fit=bounds&md=b96525cd994f5e2dbe1493789a35d032", stepTitle="Step 3", directions="""
            1. take 4 betel leaves and place it into a fine mesh cotton cloth.
            (note : we use only fine mesh cotton cloth so to extract only the juice purely )
            2. now close the cloth and beat it for some time.
            3. Now extract the juice of betel leaves into a bowl by squeezing the cloth.
        """)
    instruction90504 = Instruction(
        recipeId=33,
        imageUrl="https://content.instructables.com/ORIG/F6C/ZGTI/HJKBZ8IQ/F6CZGTIHJKBZ8IQ.jpg?auto=webp&frame=1&fit=bounds&md=c51291c1486cccb4106bf6584df5a1cb", stepTitle="Step 4", directions="""
            1. Take the rest condensed milk in a bowl.
            2. add the flavored milk mixture in  the bowl ( obtained at step 2 )
            3. add betel leaves juice extract to it.
            4. add 4 teaspoon of powdered or icing sugar to it..
            5. now blend this mixture until the whole contents get mixed.
            6. now pour the content into a plastic container.
            7. put this container in the fridger for 1 hour.
        """)
    instruction90505 = Instruction(
        recipeId=33,
        imageUrl="https://content.instructables.com/ORIG/FUC/YAF2/HJKBZ8MB/FUCYAF2HJKBZ8MB.jpg?auto=webp&frame=1&fit=bounds&md=341a967fb70086e8b3796b687e7809a5", stepTitle="Step 5", directions="""
            1. now take out the container from the fridger and scrape it into a bowl again. [ this step is done to make the ice cream more soft )
            2. add 200ml  cream to the bowl.
            3. add 4-5 drops of food colour ( green ).
            4 . now fully blend the mixture till it gets foamy.
            5. now add finely cutted betel leaves and rose leaves and add to the mixture.
            6. now blend the mixture slowly by hand with a spoon.
            7. now again pour it to the plastic container .
            8. put this container in the fridger for atleast 5-6 hours before serving.
        """)
    instruction90506 = Instruction(
        recipeId=33,
        imageUrl="https://content.instructables.com/ORIG/FQE/0PYE/HJKBZ8Q5/FQE0PYEHJKBZ8Q5.jpg?auto=webp&frame=1&fit=bounds&md=b44fb1925d217c63bdfe7662aaa25873", stepTitle="Step 6", directions="""
            1. Take out the container from the fridger and scrape it out into a small bowl.
            2 Garnish it with small rose leaves and a 1/2 teaspon gulkand.
            NOW you are ready to enjoy the lavish, rich in taste paan bahar ice cream.
        """)

    instruction90601 = Instruction(
        recipeId=34,
        imageUrl="https://content.instructables.com/ORIG/FKL/FHR3/KTPSX0Q8/FKLFHR3KTPSX0Q8.jpg?auto=webp&frame=1&fit=bounds&md=51264d70cee545bf74de9aa845f5b3f2", stepTitle="Searing the Beef", directions="""
            Add 2 tbsp oil in a large pot or pan. Sear the beef from each side, about 10 minutes until browned.

            Remove the meat from the pot or pan and leave aside.

            You can use the same pot, if your meat is lean. Clean your pot or use another one.
        """)
    instruction90602 = Instruction(
        recipeId=34,
        imageUrl="https://content.instructables.com/ORIG/FQW/3821/KTPSX0RW/FQW3821KTPSX0RW.jpg?auto=webp&frame=1&fit=bounds&md=45d063efc0c86c95ac235b1a2df0b900", stepTitle="Spice It Up", directions="""
            Heat leftover oil in a pot and add all spices and herbs.

            Cook, stirring, for one minute until fragrant.
        """)
    instruction90603 = Instruction(
        recipeId=34,
        imageUrl="https://content.instructables.com/ORIG/FNY/CMXC/KTPSX0RX/FNYCMXCKTPSX0RX.jpg?auto=webp&frame=1&fit=bounds&md=896f930773d5ed5f8d94f230d1cf70e4", stepTitle="Cook Tomato Sauce", directions="""
            Add canned tomatoes in the pot and crush them with the back of the spoon.

            Blend raw tomatoes and add them to the pot.

            Simmer the tomato sauce for 30 minutes.
        """)
    instruction90604 = Instruction(
        recipeId=34,
        imageUrl="https://content.instructables.com/ORIG/FUV/6O7K/KTPSX0S0/FUV6O7KKTPSX0S0.jpg?auto=webp&frame=1&fit=bounds&md=ded7c502c3f7f47fc9d95ece921b82b9", stepTitle="Cook the Stew", directions="""
            Add bouillon cube and water to the sauce.

            Bring to the boil and add meat back in the pot.

            Cook about 40 minutes or until desired consistency.
        """)
    instruction90605 = Instruction(
        recipeId=34,
        imageUrl="https://content.instructables.com/ORIG/FMA/FCW5/KTPSX0Q5/FMAFCW5KTPSX0Q5.jpg?auto=webp&frame=1&fit=bounds&md=34b8b21fe2f9f19d6bcf53d13bc1deff", stepTitle="Enjoy", directions="""
            Let it cool a little and enjoy! Sprinkle some fresh herbs on top.

            You can also serve it with rice, vegetables or pasta.

            This is so good just as it is, with a slice of bread.

            This African style stew can be stored in the fridge up to 5 days.
        """)

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
    instruction704 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FC1/9KDL/KR4X9552/FC19KDLKR4X9552.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=420fa4e33b2145869817cb7071bc5267",
        stepTitle="Freeze the Strawberries",
        directions='''Cut strawberries in half for small strawberries, in quarters for large strawberries. Place in the freezer for at least one hour.''')
    instruction705 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/F4L/5I7B/KR4X9580/F4L5I7BKR4X9580.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=cf7f46cc3fa66195f2115eea13828b4d",
        stepTitle="Make the Strawberry Slushie",
        directions='''Add frozen strawberries, ice from 1 ice cube tray and 1 mint sprig to a blender.''')
    instruction706 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FPB/UPQI/KR4X95E8/FPBUPQIKR4X95E8.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=cc39bf51b1ab4f8516e292f81162f4bf",
        stepTitle="Now for the Lemons",
        directions='''Juice each lemon half into a medium bowl by squeezing it. You can use a spoon to scrape out more juice. Remove any seeds.
''')
    instruction707 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FKX/0ULN/KR4X95NK/FKX0ULNKR4X95NK.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=bc756de7d5e7431d2036e6a476450e65",
        stepTitle="Make the Lemon Mixture",
        directions='''Pour lemon juice mixture and the ice from the remaining tray to the blender. Add a mint sprig.''')

    instruction708 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FA2/VBQY/KR4X94X0/FA2VBQYKR4X94X0.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=f11f079671aecdc7a874640591af0a7d",
        stepTitle="Add the Lemon Mixture",
        directions='''Add frozen lemonade mixture over the strawberry mixture in the glasses.

Add a straw. You may drink it as is or stir to blend.''')
    instruction709 = Instruction(
        recipeId=2,
        imageUrl="https://content.instructables.com/ORIG/FAC/HE5K/KR4X94WU/FACHE5KKR4X94WU.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=84265f28664fbb57776b06b682af73ef",
        stepTitle="It's Ready!",
        directions='''Garnish each glass with a fresh strawberry and a mint sprig if desired.

I made these after I had been doing some work out in my yard and I found it to be perfectly cold, smooth and refreshing......just what I needed!

I hope you give this recipe a try! It is water at its tastiest!!!''')

    instruction710 = Instruction(
        recipeId=3,
        imageUrl="https://content.instructables.com/ORIG/FD8/6404/KU5IVJMU/FD86404KU5IVJMU.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=7da428fa4f047b91484e30a3e7a916dc",
        stepTitle="Mix the Ingredients Into the Cake Mix",
        directions='''Add the eggs, oil, and water into the boxed cake mix''')
    instruction711 = Instruction(
        recipeId=3,
        imageUrl="https://content.instructables.com/ORIG/FOJ/88U1/KU5IVJOZ/FOJ88U1KU5IVJOZ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=0bad3c770eafa6b3eb6c60ba118a59ed",
        stepTitle="Do the Flan Mixture",
        directions='''In a blender, add 1 can of condensed milk, 1 can of evaporated milk, and 3 eggs''')
    instruction712 = Instruction(
        recipeId=3,
        imageUrl="",
        stepTitle="Put Mold in the Oven and Let It Bake",
        directions='''place the tube pan in the middle of the big cake pan that is filled with water. If the water doesn't cover the whole pan to the top, then add more water. Then let bake for 40-45 minutes or to the point that if you stick a fork into the cake then no batter comes with it. Afterwards let it cool.''')
    instruction713 = Instruction(
        recipeId=3,
        imageUrl="https://content.instructables.com/ORIG/FD9/UMQ9/KU5IVJQP/FD9UMQ9KU5IVJQP.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=245d3ffee78dfb58b91ebb24230ce01c",
        stepTitle="Make Chocolate Spiders",
        directions='''Melt chocolate (you can do this by putting the chocolate in the microwave or by melting it in the stove) and putting it into a small ziplock bag. Then make a tiny hole in one of the corners, squeeze some chocolate out and make a medium size ball, then add some legs to the original ball. After that put on the candy eyes and let them rest until they are completely solid''')
    instruction714 = Instruction(
        recipeId=3,
        imageUrl="https://content.instructables.com/ORIG/FQ1/D96S/KU5IVJRZ/FQ1D96SKU5IVJRZ.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=da5fd16d849c98a16762fd127cf92d60",
        stepTitle="Decorate",
        directions='''In a small bowl mix together some extra caramel and red dye.
        Pour the fake blood on top of the chocoflan and place the spiders on top of the chocoflan''')

    instruction715 = Instruction(
        recipeId=4,
        imageUrl="https://content.instructables.com/ORIG/FKV/5JP8/KSONHPXK/FKV5JP8KSONHPXK.png?auto=webp&frame=1&fit=bounds&md=0825a19fd941e2f38549d43192f228f6",
        stepTitle="Modeling Chocolate",
        directions='''We'll need a ton of modeling chocolate for the bathhouse, the food, and No-Face himself. You could use fondant for this step. but modeling chocolate is a little tastier. Modeling chocolate is easier to sculpt as well, however, it does warm faster. I used this recipe for my toad cake instructable, so I know it works.

Supplies:

2 cups corn syrup
10 cups (454 grams) chocolate almond bark (light and dark chocolate)
*DOUBLE THE RECIPE*

I used Liz's recipe here: https://sugargeekshow.com/recipe/modeling-chocola...

Steps:

Put the stove top on medium heat.
Melt the chocolate until it's smooth.
Add the corn syrup slowly when the chocolate is still hot, then stir it in until it resembles the consistency of unpulled taffy.
Dump the mixture onto some plastic wrap, spread it out, then seal it and place it in the fridge.
Cool overnight. Repeat for white and dark chocolate modeling chocolate.
Suggestions:

Make more modeling chocolate than you think you'll need! I doubled the recipe, and I still think I could have used a little more white modeling chocolate. And if you make too much, you can always freeze it for future projects.
If you're making an Instructable, don't forget to take pictures of your modeling chocolate like I did. :( Maybe you'll get lucky and already have some pictures on hand, but always double-check before moving to your next step!''')
    instruction716 = Instruction(
        recipeId=4,
        imageUrl="https://content.instructables.com/ORIG/FYN/N0RL/KSUD6CV1/FYNN0RLKSUD6CV1.png?auto=webp&frame=1&width=859&height=1024&fit=bounds&md=71b4c613cabba10f4582fdded7263c64",
        stepTitle="Frosting",
        directions='''On a stovetop, mix together the water and sugar. Cover with a lid and bring to a boil on medium-high heat.
Keep the lid on for 3-4 minutes and ensure all the sugar granules are dissolved.
Remove the lid, insert a candy thermometer carefully and continue cooking on medium-high until the syrup reaches 240° F.
When the sugar solution is at about 235° F, begin whipping the egg whites on high speed.
Add the salt to the egg whites.
When the egg whites reach soft peaks, pour the sugar solution in a steady stream on to the whipping whites while mixing on low speed. Be careful, the sugar is still extremely hot!
Continue whipping the egg/sugar mixture until it reaches stiff peaks. (Liz wraps an apron around the bowl with an ice pack to help the meringue cool down faster.)
Once the meringue is cooled, whip in soft butter and vanilla until the buttercream is light and fluffy and no longer has a butter taste. This can take from 10-15 minutes.
We thought caramel would be a good flavor to complement the vanilla flavor and gold coloring. Add a tablespoon of caramel syrup, then mix. Taste it, and add if you'd like. Add a little at a time so you don't wreck the frosting.
Add yellow and orange food coloring to achieve a light gold color.''')
    instruction717 = Instruction(
        recipeId=4,
        imageUrl="https://content.instructables.com/ORIG/FTB/4MS0/KSJD4ENC/FTB4MS0KSJD4ENC.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=863ded2af695fd5f78759e9f14f0d010",
        stepTitle="Cake Icing/Sculpting",
        directions='''Cut the caramelization off the top and bottom of your cake.
If your cake is in one pan, cut it in half so you have two pieces. Trim it so it fits comfortably onto your cake board. *KEEP THE CAKE SCRAPS, YOU WILL NEED THEM LATER* If you want to, add simple syrup to your cakes and wait for it to soak in.
Slap a good amount of frosting onto one of your cake pieces. Not too much, unless you like frosting more than cake.
Place your other cake piece on top of your frosting layer.
Add a large amount of frosting ontop of your cake, then cover the entire cake in a thin layer of frosting. Insert into the fridge to chill overnight or for at least 3 hours.
Lightly draw a semi-circle towards the top of the cake. This is where No-Face will be sitting later. Cut a thin layer away so the circle is lower than the rest of the cake.
Draw a larger semi-circle, then carve the sides so they're rounded.
Add cake scraps to the side of the larger circle, starting with larger pieces on the bottom, and ending with smaller pieces on top.
Carve so the circles begin to resemble a bathtub. It doesn't have to be perfect, we'll be covering it in modeling chocolate later.
To make the bathtub appear taller, trim away a thin layer of the rest of the cake (where the food will be sitting).
Lightly ice the entire cake again, and chill overnight or for 3 hours at least.''')
    instruction718 = Instruction(
        recipeId=4,
        imageUrl="https://content.instructables.com/ORIG/F3E/F1H4/KSJD4EVN/F3EF1H4KSJD4EVN.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=2c9f26bb7421a2776127106c1573a03e",
        stepTitle="Making the Bath",
        directions='''To make your colored modeling chocolate, fold gel food coloring in slowly, and mix until the color is uniform.
Mix teal modeling chocolate and drape it over the base of your cake (the non-bath part). Score lines into it to mimic a plank texture.
Mix brown modeling chocolate and apply it to your cake board. Score lines into it to mimic a plank texture. Mix white and brown food coloring with vodka and lightly apply it to the planks for a wood-like texture.
Add dark chocolate to the lip of the bathtub.
Mix a tan color for the area below the dark chocolate and apply it to the cake.
Mix some light blue food coloring and drape it into and over the bathtub to mimic water. Add ripples using a cake sculpting tool or toothpicks.''')
    instruction719 = Instruction(
        recipeId=4,
        imageUrl="https://content.instructables.com/ORIG/FAN/EHI2/KSJD4FFP/FANEHI2KSJD4FFP.jpg?auto=webp&frame=1&width=300&height=1024&fit=bounds&md=65f9850ca67b0d19181b0adbef37bab5",
        stepTitle="No-Face",
        directions='''Do you still have those cake scraps? Awesome! Crumble them into a mixing bowl.
Add a small amount of buttercream. Gently mix with a spoon.
Mix with your hands until the mixture resembles cake pop-dough. If it's too dry, add a little more buttercream until it reaches your desired texture. IF you need more cake scraps and you're all out, crumble up animal or graham crackers and add them to the mix until it's thicker.
Shape the cake dough into a blob-ish shape. The top should be thinner than the bottom. It's okay if it doesn't look beautiful, as No-Face is bumpy and blobby in the movie.
Roll a medium sheet of black-tinted dark chocolate modeling chocolate. Drape it over your cake pop blob, and smooth it gently. To add his hair, cut some brown modeling chocolate into spikes and add it to the top.
Roll a small ball of fondant, and squish it into an oval.
Use vodka and food coloring to paint his face. If you screw up, use more vodka to wipe the food coloring away.
Use a little buttercream to adhere his dried face to the cake pop blob.
Wrap two toothpicks in dark modeling chocolate.
Sculpt two tiny, outstretched hands. They don't have to look great, he is a spirit afterall.
Add the hands to the toothpicks, and gently insert them into No-Face. If the hands are too soft to press in, place them in the fridge for 10 minutes and try again.''')
    instruction720 = Instruction(
        recipeId=4,
        imageUrl="https://content.instructables.com/ORIG/F1L/3T7P/KSN82IMK/F1L3T7PKSN82IMK.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=06df9327a93f440e94cff65eb8a0e014",
        stepTitle="Final Assembly and Pictures!",
        directions='''Add a little buttercream to the back of the cake, preferably towards the bottom.
Gently press the bathhouse background into the cake.
Add a small amount of buttercream into the center of the bath. Carefully add No-Face. You may have to trim his backside to make the background stand straight. It's okay, he doesn't mind.
Slowly add your food to the surface of the cake. If the food doesn't stick, add a small amount of buttercream. If the food is on the edge of the cake or an angle, gently insert a toothpick into the cake, and press your food onto it.
Step back and enjoy your hard work.
And we're finished. Thank you for reading through this Instructable, I had a fun time making it AND the cake! If you want to make the cake even crazier, sculpt the frog-workers or add little hands inbetween the food. If I'm being honest though, I'm not expecting too many people to make this as a cake. However, cupcakes would be a fantastic idea, and much easier to execute. If you want to take the plunge though, all power to you! I won't give you any gold though. (unless your name is Chihiro... ) :)''')

    instruction721 = Instruction(
        recipeId=5,
        imageUrl="https://content.instructables.com/ORIG/FHT/UM2K/J1QP0HWC/FHTUM2KJ1QP0HWC.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=399be6e128d77e013534a8e5ad558333",
        stepTitle="INSTRUCTIONS",
        directions='''Prepare your ingredients as listed above.
In a large mixing bowl, combine all the ingredients above. Tip: make sure that your salad is dried using a tea towel or a salad spinner, the dressing clings better to dry salad leaves.
Top off with a dressing with a sweeter note. Enjoy!''')

    instruction722 = Instruction(
        recipeId=6,
        imageUrl="https://content.instructables.com/ORIG/FAA/T2BQ/KNRGTAIM/FAAT2BQKNRGTAIM.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=2c5764a80f2899cd3ebd0b14b111154d",
        stepTitle="Parmesan Meets Butter",
        directions='''combine parmesan, soft butter and chili powder - if you are sensitive to spicy food, start with 1/2 tsp and try the dough later.

use a spoon or fork and some pressure, until everything is well blended.''')
    instruction723 = Instruction(
        recipeId=6,
        imageUrl="https://content.instructables.com/ORIG/FHX/RN1T/KNRGTARB/FHXRN1TKNRGTARB.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=c00b6e8d2b1a3210a6f89e04e8f647f8",
        stepTitle="Kneading",
        directions='''knead in flour and water

until the dough feels smooth

if its crumbly, add a little more water.

form an even roll of the parmesan dough.''')
    instruction724 = Instruction(
        recipeId=6,
        imageUrl="https://content.instructables.com/ORIG/FP9/NT6U/KNRGUUPG/FP9NT6UKNRGUUPG.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=5316ccf55da5cf90f21b779306b82be4",
        stepTitle="Cover the Olives",
        directions='''flatten one dough piece, with your fingers

place one olive in it and form the dough around it lika a blanket

close the ends with a little pressure - moisten your finger with a dab of water if it won't close.

proceed until all olives are covered''')
    instruction725 = Instruction(
        recipeId=6,
        imageUrl="https://content.instructables.com/ORIG/F1X/85FG/KNRGUUQD/F1X85FGKNRGUUQD.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=fb7ccfbbd54fd0c427f12927d9e21c2f",
        stepTitle="Baking",
        directions='''place the olives on a baking tray covered with baking paper.

bake about 15 to 20 minutes at 200°C (393°F )

until the parmesan shell is golden brown.

Let cool on the baking tray

It is rewarding to wait until the next day before eating - if you are not that patient, wait at least until the olives are cooled down to room temperature - even if it's very tempting to try the olives right away :)''')
    instruction726 = Instruction(
        recipeId=6,
        imageUrl="https://content.instructables.com/ORIG/FED/DVP1/KNRGV0DF/FEDDVP1KNRGV0DF.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=436c8eac45d9a98ba0f62d892127799b",
        stepTitle="Enjoy!",
        directions='''Well that was easy - but soooooooo good!

let me know when you tried this delicious snack!

~I hope you enjoyed your stay~''')

    instruction727 = Instruction(
        recipeId=7,
        imageUrl="https://content.instructables.com/ORIG/FEP/DK4Y/KQGMRBTT/FEPDK4YKQGMRBTT.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=ba1a9dd7b29be9d3bec3da740f64644a",
        stepTitle="Add All of the Ingredients",
        directions='''First you will pour all of the oil in with the mint and then pour all of the vinegar. Then add the honey and the mustard. Then you will put the blender container onto the blender and start to mix the ingredients. First start at a very low speed, then go to level 3 then 6 then 10 until it looks like it is blended. You are done with the sauce.''')
    instruction728 = Instruction(
        recipeId=7,
        imageUrl="https://content.instructables.com/ORIG/FCT/MBGY/KQGMRBU2/FCTMBGYKQGMRBU2.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=016c02bd77953102e55d6a4fddbcf49d",
        stepTitle="Grilling the Ribeye",
        directions='''First, put salt and pepper on the meat. Then turn on the grill. When the grill reaches 500 degrees, scrape the grill. Then you will put the meat on the very hot grill and close the grill as fast as possible. Set a timer for three minutes. For the flip, make sure you are careful -- the fire Is going to rise a lot and get a lot hotter because ribeye is such a fatty cut. On the second side do another three minutes. when that is done you will turn off two of the burners and keep another two burners on then put the meat on the side that the burners are off and let it cook for another three minutes (on indirect heat). Remove the steak from the grill and let it rest for 5-10 minutes and you are done with the meat.''')
    instruction729 = Instruction(
        recipeId=7,
        imageUrl="https://content.instructables.com/ORIG/F28/WO4O/KQGMRENP/F28WO4OKQGMRENP.jpg?auto=webp&frame=1&width=447&height=1024&fit=bounds&md=5a46c01c23765f760d2546b0dc5d7937",
        stepTitle="Plating & Enjoy!",
        directions='''For the plating step, slice the meat off the bone and cut it into strips. Drizzle the the sauce on the meat and voila! bon appetit and I hope you enjoy it.''')

    instruction730 = Instruction(
        recipeId=8,
        imageUrl="https://content.instructables.com/ORIG/F7I/ONVU/KKWL8KEX/F7IONVUKKWL8KEX.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=0c7d50ee3433d8d6737a48dbfc3757b4",
        stepTitle="Browning the Sausage",
        directions='''I start by browning the sausage in a lightly oiled cast iron pan. Leave the sausage whole and get a nice golden brown on all the sides before removing.''')
    instruction731 = Instruction(
        recipeId=8,
        imageUrl="https://content.instructables.com/ORIG/FLO/A8ZY/KKWL8KEY/FLOA8ZYKKWL8KEY.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=fcde3198b0f62397581631c301f60314",
        stepTitle="Spinach",
        directions='''Now we are going to wilt our spinach just a little bit. If you have ever sauteed spinach before, you start with a large big beautiful bunch that fills the pan, and then, after being cooked, it turns into 1/100th of the amount you started with. With the oil leftover from browning the sausage, add the spinach with salt and pepper and wilt slightly. Remove your spinach.''')
    instruction732 = Instruction(
        recipeId=8,
        imageUrl="https://content.instructables.com/ORIG/F9P/TP07/KKWL8KF0/F9PTP07KKWL8KF0.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=f5485691e40011eb719244479c76ecac",
        stepTitle="Basic Tomato Sauce",
        directions='''Next, we are going to make a basic tomato sauce for this Rigatoni dish. Now that your skillet is empty, add a little more oil and toss in your onions. Cook until just translucent, and add your minced garlic. Cook for another minute until the garlic is slightly golden.
        I always start with whole tomatoes to make them whatever size I want based on my recipe. For this recipe, I wanted my sauce to have more texture. I like how the chunkier tomato pieces hold on to the melted goat cheese, so I break up the whole tomatoes with my hands until I get the consistency I want. You can use tomatoes that are already crushed or diced. Add salt, pepper, and a pinch of crushed red pepper. Simmer and reduce the sauce until it thickens. In the meantime, boil your water for the rigatoni. When the water reaches a roaring boil, salt your water. Salt your water like it’s swimming in the ocean. When you are cooking pasta in boiling water, it’s the only time you have a chance to flavor the actual noodles, so the saltier the water, the better
        ''')
    instruction733 = Instruction(
        recipeId=8,
        imageUrl="https://content.instructables.com/ORIG/FI3/CY1I/KKWL8KF1/FI3CY1IKKWL8KF1.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=2a5dff70ec7c9556c27e113e9f6e0472",
        stepTitle="Goat Cheese",
        directions='''Slice goat cheese and add to your reduced tomato sauce and stir.''')
    instruction734 = Instruction(
        recipeId=8,
        imageUrl="https://content.instructables.com/ORIG/FYH/WTL8/KKWL8LGW/FYHWTL8KKWL8LGW.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=2ff79816db3305338e5b34dc5c333ffe",
        stepTitle="Final Step!",
        directions='''Cut sausage into thin slices and add them and the spinach into the goat cheese sauce. Give everything a good mix. When the rigatoni is al dente, drain and add to the skillet. Stir all together and top with freshly shredded parmesan cheese.''')

    instruction735 = Instruction(
        recipeId=9,
        imageUrl="https://content.instructables.com/ORIG/FGU/49XJ/GD2J2UR4/FGU49XJGD2J2UR4.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=01e0e16f18a9a2590fa746c19beb5433",
        stepTitle="Secrets Revealed",
        directions='''I did not embark on this experiment lightly. I read everything I could find about what makes a chocolate chip cookie truly outstanding, and gained the most insight from the experiment that inspired this one, performed by David Leite for the New York Times in July of 2008. Our results, however, differed, though the few secrets revealed in the article remain invaluable.

The key secret in making amazing chocolate chip cookies seems to be in how long you let the dough sit before baking. Even Mrs. Wakefield employed this technique when she invented the original Nestle Toll House recipe - it just didn't make it onto the package!

Leaving the dough in the fridge for 24-36 hours allows the ingredients to fully soak up the liquid, and result in a firmer dough which bakes to a better consistency.

A long hydration time is important because eggs, unlike, say, water, are gelatinous and slow-moving. And since butter coats the flour, it makes it difficult for the liquids to get through to the dry ingredients.

Another hint is to rotate the cookie sheet mid-way through baking. This allows your cookies to bake evenly, regardless of where the hottest part of your oven is. This simple trick was a game-changer for me, and I'll never do otherwise again!

The NYTimes article suggests there's no substitute for a 6" cookie whose dough has been left in the fridge for at least 36 hours. But after this experiment, I care to differ.''')
    instruction736 = Instruction(
        recipeId=9,
        imageUrl="https://content.instructables.com/ORIG/F87/8PSX/GD2J2UQY/F878PSXGD2J2UQY.jpg?auto=webp&frame=1&width=419&height=1024&fit=bounds&md=01e0e16f18a9a2590fa746c19beb5433",
        stepTitle="The Prep",
        directions='''First you want to toast you some nuts. This makes for the extra yum. If you're allergic, I guess you should skip this part.
In a pre-heated 350oF (180C) oven bake:

 2 cups (about 225 g) nuts (I prefer pecans in this recipe)
for 10 mintues on an ungreased cookie sheet. Let cool. If you don't it will cause your chocolate pieces to get melty in the batter. Which is what happened to me. Which I rather liked and will probably be doing again. So choose your own adventure.

While those are baking, chop up:

 14 ounces (400 g) bittersweet chocolate
Insider tip: for the ultimate cookie, use only chocolate with at least 60 percent cacao content and shoot for a ratio of chocolate to dough of no less than 40 to 60.''')
    instruction737 = Instruction(
        recipeId=9,
        imageUrl="https://content.instructables.com/ORIG/FXW/GXFM/GD0R1A41/FXWGXFMGD0R1A41.jpg?auto=webp&frame=1&width=445&height=1024&fit=bounds&md=c70b2a5efb23db0f196dc57faa355242",
        stepTitle="The Procedure",
        directions='''The primary step in most cookie recipes is to sift together the dry ingredients. So do that. In a bowl, sift or whisk (easier!) together:

* 2 1/2 cups (350 g) all-purpose flour
* 3/4 teaspoon baking soda
* 1/8 teaspoon salt

In a separate bowl (preferably with an electric mixer) beat together:

* 1 cup (8 ounces/225 g) unsalted butter, at room temperature
* 1 cup (215 g) packed light brown sugar
* 3/4 cup (150 g) granulated sugar
* 1 teaspoon vanilla extract

One at a time, add:

* 2 eggs

beating thoroughly after each addition until each is incorporated.

Slowly stir in flour mixture until fully incorporated.

Finally, stir in chocolate and nuts.''')
    instruction738 = Instruction(
        recipeId=9,
        imageUrl="https://content.instructables.com/ORIG/FIV/13MU/GD2JKDVY/FIV13MUGD2JKDVY.jpg?auto=webp&frame=1&width=841&height=1024&fit=bounds&md=cbdd360417f66ad0038c27d368803763",
        stepTitle="The Hard Part",
        directions='''You know what I'm going to say. It's time to wait. It's time to take all this precious cookie dough you just made. . . and not eat it.

Divide the dough into quarters. Roll each dough into a log about 9in (23cm) long and wrap in plastic.

Stick em in the fridge for the next 24 hours, and try to forget you knew anything about them.''')
    instruction739 = Instruction(
        recipeId=9,
        imageUrl="https://content.instructables.com/ORIG/FYY/D99W/GD0R1A40/FYYD99WGD0R1A40.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=ce6c8614f51b843af54ae0cdf7d7825f",
        stepTitle="Let's Be Serious",
        directions='''You are not going to wait the 24 hours. I know this, you know this, who are we kidding? Nonetheless, it's absolutely worth the wait, so here's my suggestion to get you through the next 24 hours.

Though this is not in the original recipe, I strongly recommend saving apart a small portion of dough - 1/2 of one of the logs maybe, and proceeding to the next step. Not only will this quell your desire to break into the fridge at midnight and eat one whole log straight from the wrapper, it will give you the opportunity to compare and contrast the benefits of allowing your dough to rest.

So do it! Just don't tell David I said so. ;)''')
    instruction740 = Instruction(
        recipeId=9,
        imageUrl="https://content.instructables.com/ORIG/FKW/WP81/GD2JKDW0/FKWWP81GD2JKDW0.jpg?auto=webp&frame=1&width=749&height=1024&fit=bounds&md=e0203ab0c2980c6fbbbffafe397e0b70",
        stepTitle="The Baking",
        directions='''Preheat the oven to 350°F (175°C).

Line baking sheet with parchment paper or silicone baking mat.

Slice the logs into disks 3/4 inch (2 cm) thick and place the disks 3 inches (8 cm) apart on the prepared baking sheets. If the nuts or chips crumble out, push them back in.

Scoochmaroo Super Tip: Sprinkle the cookie slices with a small amount of sea salt. This will really make them sing!

Bake the cookies for 10 minutes, rotating the sheet midway through. If you prefer a chewier cookie, scale back the time a bit

(how did I not get a picture of the cookies being baked? I don't know!!)

Let cookies cool on the baking sheet until firm enough to transfer to a wire rack.

Baked cookies will store in an airtight container for 4 days. Unbaked dough can be refrigerated for up to a week or frozen for up to a month.''')

    instruction741 = Instruction(
        recipeId=10,
        imageUrl="https://content.instructables.com/ORIG/FZC/3XV8/IUHMTP3T/FZC3XV8IUHMTP3T.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=a7603b33b54764a07f374827a99d7865",
        stepTitle="Assemble",
        directions='''Cut the chocolate cookie wafer in half with the serrated knife (saw across).

Use any broken bits to make 2 tiny triangle bat ears.

Spread peanut butter on one side of the graham cracker.

Position the wings and ears and then sandwich them in place with a second graham cracker.

Add 2 gel dots for the eyes and a gel smile.''')
    instruction742 = Instruction(
        recipeId=10,
        imageUrl="https://content.instructables.com/ORIG/FY5/40NC/IUHMTP41/FY540NCIUHMTP41.jpg?auto=webp&frame=1&width=703&height=1024&fit=bounds&md=74cb4c99aaa3774ed6d8f9ca01139f1d",
        stepTitle="Serve",
        directions='''Put the googly eyes on the gel dots, then add the sprinkle “fangs" with the tweezers.

Set up a production line and you’ll have a plate of bats in no time!''')

    db.session.add(jamiInstruction1)
    db.session.add(jamiInstruction2)
    db.session.add(jamiInstruction3)
    db.session.add(jamiInstruction4)
    db.session.add(jamiInstruction5)
    db.session.add(jamiInstruction6)
    db.session.add(jamiInstruction7)
    db.session.add(jamiInstruction8)
    db.session.add(jamiInstruction9)
    db.session.add(jamiInstruction10)
    db.session.add(jamiInstruction11)
    db.session.add(jamiInstruction12)
    db.session.add(jamiInstruction13)
    db.session.add(jamiInstruction14)
    db.session.add(jamiInstruction15)
    db.session.add(jamiInstruction16)
    db.session.add(jamiInstruction17)
    db.session.add(jamiInstruction18)
    db.session.add(jamiInstruction19)
    db.session.add(jamiInstruction20)
    db.session.add(jamiInstruction21)
    db.session.add(jamiInstruction22)
    db.session.add(jamiInstruction23)
    db.session.add(jamiInstruction24)
    db.session.add(jamiInstruction25)
    db.session.add(jamiInstruction26)
    db.session.add(jamiInstruction27)
    db.session.add(jamiInstruction28)
    db.session.add(jamiInstruction29)
    db.session.add(jamiInstruction30)
    db.session.add(jamiInstruction31)
    db.session.add(jamiInstruction32)
    db.session.add(jamiInstruction33)
    db.session.add(jamiInstruction34)
    db.session.add(jamiInstruction35)
    db.session.add(jamiInstruction36)
    db.session.add(jamiInstruction37)
    db.session.add(jamiInstruction38)
    db.session.add(jamiInstruction39)
    db.session.add(jamiInstruction40)
    db.session.add(jamiInstruction41)
    db.session.add(jamiInstruction42)
    db.session.add(jamiInstruction43)
    db.session.add(jamiInstruction44)
    db.session.add(jamiInstruction45)
    db.session.add(jamiInstruction46)
    db.session.add(jamiInstruction47)
    db.session.add(jamiInstruction48)
    db.session.add(jamiInstruction49)
    db.session.add(jamiInstruction50)
    db.session.add(jamiInstruction51)
    db.session.add(jamiInstruction52)
    db.session.add(jamiInstruction53)
    db.session.add(jamiInstruction54)
    db.session.add(jamiInstruction55)
    db.session.add(jamiInstruction56)
    db.session.add(jamiInstruction57)
    db.session.add(jamiInstruction58)
    db.session.add(jamiInstruction59)
    db.session.add(jamiInstruction60)
    db.session.add(jamiInstruction61)
    db.session.add(jamiInstruction62)
    db.session.add(jamiInstruction63)
    db.session.add(jamiInstruction64)
    db.session.add(jamiInstruction65)
    db.session.add(jamiInstruction66)
    db.session.add(jamiInstruction67)
    db.session.add(jamiInstruction68)
    db.session.add(jamiInstruction69)
    db.session.add(jamiInstruction70)
    db.session.add(jamiInstruction71)

    db.session.add(instruction50101)
    db.session.add(instruction50102)
    db.session.add(instruction50103)
    db.session.add(instruction50104)

    db.session.add(instruction50201)
    db.session.add(instruction50202)
    db.session.add(instruction50203)
    db.session.add(instruction50204)
    db.session.add(instruction50205)
    db.session.add(instruction50206)
    db.session.add(instruction50207)
    db.session.add(instruction50208)

    db.session.add(instruction50301)
    db.session.add(instruction50302)
    db.session.add(instruction50303)

    db.session.add(instruction50401)
    db.session.add(instruction50402)
    db.session.add(instruction50403)
    db.session.add(instruction50404)

    db.session.add(instruction50501)
    db.session.add(instruction50502)
    db.session.add(instruction50503)

    db.session.add(instruction50601)
    db.session.add(instruction50602)
    db.session.add(instruction50603)
    db.session.add(instruction50604)

    db.session.add(instruction50701)
    db.session.add(instruction50702)
    db.session.add(instruction50703)
    db.session.add(instruction50704)
    db.session.add(instruction50705)
    db.session.add(instruction50706)

    db.session.add(instruction50801)
    db.session.add(instruction50802)
    db.session.add(instruction50803)
    db.session.add(instruction50804)
    db.session.add(instruction50805)
    db.session.add(instruction50806)
    db.session.add(instruction50807)
    db.session.add(instruction50808)

    db.session.add(instruction90101)
    db.session.add(instruction90102)
    db.session.add(instruction90103)
    db.session.add(instruction90104)

    db.session.add(instruction90201)

    db.session.add(instruction90301)
    db.session.add(instruction90302)
    db.session.add(instruction90303)
    db.session.add(instruction90304)
    db.session.add(instruction90305)
    db.session.add(instruction90306)

    db.session.add(instruction90401)
    db.session.add(instruction90402)
    db.session.add(instruction90403)
    db.session.add(instruction90404)
    db.session.add(instruction90405)

    db.session.add(instruction90501)
    db.session.add(instruction90502)
    db.session.add(instruction90503)
    db.session.add(instruction90504)
    db.session.add(instruction90505)
    db.session.add(instruction90506)

    db.session.add(instruction90601)
    db.session.add(instruction90602)
    db.session.add(instruction90603)
    db.session.add(instruction90604)
    db.session.add(instruction90605)

    db.session.add(instruction701)
    db.session.add(instruction702)
    db.session.add(instruction703)
    db.session.add(instruction704)
    db.session.add(instruction705)
    db.session.add(instruction706)
    db.session.add(instruction707)
    db.session.add(instruction708)
    db.session.add(instruction709)
    db.session.add(instruction710)
    db.session.add(instruction711)
    db.session.add(instruction712)
    db.session.add(instruction713)
    db.session.add(instruction714)
    db.session.add(instruction715)
    db.session.add(instruction716)
    db.session.add(instruction717)
    db.session.add(instruction718)
    db.session.add(instruction719)
    db.session.add(instruction720)
    db.session.add(instruction721)
    db.session.add(instruction722)
    db.session.add(instruction723)
    db.session.add(instruction724)
    db.session.add(instruction725)
    db.session.add(instruction726)
    db.session.add(instruction727)
    db.session.add(instruction728)
    db.session.add(instruction729)
    db.session.add(instruction730)
    db.session.add(instruction731)
    db.session.add(instruction732)
    db.session.add(instruction733)
    db.session.add(instruction734)
    db.session.add(instruction735)
    db.session.add(instruction736)
    db.session.add(instruction737)
    db.session.add(instruction738)
    db.session.add(instruction739)
    db.session.add(instruction740)
    db.session.add(instruction741)
    db.session.add(instruction742)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the instructions table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()
