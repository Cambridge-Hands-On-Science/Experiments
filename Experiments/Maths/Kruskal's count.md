# Kruskal's count

**Players follow playing cards around a circle and watch as they magically come together** - Players follow playing cards around a circle and watch as they magically come together

Last initially checked on 2025-01-17 by Asmita Niyogi (an637@cam.ac.uk) and double-checked on 2025-01-26 by Margaret Johncock (mllyj2@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**Probability**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- * One pack of giant cards
- * Two normal packs of cards (red and blue backs)
- * Various coloured duplo pieces
- * Monopoly board print out

<br/>

## Experiment Explanation 

By placing cards on the floor in a circle and assigning a number of steps around the circle to each card, it can quickly be seen that people starting on cards all around the circle will converge. The question is why does this happen, and what will make them converge quicker?

You can then predict the future by laying out a whole deck of cards and predicting (with about 90% accuracy) what the last card they'll pick is.

**Setup**
You can either set up with standard or oversized cards. For the large ones spread the cards in a large circle, not every card needs to be used if space is limited, with plenty of space around the cards. For standard cards you can set up on a table, either in a circle or as multiple rows of around 8 cards, you may want to set up with cards in between or curving to make more of a snake shape as well so people know what to do when they reach the end of a row.
If you need to skip cards for space you'll probably find leaving out picture cards saves the complication of explaining how to move on them.
With the small cards duplo pieces can be used as placeholders. With the large cards, everyone can be their own placeholder, standing on the cards. (Warning, the whole point of this experiment is that everyone ends up on one card, so don't play with so many people that it becomes a scrum)

**Explanation and Demonstrating**

1st part. The circle
Much of the point of this experiment is that you can, with the children's instruction, vary the rules of the game somewhat to examine the effects. However a basic idea of the rules is et out here:

Lay about half the deck on the floor in a circle (can use the whole deck, or even more than one, but the game will take longer and space is an issue), it doesn't really matter which cards go down, although lower cards will lead to a shorter game.

For cards 2-10 players will move that number, aces will move 1 and jack, queen, king 5 places each. If you're not using all the cards you may want to have some of the high numbers move less spaces but try and see what works.

Once everyone's moved, they check their current card, and move again as appropriate.

Repeat, indefinitely. Although at some point everyone will end up on the same card, or at least going round the same sequence of cards ad-infinitum.

You can challenge people to try and work out who needs to move to catch everyone up to each other, or challenge them to see who the first person to land on a particular card is (if you pick one not on the circuit it becomes much more clear that they're confined to a small subset of cards)

Now, why does this happen? 

It's not too hard to see that everyone on any particular card will then stick together for the rest of the game, as they are all on the same card being acted on by the same rules.

However, there are more than one 'routes' to most card (not true for all, and abundantly true for some), meaning that it's not just people coming from one particular card that might end up on the next card. Thus the group slowly accrues people as others happen to find their way into it.

This explanation is simple enough, and most children should grasp it. But what we really want to ask them is what happens when they change the rules. Particularly, what can we change to make the game quicker or longer.

What happens when we increase the number of cards? The game gets longer as there are the same number of people spread out over more possible spaces.

What about if we reduce the number of steps, try -1 or even more? On writing this I'm not even sure, have a go yourselves!

Why do we set a low value for all face cards, what happens when we increase it? In the long run this should make the difference between the mean amount of time, and that found in experiment, bigger. I.e. increases the standard deviation, but this is hard for anyone to grasp. What you will instead see is that people flit about the board much faster, and even if it doesn't prove that the system has higher uncertainty, it'll certainly feel like it.

What about if you multiply all the step values by 2? Actually groups should form at the same rate as before, but you should eventually see two, roughly equal sized groups, unable to meet, as of course, if they are an odd number of cards away from each other there's no mechanism by which they'll come together.
Once you've done this sometimes it's fun to try with multiplying by 3. People may feel that three groups should form however as 3 doesn't divide 52 you just end up moving further and still bunching up. It might increase the chance of independent cycles though. If they're really keen try 13 afterwards.

2nd part. The ladder

After you've shuffled and layed out the deck, pick one of the first 9 cards and play the game, as before, reading the cards left to right, going down line by line like a book. (If there's space you can even lay them out in a very long line) When you go past the far end, take a note of the last card of the deck you were on (e.g. if you land on a five, with only three cards left, that's your card).

There's now roughly a 85% chance that any card picked on the first row will lead to this particular card. The reason for this is much like the first part, that there are many routes to one card, but only one route off of it. I suggest getting the first volunteer to do it on their own, when you can astound them by guessing where they'll end up, and then letting the rest all go together, and they may begin to notice that they've all grouped together long before the end.

$\text{P}(\text{success}) \sim 1 - (1-x^{-2})^N$

$x$ = average card value, $N$ = number cards

Again you can experiment with changing the rules and see how well your guesses work. Adding more cards or reducing the step length will increase your likelihood of being right, simply put, the more steps people take, the more likely they are to coincide.

--Real World Applications--

What we're really demonstrating here is a many to one mapping, where there are lots of paths onto one card, but only one path of it. I wouldn't really recommend going into too much detail about this with children, but we can talk about some other interesting examples of many to one mappings.

Buses bunching up are a fun example, there the reason for the bunching (that the first has to pick up lots of passengers, taking a long time allowing the next bus to catch up and as the gap shortens, the number of passengers the next bus has to pick up reduces markedly) is different, but the effect is much the same, showing that once these things come together, the only way to split them apart is ending the game (or in this case the bus line) or artificially holding one back.

This experiment also links to ideas of when things coincide, for example with only even valued cards, it's clear that separate groups that will never meet must form. A really cool example of this in nature is with cicada lifetimes. Predators have a boom, bust style life cycle, where food is plentiful, they over populate, over predate, food becomes scarce, populations dwindle and thanks to low predation the populations of prey increases and the cycle repeats. The cicadas who only emerge after a number of years, don't want to emerge during any of the predator booms, as this would decimate their populations, so in order to avoid this, they have developed prime number life cycles, such that the number of years between periods when they emerge during high predator populations is maximised. As this will happen every lowest common multiple of both the lifecyles, prime numbers maximise this time. You can try and visualise this experimentally by getting people to move around different multiples of the value, those who have common factors should land on the same card more frequently than those whose multiples are coprime. It's important to note that they haven't "chosen" their life cycle, only that the ones with the favourable length cycles have survived best and reproduced to form the largest remaining populations a la natural selection.

There are a few more abstract examples, like water in rivers, that joins together from many different tributaries into one body of water that flows to the sea. You could even talk about the way new technology is invented and sold, different companies often follow the same path (touchscreen on a phone? preposterous!) but lag behind or jump ahead of each other in much the same way that people on the cards lag behind or stay ahead of others.

There are also plenty of examples in computing of many to one mappings, and if you think of any other good ones let us know and we'll add them in to this description!

You could also relate this to other Markov Chains, if random walks is out that's a good example of a slightly different Chain where what you do is not deterministic at each step. You could even do a random walk on this by flipping a coin to decide if you go clockwise or counter-clockwise at each step. Who knows what will happen. You could also talk about this process as being a 'smoothing out' of the randomness of where people start. You can predict very well what card someone might be on after 1000 steps just by picking one in the cycle people get trapped in, no matter where they choose to start. This can then be related to Brownian motion (a continuous time Markov Chain) imagine dropping some food colouring in a fish tank, at the start it's particularly random just a series of droplets, after an hour everything has smoothed out and your fish tank has pale coloured water. If you're feeling brave relate this to Entropy rates and Entropy.
An example lots of people like is Monopoly, it's an irreducible markov chain and has an interesting stationary distribution. Essentially as there are lots of ways to go to jail that skewes the distribution to around 9% jail time, then rolling a double to get out skewes further for Trafalgar square at 3%. You can then use this to estimate how many houses you should optimally buy, however it's all probabilistic, you can get people to think how long it takes to realise these expectations, for Monopoly it's quite a while but for Kruskal it's pretty quick. This introduces mixing times.


<br/>

## Risk Assessment

### **Hazard**: Small parts

**Description**: Children swallowing Duplo pieces, potential choking hazard.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: The Duplo pieces should be sufficiently large to discourage swallowing, but keep an eye out for children putting them in their mouths anyway.
Call first aider if child swallows, if choking encourage child to cough.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Limited cards

**Description**: Many children trying to occupy the same card and people get pushed around.

**Affected People**: Public

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: Keep the number of children playing the game on the giant cards under a sensible limit, I would suggest 8 at a time, and discourage them from running or any form of pushing and shoving.
Call first aider in case of injury.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Cards

**Description**: Cards are slippery if stood on.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Discourage people from actually stepping on the cards.
Call first aider in case of injury.

**After Mitigation**: Likelihood: 1, Severity: 1, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2014-01-20 - Zephyr Penoyre (jp576@cam.ac.uk), **Check 2**: 2014-01-27 - Nunu Tao (nmt26@cam.ac.uk)

**Check 1**: 2015-01-07 - Tim Morgan Boyd (tmb58@cam.ac.uk), **Check 2**: 2015-01-31 - Richard "Miffles" Mifsud (rwm41@cam.ac.uk)

**Check 1**: 2015-12-31 - Joanna Tumelty (jt574@cam.ac.uk), **Check 2**: 2016-01-02 - Tim Morgan Boyd (tmb58@cam.ac.uk)

**Check 1**: 2016-12-09 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2017-02-06 - Mithuna Yoganathan (my332@cam.ac.uk)

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-01-30 - Jean Pichon (jp622@cam.ac.uk)

**Check 1**: 2020-01-07 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2020-01-16 - Jean Pichon (jp622@cam.ac.uk)

**Check 1**: 2020-12-28 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Emma Crickmore (elc75@cam.ac.uk)

**Check 1**: 2023-02-12 - Emma Crickmore (elc75@cam.ac.uk), **Check 2**: 2023-02-14 - Asmita Niyogi (an637@cam.ac.uk)

**Check 1**: 2024-02-15 - Lauren Mason (llm34@cam.ac.uk), **Check 2**: 2024-02-15 - Isobel Gilham (ig419@cam.ac.uk)

**Check 1**: 2025-01-17 - Asmita Niyogi (an637@cam.ac.uk), **Check 2**: 2025-01-26 - Margaret Johncock (mllyj2@cam.ac.uk)
