# Sieving

**Simple Algorithms to Reveal Hidden Sequences** - Simple algorithms to reveal hidden sequences. Explore what numbers are revealed by applying simple rules and encounter programming concepts like loops.

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
- 100 Counters (pieces from Othello, Reversi, etc. with two coloured sides are ideal but you can use counter/not counter for the states)
- A board labelled with natural numbers 1 to 100.
- 
- Currently this equipment is shared with "Game of Life" experiment.

<br/>

## Experiment Explanation 

As part of this experiment you have a large board, this represents the first few positive integers, one per square. You've also got some binary way to indicate state, two sides of a counter or presence/absence of a counter. We'll talk about 'green', 'good', 'present', 'alive' as a means of saying in a set and 'red', 'bad', 'absent', 'dead' to say not in the set, I'll try and stick to the former. We use flip to denote a change between these states. I'll use 'set' and 'sequence' interchangeably too, I prefer 'set' but feel 'sequence' is a better simple word. Obviously our sets go on ad infintum, we've stopped at one hundred because we've chosen too, you can go on as far as you like, it'll just take more time. There's only two examples but they're both really good, I'm not aware of anymore algorithms which are a slight variations on this theme, if you know any please let me know. The final algorithm has a similar flavour but is disntictly less simple, maybe use it as an interesting idea for the advanced.

-----Squares-----
So we're going to run a very simple algorithm, we start with everything red. This is like a guess we don't know what's in our set. We're going to try and build it up gradually.
We then flip all multiples of one, all multiples of two, etc. What is the result?
We find the numbers remaining are all the squares. Let's think about why. Let's try and count how many times we flip a counter. Well we flip once for every number dividing it, they started red so we need an odd number of flips to get to green. So we need an odd number of divisors. This only happens at the squares, we can pair off divisors of n=ab, but for squares and only them we have n=a^2 and can't pair a!
By division here we mean integer division, so no remainders.
You can very easily do this by repeated addition, there's no multiplication required.
You can talk about how this is 'well defined' we have an infinite number of possible divisors, but we can immediately rule out any divisors bigger than the number so we only need to check finitely many. When running through flipping counters you may want to note how you never flip any before the current number. This is a potential optimisation of the algorithm, when you start looking at large numbers you'll notice this saves you a lot of time. If you start trying to do it quickly you'll find it's easiest to count along by the current number, this means you don't even need to do any division.

---Primes----
Now we start with 1 red and everything else green. We know 1 isn't in the set this time. Then we scan ahead and find the next green number, we flip all it's multiples but leave it green. So what numbers remain green? It's those we never flip. That means they have no divisors, other than 1 and them selves. This means they're prime! 
There are again numerous improvements we can make, there's no point continuing past 10 as everything that's less than 100 has some prime factor <= 10. If not think of a number with all it's prime factors bigger than 10, well if it's only got one prime factor, it's prime, so it must have at least two. But the two factors are at least 11 and the smallest such a product can be is 11*11=121>100. 
Again there are a few tricks to speed up things, what might be the problems with using it to find large primes. We'd need a lot of space, even on a computer we need to find better ways. 
One method like this one we pick random numbers smaller and see if there are any factors in common. Once we've done this enough times we might be happy the number is 'probably prime'.

---Sundaram (Prime(ish))----- 
This is a more advanced algorithm, we loop over i and j. We flip the numbers (i+j+2ij), we keep increasing j and when we go off the board increase i and let j drop back to i. This generates a rather odd sequence starting 1,2,3,5,6,8,9,11,14,15,18,20,21,...
It's not immediately obvious how these are related. In fact it's a rather odd relation. Think about the primes bigger than 2. They're all of the form 2k+1 as they must be odd. What we get by doing this is the sequence of ks. If you double and add one you should recover the primes, but notice you'll get ones all the way up to 202 this time!
It works because we automatically exclude the evens so we want to know when 2k+1 prime. If k=i+j+2ij then 2k+1=2i+2j+4ij+1=(2i+1)(2j+1) so it's non prime. Otherwise 2k+1=pq and p and q must be odd as 2k+1 is. Hence let p=2i+1, q=2j+1 then k=1+j+2ij.


<br/>

## Risk Assessment

### **Hazard**: Counters

**Description**: People eat counters. (choking hazard)

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: Tell them not to eat counters. Make sure you know how many counters you're using and where all the counters are.
Call first aider in event of swallowing.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Counters

**Description**: Someone slips on a dropped counter.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Pick counters up if left on floor.
Call first aider in event of injury.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-01-19 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-02-07 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-02-08 - Jared Jeyaretnam (jaj55@alumni.cam.ac.uk)

**Check 1**: 2019-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2019-02-04 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2020-01-31 - Beatrix Huissoon (beh37@cam.ac.uk), **Check 2**: 2020-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk)

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk)