# Mechanical Calculation

**Adding numbers using mechanical calculators.** - Electronic calculators are everywhere but how can we get these machines to understand simple tasks like addition? Explore some of the first decimal calculators and then explore modern binary arithmetic. 

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
- The binary adder (needing repairs/replacement)
- A bag of marbles
- Decimal Gear Calculator (To Be Made)
- The Mystery Calculator Game
- Simple Pocket Calculator (need to find)
- Dominoes
- Slide rules
- Addiator
- Percentage calculator

<br/>

## Experiment Explanation 

NB - This needs someone to print all the plans off thingiverse before it can be used. The old binary adder is deceased and some other things need buying too.

Lets start by thinking how we did calculations before calculators? We can think about operations we may want to do, for instance addition, subtraction, multiplication and division. We may want to do more complicated operations like exponentiation or even work out values for logarithms or trigonometric functions. This is all very easy on a normal calculator but hard in your head! People have needed to work these out for a long time before calculators became widespread. How can we work them out? Think of these operations are easiest and which hardest? Addition is probably the easiest so we'll aim to reduce lots of what we do to being addition. 

You can also consider how these devices help, do they make calculations easier, improve memory or what? 

How do operations relate? Well subtraction is addition of a negative number and multiplication is repeated addition, then on to exponential being repeated multiplication. We have the concept of an inverse now, addition and subtraction are inverses, as are multiplication and division and logarithms and exponentiation. This gives us some good ways to make calculations easier!

The first 'calculator' we'll look at is one of the oldest! The abacus, we have a 'soroban' abacus which is still popular in Japan and other Asian countries, even with modern calculators. This abacus only has 5 beads, unlike some more common ones in the UK with 10, we use the bead above the line to count as 5. We count the beads touching the 'reckoning' bar in the middle. In Japanese primary schools many still teach use of the soroban, with teachers singing sequences of calculations and students performing them. They then move on to anzan, which uses an imaginary soroban. It's no longer compulsory to be taught in schools but a grade three in the Japan Abacus Committee exams is required to work in public service. Addition is fairly straight forward however you can do more operations. 
For subtraction we said that it's the inverse of addition, so we look at a method of subtraction which only uses addition! To do this we need to take a complement of the number we want to subtract. We do this by looking at each digit, and working from the left the first non-zero digit we turn to (10 - it) and the rest become (9- it). For instance (456 -> 544), (290->710), (9->1). You should notice a number and it's complement add to a power of ten, this is very important. Say we want to do (563 - 198) we turn 198 into it's compliment, 802. We then do 563+802=1365. We then take away 1000 for 365. Can you see how this works? The operations are associative, so by doing (563+802)-1000=563+(802-100)=563-198. Often if we do 321-45 we pad out the compliment to 955 so we can drop the leading 1, however we could subtract a 100. There are procedures for multiplication, division, square roots and more.

The next method we have is Napier's bones, created in 1617 (by Napier). This is a sequence of vertical strips, each has a number at the top. It's designed to turn a multiplication to multiple additions and works like long multiplication. We need to split one number into individual digits, for a simple example we'll consider 6 x 841. We take the 8, 4 and 1 strips and line them up, we then look across the sixth row. We want to add along the diagonal, carrying ones. This gives the result, 5046. To do multiple digits you need to put on zeros and add.

While we're with Napier we'll look at another method of calculation using maths he came up with, the slide rule! This gives us a way to turn multiplication into addition and a handy way of doing it. To use to work out 4x3 line up the slide with 4 then read off the number that 3 on the slider is at, which should be 12. For division, say 6/3, line 3 on the slide with 6 on the fixed and read where 1 on the slide is, which should be 2.
This works with logarithms which we mentioned before as the inverse of exponential. You'll notice the scale is not like a normal number line, it's dashes are drawn according to log(x). Explain logs.

We have some log tables as well, these have also fallen out of fashion, however you can look up numbers and use them to turn multiplication to addition. There are also tables for lots of other common functions. You may wonder how these were made without computers, they were done by hand by lots of people. This creates lots of problems, many of the books have several errors which went unnoticed for many years, being copied into other books.

There's also an Adinator in here which is another calculation tool which works by COPY AND PASTE DETAILS.

These methods are all great and worked well right up until the 1970s when we saw an emergence of computers and calculators which put the slide rule out of business. These need a totally new way to work and leads us to rethink the entire way we calculate things. If we're going to do multiple back to back calculations we need to remember our intermediate results, with the exception of the abacus, this has to be done in our head. Our electronic machines need some way to remember the state.

Some of the first attempts used gears, see the decimal gear calculator. To add number a to b we need to set the machine with a displayed at the bottom, we then turn the units, tens and hundreds gears separately each a number of clicks corresponding to the number in the units,tens and hundreds place of b. You can see the additional gears at the back are turned and offset slightly back, when we 'overflow' in one column they knock the next one. If we were going to do a very large calculation and weren't sure if it would be too large for the calculator when the final gear overflows we could use the same idea to indicate that, original mechanical computers would often ring a bell. We're remembering state by the position of the gears. So, are their gears in your mobile phone? Obviously not! We have a better way to store things using electricity. For the gears there are 10 positions, but we can easily keep 2 positions using on and off. Now for the rethink which is a copy paste of the original binary adder experiment.

Binary Adder
Get people to figure out what it does by repeatedly adding one, see if they can spot how to read a number off or add a number other than one. Talk about how this is how computers represent numbers. Why do they use something different? Easy to store in this format instead of 10 possible digits we only have one, we can then store this as +ve or -ve, on/off or something like that.
There's also options to talk about logic, very easy switches for operations AND and XOR (exclusive or). How do we add numbers using these? AND to see if we need to carry one, XOR tells us if what we need in that bit.
You can also demonstrate overflow by adding big numbers together.
You could talk about how computers store negative numbers, sign and magnitude is probably most obvious way of doing it. There's also 2's complement. Or you could talk about fractions and storing the number of halves, quarters... or as numerator denominator.
If you wanted you can even get people to play about with finger binary. We can count up to 31 on one hand by using binary and whether a finger is bent or not. 

The "Mystery Calculator" game is formed of a couple of cardboard sheets with numbers on. The idea is to get a child to pick a number from 0 to 63, you then lay out the cards and ask them to pick out those with there number on, just by adding up the top left corners you can guess there number. How is it working, well look at the numbers on the cards, the first card only has odd numbers on it, the final card has everything from 32 to 63. Maybe we should think about binary? What happens if we write these numbers out, we'll find being on card n means you have a 1 in the nth place of your binary expansion. 
This leads on to questions about how much information we have and how this relates to binary, with 6 cards and you picking out those with your number on answers 6 yes or no questions about your number. So we'd expect to be able to determine the number from 2^6 possibilities but no more. These questions are really nice because we always need these 6 questions to determine the number, every possible way of answering the questions matches a number and it doesn't matter about order or anything like that.
Obviously we could ask different questions, one way might be asking "Does 2 divide your number?", "Does 3 divide your number?", all the way up to "Does 61 divide your number?". But that's 18 questions! Also say we ask "Does 47 divide your number?" and the answer is "Yes" we know the number is 47, we only needed that question. Do these questions actually identify the number uniquely? What about 6, 12, 18, etc. We need more questions about if 4, 9, etc. divide the numbers. So what's the problem with this choice of questions that means they need a lot more to get the same information. Well there's lots of overlapping information.
If I have "Does 43 divide your number? Yes" then I know the answer to every other question as I know your number is 43.
If I have "Does 43 divide your number? No" all I know is your number isn't 43, so I've gained very little.
If you picked numbers at random I only had a 1/64 chance of getting a yes and most of the time I get little information.
The original questions have no overlap and this set has several ways options of what to ask. The originals also exclude exactly half the options at each question whereas these are less even.
We can also find a lot more structure in the originals. "Is your number 32 or larger?" If Yes take away 32 from your number for the next question. "Is your number 16 or larger?" If yes takeaway 16 etc. This is one way of expressing these questions.

Dominoes
If you wanted to talk about logic gates you can build some out of dominoes, this is a little painful however there are printed out templates which you can carefully place dominoes on. See if you can figure out how they work. You'll need to knock both inputs simultaneously as timing is important. Think about how you can add binary numbers with these, for instance adding binary digits x and y. We find the units column is the XOR of these and the carry is the AND. What about two digit strings? 

<br/>

## Risk Assessment

### **Hazard**: Model

**Description**: Possibility of sharp edges or splinters on the model, if damaged.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Check for damage before demonstrating, and avoid knocking or dropping during use.
Call first aider in event of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Marbles

**Description**: Marbles could present a slip hazard if dropped.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

**Mitigation**: Keep unused marbles in a container, and keep track of how many there are.
Call first aider in event of injury.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3

<br/>

### **Hazard**: Marbles

**Description**: Children may eat marbles and could choke.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: Watch children with the marbles, only give them one at a time to immediately put in the machine. Call first aider in event of injury.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Gears

**Description**: Gears may trap fingers.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Make sure only one person using calculator and turning gears properly.
Call first aider in event of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2015-02-12 - Tom Comerford (tafc2@cam.ac.uk), **Check 2**: 2015-02-12 - Zephyr Penoyre (jp576@cam.ac.uk)

**Check 1**: 2016-12-09 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2017-02-06 - Mithuna Yoganathan (my332@cam.ac.uk)

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2019-02-04 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2020-01-31 - Beatrix Huissoon (beh37@cam.ac.uk), **Check 2**: 2020-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk)

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk)