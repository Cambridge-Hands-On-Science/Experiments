# Horse Racing

**Probabilities of rolling dice.** - Understanding the probabilities behind throwing pairs of dice.

Last initially checked on 2025-01-12 by Asmita Niyogi (an637@cam.ac.uk) and double-checked on 2025-01-26 by Jessica Trevelyan (jet81@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**Probability**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Duplo blocks (horses) and cardboard racetrack
- 2 giant write on/ wipe off dice
- 3 giant normal dice
- Lego blocks and baseplate
- Drywipe pen for writing on dice and lego
- Laminated sheet of paper for use as whiteboard
- (There are other misc dice in the box which may be useful, including a D12)

<br/>

## Experiment Explanation 

**The Horse Race**

This can be done either with duplo horses on the boards, or if space permitting with the children playing the part of the horses. 

(If children are playing the part of the horses make sure they're all taking steps of the same length roughly, chances are they'll all take the biggest steps they can but particularly tall children might have to have their ambitions tempered a little)

Each horse has a number associated with it, in the most basic formulation, with two normal dice, the numbers range from 2 to 12, although with less children it's better to assign them numbers nearer the middle rather than the edges.

Each step, roll both dices, get everyone to shout out what they both add up to and whoever's number is shouted out moves forward one step. Done like this, horse number 7 should win pretty comfortably everytime (although the shorter a track you use, the more likely 6 or 8 or even others might win).

What's the reason for this, simply put a seven is the most likely number to be rolled. The easiest way of explaining this is showing them how many different ways there are to add up two dice to seven (1+6, 2+5...5+2, 6+1). There are 6 ways to add up to seven, 5 to add up to six or eight and so on until only 1 for two or twelve. There are 36 total possibilities (and each is equally likely), so the chance of getting a seven is 1/6. Depending on ages you may find they've seen some of this before in schools so you may move through it quite fast.

People might ask how 6+1 and 1+6 are different. The formulation used above ensures all 36 possibilities are equally likely, which makes all the calculations much easier. One way to look at it is throwing the dice one at a time and showing that the two different possible orders shows that there are twice as many ways to get, for example, 1 and 2, than there are to get 1 and 1. This point is quite subtle and I wouldn't advise going into it unless prompted or if you have a really great explanation!

Now, using the wipe clean dice, try changing up the rules to see what effect it has on who wins. I advise having explained all the different probabilities to them already. Maybe even make a chart of how many different ways there are to add up to each outcome.

There are lots of things you can try here, but here are a few ideas, you may find some work better with different ages:

1. **Change Dice Numbers**

Subtract one from each side of one dice (or better yet, change the six to a zero!) - Now six and seven should be neck and neck. You can either show them this beforehand, or get them to guess which horse they're going to be and see whose understood it (nothing wrong with letting more than one person be represented by the same number now, but keep them in separate lanes).

Change all sides except three and four of both dice to one - Firstly get them to pick horses, explain why now there are only 6 options (2, 4, 5, 6, 7, and 8), as 7 is still a possibility many will likely go for it, but of course now number two should fly ahead, as there are hugely more ways of making 2, and all others should stay roughly level (two ways to make all other numbers)

Change how many steps some numbers get to take - Why not let all numbers less than 4 and more than 10 take two steps each time they're picked, now the race should be much more even. Ask them to work out how many steps the people with numbers 2, 3 and 4 would need to take each go to be neck and neck with seven (the answers are six, three and two respectively). This introduces the concept of an expectation value, the product of probability and result (here counted in steps forward), and that events with the same expectation value should have roughly the same total result after a lot of tests.

There is also a D12 in the Maths box which can be used, this obviously makes the game totally fair. 

2. **The two dice**

This is a very nice demonstration of why the previous experiment works. Simply ask people to throw two dice, and put a lego brick in the column relating to their result. Quite quickly a pretty uniform distribution should build up, looking like a pyramid (this isn't actually the underlying distribution, just the fact that we've got very few different possibilities flattens the sides of what should look like a bell curve). That said, at times it will look quite irregular and it's a good chance to talk about error, lots of people will think the dice must be weighted to cause irregularities but actually it's simply that there is a natural variation to any test and that only for a large number of tests is this smoothed out (error in mean scales as 1/sqrt(N) and roughly speaking so does all the variations, where N is the number of tests). 

Now try it with three dice, this should give a smoother curve, but will take much longer to build up as there are now 15 possible values. You should see something akin to a bell curve with long tails, a rise in the middle with a flat top, and symmetric across the line between 11 and 12.

You can put name labels on both curves but you may want to periodically deconstruct the two dice curve, so you can keep talking about the variation from the expected shape. Definitely put labels on the three dice curve, and encourage people to try multiple times and to come back and see how it's developing.

See here for how it evolves for one, two three or four:
http://www.syque.com/quality\_tools/toolbook/Variation/measuring\_variation.htm

You could link this to central limit theorem and talk about how heights are distributed roughly normally, as are most other things.

3. **How long until you roll a six?**

Very simple premise but a slightly more complex explanation this one: throw a dice as many times as necessary until you get a 6. What distribution would you expect to see?

What we actually see is that the highest possibility occurs on the first throw (1/6th of total bricks should be here) and then reduces in a smooth curve that in theory goes on to asymptote to 0 at infinity.

Now get them to do the same but now waiting for either a five OR a six. And then again with either four, five or six. (Make sure they do all three tests so that there are about the same number of bricks in each distribution)

You should see that the second has a higher peak then drops quicker and even more so for the third experiment.

These are all geometric distributions (http://en.wikipedia.org/wiki/Geometric\_distribution) relating to some probability p (p=1/6 for the first, 1/3 for the second and 1/2 for the third)

If the person you're explaining to seems comfortable with fractions, you can try the full explanation:

Firstly (and this works with all ages), try and get them to work out the probability of throwing the particular value, and show them that this fraction is almost exactly the fraction of bricks in the first column.

Secondly, ask them what the probability is of NOT throwing the required value, explaining that probabilities must add up to one (or do it in percentages adding up to 100%). Obviously this is the fraction NOT in the first column.

Thirdly, (and this is where you may want to stop for younger kids) show them that for every throw that you don't throw a six, the probability compounds by 5/6ths, and on the final throw that you do there is an added fator of 1/6th. Or more fully, the probability of throwing the first six on the nth throw is (5/6)^n-1 * (1/6).

The main thing to get across here is that all probabilities must add up to one, and some idea that the more likely situation should have the tallest peak at n=1 and then drops off much faster.

Write the initials on each brick that someone places on the distribution and watch how it builds up over the event.

<br/>

## Risk Assessment

### **Hazard**: Small parts

**Description**: Children swallowing dice, Duplo or Lego pieces

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: The Duplo pieces should be sufficiently large to discourage swallowing. Do not use Lego with very small children and keep a close eye on the box of Lego and dice.
If child swallows, call first aider and encourage child to cough if choking.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Dice/Duplo blocks/lego pieces

**Description**: Dice/Duplo blocks/lego pieces could be a trip hazard if dropped on floor.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Keep an eye on where any dice go, and try to confine them to a desk or fixed area. Do not let multiple unattended children use dice at the same time. Quickly pick up any items which have fallen.
Call first aider in case of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2014-02-02 - Zephyr Penoyre (jp576@cam.ac.uk), **Check 2**: 2014-02-08 - Nunu Tao (nmt26@cam.ac.uk)

**Check 1**: 2015-01-07 - Tim Morgan Boyd (tmb58@cam.ac.uk), **Check 2**: 2015-01-31 - Richard "Miffles" Mifsud (rwm41@cam.ac.uk)

**Check 1**: 2015-12-18 - Joanna Tumelty (jt574@cam.ac.uk), **Check 2**: 2016-01-02 - Tim Morgan Boyd (tmb58@cam.ac.uk)

**Check 1**: 2017-01-09 - Joanna Tumelty (jt574@cam.ac.uk), **Check 2**: 2017-01-06 - Mithuna Yoganathan (my332@cam.ac.uk)

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2020-01-07 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2020-01-27 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2020-12-28 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Margaret Johncock (mllyj2@cam.ac.uk)

**Check 1**: 2023-02-12 - Emma Crickmore (elc75@cam.ac.uk), **Check 2**: 2023-02-14 - Asmita Niyogi (an637@cam.ac.uk)

**Check 1**: 2024-02-15 - Lauren Mason (llm34@cam.ac.uk), **Check 2**: 2024-02-15 - Charlotte Marshall (csm69@cam.ac.uk)

**Check 1**: 2025-01-12 - Asmita Niyogi (an637@cam.ac.uk), **Check 2**: 2025-01-26 - Jessica Trevelyan (jet81@cam.ac.uk)
