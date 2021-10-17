from app.models import db, Instruction


# Adds instructions
def seed_instructions():
    jamiInstruction1 = Instruction(
        recipeId=21,
        imageUrl="https://content.instructables.com/ORIG/FSA/3CUS/KN8W3OI0/FSA3CUSKN8W3OI0.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=56a6ec8de5a7f05b68e33474d636d7b5",
        stepTitle="The Tomatoes",
        directions="During the summer I'm too busy to make soup and sauce. So I freeze a lot of my tomatoes. I cut out the core and remove any blemishes. Even large cracks are no problem, just slice out the bad and freeze the rest. No blanching required. Leave the skin on as well. Its easy to keep up with the crop this way. The beets in the picture are for the soup, not the wine. Though they could add a unique color I'm sure.")
    jamiInstruction2 = Instruction(
            recipeId=21,
            imageUrl="",
            stepTitle="Step 2: Skin Removal",
            directions="The skin is easy to remove when the tomato is frozen. You run a bit of lukewarm water over it, and the skin lets go. Keeping the tomato frozen is key to not loosing the meat with the skin.")
    jamiInstruction3 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/F9H/UI6K/KN8W3QJC/F9HUI6KKN8W3QJC.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=07f3614e3efb526ee7024b05ac3bed85",
            stepTitle="Compost the Skins",
            directions="These are the skins from 40 liters of tomatoes. I don't plan on using them in my fermentation, so they just go into the compost.")
    jamiInstruction4 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/F76/IJ08/KN8W3QJD/F76IJ08KN8W3QJD.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=fc76cfa90fb2713e1edf0d87859efabe",
            stepTitle="Collect Liquid",
            directions="It will take a few days for the tomatoes to thaw. Once they do, they create lots of watery juice. To make soup, I don't want all this extra liquid. To boil it down is a waste of energy. Rather than tossing it out, I'm going to convert it into an amazing wine. I use a sieve spoon and large measuring cup to separate the solids from the juice.")
    jamiInstruction5 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FS4/5IWE/KNABJT3W/FS45IWEKNABJT3W.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=1a5c522fe6eeae7d0f3a09e3080f0ca7",
            stepTitle="The Hydrometer",
            directions="I use the potential alcohol scale when adding sugar. I want an 11% wine. I use the specific gravity to determine when the fermentation is done. When it reaches 0.990 the fermentation is done.")
    jamiInstruction6 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FLB/HXV6/KN8W3QX1/FLBHXV6KN8W3QX1.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=dfae2a67bef5c3bada5acb5641b4791d",
            stepTitle="Get the Specific Gravity Right",
            directions="This step is important. To get the alcohol content you want, you'll have to add sugar. I fill the pot and bring it to a boil. I dissolve two cups of sugar and let it cool till the next morning. When I check my possible alcohol, it registers 11%. Now I know how much sugar is required for each pot to create my juice. I boil each pot of juice to kill any wild yeasts as well as adding sugar. If the alcohol level is to low, I would dissolve more sugar and add it. If to high, I would make a new pot with less. It's not rocket science. There is an entire pail to work with so there are lots of chances to make adjustments.")
    jamiInstruction7 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FDK/ME6V/KN8W3REK/FDKME6VKN8W3REK.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=3abd6acc916d8af8875b973c296d7e5f",
            stepTitle="Prep the Yeast",
            directions="After the juice has cooled to room temperature, its time to get the fermentation started. I'm using Lalvin 1118 but I would have preferred Lalvin 1116. I find it to be a much gentler yeast. It works slower and makes a smoother wine. Due to COVID 19 I found it hard to find supplies in my area. I'm sure this will be fine though.  In a small bowl add 1/4 cup of warm water, slightly warmer than body temperature. Add the yeast and stir it around until it sinks into the liquid. In about 15 minutes it will come alive and start bubbling and foaming. This is when I pour in some of the juice. I leave it for another 15 minutes or so. These pics give a good idea of how the process works. If the yeast is expired it won't work, and you'll need to buy more. Always check the best before date when you buy it.")
    jamiInstruction8 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FAS/6SYV/KN8W3REJ/FAS6SYVKN8W3REJ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=3ce7d5b3e92c00d3b5c5021679b51486",
            stepTitle="Pitch the Yeast",
            directions="The juice must be put into a carboy before you pitch the yeast. A siphon hose is the easiest way to do this. Now that the yeast culture is working well, its time to add it into the carboy. Once the yeast culture is added, install an air lock. That's it, now you wait.")
    jamiInstruction9 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FNK/GCYF/KN8W3T80/FNKGCYFKN8W3T80.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=2c9d03af64a4a14de2aa866e581828d4",
            stepTitle="AAAAHHGH!!!",
            directions="Wow! I guess the yeast is working well. Glad I wrapped the towel around the base of the carboy")
    jamiInstruction10 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FEJ/1WR3/KN8W3TJB/FEJ1WR3KN8W3TJB.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=01b6d442784acedb3100a30386f35859",
            stepTitle="Create Some Air Space",
            directions="This should have been done earlier. Make sure you leave enough space at the beginning to avoid a mess. This will involve a gallon jug and another air lock. I knew this, but I was rushing yesterday and neglected to do it.")
    jamiInstruction11 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FDR/KMXU/KN8W3TT3/FDRKMXUKN8W3TT3.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=18e9755ea361fe5fd14632ca5b4ba7f6",
            stepTitle="Day 3",
            directions="This is day 3. The color is changing and bubbling isn't as vigorous.")
    jamiInstruction12 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FMV/987E/KN8W3TTK/FMV987EKN8W3TTK.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=da858f1e7b635f45762516dbbaab51b3",
            stepTitle="Day 7",
            directions="On day 7 the fermentation has pretty much stopped. The specific gravity is down to 0.990 so I think it's tome to kill it off and start the clearing. I crush and add 5 campden tablets to the carboy. I also pour in contents of the gallon jug. I use a piece of paper and a hammer to crush the tablets. Then pour the powder in. You can use the potassium metabisulphite powder, but the tablets make it easier to measure.")
    jamiInstruction13 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FSH/YUFI/KN8W3UMI/FSHYUFIKN8W3UMI.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=519e241a2b224b5e360e9577727bad75",
            stepTitle="Day 12",
            directions="I let the wine sit for 5 days. Now I'll siphon it over to a new clean carboy. I'll add 5 more crushed campden tablets to sterilize and neutralize the oxygen introduced while siphoning. Then replace the air lock.")
    jamiInstruction14 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/F2G/XUBR/KN8W3V78/F2GXUBRKN8W3V78.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=fad65e7fcca43bc740ffae7c53c854ab",
            stepTitle="Day 15 Filter Time",
            directions="Rather than wait for the wine to clear naturally, I'm going to filter it. I set up my filter machine, and a bucket with a few gallons of water sterilized with potassium metabisulphite. This will be used to clean my hoses, and soak my filter pads.")
    jamiInstruction15 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FT9/4BSA/KN8W3VQ6/FT94BSAKN8W3VQ6.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=445db3522da076322fe522853be0edc9",
            stepTitle="Sterilize",
            directions="I will soak the hoses, filter pads and brackets to sterilize them.")
    jamiInstruction16 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FN9/4PK3/KN8W3VZ2/FN94PK3KN8W3VZ2.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=8e49ec910800255fb6426a34ff2c8b2f",
            stepTitle="Assemble the Filter",
            directions="I now assemble the filter.")
    jamiInstruction17 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FPG/CNZ0/KN8W3W4D/FPGCNZ0KN8W3W4D.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=d5c1fd9a57e4c65363e333083a1ee698",
            stepTitle="Run the Filter",
            directions="To charge the filter, I circulate the sterile water mixture first. Then I transfer the siphon hose into the wine. I run the filter until wine comes out the exit hose. Then I transfer the exit hose to the empty carboy. I added a clamp to my filter. In the past I found it would leak around the edges without it.")
    jamiInstruction18 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FL5/X5TP/KN8W3XKC/FL5X5TPKN8W3XKC.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=a3001f09df4b3cd97e276b03a7e8d021",
            stepTitle="Filter With #1 Filter",
            directions="I filter the carboy with the #1 filter to remove the largest particles. As you can see the wine is still cloudy. The sediment left is from the past 3 days. I'll wash it out while #2 filters soak.")
    jamiInstruction19 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FMA/TJIM/KN8W3YKB/FMATJIMKN8W3YKB.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=7fdd56ec392b11468c341691b0664b8e",
            stepTitle="Soak Filter #2",
            directions="The #2 is a finer filter. I soak it and then swap out the #1's then continue filtering.")
    jamiInstruction20 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FOR/PWQ9/KN8W3YKD/FORPWQ9KN8W3YKD.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=a90178aa6d4422aea81738ee645c4343",
            stepTitle="Filter #2",
            directions="As you can see the wine is much clearer this round. No need to clean the carboy this time. But another filtration is needed.")
    jamiInstruction21 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FN2/5HPR/KN8W3ZVW/FN25HPRKN8W3ZVW.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=50694bc4fa1c818efd55e55229f4a304",
            stepTitle="Filter #3",
            directions="Filter #3 does a nice job of clearing this wine up to a crystal clear amber nectar.")
    jamiInstruction22 = Instruction(
            recipeId=21,
            imageUrl="https://content.instructables.com/ORIG/FLF/K7AS/KN8W40KX/FLFK7ASKN8W40KX.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=95c3d2bda526b17458782a704e8bbd61",
            stepTitle="Oh Yeah!",
            directions="Filtering is kind of cheating the process. It allows you to take a lot of waiting and siphoning out of the process. It could take a few months to achieve this kind of clarity. But you don't need a fancy filter to get there. Just patience. Wine also seasons with age. Although young wine like this is perfectly good to drink, you will want to stash a few bottles away for a year or two so you can enjoy a more interesting flavor profile.  If you have any questions don't hesitate to ask.  Cheers!")
    jamiInstruction23 = Instruction(
            recipeId=22,
            imageUrl="https://content.instructables.com/ORIG/FVK/VKT4/KNABJRMM/FVKVKT4KNABJRMM.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=49d185084ec84c04bda26032a133076d",
            stepTitle="Enjoy!",
            directions="This wine is quite nice. No one would ever guess it was made with tomatoes.")
    jamiInstruction24 = Instruction(
            recipeId=22,
            imageUrl="https://content.instructables.com/ORIG/FZ5/JK2Q/KIKA4K02/FZ5JK2QKIKA4K02.png?auto=webp&frame=1&width=400&fit=bounds&md=6ad949a89730fcb964c195e83e2999cb",
            stepTitle="Prep",
            directions="Start by prepping your milk. Mix 3/4 cup whole milk with 3/4 cup goat milk.  Put a little bit of your milk in a separate bowl and mix in 1 tbsp corn starch. Set this aside for later.  Now chop up your dark chocolate (so it melts easier).")
    jamiInstruction25 = Instruction(
            recipeId=22,
            imageUrl="https://content.instructables.com/ORIG/FBY/PDBB/KIKA4JZT/FBYPDBBKIKA4JZT.png?auto=webp&frame=1&width=400&fit=bounds&md=9b89836f25b267acbfa214c8206b0c58",
            stepTitle="Cook",
            directions="Over medium heat, mix your dark chocolate with a bit of your milk and stir till the chocolate is melted. Add in the rest of the milk, the corn starch mixture, 1/2 pod vanilla bean, 1 tbsp cocoa powder, 3 tbsp honey, 3 anise pods, and a pinch of salt.  Stir constantly until it reaches a thickness you like.")
    jamiInstruction26 = Instruction(
            recipeId=22,
            imageUrl="https://content.instructables.com/ORIG/FKX/MK13/KIKA4JZV/FKXMK13KIKA4JZV.png?auto=webp&frame=1&width=933&fit=bounds&md=d258a2fd268e12a33419cae0b087a209",
            stepTitle="Icing a Cup",
            directions="Take some white chocolate, and melt it down till its melted, but not too runny.  Grab your favorite drinking cup and glaze the rim with the white chocolate.")
    jamiInstruction27 = Instruction(
            recipeId=22,
            imageUrl="https://content.instructables.com/ORIG/FAV/NFH8/KIKA4JZY/FAVNFH8KIKA4JZY.png?auto=webp&frame=1&width=400&fit=bounds&md=2c3670dd36641e39d049a31ecea16221",
            stepTitle="Pour and Garnish",
            directions="Pour your hot chocolate into your cup. Garnish with whip cream and then top with some ancho chili.")
    jamiInstruction28 = Instruction(
            recipeId=22,
            imageUrl="https://content.instructables.com/ORIG/F65/IMP7/KIKA4JZZ/F65IMP7KIKA4JZZ.png?auto=webp&frame=1&width=933&fit=bounds&md=fff7c1f2b6f615dfe2520c1a27b56928",
            stepTitle="Enjoy!",
            directions="That's it! Easy! Delicious!  Now enjoy! The flavors in the hot chocolate, mixed with the ancho chili, blended with the white chocolate that melts as you drink the hot chocolate, all come together into one amazing cup of hot chocolate!")
    jamiInstruction29 = Instruction(
            recipeId=23,
            imageUrl="https://content.instructables.com/ORIG/FY6/30Y6/KQ57CNZ0/FY630Y6KQ57CNZ0.jpg?auto=webp&frame=1&width=300&height=1024&fit=bounds&md=b40d8f6568bccbb28b9164c3a16de02f",
            stepTitle="Make the Brownie Bases",
            directions="Place the chocolate, butter and caster sugar in a microwave safe bowl and heat in the microwave for 30 second bursts, stirring in between each burst until fully melted.  To add the eggs place them in a bowl and add a few spoons of the warm brownie mixture to the eggs and mix together then add it to the chocolate mixture. This helps to 'temper the eggs' to stop them from cooking if the mixture is too hot.  Then add the vanilla bean, bi-carb soda, salt and cocoa powder (sifted) and mix until it all comes together.")
    jamiInstruction30 = Instruction(
            recipeId=23,
            imageUrl="https://content.instructables.com/ORIG/F3H/J4A6/KQ57CO68/F3HJ4A6KQ57CO68.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e9ac6617af2a3ffd24951d157028a337",
            stepTitle="Bake the Brownies",
            directions="For these brownies you want to have a specific thickness so that all the ice cream fits into your pan. I am using a 20cm x 20cm x 5cm (8inch x 8 inch x 2 inch) square baking tin.  Then take 2 sheets of baking paper and cut them into long rectangles so that they can cross over each other in the pan. This will help lift out the brownies and ice cream sandwiches from the pan later.  Pour 1 and 1/3 cup of the brownie mixture into the brownie tin and spread it around the pan, then drag the knife through the mixture to even it out and remove any bubbles. Then place a square of baking paper over the top of the brownie mixture and this will help it bake evenly.  Preheat the oven to 170 degrees Celsius (340 degrees Fahrenheit) and bake for between 15-17 minutes.  When the brownies come out, while they are still hot press a tea towel over the top to make the brownie more dense and to even it out. Then let them cool for 15 minutes, remove the brownie from the pan and repeat this process to bake the other half of your ice cream sandwiches.  When they are both done place them in the freezer to cool while you make your ice cream.")
    jamiInstruction31 = Instruction(
            recipeId=23,
            imageUrl="https://content.instructables.com/ORIG/FOQ/AJZB/KQ57CO6V/FOQAJZBKQ57CO6V.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=a35d6023f5c91f1f7bade29e08240113",
            stepTitle="Make the Ice Cream",
            directions="To make the ice cream place your thickened cream and vanilla bean into a large bowl of a stand mixer with a whisk attachment on high until it reaches firm peaks (approx 90 seconds). Then add the cold sweetened condensed milk and salt and beat on high for a few minutes until light and fluffy with firm peaks.")
    jamiInstruction32 = Instruction(
            recipeId=23,
            imageUrl="https://content.instructables.com/ORIG/F39/C4Q8/KQ57CP0P/F39C4Q8KQ57CP0P.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=80637ed9d25186dd021053349ec53283",
            stepTitle="Colour the Ice Cream",
            directions="Separate the ice cream evenly into 5 separate bowls (roughly 1 and 1/3 cup each) and add food colouring until you reach a depth of colour you are happy with. Making red, yellow, green, blue and purple.  **Then place each colour in a separate piping or ziplock bag. To make this easier you can place the bag in a mug and stretch the bag over the mug. This helps keep the bag open while you pour in the ice cream.  I find putting it in the bags helpful for layering the ice cream later (you will see what i mean).")
    jamiInstruction33 = Instruction(
            recipeId=23,
            imageUrl="https://content.instructables.com/ORIG/FQC/C45Z/KQ57CPW9/FQCC45ZKQ57CPW9.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=b95566b46b2d2a0223c4f4ef47ba26c4",
            stepTitle="Layering the Ice Cream",
            directions="Take the brownies out of the freezer, making sure that it is cold before adding the ice cream (otherwise it may melt).  Start by piping the purple ice cream layer on the bottom brownie. By piping the ice cream across the brownie you can see the thickness of the layer and try to keep it more even. Then with a butter knife lightly run in along the pan in one direction then perpendicular at 90 degrees to 'cross-hatch' the ice cream. this helps to make it even and remove any air bubbles.  Then repeat the same piping and knife technique with the rest of the colours in the order of blue, green, yellow and red. ** You will see that the amount of ice cream and the thickness of brownies is made exactly for this pan. if you make your brownies too thick the ice cream may overflow out f the pan.  Then add the top layer of brownie on top of the ice cream roughly in the middle over the brownie base to line them up to top off the sandwich.  Then cover with glad wrap and place into the freezer for a minimum of 8 hours (i typically leave in the freezer over night or the day before i need them)")
    jamiInstruction34 = Instruction(
            recipeId=23,
            imageUrl="https://content.instructables.com/ORIG/FW1/NYE3/KQ57CQQL/FW1NYE3KQ57CQQL.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=efbd353d9b0f536029ed3e42f1ef52cb",
            stepTitle="Cut the Ice Cream Sandwiches",
            directions="Take the ice cream sandwiches out of the freezer and pull them out of the pan. Then run a hot knife under water and cut the sandwich in half. Make sure to run the knife under hot water in between each cut to make sure the colour stays beautiful and vibrant!  Then cut them into smaller bits to whatever size you like. Either 8 large slices or 16 smaller squares.  These are very rich so it might be better to make smaller ice cream sandwiches. Then individually wrap them in glad wrap and store in the freezer in a large zip lock bag for up to a month.")
    jamiInstruction35 = Instruction(
            recipeId=24,
            imageUrl="https://content.instructables.com/ORIG/FVA/3W9N/KNG1BIDT/FVA3W9NKNG1BIDT.jpg?auto=webp&frame=1&width=831&height=1024&fit=bounds&md=a05f6d84bed0bdebbaeb7db2462393d9",
            stepTitle="Prepare the Apples",
            directions="Cut apples into quarters and remove the seeds and cores.  Using cheese grater slicer, slice all apples as evenly as possible. They should all be uniformly thin.  Mix a good amount of food dye to 2 tablespoons of rose water and 2 cups of boiling water. Add to apples and Immediately cover and let sit for 20 minutes. Apples should be pliable.  Once apples are soft, lay them out on paper towels and pat dry.")
    jamiInstruction36 = Instruction(
            recipeId=24,
            imageUrl="https://content.instructables.com/ORIG/FFY/S117/KNG1B6DI/FFYS117KNG1B6DI.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=53f26c578b1f542eefa337907e8e6f58",
            stepTitle="Prepare the Pastry",
            directions="Cut puff pastry sheets into strips. If using Pepperidge Farms puff pastry sheets, one sheet will make 6 roses. Keep as cold as possible. It will be easier to handle.  Brush strips with melted butter, sprinkle with cinnamon and sugar, and add almond paste if you desire. You can substitute almond paste for jam.  Place apples on puff pastry. I used 8 slices per rose, but all apples are created different.  Fold the bottom half of pasty over the apples.  Brush the pastry again with a bit of butter, and sprinkle cinnamon and sugar.  Roll up to create a rose.  At this time, adjust the pedals to make it bloom and place in the fridge while you create the others.")
    jamiInstruction37 = Instruction(
            recipeId=24,
            imageUrl="https://content.instructables.com/ORIG/F3Q/PS2Y/KNG1B6DL/F3QPS2YKNG1B6DL.jpg?auto=webp&frame=1&crop=2:3&width=400&height=1024&fit=bounds&md=ff92092675748fa31ce6a3eb879ab8d8",
            stepTitle="Paint",
            directions="Once all roses are completed, Mix a teaspoon of vodka with food dye to create edible paints. Paint the base and inside of the rose. You don’t want any visible pasty showing. The bottom can be left unpainted.  Place all rolls in the refrigerator for 15 minutes.  Spray cupcake pan and add the Mourning buns.  Brush apples with lightly beaten egg wash  Bake at 400°F for 35 - 40 minutes. Lightly place tin foil on the apples during the last 15 minuets if cooking  Let cool and Enjoy.")
    jamiInstruction38 = Instruction(
            recipeId=25,
            imageUrl="https://content.instructables.com/ORIG/FWD/AII5/KNYM0P7Q/FWDAII5KNYM0P7Q.jpg?auto=webp&frame=1&crop=3:2&width=301&height=1024&fit=bounds&md=95021644262cad1a7b5b2cd4c4d2ee3a",
            stepTitle="Squeeze the Whey From the Curds",
            directions="Place a colander over your large bowl and lay 2 thin layers of cheesecloth over the colander. Pour 1lb of cottage cheese on your cheesecloth and squeeze your whey out. Squeeze as much whey as you can because the whey can cause crazy splattering when you fry your nuggets.Remember liquid and oil don't mix!!  Once your curds feel relatively dry, transfer them into a different bowl together with your other shredded cheese. Reserve the whey as you will using it to make the thick cheese sauce.  If you wish, you can add a few handful of chopped pepperoni. If you are a vegetarian, you can omit the meat altogether.  ")
    jamiInstruction39 = Instruction(
            recipeId=25,
            imageUrl="https://content.instructables.com/ORIG/FV9/CE36/KNYM0P8W/FV9CE36KNYM0P8W.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=cd2feeb3e6b20a6bda63930c418d060e",
            stepTitle="Make Your Cheese Sauce",
            directions="You will need about 1/2 cup of whey that you reserved earlier.  Place 1/2 a cup of whey into a small saucepot and heat on your stove at medium heat, or a microwave, until it is warmed up. Place five slices of American cheese inside your warm whey and reheat it again until the cheese is warm and melting. Use a whisk and whisk up the mixture until it resembles a thick cheese sauce .  Once thicken, remove from heat and let it cool down completely. It must be completely cool or it will melt the other cheeses. I place them in the freezer to hasten the cooling, ensure to whisk it occasionally.")
    jamiInstruction40 = Instruction(
            recipeId=25,
            imageUrl="https://content.instructables.com/ORIG/FZC/TD4F/KNYM0PA8/FZCTD4FKNYM0PA8.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=7467597723e6eca85a241225a1f6c713",
            stepTitle="Make the Nugget Filling",
            directions="First, mix in your cornstarch into your cooled cheese sauce. If you wish you can add a tablespoon of cayenne pepper for some heat. Then gradually add in your cheese sauce into your bowl of mixed cheeses. So slowly add them as you go.  Your filling should not be too runny, it should be able to hold it's shape despite looking shaggy and lumpy.")
    jamiInstruction41 = Instruction(
            recipeId=25,
            imageUrl="https://content.instructables.com/ORIG/FZY/J6PZ/KNYM0PC6/FZYJ6PZKNYM0PC6.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=99859d8480128547eda3bd28e9e92b76",
            stepTitle="Shape Them",
            directions="Using clean and dry hands, shape them into your desired shape. It can be as little or as big as you want. Tho I highly recommend you don't go any bigger than 2 inches as it will not cook and melt the cheese thoroughly while frying. Smaller is better.  Place them on a tray or a plate lined with parchment paper to prevent sticking.  Once complete, place them in the freezer for 5-10 minutes until firm and slightly harden. It doesn't have to freeze completely, just firm enough to work with.")
    jamiInstruction42 = Instruction(
            recipeId=25,
            imageUrl="https://content.instructables.com/ORIG/F8I/59HO/KNYM0PEF/F8I59HOKNYM0PEF.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=339170b3a3a0248fc8e3dff3d1ed4659",
            stepTitle="Breading Station",
            directions="Dredge your harden nugget into the flour. Followed by the egg wash coating and then to your breadcrumb mixture.  Repeat until you complete all of them.")
    jamiInstruction43 = Instruction(
            recipeId=25,
            imageUrl="https://content.instructables.com/ORIG/FVB/70F6/KNYM0PI2/FVB70F6KNYM0PI2.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=314f6a86ed82d8415fc843b424240b42",
            stepTitle="Fry Your Cold Nuggets",
            directions="Once the nuggets are cold and firmed up, you have a choice to either fry them immediately or neatly place them in freezer-safe bags for future use.  TO FRY:  In a medium pot or oil fryer, heat enough oil to deep fry them.  Heat your oil to about 300-325 degrees Fahrenheit.  Any lower, and your nuggets will sit in oil and get overly greasy.  Too hot, you risk burning your breadcrumbs even before getting a chance to thoroughly melt your cottage cheese.  Fry the nuggets within that temperature range, about 2 big nuggets at a time. Do not overcrowd your fryer. Fry them for approximately 3 minutes on each side. 6-10 minutes total.You want to fry them long enough that you give the cottage cheese time to melt properly and turn creamy, if not you be left with a very lumpy nugget.  Once fried, transfer them to a wire rack to drain off any excess dripping oil.  Serve immediately while hot.")
    jamiInstruction44 = Instruction(
            recipeId=26,
            imageUrl="https://content.instructables.com/ORIG/FRJ/QMEA/KN36CAG6/FRJQMEAKN36CAG6.jpg?auto=webp&frame=1&width=284&height=1024&fit=bounds&md=78e5419ea1f19ab3c4f8a02a997d4945",
            stepTitle="Cook Eggs",
            directions="Some people boil their eggs in a pot  Others even cook them in an Instant Pot(pressure cooker)  I have an egg cooker, and love it. I actually have two; this one is a little bigger and can do 10 eggs at once.  You place the eggs in the indentations, pierce the egg top with provided spike, add varying water amount to achieve soft to hard(it also poaches and cooks omelets), turn on and that's it. It automatically shuts off when water is gone.  I like to put them in a bowl of cold water, and place into fridge. This stops them from cooking any further.  I like medium-boiled for deviled eggs.  Peeling eggs  Tap eggs gently on a hard surface, all around the egg. Carefully pull away the egg shell. I would also recommend pulling away the thin membrane if you plan on dying them. Color comes out more consistent.  Slice eggs exactly in half, lengthwise.  Place yolks in a bowl, this will be used in the filling recipe.  Try to remove all of the yolk, as some left behind will also affect the dyeing process.")
    jamiInstruction45 = Instruction(
            recipeId=26,
            imageUrl="https://content.instructables.com/ORIG/F0G/0NIJ/KN36CAGF/F0G0NIJKN36CAGF.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=ee33fc41714e46a90adb7c78eecab14c",
            stepTitle="Dye Egg Whites",
            directions="Get 4 small bowls, glass or ceramic is best.  Add 10 drops of each color to each bowl, for purple 5 red and 5 blue.  Add 1 Tbsp of white vinegar, stirring, add enough water to fill bowl halfway. Stir.  Add 4-6 egg halves to each bowl. The eggs should be submerged; add more water if necessary.  Gently stir the eggs around. Do this occasionally, every few minutes.  For a light pastel, 5-10 minutes should be good(they will dry a little darker than they initially appear)  For a saturated color, it may take up to 30 minutes.  While waiting, let's make the filling....")
    jamiInstruction46 = Instruction(
            recipeId=26,
            imageUrl="https://content.instructables.com/ORIG/F3E/YPEB/KN36CAGY/F3EYPEBKN36CAGY.jpg?auto=webp&frame=1&width=300&height=1024&fit=bounds&md=edbe0f4e22546f03d32dcb46d2e3c9cc",
            stepTitle="Puree Chickpeas",
            directions="Besides just the yolks and mayo/mustard, you'll also add chickpeas and... vodka!  If you don't want the vodka thing, you can also use pre-made hummus instead. : )  First puree the chickpeas. I used a magic bullet. There is not enough moisture in the chickpeas, so you need 2 oz of liquid, or vodka to produce a creamy puree.")
    jamiInstruction47 = Instruction(
            recipeId=26,
            imageUrl="https://content.instructables.com/ORIG/FIY/VIT0/KN36CAH5/FIYVIT0KN36CAH5.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=e4206d6d8ffffdd2d91a6eafeb28588b",
            stepTitle="Make Egg Filling",
            directions="Mash up egg yolks. A pastry blender or two folks works well.  To that add 1/4 cup of mayo. I used Primal Kitchen's chipotle lime.  Add 2 Tbsp of Dijon mustard  And add two pinches of salt  Combine thoroughly")
    jamiInstruction48 = Instruction(
            recipeId=26,
            imageUrl="https://content.instructables.com/ORIG/FXK/5TIY/KN36CAHP/FXK5TIYKN36CAHP.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=dccbd52b84b71e840286ca85ba265721",
            stepTitle="Combine Mixtures, Add Kimchi, Chill",
            directions="Now combine the chickpea and the yolk mixtures  Some people add pickles to deviled eggs, I thought mild kimchi would be nice, and extra nutritious.  Chop the kimchi so that all the strands are small bits  Add to filling  If you need to put in fridge because you are doing this ahead of when you need them, place saran wrap over the mixture, touching it, and secure around bowl.  Eggs should be nice and dark at this point...")
    jamiInstruction49 = Instruction(
            recipeId=26,
            imageUrl="https://content.instructables.com/ORIG/FV5/8479/KN36CAIL/FV58479KN36CAIL.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=b3e17aea915e988dd7d7a5f1065ef76b",
            stepTitle="Dry Eggs and Fil",
            directions="Allow the excess water from the eggs to be absorbed by a couple of paper towels.  I did this the night before, so I also covered with saran and put them in the fridge. No problems, dyed looked just the same.  You should not make the deviled eggs too far ahead of when you'll be serving them to your guests. Best to fill the bottoms with the filling no more than one hour before serving, then pop in fridge for 1/2 hour.  You want to put something on the serving plate so the eggs won't slide around.  I used shredded coconut. (You can save it after, no reason to throw away, though I did put it in the fridge)  It looked beautiful and did the trick!  For a final detail I sprinkled chipotle chili powder on top.  Looks like paprika but gives a tiny kick.  My family loved them, and these would be a big hit at a spring-themed party.  Now that you know how easy it is to dye the whites, inspiration abounds! You could adapt these for any season or holiday, changing up the color schemes to fit.")
    jamiInstruction50 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/FP0/VTXD/KFZEJGHN/FP0VTXDKFZEJGHN.png?auto=webp&frame=1&width=301&fit=bounds&md=bb173449736f8e8eb8fccbdc25e2048d",
            stepTitle="Making the Tuna Mousse",
            directions="Put 400gr of tuna, a handful of washed and squeezed salted capers, 7 pitted olives and 3-4 anchovy fillets in a mixer. Mix everything together until you get something like the fourth photo.")
    jamiInstruction51 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/F2N/FEMO/KFZEJGHX/F2NFEMOKFZEJGHX.png?auto=webp&frame=1&width=383&fit=bounds&md=21e5cada6ce7a31ed890849214575195",
            stepTitle="Adding Potatoes",
            directions="I prefer not to blend the potatoes. Instead, I crush them with a fork, but you can use a potato masher if you like. When you're done, add a pinch of salt (not too much, because the tuna condiment is pretty salty already!), then mix it with the tuna mousse using a fork or a spatula. If you want and you like, you can add a few more capers in this step.")
    jamiInstruction52 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/F4O/BCWD/KFZEJGI7/F4OBCWDKFZEJGI7.png?auto=webp&frame=1&width=404&fit=bounds&md=8d86b5424e5bb85685371a0223751d0f",
            stepTitle="Getting Hands Dirty!",
            directions="What you have to do now is to free your imagination! Put the dough on a plate and try shaping it like a fish. I suggest you to moisten your hands, so the surface will turn out smoother. If you want, you can also use a straight knife to shape the fish even better :)")
    jamiInstruction53 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/FD6/1AC4/KFZEJGIP/FD61AC4KFZEJGIP.png?auto=webp&frame=1&width=296&fit=bounds&md=bbf5a7067a57cdc6d2cf648c6647ac45",
            stepTitle="Adding Mayonnaise Glaze",
            directions="It is now time to cover the fish with mayonnaise! You don't have to make a shiny surface, because we'll be covering it with more decoration!")
    jamiInstruction54 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/FD9/R34H/KFZEJGGA/FD9R34HKFZEJGGA.png?auto=webp&frame=1&width=388&fit=bounds&md=2460eb5dad6c9d98982778c746398f02",
            stepTitle="More Mayo Decoration!",
            directions="Using a tube of mayonnaise, we can now highlight the shape of the fish and make a few more decorations. I suggest you to cover the side too, using the tip of a knife to join each 'strip' of mayo.")
    jamiInstruction55 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/FYG/3KLQ/KFZEJGGS/FYG3KLQKFZEJGGS.png?auto=webp&frame=1&crop=3:2&width=394&fit=bounds&md=0fcf04b7155aabfd55a6dea1107731df",
            stepTitle="Adding Peppers and Olives",
            directions="It is now time to add pickled peppers and olives to further decorate the fish. Cut them to the appropriate shapes in order to fit them inside the mayo scales you made in the previous step.")
    jamiInstruction56 = Instruction(
            recipeId=27,
            imageUrl="https://content.instructables.com/ORIG/FOE/H72C/KFZEJGHE/FOEH72CKFZEJGHE.png?auto=webp&frame=1&width=789&fit=bounds&md=5a040e379a97428e9b9cabb26280f72a",
            stepTitle="Done!",
            directions="Your fish-shaped potato mash and tuna is finished! Time to finally eat it! Mmmmh, delicious!!!  I hope you had fun following this recipe, let me know if you make your own :)")
    jamiInstruction57 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/FHV/WCVP/KAB2MKY8/FHVWCVPKAB2MKY8.png?auto=webp&frame=1&fit=bounds&md=6c2a8ac7f32fcfca87b6d08aba39bbc9",
            stepTitle="Bake the Brioche Buns",
            directions="Using a stand mixer with the whisk attachment, whisk the milk, butter, sugar and yeast. Add eggs and whisk until combined.  Change out the whisk for the dough hook. Add the flour and salt and mix on low-medium for 8-10 minutes. The dough should appear sticky, soft and smooth but come away from the bowl.  Cover the bowl with cling wrap and place in a warm area. Let the dough rise for 1-2 hours or until doubled in size. Once risen, punch the dough to deflate.  Lightly flour your work space and scrape out the dough. Divide into 8 pieces and shape each one into buns by rolling into balls.  On a large baking tray lined with baking paper, arrange the buns, making sure none are touching. Cover with a towel and let rise again in a warm area for 30 minutes to an hour or until they've risen and puffed up a little.  Use this time to preheat the oven to 200°C/400°F.  Before placing in the oven, whisk together the yolk with 1 tsp of water and brush over the tops of the buns. Sprinkle on the sesame seeds if using.  Bake for 15 minutes or until golden. Let the buns cool on a rack before assembling burgers.")
    jamiInstruction58 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/FHS/J1ED/KA9N97IN/FHSJ1EDKA9N97IN.png?auto=webp&frame=1&width=600&fit=bounds&md=e0c67709a9f51cb1e0892c7bccef8f62",
            stepTitle="Make the Burger Sauce",
            directions="Mix all the ingredients together in a small bowl.  Either serve immediately or spoon into a jar and place in the fridge for at least an hour for the flavours to work their magic.")
    jamiInstruction59 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/F7E/ICZE/KA9N985H/F7EICZEKA9N985H.png?auto=webp&frame=1&width=600&fit=bounds&md=a37be3524bdb1d998790986bb4a6b66c",
            stepTitle="Pickle the Onion",
            directions="Thinly slice the red onion.  Combine the vinegar, water, salt and sugar in a small bowl.  Scrunch the onion slices in your hand before transferring to the bowl and mixing all together.  Allow to rest for 30 minutes before serving.")
    jamiInstruction60 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/FCW/IKPB/KA9N98B4/FCWIKPBKA9N98B4.png?auto=webp&frame=1&width=400&fit=bounds&md=5f9e659b60fdeeef5e1d09c3e9619313",
            stepTitle="Make the Beef Patties",
            directions="Divide the mince into 4 portions. Without handling the beef too much, shape each portion into plump balls. Try not to take too long doing this as the more you shape them, the tougher they will be.  Generously sprinkle salt and pepper onto both sides of the balls.  Using a large fry pan on medium high, heat a drizzle of oil.  Once the oil is hot, place all the balls in the fry pan. Using a burger press or potato masher, press down on each patty until thin. The patties won't be perfectly round, but the craggily bits that form will get crispy and give the patty extra texture and flavour.  Fry on one side for about 3-4 minutes before flipping. The second side should take 2-3 minutes to cook.  In the last 30 seconds, place a slice of cheese on top of each patty and let it melt.  Once cooked, rest patties on a plate for a few minutes before assembling the burgers (or add straight to the bun and eat immediately for a super juicy burger)")
    jamiInstruction61 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/FC6/DF2A/KAB2MG2T/FC6DF2AKAB2MG2T.png?auto=webp&frame=1&fit=bounds&md=9409c148711bba3a0105cb33dac405f4",
            stepTitle="Assemble the Burger",
            directions="As a frequent burger maker, I feel I have somewhat perfected the art of assembling a burger that prevents spillage of the filling and soaking of the bun. The above order of ingredients is my own personal favourite method of assembly, but really, it doesn't matter that much. Burgers aren't fancy French pastries that require strict measurements and steps, so go ahead and just build that burger. You know it's going to be good regardless!")
    jamiInstruction62 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/FZQ/81F0/KAB2MHTG/FZQ81F0KAB2MHTG.png?auto=webp&frame=1&fit=bounds&md=476a53b82f40b10afd80853fe0d4c1f5",
            stepTitle="Bake the French Fries",
            directions="Peel all the potatoes and then slice into wedges or medium sized strips  Place all the cut potatoes in a large bowl and add enough water to cover them. Soak the potatoes for 20 minutes (Soaking gets rid of some of the starch and results in crispier fries).  While you wait for the potatoes to soak, preheat the oven to 200°C/400°F and line two large baking trays with baking paper.  Once soaked, rinse the potatoes and thoroughly dry them by patting them down with a tea towel.  Transfer to the large bowl and drizzle a generous amount of oil and a good sprinkling of salt and pepper. Use your hands to mix everything up and ensure all the potatoes are covered in oil.  Spread the fries over the two baking trays, making sure to leave space between each one for maximum crispiness.  Bake in the oven for 25-35 minutes or until golden and crunchy. Don't forget to take them out about halfway through to flip as this ensures even browning of the fries.  Before serving, toss the fries in more salt or any other seasonings of choice.")
    jamiInstruction63 = Instruction(
            recipeId=28,
            imageUrl="https://content.instructables.com/ORIG/FRY/JA3V/KAB2MITG/FRYJA3VKAB2MITG.png?auto=webp&frame=1&fit=bounds&md=065dd9cdedcddaf35edb795def78bbb5",
            stepTitle="Blend the Chocolate Milkshake",
            directions="In the jug of a milkshake maker or blender, add the milk, ice-cream and a large drizzle of chocolate syrup.  Blend until there are no more lumps and the milkshake is frothy.  In your serving glass, drizzle the chocolate syrup all around the inside before pouring the milkshake in.  Top with a squirt of whipped cream and a maraschino cherry (or two).")
    jamiInstruction64 = Instruction(
            recipeId=29,
            imageUrl="",
            stepTitle="Preparing the Tomatoes",
            directions="")
    jamiInstruction65 = Instruction(
            recipeId=29,
            imageUrl="https://content.instructables.com/ORIG/F9Y/1R5V/KQQMU1KN/F9Y1R5VKQQMU1KN.jpg?auto=webp&frame=1&width=580&height=1024&fit=bounds&md=5e0397a6b3c7b5604e84f1ae4a121c1e",
            stepTitle="Preparing the Tomatoes",
            directions="Preheat the oven to 400°F or 200°C  Rinse and dry the tomatoes.  Slice off the top of each to make a lid and set these to one side.  Using a teaspoon, carefully remove the inside of each tomato,  Place the tomato shells onto a buttered heat-proof dish.")
    jamiInstruction66 = Instruction(
            recipeId=29,
            imageUrl="https://content.instructables.com/ORIG/FI7/HX87/KQQMU1QP/FI7HX87KQQMU1QP.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=818964d932768762dd21d961c96531c2",
            stepTitle="Preparing the Filling",
            directions="Sauté the red onion until it begins to soften. Add the chopped interior of the tomato and let this simmer briskly until it loses most of its liquid.  Split the skins of the sausage and add the meat to the pan and cook these until the sausage meat has browned and the sauce has thickened.  Add the herbs and mix well.")
    jamiInstruction67 = Instruction(
            recipeId=29,
            imageUrl="https://content.instructables.com/ORIG/F3L/WJZB/KQQMU1RA/F3LWJZBKQQMU1RA.jpg?auto=webp&frame=1&crop=3:2&width=378&height=1024&fit=bounds&md=c7a06bddf218a546e6ba745563b5d7a3",
            stepTitle="Filling, Cooking, Enjoying!",
            directions="Using a teaspoon stuff each tomato with the filling.  Put a 'lid' onto each tomato.  Place in the oven for 10 minutes or until the cherry tomatoes are cooked.  Allow them to cool slightly if you are taking them straight to the table. Tomatoes hold their heat too well!  Enjoy!")
    jamiInstruction68 = Instruction(
            recipeId=30,
            imageUrl="https://content.instructables.com/ORIG/FPV/HIBT/JGGTG029/FPVHIBTJGGTG029.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=1f457af2ae142af8cae32f8ef6e58360",
            stepTitle="Boil",
            directions="Mix the water and agar in a pot, bring it to a boil, and let it boil for 30 seconds. Take the pot off the heat, and let the bubbles escape. Skim off any foam from the top.  Let the liquid cool till it stops steaming. This will make it easier to coat the parchment paper evenly. Pour the liquid onto a baking sheet with parchment paper and quickly tilt it to distribute the liquid in an even, thin layer.  Set the baking sheet aside, and let the plastic dry for at least 24 hours or more.  NOTE: I have tried both pouring the plastic onto aluminum foil and directly onto a plate, and neither worked as the plastic stuck. Parchment paper is the way to go.")
    jamiInstruction69 = Instruction(
            recipeId=30,
            imageUrl="https://content.instructables.com/ORIG/FFV/WL3Y/JGGTFX58/FFVWL3YJGGTFX58.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=865231e593d5a699ce1ac2693d8118e3",
            stepTitle="Cut",
            directions="When the plastic is completely dry, it should peel off easily. Carefully remove it from the parchment paper. Trim the edges, and cut the plastic into appropriately sized squares.")
    jamiInstruction70 = Instruction(
            recipeId=30,
            imageUrl="https://content.instructables.com/ORIG/FR6/FRG9/JGGTFZRA/FR6FRG9JGGTFZRA.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=45f3aa01a378c6d1fd8ff4bece07b975",
            stepTitle="Fill",
            directions="Put your desired filling (I used trail mix) onto one half of a piece of plastic, and check to see that the other half can be folded over to close the pocket.  Brush some water around the edges of one half of the plastic, and fold over the other half, pressing on the edges to adhere. If the edges do not adhere very well, try folding the edges to secure the filling better.  Let the seams dry for half an hour before packing and enjoying the little pouches.")
    jamiInstruction71 = Instruction(
            recipeId=30,
            imageUrl="https://content.instructables.com/ORIG/FLK/356K/JGGTFXAM/FLK356KJGGTFXAM.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=f88b571bb1447090f138c92c08d1cc88",
            stepTitle="Verdict",
            directions="VERDICT:  Taste: I think these trail mix pouches actually taste quite good, even though they challenge the sensory experience of eating trail mix a bit. The first impression is that you are stuffing, well, plastic in your mouth, and the plastic can have a very slight salty flavor from the agar, but as soon as you start chewing, the plastic disappears, and you get all the goodness from the trail mix. If you really think about it, the edible plastic adds a slight, chewy gummy-bear texture in the background, but it goes perfectly with the dried fruit.  Durability: The plastic holds up pretty well to scrunching, even though it may rip in areas that are very thin. However, the seams are a bit fragile and can easily open so that trail mix falls out. Also, the plastic is sensitive to humidity. So I probably wouldn't stuff these goodie bags in the kids' pockets if I knew they were going to play in the rain or stick their hands in the pocket a thousand times to feel if the treat is still there (even though I think I might actually slip one of these in my own pocket, hmmm, but for the kids, maybe put it as a surprise in the sack lunch for school). I think the best way to store and carry these plastic pockets with trail mix would be in a real food-grade plastic bag or container.  I hope you liked this instructable! If you did, please vote for me in the Science of Cooking contest and Pocket-Sized contest. Thank you! Also, if you try this out, please share the result and any modifications in the comments!")


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

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the instructions table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()
