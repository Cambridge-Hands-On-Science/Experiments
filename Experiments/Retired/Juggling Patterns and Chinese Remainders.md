# Juggling Patterns and Chinese Remainders

**Maths through the medium of juggling** - Learn about sequences, periods, patterns, and the Chinese remainder theorem through the medium of juggling balls. 

Last initially checked on 2021-01-22 by Polly Hooton (prh43@cam.ac.uk)) and double-checked on 2021-01-22 by Grace Exley (gae23@cam.ac.uk))

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- 3 juggling balls (or 5)
- Ability to juggle (not in box)
- Metronome or beat (optional)
- Whiteboards and pens

<br/>

## Experiment Explanation 

It's worth putting here for emphasis, THIS EXPERIMENT REQUIRES A DEMONSTRATOR WITH SKILL AT JUGGLING, since this isn't a course in tripos yet it is basically fairly restricted who can demo this. Although lots of mathmos can juggle it's a generalisation to say all can (I (TW) can't juggle but wrote this though) 

There are two possible ways to introduce this. 

What is maths? 
What do we study in maths? Numbers, patterns, etc.
So let's look at some objects called a sequence, a sequence is a list of numbers, one after another. Write some sequences. Most sequences go on for ever. We can't write for ever. Lots of sequences repeat eventually. We call the length of this repetition the period. Now what sequences can we associate to juggling?
Juggle to a beat, only throw a ball on a beat. We can think about at each beat how many beats that ball is in the air. For the simplest three ball juggle this gives the sequence 3,3,3,... This has period 1. We can juggle other patterns too. We have lots of sequences we can write down, we call a sequence a juggling sequence if we can get it from a valid juggle. 

What is juggling?
Start juggling to a beat, can we observe a pattern, can we write it down using maths? This juggling is hot potato style, we catch and immediately throw on the same beat and don't catch two balls on one beat.That's going to be our aim. Think about each beat we through a ball, how long is it in the air? If there isn't a ball we can write zero. We call it a n-throw. This builds up a sequence of numbers, this is where we can use maths. Eventually our juggle repeats and so the sequence repeats if we kept juggling forever, we call this the period. We call any sequence we get this way a juggling sequence. 

Juggling sequences
Now we can turn different juggles into sequences let's think about what we've encoded. What about the number of balls? Take the sequence 3,3,3,... It doesn't work with five balls as we'd end up with more balls landing than hands, 5,5,5,5,5,... Doesn't work with three as on beats 4 we'd need to throw a ball for 5 beats but all our balls are already in the air. So maybe it does encode the number of balls somehow. This is to do with the period. The numbers in the sequence tell us how long each ball is being thrown for, we know at the end of the period we've 'reset' to like the beginning, we also know how many beats that's been. So if we add up the total number of beats we've thrown balls into the air for, then divide by the number of beats that have passed, we'll get the number of balls in the juggle.

Sequences can give us the same juggle for instance 5,0,1,... 0,1,5,... 1,5,0,... Can you see why?

We can draw pictures of to show if a sequence can be juggled. We put dots for each beat and write the sequence underneath. Then put an arced line corresponding to the ball being thrown up and landing that many beats away. Can you see what a good and bad diagram would look like? If we have a line into a beat we need a line out. Also this is the only way we can have a line into a beat. How large will this diagram have to be? We'll need to cover the period! 

Is 1000000, 1,1,... Jugglable? Can you draw its diagram, you'll need a million dots....

We need a better method. This is where we can use maths, yay! 

We've already shown a few sequences can't be juggling sequences. For instance 3,1,1,... Can't be as the number of balls wouldn't be an integer! We also catch two balls on beat 4. Any more sequences? 

An algebraic process is as follows. Take your sequence and add on their position (0 indexed). We'll test 4,4,1,3,.... After adding we get 4,5,3,6. We then want to take the remainder mod the period. This gives us 0,1,3,2. If and only if we get all different numbers it's a juggling sequence. This uses Chinese remainder theorem to guarantee there's no collision, you should explain this.

We can then figure out things we can do to sequences to alter them and still make them juggling. 
For instance adding a multiple of the period won't affect the remainder. 
What about swapping things, if we do a swap and then increase the thing on the left by one and right decreases by one that works with the addition step.
Increasing the period by multiplying by an integer. This doesn't change anything as the second repeat gets an extra bit. 
It turns out every juggling sequence can be obtained by doing these operations on constant sequences which are easily Jugglable. 



You can link this to cyclic group stuff from Hexaflexagons. 


<br/>

## Risk Assessment

### **Hazard**: Juggling Balls

**Description**: Children hit by balls or flailing arms in juggling process.

**Affected People**: Children (or demonstrator if children are attempting to juggle)

**Before Mitigation**: Likelihood: 4, Severity: 3, Overall: 12

**Mitigation**: Make sure patterns to be juggled are sensible (i.e. not requiring more balls than juggler has experience with and contain low numbers). If children are juggling get them to stand apart and to not chase after balls that are dropped.  Demonstrator to retrieve and keep track of all balls (e.g. don't let kids climb under tables to retrieve them). Don't performing experiment near a road or path. Make sure juggled items are soft in case of impact. Use soft juggling balls or beanbags.

**After Mitigation**: Likelihood: 2, Severity: 1, Overall: 2

<br/>

### **Hazard**: Whiteboard Pens

**Description**: Children could be tempted to lick the pens and become sick as a result.

**Affected People**: Children

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Monitor the pens and don't let very small children use them (at least without supervision).
In case of licking, call first aider, or tell parent to contact GP if child feels ill later.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3

<br/>

## Risk Assessment Check History 

**Check 1**: 2019-01-28 - Thomas Webster (tw432@alumni.cam.ac.uk)), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk))

**Check 1**: 2020-02-05 - Conor Cafolla (ctc43@cam.ac.uk)), **Check 2**: 2020-02-05 - Grace Exley (gae23@cam.ac.uk))

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk))