# Sorting

**Pretend to be a computer** - How do computers work? This experiment gets you to think like a computer and try and put a selection of numbers into order.

Last initially checked on 2021-01-22 by Polly Hooton (prh43@cam.ac.uk)) and doublechecked on 2021-01-22 by Grace Exley (gae23@cam.ac.uk))

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
- Some laminated coloured/numbered cards
- Laminated instructions for sorting algorithms
- Uncooked spaggetti
- (Alternatively you can use giant playing cards to sort)
- --Extra Networks-----
- Temporary Spray Marker

<br/>

## Experiment Explanation 

Introduce the problem, why do we want to sort things? People's names in alphabetical order makes them easier to find.
Explain how computers work with fixed memory locations and we can ask people to swap positions.
Ideally in this experiment we'll use cards with colours on one side. This is because computers need to check which number is bigger as a comparison operation. I'd recommend choosing an ordering in some arbitrary way, alphabetical, word length or your personal ranking of favourite colours all work well. You can also get everyone to stand with their back to the computer and their number towards you like bellow.
 <-card person
you-> <-card person <-Computer
 <-card person
<- is direction the person is looking.
Pick one person to be the computer and give everyone else a number and get them to face away from the computer the computer can ask to to compare which of two people have a larger number and ask people to swap places.
Get one people to be the computer and ask them to sort the other participants (each given a number card) into order by asking people to swap places and for comparisons.
Get them to explain how they picked who to swap and who to compare.
Computers have rules which tell them how to decide when to compare and swap people. (you may want to use the words algorithm or program). Here are some common sorting algorithms.
BUBBLE SORT
1) Start at the beginning of the list and compare each adjacent pair. If they're in the wrong order ask them to swap
2) Start again from the beginning doing the same and repeat once for each number to be sorted
We can ask people what this does? It moves the largest element to the end of the list (they bubble to the top). This means we don't actually have to check the last elements as they're already the biggest. This saves a bit of effort. For advanced groups this take a quadratic amount of operations and this saving is linear, i.e. doesn't make much difference in the long run.
SELECTION SORT
1) Look at the unsorted section. Compare people along the line with the person who is smallest so far
2) Swap this person to the first of the unsorted positions. Repeat.
This is quite like Bubble sort in that we select smaller elements and move them to the front. However what we do is a lot less swaps, we do a lot of comparisons and remember how many people we've sorted and who's the smallest so far. Imagine sorting fragile things or large things fewer swaps is better. Still quadratic in comparisons but linear in swaps.
INSERTION SORT (allow people to insert a person between two others)
1) Take the first unsorted element. Compare against everything before until you find something it's bigger than and insert it there.
2) Repeat until everything sorted.
This seems very much like Selection sort, really it is however instead of searching through unsorted things to find the biggest we're finding the correct place for the next element to go. You can see if they can figure out how this new insert operations works in terms of swaps. It turns out to be start at the one on the left and swap pairs upto the right then do the same back. This is again a lot of swaps.

It's probably worth comparing when these are better, it really depends on if it's easy to insert things (imagine cards, these are easy to insert and there's no need for a complex sequence of swaps). Insertion works well if everything is "nearly" in the right order before you start. Imagine how quickly you can add one new thing to a sorted list.

More complicated sorting algorithms exist here are some nice ones that are similar
1) Cocktail sort - like bubble sort but once we reach the end we go back down the list in the opposite direction
2) Comb sort - we get finer and finer in our sorting, with n items we compare the end points, then items (1,n-1) and (2,n), then compare those n-3 apart etc.
Why do these exist? Get people to come up with orders that make lots of people swap in bubble sort (sorted in the opposite order). These get dealt with faster by these. These are called hares (move quickly to the right) and tortoises (move slowly to the left).

We also have recursive sorts you can talk about
QUICK SORT
1) pick an element
2) compare everything to this element and insert to left or right based on this.
3) repeat on the two new smaller sections
Why is this good? well imagine multiple computers they can each now sort the new halves. We also can with good choice of pivot reduce down to half in each side. This is actually less than a quadratic amount of work (with a good choice of pivot)

Also more specialised
COUNT SORT
1) keep a tally of how many times each thing appears then output that many of the things at the end
great for very few numbers
LSD RADIX SORT
1)sort everything based on the least sig digit, then second least, etc
#throwback to punch cards
BONGO SORT
Randomly shuffle check if in order if so stop.
Hopefully they should see this is not the best method but it's an interesting problem of how long you'd expect it to take (n! possible orderings and 1 correct one (assuming no equlaity))
SPAGHETTI SORT
for the list cut pieces of spaghetti to each length and then hold them all in a fist an press against a table. Then press the other palm down till it touches one piece of spaghetti this is the largest. remove and repeat. This is linear in time, it's so good because our hand is essentially doing parallel comparisons.

If you wanted to bring in some more computer science think about how lists are stored on a computer? How will this effect how well each sorting algorithm performs? Well the 'data structure' will affect the speed of operations like swap and compare, if we have a specific data structure in which swapping is very efficient we may be willing to accept lots more swaps in exchange for less time consuming comparisons. Some data structures include.
Arrays - This is a continuous block of memory and most like what we've used in the above, we need some external memory to do the swaps and need to use these pairwise swaps.
Linked Lists - We can easily swap to a using people as a model of linked lists. Give one person a marker (a hat from welcome to jail) they are the 'head' of the list. Every person must point at another person, this is called a 'pointer' to the next element (in this case very literal). To go through the list start from the head and then move to the person they're pointing to and so on. In this list we don't have to do swaps in the same way, we just ask people to change where they're pointing. This is great for inserting things, we only have to alter one pointer, can you see how to do this? 

-----------Sorting Networks-----------
Lots of these computations were slow because we only did one thing at a time. It'd be much faster if we could multitask. Modern computers have multiple cores which is just like this. This is called parallelization.
What we'll do here is a slightly different parallel operation to spaghetti sort, we're still doing a simple comparison but can do several 2 way comparisons at the same time.
We can see how this would be good for quick sort where we split, after each split we can sort each part in parallel, but we can actually come up with other ways, for instance we'll draw a network. People will start on the start squares and follow the arrows, when they reach a circle they wait for someone else to arrive. When two people are at the circle they then compare numbers and the bigger takes the bottom/right arrow and the smaller the top/left arrow. When you reach a square your done and top to bottom you should find the numbers sorted.
You'll need to draw the networks in advance to try them out.
What happens if you swap left and right? You're sorted in the opposite order.
If you can come up with a way for people to draw their own that'd be great but don't give them the spay marker.


<br/>

## Risk Assessment

Following the numbers on a card around a circle.
<table border=1>
<tr><td>Hazard</td>
<td>Risk</td>
<td>Affected Person(s)</td>
<td>Likelihood</td><td>Severity</td>
<td>Overall</td>
<td>Mitigation</td>
<td>Likelihood</td>
<td>Severity</td>
<td>Overall</td>
</td></tr>
<tr><td> Raw spaghetti </td><td>
Children eating raw spaghetti that has been touched by many other children. They may also choke on small bits of spaghetti.
</td><td>
Public
</td><td>
2
</td><td>
5
</td><td>
10
</td><td>
Prevent loose spaghetti being left accessible, especially with young children around.
Call a first aider if child swallows; if choking encourage child to cough.
</td><td>
1
</td><td>
5
</td><td>
5
</td></tr>
<tr><td>Dropped spaghetti</td><td>
Spaghetti slip hazard.
</td><td>
All
</td><td>
2
</td><td>
3
</td><td>
6
</td><td>
Pick up dropped spaghetti.
Call first aider in case of injury.
</td><td>
1
</td><td>
3
</td><td>
3
</td></tr>
<tr><td>Solvent</td><td>
Spray marker is a solvent and may be abused.
</td><td>
Public
</td><td>
3
</td><td>
3
</td><td>
9
</td><td>
Use in a well-ventilated area and don't allow children to use.
Call first aider in case of injury.
</td><td>
1
</td><td>
3
</td><td>
3
</td></tr>

<br/>

## Risk Assessment Check History 

**Check 1**: 2017-02-09 - Thomas Webster (tw432@alumni.cam.ac.uk)), **Check 2**: 2017-02-10 - Andrew Sellek (ads79@cam.ac.uk))

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk)), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk))

**Check 1**: 2019-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk)), **Check 2**: 2019-02-04 - Thomas Webster (tw432@alumni.cam.ac.uk))

**Check 1**: 2020-01-31 - Beatrix Huissoon (beh37@cam.ac.uk)), **Check 2**: 2020-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk))

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk))