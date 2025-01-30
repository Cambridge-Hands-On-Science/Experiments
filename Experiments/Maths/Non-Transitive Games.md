# Non-Transitive Games

**What's the best option in games of chance?** - Some games really aren't fair. Even if your opponent knows your exact move you can still beat them. Explore some of these games and find out there might not be a sensible best choice.

Last initially checked on 2025-01-26 by Jessica Trevelyan (jet81@cam.ac.uk) and double-checked on 2025-01-30 by Isobel Gilham (ig419@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Games**



**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Many sets of 4 non-transitive dice:
  - Orange - 2,2,2,2,6,6
  - Yellow - 3,3,3,3,3,3
  - Green - 1,1,1,5,5,5
  - Blue - 0,0,4,4,4,4
- A Microsoft box, which has the same dice 
- A set of Grimes Dice (seems to be missing)

<br/>

## Experiment Explanation 
_Currently copy-pasted from [aka.ms/ntdice](https://aka.ms/ntdice); TODO write our own or switch back to Grime Dice..._

### About the dice

First of all, let us examine the dice in detail. Here we have ‘flattened’ the dice to show the numbers on each of the faces.

  - Orange - 2,2,2,2,6,6
  - Yellow - 3,3,3,3,3,3
  - Green - 1,1,1,5,5,5
  - Blue - 0,0,4,4,4,4

We see that the choice of numbers is unusual. But in all other respects these are normal, fair dice. If we pick two of the dice and roll them, we can see which comes up with the higher number. We will say that the die with the higher number is the winner. Notice that each of the numbers 0, 1, 2, 3, 4, 5, and 6 appears on only one of the dice, which means that when we roll one die against another, there can never be a draw.

First, suppose you roll the orange and yellow dice. Two thirds of the time the yellow die will come up with a higher number than the orange die. We say that the probability that the yellow die will win is two thirds. If we make a large number of such rolls and keep track of which die wins, then there is a very high chance that the yellow die will win more often than the orange die.

Likewise, two thirds of the time the blue die will win against the yellow die, and two thirds of the time the green die will win against the blue die. So, yellow beats orange, blue beats yellow, and green beats blue.

It therefore seems as if the green die has the highest chance of winning and the orange die has the lowest. But now for the surprise: if you roll the green die with the orange die, then two thirds of the time it is the orange die that will win!

These are known as _non-transitive_ dice. 'Transitive' means that if A beats B and B beats C then A beats C. We see that these dice do not have this property. One way to visualise this is to arrange the dice in a circle, such that each die beats the previous one.

**Yellow beats orange, blue beats yellow, green beats blue and orange beats green.**

This is rather like the game of “rock, paper, scissors” in which scissors beats paper, and rock beats scissors, but paper beats rock.

### A simple game

You can use this non-transitive property to play a game with a friend. Invite them to examine the dice and then to select any one of them. Without telling them the secret, you now select the next die in the sequence, and then you make, say, 9 rolls against your friend, and keep note of how many times each of you rolls the higher number. Over a sequence of 9 rolls it is very likely that you will roll a higher number more often than your friend.

### How the dice work

Look first at the orange die, and notice that it has four copies of the number 2 and two copies of the number 6. Two-thirds of the time, when we roll the orange die it will give a 2, and one third of the time it will give a 6. Therefore, if we roll the orange die against the yellow die (which always gives a 3), the yellow die will, on average, win two-thirds of the time, and will lose one-third of the time. You can repeat this game several times, each time allowing your friend to choose their die first.

Now look at the blue die, and notice that it has four copies of the number 4, and two copies of the number 0. When we roll it against the yellow die, it will therefore give a 4 two thirds of the time, in which case it wins, and a 0 one-third of the time, in which case it loses.

Now suppose we roll the green die against the blue die. The green die has three copies of the number 1 and three copies of the number 5. To work out the probability that the green die will win we first note that there is a probability of 1/2 that the green die will give a 5, in which case it is certain to win against the blue die. Likewise, there is a probability of 1/2 that the green die will give a 1, in which case there is a probability of 1/3 that it will win. The overall probability that the green die will win is then given by multiplying the probabilities:

$$
\left(\frac{1}{2}\times 1\right) + \left(\frac{1}{2}\times \frac{1}{3}\right) = \frac{2}{3}
$$

Finally, consider the probability of the orange die winning against the green die. There is a probability of 1/3 that the orange die will produce a 6, in which case it is certain that the orange die will win. There is similarly a probability of 2/3 that the orange die will produce a 2 in which case there is a 1/2 chance that the orange die will win. The overall probability of the orange die winning is again obtained by multiplying the probabilities:

$$
\left(\frac{1}{3}\times 1\right) + \left(\frac{2}{3}\times \frac{1}{2}\right) = \frac{2}{3}
$$

### Bonus story from Microsoft!

Warren Buffett once challenged Bill Gates to a game of dice. “Buffett suggested that each of them choose one of the dice, then discard the other two. They would bet on who would roll the higher number most often. Buffett offered to let Gates pick his die first. This suggestion instantly aroused Gates’ curiosity. He asked to examine the dice, after which he demanded that Buffett choose first.” Buffett was using a set of non-transitive dice!


### Grime Dice (which we seem to have lost...)
_At some point we should buy a proper set from [MathsGear](https://mathsgear.co.uk/collections/dice/products/non-transitive-grime-dice)._

There should be a set of dice in the box with the following numerals:
- red - 9,4,4,4,4,4
- blue - 7,7,7,2,2,2
- olive - 5,5,5,5,5,0

(They're slightly larger than normal so we can move onto 5 dice later using the same ones)

Take turns with your opponent to pick a dice and see who can roll the highest number. Try a best of three or five to decide which dice to pick, if they pick first you can always beat them. What you'll find is Red > Blue > olive > Red. Get them to construct two of the chain and ask them to guess what happens with the third pairing. Most will think that it's going to be transitive and Red will beat olive, however it isn't! Easy way to remember the order is increasing word length.

Any easy way to relate this is to rock, paper, scissors. Here Rock > Paper > Scissors > Paper. When we pick at different times this games becomes very unfair. With the dice there's no certainty but you can explain by playing multiple times you make it more likely.

You can take some maths and try and work out the winning probability. Red beats Blue if we get a 9 straight away, that's probability 1/6. If we get a 4, 5/6 probability, then we win when Blue gets a 2, probability 1/2, these are 'independent events' so we can get a total probability of 1/6 + 5/12 =7/12 > 1/2. You find this is the same for all pairings. 

If they've understood flip it around and let them beat you. Then move to two dice and keep going first. You'll want to increase the number of rolls to make it a best of 5 at least. You'll notice that in fact the order swaps around when you look at the totals. It should decrease to about 57%.

Lets add in 2 more dice. We want to be able to beat 2 players simultaneously

- yellow - 8,8,3,3,3,3
- magenta (pink) - 6,6,6,6,1,1

There's an alphabetical chain and a word length chain. Alphabetical chain has a higher win probability if there's only one player. If there's two you can find a unique dice to beat both.

This analogues Rock,Paper, Scissors, Lizard, Spock (from The Big Bang Theory TV show) with new rules

Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporises Rock, (and as it always has) Rock crushes Scissors.

In this game the doubling of dice reverses the word length chain and the alphabetical chain remains more or less the same apart from the fact red and olive flips technically but remains very close to 50-50. Overall 59% win chance.

For beating two players we're at 44%. You may think that's bad as you still lose fairly often but you only lose to both 22.7% of the time. Consider a game where both opponents pay £1 and you'll pay out £1 to anyone who rolls higher. For 100 rolls you make £88 on the games you beat both on 44 rolls, lose £46 when you lose to both on 23 rolls and the rest of the time you make nothing (but don't lose anything either). So you're £42 in profit!

Inspired by the experiment here:
http://singingbanana.com/dice/article.htm



If you have a spare table this is a very easy experiment to float with by only going up to the Rock-Paper-Scissors part of the experiment. Demonstrate you can always win and sometimes "better than" isn't transitive.

<br/>

## Risk Assessment

### **Hazard**: Dice

**Description**: Children swallowing or choking on dice.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: Don't use with small children and keep the dice attended.
Call first aider if child swallows, if choking encourage child to cough.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Dice

**Description**: Dice could be a slip hazard if dropped on floor.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Keep an eye on where any dice go, and try to confine them to a desk or fixed area. Do not let multiple unattended children use dice at the same time.
Call first aider in case of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Rock Paper Scissors

**Description**: Kids getting too enthusiastic and attacking others when playing rock paper scissors

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: Encourage kids to be calm. Make them stop if they are being silly / don't play RPS with them
Call first aider in case of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2017-02-09 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2017-02-11 - Fiona Coventry (fiona.coventry@cantab.net)

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2020-02-05 - Andrew Sellek (ads79@cam.ac.uk), **Check 2**: 2020-02-05 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk), **Check 2**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2022-02-05 - Andrew Sellek (ads79@cam.ac.uk), **Check 2**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk)

**Check 1**: 2023-02-05 - Emma Crickmore (elc75@cam.ac.uk), **Check 2**: 2023-02-16 - Lauren Mason (llm34@cam.ac.uk)

**Check 1**: 2024-02-15 - Peter Methley (pm631@cam.ac.uk), **Check 2**: 2024-02-15 - Lauren Mason (llm34@cam.ac.uk)

**Check 1**: 2025-01-26 - Jessica Trevelyan (jet81@cam.ac.uk), **Check 2**: 2025-01-30 - Isobel Gilham (ig419@cam.ac.uk)
