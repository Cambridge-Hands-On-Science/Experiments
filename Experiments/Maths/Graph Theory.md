# Graph Theory

**Find out about the mathematics of Graphs.** - Experiment with graphs finding out about what structure we can find in randomness, how to colour maps with few crayons and what shapes you can draw without taking your pen of the paper.

Last initially checked on 2022-02-09 by Joshan Parmar (jp862@cam.ac.uk)) and doublechecked on 2022-02-09 by Conor Cafolla (ctc43@cam.ac.uk))

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Maths**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Lots of plain paper,
- Coloured pens,
- Or
- Whiteboards and Coloured Markers
- ------------
- Optional CHaOS Graph Theory Booklet with sketches of some of the things you may like to do.
- The following booklets formed the inspiration and may be useful.
- Http://jdh.hamkins.org/math-for-seven-year-olds-graph-coloring-chromatic-numbers-eulerian-paths/
- Http://jdh.hamkins.org/math-for-eight-year-olds/
- -----------
- Utility Problem Mug (Please Draw on it with erasable pens)
- K7 Mug (Please don't draw on it)

<br/>

## Experiment Explanation 

We might want to understand various properties about different mathematical structures. A graph is a very simple structure, it has points (or vertices) connected by lines (or edges). We can think of edges as meaning close by or related to.
Can we think of some graphs in daily life? Maybe a family tree where vertices are people and edges are between parents and their children. We could also have cities and trains between them. 
There are lots of directions you can then take for this experiment, it really depends on the demonstrator but here are all good ideas. Some of these can then be combined into CHaOS+ activities.
--------Vertex Colouring -----
One thing we might want to do is colour in our vertices so ones connected by edges are different colours. Ask people to draw some graphs and colour them in. Most people seem to avoid drawing crossing edges so you should be able to keep colours low.
Ask people with three colours what they have that's stopping them using only 2 colours. You can normally find a triangle or pentagon (or larger odd cycle) which is preventing them.
How can we increase the number of colours we use? Add a new vertex and an edge to all existing colours or more edges between things of the same colour. Can we keep doing this indefinitely? Yes as long as we don't mind edges crossing when we draw them. If we mind about that people will struggle when you try and draw a K5. Most people seem to believe this is hard. We call a graph with no crossing edges planar.
You could divert to talk about the utilities problem. Given 3 houses and 3 utilities (gas, water, electricity) can you connect each of the houses to the utilities without any of the 9 edges crossing? Again you can be convinced this isn't possible. If were allowed to glue edges of the paper together though we can actually do it on a torus. You can use the mug to demonstrate this fact, notice you need to draw some lines over the handle. Note topologically mugs are torus shaped.
What about if we start talking about maps. What is a map? It's just a collection of regions (or countries or faces) and we'll colour it so neighbouring things need different colours. If they share only a point as a boundary they can be the same colour. 
You'll find people use 2-4 colours, if they use more they've gone wrong. (This is the 4 colour theorem). Can they see a correspondence between the graphs and maps? If we stick a vertex in the middle of each region and connect with edges those sharing a boundary. We can make this so the edge goes through the boundary and doesn't cross.
We can also colour the entire outside one colour too. See if they can do this and find what this does to the graph. You might also like to turn planar graphs into maps by doing the reverse to this.
If you've convinced them about the colouring you can show them the K7 mug. This has a K7 drawn and it's map coloured on the surface of a mug. Maybe it isn't the same as a plane?
------------------------Eulerian Cycles -------------------
What shapes can we draw without taking our pen off the paper or going over a line twice?
Have a go at drawing things and seeing what's possible. The famous counter example is the bridges of kronenburg. There may be objections this graph has multiedges, we could just put more vertices in though to make them distinct. 
Let's try counting how many times we pass through vertices. In the middle we need to enter and then leave the vertex, each time we do this we use two edges so we need things in the middle to have an even degree (number of edges coming out). This gives us a good idea of where to start when we have 2 vertices of odd degree as we'll need to start and finish at these two points. If we have more than 2 we know we've got an odd one in the middle so it's impossible. What if there are no odd vertices? Well we'll need to start and finish in the same place, count the edges out of the start and we need to make it even.
You may get some questions about what happens if there is only one vertex of odd degree. See the handshake lemma for this case.
++++++ How do we know these cases with 0 and 2 odd vertices are possible? We didn't really prove it just showed others weren't and constrained how we find them. We can do this by induction. Take a graph with this property with the smallest number of edges, remove an edge and we know we can do this (else what we get has less edges) and then use this final edge. We can check what we get is only 0 or 2 odd vertices and everything matches up.
-------------Handshake Lemma --------------------
How many vertices off odd degree can we have? Draw and try. Let's start adding edges and try and add up the total degrees. We find as we add an edge the total increases by 2 each time so we have some vertices of even degree which sum up to an even number and some odd vertices, we'll need these to sum to an even number so we need an even number of them, hence we can't have an odd number of vertices of odd degree.
-------------Edge Colouring---------------------------
We can also colour the edges we have, one way might be that all edges meeting at a vertex have to be different colours. We need to look at something called the max degree, this is going to be the largest of the degrees any vertex has. We know all edges out of this vertex will need different colours, so this is a lower bound on the number of colours we need. Try colouring some things and see how many more you can get too. An odd cycle is a good example that you might need more. Vizing's Theorem says that one more colour is the worst possible, so we divide up everything into two classes. 
++One could prove this again by induction removing an edge and considering an alternating path of different colours.
------------Ramsey Theory---------------------------
Lets try a different way of colouring the edges. We'll only use two colours (wlog red and blue) and can colour edges however we'd like. We're going to look at what we can find in the edges of the same colour. We'll look at graphs where all vertices are joined by an edge. Take 6 vertices and colour all 15 edges. Can we do this to avoid making a triangle? What about if we only have 5 vertices? This shows that the Ramsey number called R(3,3)=6. R(4,4)=18 so it's probably a bit far, but you could talk about antisymmetric ones like R(3,4)=9 which avoids a red K3 and blue K4. By doing this we've found some order in the graph, even if we'd coloured it randomly we've found a smaller nice substructure which is very important in physics.
It's actually really hard to find these numbers. In fact all we know about the next ones is 43<=R(5,5)<=48, 102<=R(6,6)<=165, 205<=R(7,7)<=540. Why is it so hard? How many ways can we colour these? We have n vertices so n choose 2 edges, this is like n squared. We can colour these each either red or blue so that's (2^(n^2)) possible colourings. This number is very big, for around n=16 there are more configurations than atoms in the universe and n=20 we surpass possible games of chess. This means we can't use a computer easily at this point and need to do it mathematically.
-----------Euler Characteristic---------------------
We want to try and find something special about connected planar graphs. One thing we could do is look at some parts. Lets count the number of edges, E, and vertices, V. We'll also want to count something else, we'll call these the regions or faces of the graph, R. (These are slightly different to the countries we had when map colouring as we're using the edges as borders.) We also need to count the outside as a face. Let's calculate a few examples of V-E+R. One should always find that this gives us the answer of two. We call this the Euler characteristic of the graph. Can we see why it's always 2? Start with 2 vertices connected by a line, this has characteristic two. If we add a new vertex we'll need to also add an edge to make the graph connected and this won't make a new region so we remain unchanged. If we add a missing edge between two existing vertices then E and R increase by 1 and so we don't change the characteristic.
If you talked about the utility problem you can try and calculate it's Euler characteristic, the regions are more tricky to see however it only has three (easy to see on a torus). This gives it an Euler Characteristic of 0.
Using the utilities and K7 mug you can work out the Euler characteristic of a mug which is also 0, and is why K7 and K3,3 are draw able on a mug but not a plane. On the mug you may get more questions about what a face is? The technical definition of a face on a surface is if we remove the edges and vertices a face is a connected component. 
++++++++++++5-colour Theorem++++++++++++++++
If you are feeling brave it's possible to prove this with very advanced groups. You'll need to have covered Euler Characteristics and Map Colouring.
Firstly look at the Euler Characteristic and think about relating faces and edges.
We'd like to say there a not many edges relative to vertices. We can add lots more edges where possible to keep the graph planar. Let's say we have a non triangular face we can draw a line across it and get closer to triangles. If we have an edge that's only in one face then we can add another edge to make two faces. You may need to demonstrate this to convince people it's possible.
Then each edge is part of two different faces. Each face has 3 edges making it up. So 3R=2E.
Then we have V-E+R=2 so V-E+(2E/3)=V-(E/3)=2
So E=3V-6.
But we added edges to get this new E so we know originally we had E<=3V-6.
What does this say about the minimum degree? Well if we add up all degrees that's bigger than V times the smallest. Also this sum is 2E<=6V-12. So the smallest must be less than 6.
This means we can easily prove the 6-colour theorem, colour a graph minus something of degree <=5 and there's a colour remaining when we stitch it back together.
Lets say we take the graph with the fewest number of vertices we can't 5 colour. And find a vertex of degree <= 5. If we remove it we can colour the rest (by induction) so we only need to colour that one. If it was degree <=4 or had 5 neighbours with a colour in common it's easy as we can use that free colour. Otherwise we have one neighbour of each colour. Consider in the drawing two colours not next to each other.

<br/>

## Risk Assessment

### **Hazard**: Scissors

**Description**: Risk the children will grab scissors and injure themselves.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

**Mitigation**: Make sure you cut out any required paper before the kids arrive. If you need to have scissors on the table, have the safety scissors.
If there are any cuts, call a first aider.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Coloured pens

**Description**: Risk that children will take and possibly eat coloured pens.

**Affected People**: Public

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Watch small children with pens.
Alert parents immediately if children aren’t being sensible and call a first aider if necessary.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3

<br/>

### **Hazard**: Utilities Problem Mug

**Description**: Porcelain mug could smash into sharp pieces and cause cuts.

**Affected People**: All

**Before Mitigation**: Likelihood: 4, Severity: 3, Overall: 12

**Mitigation**: If the mug smashes, move children out of the area and sweep/vacuum for pieces. Call a first aider in the event of an injury.

**After Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

<br/>

### **Hazard**: K7 mug

**Description**: Possible ingestion of the paint on the mug.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: It shouldn't be used as a mug ever. The mug shouldn't be used for drinking or licked. Keep out of children’s reach. If children do ingest paint, inform parents to take them to GP if illness develops. Call a first aider if necessary.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk)), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk))

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk)), **Check 2**: 2019-01-18 - Josh Garfinkel (jlg70@cam.ac.uk))

**Check 1**: 2020-02-05 - Andrew Sellek (ads79@cam.ac.uk)), **Check 2**: 2020-02-05 - Beatrix Huissoon (beh37@cam.ac.uk))

**Check 1**: 2021-01-22 - Conor Cafolla (ctc43@cam.ac.uk)), **Check 2**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk))

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk)), **Check 2**: 2022-02-09 - Conor Cafolla (ctc43@cam.ac.uk))