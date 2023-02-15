# Thinking Caps

**nan** - Can you work out the colour of your own hat?

Last initially checked on 2023-02-15 by Emma Crickmore (elc75@cam.ac.uk) and double-checked on 2022-02-09 by Conor Cafolla (ctc43@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **This experiment can take place outdoors**
- Paper hats in 4 colours, with at least 5 in 2 different colours. Contact Josh (jlg70) for instructions on how to make paper hats, or just watch a youtube video.
- Charts detailing possible configurations of hats for a couple of the problems.

<br/>

## Experiment Explanation 

This demonstration involves getting visitors to solve problems using paper hats. Presented below are some ideas for problems, but feel free to come up with your own. This was developed for and used on mini-tour 2017 for CHaOS PLUS, but some of the ideas can be presented to our general audience. The following are presented roughly in order of ascending difficulty, but anything with a star is more difficult. Only do starred ones if you are very comfortable with the material.

I like to present this in the context of a jail, with me being a sadistic jailer forcing people to cooperate and solve puzzles to escape.

a) 2 people, 2 colours of hats. Put one hat on each person, and let them see the other person. 
Can they work out anything about the colour of their own hat: no, decisions were independent
What if they can speak to each other: yes, just tell the other person their hat colour
Suppose they guess one after the other, is there a way that at least one of them can be correct: yes, the first person just guesses the other person's colour
*What if they guess at the same time, agreeing a strategy beforehand: Often people say guess randomly. this has a 75% chance of working. get them to work this out. What other strategy could they use, incorporating the information about the other person's hat? They could guess the same, which has a 50% win rate. They could guess differently, which has a 50% win rate. one person guesses the colour they see, the other person guesses the opposite of the colour they see has a 100% win rate, combining the above 2 strategies.

Note: The above strategy means that 100% of the time exactly one person gets the right answer. This is the best we can do - i.e. no strategy exists that works 100% of the time where sometimes both people get the right answer. The reason for this is that regardless of strategy the expected number of correct answers for each person is 1/2, so any strategy averages 1 correct answer between the 2. Thus if it ever exceeds 1 it must also sometimes fail.

*b) As in the last part above, but we have 3 people. This is easy, because 2 people just play the game and ignore the other person. So what if there are 3 potential colours of hats? In this case the strategy is harder, and you will need to teach a bit of modular arithmetic. A nice way to approach this is to rephrase the 2 hat strategy. One person was right when there were an even number of red hats, and the other right when there were an odd number. Instead of calling the hats red and blue, lets call them 1 and 0, and have one player assume that the hats add up to 0 and the other to 1. They can then determine the colour that their own hat needs to be for them to be correct. But wait, what if the sum of the hats is 2? Well, in order to make this work we are going to have to do a funny sort of math where 2=0. So what is 1+1 you ask? 0 they say. There are no other sums, since all numbers are 0 or 1, and they can probably do 0+0 and 1+0. 

Now, for 3 hats, instead of calling them red and blue and green, call then 0 1 and 2 and do the same thing. Here we use a different sort of funny maths where 3=0. Get them to do all the sums in this maths (2+1 = 0 and 2+2 = 1). If one player assumes the sum is 0, another assumes it is 1 and the last assumes it is 2 then one of them has to be correct. the challenging part of this is trying to get kids to come up with most of it themselves. This should be possible with older kids (15+) but I haven't tried with young ones.

c) A line of n people, 2 possible colours of hats, one hat on each person. Each person can see all the hats of people in front of them in the line, none of the hats behind them. People guess one after the other, starting at the back of the line. They can agree on a strategy beforehand.
Can we guarantee somebody gets it right: yes, person at back just says the colour they see on next person, next person says that colour
How many can we guarantee: Half (rounding down), using the above stratergy
What if there are 3 people, can we definitely get 2 right (half rounded up): yes, the person at the back says red if they see 2 of the same colour, blue if they see 2 different colours. This tells the next person if their hat is the same or different to the one they see. Then the person at the front knows if their hat is the same or different to what they just heard.
*In general, what is the best we can do: n-1, since the person at the back reports the parity of the number of red hats they see (red = even number for example), and then everyone can determine their hat from what they have heard before.

*d) As before, but the line goes infinitely far forward. What is the best you can do (will infinitely many people always get it wrong). It turns out that the answer is no, you can make sure that at most finitely many people get the answer wrong (if you assume the axiom of choice). When discussing strategy, divide all possible sequences of hats into equivalence classes based on whether 2 sequences are eventually the same, and then pick a representative from each class. All people answer as if they are in the representative of whatever class they are in. Since the sequence they are answering in and the sequence they are actually in differ only finitely many places, only finitely many people will be wrong.

e) Now we have 3 people and 2 possible colours of hats. The rules are as before, except at least one person has to get it right and nobody can get it wrong. Strategy can be discussed.
What is the best we can do: 12.5%, since if nobody can get it wrong everyone must be right
What if we allow passing: a simple strategy is to have one person guess, and the other 2 pass, giving a 50% win rate. Can we do better than this? It turns out that there is a better strategy. Since each person who guesses is wrong/right 50% of the time, the only way we can do better is to have the correct answers spread out but have everybody be wrong at the same time. To do this, we use the following strategy - if you see 2 of the same colour hat say the opposite colour, otherwise pass. Thus exactly one person will be right 75% of the time, and 25% of the time everybody will be wrong. A table illustrating this should be included in the maths box.





<br/>

## Risk Assessment
### **Hazard**: Hat corners
**Description**: Risk that children will poke their eyes with pointy hat corners.

**Affected People**: children

**Before Mitigation**: Likelihood: 2 , Severity: 2, Overall: 4

**Mitigation**: 'Make sure that children handle hats as little as possible, and mostly just wear them. When they do handle them make sure you know who has them and whether they are being sensible.
Call first aider in case of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall:2 

<br/>
### **Hazard**: Hats
**Description**: Risk that hats will fall on floor and children will slip on them.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4 

**Mitigation**: Make sure you know where hats are at all times and that children are not running around in a way that could be dangerous if hats fall.\r\nCall a first aider in the event of an injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>
### **Hazard**: Paper
**Description**: Risk that children will cut themselves on paper edges.

**Affected People**: children

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Make sure that children handle hats as little as possible, and mostly just wear them. When they do handle them make sure you know who has them and whether they are being sensible.\r\nCall first aider in case of injury.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk), **Check 2**: 2018-01-16 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2020-01-07 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2020-01-27 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2020-12-12 - Yian Aaron Koh (yak23@cam.ac.uk), **Check 2**: 2021-01-22 - Richard "Miffles" Mifsud (rwm41@cam.ac.uk)

**Check 1**: 2022-02-09 - Grace Exley (gae23@cam.ac.uk), **Check 2**: 2022-02-09 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2023-02-15 - Emma Crickmore (elc75@cam.ac.uk), **Check 2**: 
