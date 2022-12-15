# The Game of Life

**A game about life.** - Watch populations evolve from simple beginnings, explore stability of patterns and model a computer in one experiment on cellular automata. See even more complex patterns on a computer too!

Last initially checked on 2021-01-22 by Polly Hooton (prh43@cam.ac.uk) and double-checked on 2021-01-22 by Grace Exley (gae23@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Computer Science**

**Maths**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **Electricity needed**
- Counters with binary states (Othello/Reversi pieces, coins, counters with drawings on, etc)
- A square grid to place the counters.
- 
- Currently this uses exactly the same equipment as the "sieving" experiment with a 10x10 wooden grid and red/green counters.
- Laminated printout of patterns.
- --Optional-----
- You may wish to use a computer and a game of life program.
- 'Golly' and 'Mireck's Celebration' are two such programmes.

<br/>

## Experiment Explanation 

As part of this experiment you have a large board, this represents the cells of our automata, the labelling is not important for this experiment. If you don't have a grid you can just lay out the counters in a square lattice or draw on on paper. You've also got some binary way to indicate state, two sides of a counter or presence/absence of a counter. We'll talk about 'alive', 'green', 'good', 'present', '1' and the opposite notions of 'dead', 'red', 'bad', 'absent', '0'. I'll try and stick to the former but may fail. We use flip to denote a change between these states and often 'birth' to mean 'dead' to 'alive' and 'death' for the opposite transition. Obviously our grid should go on ad infintum but we don't have a big enough box for that. You may choose any size you wish, 10 by 10 is small but use able. You may want to simulate this experiment on a computer too.

So what is the Game of Life? 
It's worth knowing some of the History. Initially people wanted to design something that simulated 'life', mathematicians defined this to mean it can 'reproduce' and also simulate a computer.
They looked at things called cellular automata, we have a grid (normally square) and in each put in a counter to indicate if the cell is alive or dead. We then run a series of rules to determine the change between turns.
While it's called a game there's not any players, you choose an initial configuration of cells and then let the game play for ever. We also don't have a boundary, you can make things as big as possible and they can drift arbitrarily far.
The game is by Conway who wanted to make something "interesting and unpredictable", you'll find stable patterns, drifting patterns and cycles. It also turns out that it satisfies the two properties for 'life'. His 4 design principles were
1. No explosive growth.
2. There are small patterns with chaotic, unpredictable outcomes.
3. There are 'self-replicators'.
4. The rules are simple.

So the rules are. We start by picking some cells to be alive. We then work in 'turns' or 'ticks' we apply all the rules simultaneously so all 'births' and 'deaths' happen at the same time. The neighbours of a cell are those in the 8 cells around it, this includes the diagonal neighbours but not the cell its self.
1. Any live cell with 0 or 1 live neighbours dies of under-population/loneliness. 
2. Any live cell with 2 or 3 live neighbours lives on.
3. Any live cell with 4,5 or 6 live neighbours dies of over-population.
4. Any dead cell with exactly 3 live neighbours becomes alive by reproduction.
5. All other dead cells stay dead.

To do this you'll need to think of a snapshot and turn over based on that. If you want to explore big patterns your best looking at a computer.
Why not try and look for a stable pattern, these are rather boring patterns that don't do anything, so we'll need every cell to have 2 or 3 neighbours, see if you can find some. Thinking about making things relatively symmetric is a good idea, lots of small stable shapes have rotational and/or mirror symmetries, can you find one only with a single diagonal mirror symmetry? (loaf or boat work) You'll need to test the shapes under one iteration, you could maybe let them run an initial guess a few times to see if it stabilises while they understand the rules, don't try it too long though because of number 2 in the motivations, it'll probably also 'vanish'.

0000
0110
0110
0000
Square

000000
001100
010010
001101
000000
Beehive

000000
001100
010010
001010
000100
000000
Loaf

00000
01100
01010
00100
00000
Boat

00000
00100
01010
00100
00000
Tub

One cheeky one that also works is
000
000
000
Vannished

No let's try and look at some patterns that move, another interesting type of pattern is an oscillator, these cycle round a few shapes and then return. You might have found some trying the previous exercise. If not here are some you might try and find.

00000 -> 00000
00000 -> 00100
01110 -> 00100
00000 -> 00100
00000 -> 00000
Blinker

000000 -> 000000
000000 -> 000100
001110 -> 010010
011100 -> 010010
000000 -> 001000
000000 -> 000000
Toad

000000 -> 000000
011000 -> 011000
011000 -> 010000
000110 -> 000010
000110 -> 000110
000000 -> 000000
Blinker

On a computer you might also like to try the following, warning they get bigger than 10 by 10!

000000000000000
000111000111000
000000000000000
010000101000010
010000101000010
010000101000010
000111000111000
000000000000000
000111000111000
010000101000010
010000101000010
010000101000010
000000000000000
000111000111000
000000000000000
Pulsar (period 3)

00000
01110
01010
01110
01110
01110
01110
01010
01110
00000
Pentadecathlon (period 15)

Now we've seen these we might believe everything eventually becomes one of these stable or oscillating things, if it did we could sort of draw a box for each pattern and trap it. We'll talk about some patterns that need a big box later but in fact that's not the case. If you run a few computer trials you'll find sometimes you can 'fire' alive cells off the screen. You could try and make a shape like this on the grid, the simplest has 5 live cells and fits in a 4x4 square. 

00000 -> 00000 -> 00000
00100 -> 00000 -> 00000
00010 -> 01010 -> 00010
01110 -> 00110 -> 01010
00000 -> 00100 -> 00110 etc.
Glider

0000000
0010010
0100000
0100010
0111100
0000000
Lightweight Space Ship (LWSS)

For computer users you may want to try and come up with some 'hard to kill' paterns, these take a while to settle into a combination of these types, a few you can try are bellow.

00000
00110
01100
00100
00000
R-pentomino

0000000000
0000000100
0110000000
0010001110
0000000000
Diehard

000000000
001000000
000010000
011001110
000000000
Acorn

These are called 'Methusulas' and Diehard takes 130 turns to fully disapear, which is thought to be maximal among 7 cell starts. Acorn takes 5206 turns and fires off 13 gliders.
The sheet also contains several large patterns like the "Gosper Glider Gun" and the "Block-laying switch engine" which periodically fires off gliders and blocks respectively. There are even breeders which leave behind trails of guns as they move along each gun firing out gliders. 


<br/>

## Risk Assessment

### **Hazard**: Counters

**Description**: People swallow or choke on counters

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: Tell them not to eat counters. Take away from very small children if they are trying to eat them.
Call first aider if child swallows, if choking encourage child to cough and call a first aider.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Dropped counters

**Description**: Risk of slipping on counters.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

**Mitigation**: Pick counters up if left on floor
Call a first aider in the event of injury.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-01-21 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-02-07 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-02-08 - Jared Jeyaretnam (jaj55@alumni.cam.ac.uk)

**Check 1**: 2019-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2019-02-04 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2019-12-26 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2020-01-27 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk)