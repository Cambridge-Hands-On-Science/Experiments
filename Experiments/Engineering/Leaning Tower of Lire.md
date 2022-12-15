# Leaning Tower of Lire

**Balancing blocks on the edge** - Explore this famous block stacking problem and see how far you can build off the edge of a table. 

Last initially checked on 2022-02-01 by Polly Hooton (prh43@cam.ac.uk)) and doublechecked on 2022-02-06 by Lauren Mason (llm34@cam.ac.uk))

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Engineering**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Table/ small ledge (Turn over one of the cantilever bases)
- Blocks (from Cantilever Bridge)

<br/>

## Experiment Explanation 

This is a great follow on to Cantilever bridges, if they've seen that experiment this expands on one of the initial things many people try.
Your challenge is given N identical blocks place them in a stack (one on top of each other) and try and maximise the overhang over a table edge.
If they've seen Cantilever they may try the cantilever solution, however the twist here is you're only allowed one brick per layer (this means the tower must be N bricks tall).
We'll now talk through some physics that we'll need to figure out how well we can do.
Centre of Mass - We can view gravity as acting through one point of the block, we call this the CoM, if the block is uniform it'll be in the centre, sort of where you'd expect.
Try placing the block on the edge of the table and moving it's CoM around, where can it balance? You'll find that you can get out until the CoM is right on the edge but no further. This means for N=1 we've solved the problem! The answer is 1/2 (times the length of the block).
Moments - A Moment is a turning force, this is what we get when the block is on the table. For a moment, we need a pivot. With one block our only pivot is the point on the edge of the table, friction holds the block enough so that what we experience here is just a turning force (initially you'll notice a slip later once it's started falling, see the falling toast experiment for more on this though). The forces are the gravitation acting through the CoM and a reaction force from the table supporting the brick.
Levers - levers increase the force with distance. With moments we need to consider a levered force by timising the force by distance from the pivot. If the forces clockwise and counterclockwise (ccw) balance then there's no tip. If we have an unbalanced force twisting us into the table then it won't tip but we could extend further!
So going for N=2 case now. We can keep extending like before but we need to decide which order is going to give us the best overhang. As we need to consider the CoM it would be better if there was the least total overhang, this means that the overhang between blocks on one layer and the one above should increase as we get higher up.
Obviously don't tell them this let them try it. If they place something on top of the N=1 solution it'll pivot (unless it's not more overhanging). They'll actually need to place something underneath it.
The maximum turns out to be 1/2 + 1/4 = 3/4.
Ask them how far out they think they can reach? Can they get arbitarily far if they can make N large?
It turns out you can, the optimum is 1/2*\sum\_{i=1}^{N} 1/i. This is half the harmonic series so it does in fact diverge, which you can show as 2^n terms in a row are all greater than 1/2^n so sum to 1. However it doesn't diverge quickly! To span a gap of 1,2,3,4,5,6,... you need N=4, 31, 227, 1674, 12367, 91380, ...
Asymptotically this is roughly log(N)

You can allow multiple blocks per level if you like, this copies cantilever bridges and the solution is the same. Counterbalancing gives the optimum and it scales like N^{1/3}.



<br/>

## Risk Assessment

('Tower of blocks', 'A very tall tower may mean bricks have enough energy to bruise when the tower falls down.', 3, 2, 6, 'Demonstrator to monitor building, anticipate collapse, and get children to stand back.\r\nCall a first aider in the case of an injury.', 2, 2, 4)

<br/>

('Board/ Blocks on floor', 'There is a trip hazard from the board or blocks placed on the floor.', 4, 2, 8, "Don't put the experiment in an area which is likely to be used as a thoroughfare.\r\nCall first aider in the event of injury.", 2, 2, 4)

<br/>

('Gaps between boards', 'Children may pinch their fingers in between the boards on the floor.', 2, 2, 4, 'Demonstrator to ask children to not place their fingers where they can be pinched between the boards. Tape gaps between boards and boards and floor.\r\nCall first aider in the event of an accident.', 1, 2, 2)

<br/>

('Blocks', 'Possible splinters from the wooden blocks.', 2, 3, 6, 'Demonstrator to make sure only wooden blocks with no splinters coming out are used. Report any blocks that aren’t smooth/sand them smooth.\r\nCall first aider in event of injury.', 1, 3, 3)

<br/>

## Risk Assessment Check History 

**Check 1**: 2019-01-09 - Thomas Webster (tw432@alumni.cam.ac.uk)), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk))

**Check 1**: 2019-12-29 - Käthe-Marie White (kmw54@cam.ac.uk)), **Check 2**: 2020-01-24 - Polly Hooton (prh43@cam.ac.uk))

**Check 1**: 2021-01-21 - Polly Hooton (prh43@cam.ac.uk)), **Check 2**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk))

**Check 1**: 2022-02-01 - Polly Hooton (prh43@cam.ac.uk)), **Check 2**: 2022-02-06 - Lauren Mason (llm34@cam.ac.uk))