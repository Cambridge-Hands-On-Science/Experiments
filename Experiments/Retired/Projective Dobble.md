# Projective Dobble

**The maths of Dobble** - Introduction to axiomatic maths and projective geometry via the card game Dobble. Learn how to make your own Dobble decks by constructing the "axioms of Dobble" from the rules, then developing methods to build these.

Last initially checked on nan by nan) and double-checked on nan by nan)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Games**

**Pure Maths**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Requires the printouts as follows:
- 4 x symbol cards (14 symbols)
- Railway Track picture
- Fano Plane Picture
- 3x3 Grid Extension Picture
- Fano Plane Dobble Deck (7 cards)
- 3x3 Dobble Deck (13 cards)
- (optional) Dobble Deck (55/57 cards)

<br/>

## Experiment Explanation 

Dobble (or Spot it!) is a card game that's similar to snap. A Dobble deck contains a set of cards, each card has several symbols (normal Dobble is 8 per card, kids 6) on it and the unique property that any two cards share exactly one symbol. To play reveal one card, players look at it, then reveal a second, the first to shout the symbol matching wins. The winner claims the first card, the second card stays face up and the game continues with a new card revealed. Try playing a few games using the deck with 4 symbols.

We now want to link everything back to maths. Dobble has some interesting properties and we want to study decks of Dobble cards. To do so we need to say the rules we want Dobble decks to have, these are called axioms. In maths axioms are our basic assumptions about any objects, so our axioms of Dobble better be true of any deck of Dobble cards. Our first axiom is simple:

1) For any two cards there exists exactly one symbol appearing on both cards.
2) Each card has the same number of symbols.
3) No symbol is repeated on a single card.

We'll discover our next axioms by trying to make Dobble Decks with an increasing number of symbols. Dobble with only one symbol is boring. We just have lots of copies of the same card! We don't like this so we stop it.

4) Each card is different.

This does allow us to have a deck with only a single card (if you like this or not depends, we'll introduce another axiom later to stop it). When we get to two symbols we need to make sure we're actually using them.

5) Each symbol appears on at least one card.

With these rules so far our Dobble decks only have a single card, but when we get to three we get our first (slightly) interesting Dobble deck. This looks a bit like Dominoes. So with 3 symbols and 2 per card we get our first Dobble Deck!

Now with 4 symbols and 2 per card we can't quite have dominoes like before but we can do something (laminated example). With one symbol in common between all three cards. This makes a very boring game of Dobble, so we add another rule. 

6) For any symbol, there's a card without that symbol. (If you want to allow 1 card decks you'll need to rephrase this)

What about 4 symbols and 3 per card? Have a try and whatever happens it seems like axioms (1) keeps failing, we can't get exactly one symbol. But we'll actually need to prove it! If we have three symbols and two cards then there are six symbols we need to pick however there are only 4 symbols available. Since we need to stick to (3) we end up with two symbols in common. This argument is called the pigeon hole principle. Formally we'd argue there's a symbol on both cards, 4 remaining slots and 3 symbols that can be used (as by (3) the repeated one can't appear again) thus by pidgeonhole there's a repeat.

Now we move up to 5 symbols and 3 per card. We can get two cards but then get stuck trying to make a card without the common symbol. So if we move to 6 symbols we get a 3 card deck! But we can actually do better. We can add a fourth card by taking the unmatched symbol from each and making a new card.

So far we've found nice Dobble decks at 3 and 6, is there anything special about these? It turns out the triangular numbers have an important link and we can make Dobble decks with a triangular number s of symbols per card we can make (s+1) cards using T(s) symbols using the same pattern. 

***********************Projective Geometry****************************
Lots of times in Maths we want to take our axioms (which describe a thing we want to find out about) and then show some kind of object we understand satisfies those axioms. For Dobble one such setting is that of geometry. We'll now start interpretting our original Dobble axioms but in a geometric sense. Instead of saying "symbol" we're going to say "point" and instead of "card" we're going to say "line". A line has lots of points much like a card has lots of symbols. A deck is now a collection of lines. So now our axioms become.

1) For any two lines there exists exactly one point appearing on both lines. (i.e. Every pair of lines has a unique intersection)
2) Each line has the same number of points.
3) No point is repeated on a single line.
4) Each line in the collection is different.
5) Every point has at least one line passing through it.
6) For any point, there's a line not passing through that point.

This roughly lines up with what we expect of geometry with a few exceptions. To make sense of (2) we insist on their being only a limited number of points, for instance just imagine a grid of points where if you go off one end you wrap around and appear at the same point on the other side. Then the only problem is (1), we have parallel lines which can never meet! 

This requires us to take an alternative idea of geometry, mathematicians call this projective geometry. Look at the picture of the train tracks. It looks like the parallel tracks eventually meet on the horizon. In projective geometry they do. The general rule of projective geometry is our equivalent axiom (1) holds. Look at the Fano Plane diagram which has 7 points and 7 lines. Notice that because we this new axiom (1) we don't end up with straight lines when we try and draw it on our normal (non-projective) piece of paper. 

Our first challenge is to lay the symbols out so each line matches up with a card. Try this with the Fano Plane deck. You'll find you're able to make the cards into a triangle shape, then add a card in the middle. Our final line ends up being a circle. However we never said our lines had to be straight. Here each "card" corresponds to a "line" as in our axioms.

The next concept that makes projective planes interesting is duality. This means swapping "lines" and "points". We can actually do this. Try lying out the cards in the deck so each "card" is now a "point" and every "line" has some "symbol" in common. We call this duality. 

We can also make projective planes from usual planes by introducing some new "points at infinity" for each direction we could head towards infinity in. On a 3x3 square grid this is up, right up diagonal, right, right down diagonal. While we could go down to infinity as we wrap around that's the same as going up. 

Now lets show how we make a Dobble deck from a grid like this. We work through each of the parallel lines in those four directions. For each of the three parallel lines we choose a symbol and place that on all 3 cards, we also place this symbol on the "point at infinity" for this direction. This gives us 4 symbols on all our finite cards and 3 on all our "point at infinity" cards. However the easy way to solve this is to add a new infinite symbol to these four "points at infinity" cards. This represents the "line at infinity".

The actual game of Dobble is made in this fashion! It just uses a 7x7 grid and there are more points at infinity corresponding to making "knights moves" in different directions. You can lay out an actual game of Dobble like this and try it. Sadly with 8 symbols per card and 57 symbols you can get 57 different cards, however a commercial game of Dobble only has 55. 

When the cards are printed out I'll add some cool tricks about duality. You should be able to find the dual symbol to a card then choose a card, look at it's dual symbol, find all cards with that symbol on them, then look at the duals of all these cards and that should be the symbols on the original card (careful if it's dual to a symbol on it's self "self-dual"). This is an example of taking the dual of a dual and coming back. 

We can also show take theorems in projective geometry and find them in Dobble. For instance Pappus' Hexagon theorem says take two lines, pick three points on both lines, draw the lines between pairs these, the three points of intersection form a line. (See picture). If you do this in Dobble pick two sets of three cards that share a symbol. for each pair find the (unique) card sharing both symbols. The three cards you get from this all share a symbol.

<br/>

## Risk Assessment

Laminated things are tasty and sometimes pointy.

<br/>

## Risk Assessment Check History 

