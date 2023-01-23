# Traffic Control

**Finding interesting maths in everyday traffic** - Does building bypasses make journeys faster? How can we optimise traffic flows? What causes traffic jams? Why do I stop for no reason? What's a stationary wave?

Last initially checked on 2021-01-22 by Polly Hooton (prh43@cam.ac.uk) and double-checked on 2021-01-22 by Grace Exley (gae23@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**AI**

**Operational Research**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **Electricity needed**
- Currently this experiment has:
- 6 RC cars
- Traffic Cones
- Unasembled Electrical Components to make lights and sensors
- 
- There is also some scalextrik track and cars however it was expensive to extend the experiment in this way as you need multiple cars on a track.

<br/>

## Experiment Explanation 

So it may not seem like it but traffic is a really interesting area of mathematics, we call these things operational research or OR. OR looks at lots of everyday things like queues (for instance is it more efficient to have one queue served by multiple people or one queue for each server?).

Braess's Paradox

One model of traffic is using graph theory, this makes [major] junctions into dots (or vertices) and on each edge we put a function which says how long it takes to travel that piece of road with a set number of cars on it. We'll assume this function is non-decreasing (additional cars never make a road faster). Cars travelling from S to T via a network of roads like in the following ascii

 t
g/ \ f 
x y 
f\ /g
 s

Where f(n)=n/100 and g(n)=45 where n is the number of cars on the road. So the solution is for half of cars to go via x and the other half via y. This means the average travel time is (45+N/200) where N is the total number of cars. If you want concrete 4000 cars then 2000 go via x and 2000 via y for a time of 65 minutes. 

Let's try and build an additional road, more roads should make things faster, right? So let's build a road from x to y. As we're trying to make this bypass super useful let's say it takes 0 minutes, (you can instantly jump from x to y) [if this is too far out then say 5 minutes and it probably works, else just add 5 to f and g]. So what happens to our traffic? Well when it opens a few drivers going through x will take this new road, they'll find it only takes just over 40 minutes, saving them 25. The journey (s-x-t) also got a few seconds faster and (s-y-t) slightly slower. As this news gets out then more people are going to try the new route, people going via y will swap to going via x and then onto the new route. When 2500 people are on (s-x-y-t) and the rest on (s-y-t) it takes those (s-x-y-t) people exactly 65 minutes (the same as before) and the people stuck on (s-y-t) a full 85 minutes! Were someone to try (s-x-t) they'd find that taking 80 mins. This means more of the (s-y-t) people swap. Eventually everyone uses this new road taking (s-x-y-t) for a travel time of 80 minutes, the other routes (s-x-t) and (s-y-t) take 85 minutes now. Adding a new road has delayed everyone by 15 minutes. If everyone agreed not to use the road it would be much faster for everyone, however we couldn't trust people to do that! This is Braess's paradox. It's a common phenomenon; we can often fix this using a toll on the road from (x-y) which limits the traffic on it. It will still cause the surrounding routes to slow down a little bit however by choosing the toll you can balance this out.

The paradox is a bit constructed as some roads have a fixed travel time and other scale linearly, neither is really accurate.

I'm not sure if by using some traffic lights and a microcontroller this could be done in Scalextric?

Phantom Queues and Jamitons
We have a flow of cars along the road, what other things do we have flows of? Water/fluids. So we take these results and use them on cars. This gives us a nice model where everyone travels uniformly, until we hit a certain traffic density, then weird effects start to occur. Ever wondered why the motorway sometimes comes to a complete standstill, even though there's nothing causing a blockage? This is just one of many things explained. The new domain is unstable, any small effects amplify. Like solitons in stationary waves we call these jamitons.

So a simple model of this takes a circular track, place all the cars in a single track evenly spaced around the track, give everyone and you a car and get them to drive around at a constant speed. Let everyone get into this pattern. The aim is the track is slightly too small so you're in the unstable region due to the traffic density. Then you introduce a jamiton, this may take some practice but a slight application of the breaks should either cause a crash or a jamiton! Hopefully the breaks then propagate round the loop and cause someone to end up coming to a complete stop. This is called a phantom traffic jam, one of the ideas behind smart motorways is to prevent the high density build up required to cause these.
The other thing done in real life is 'ramp metering', traffic lights on slip roads which slow the flow of people joining when a high density patch goes through. Encouraging people to not change lane also helps as this further amplifies the problems.

Traffic Control
The idea for this is to explain a couple of techniques for controlling traffic lights. So we have a large track set up with several light junctions, we've seen what can happen with small breaking so stopping for traffic lights can cause major delays, this should give us an idea of why it's important to make them optimal. While driving around let people know they need to stop for red lights! There's also the factor that by driving at constant speed it's more efficient saving the environment and money.
So we have a few different types of lights here. One type is a fairly classic dumb light which works on a timer. One is an ANPR (Automatic Number Plate Recognition) light which detects the number painted on the car so can keep track of where they are and change the lights. There's also inductive loops under the track which detect a current when the metal cars drive over them and finally there's microwave sensors which bounce microwaves of the cars and use the Doppler effect to get their speed. 

In future vehicles may have sensors like GPS for position and velocity not only on board but also being broadcast over wifi to nearby vehicles and to central road infrastructure. 

There are lots of ideas for how to improve roads. One is introducing a road pricing scheme via ANPR where people are charged an amount of road tax based on the roads they use and the times they travel. Simple versions are already in place in London (Congestion charge) and Stockholm. 


<br/>

## Risk Assessment

### **Hazard**: Cars

**Description**: Cars fly off tracks, causing trip hazard, or possibly hitting people.

**Affected People**: All

**Before Mitigation**: Likelihood: 4, Severity: 2, Overall: 8

**Mitigation**: Don't allow children to get in amongst track, keep face etc away. Don't chase after flying cars, consider flight path in set up of experiment in relation to walkways.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Track electricity

**Description**: Children touching electrified track may get a shock. Car motors may burn out. Track may short in rain or a spillage.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

**Mitigation**: Only use experiment inside and keep liquids away from experiment. Make sure power supply is in good condition and track sections are healthy. Encourage children not to touch track and demonstrator to place cars on track. Keep track power to reasonable volt and amp ranges. If using an external supply for power consult the Scalextric manual for instructions on how to do so safely.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Small parts

**Description**: Children may swallow small parts (e.g. any traffic lights, parts of cars that come off etc.) and choke.

**Affected People**: Public

**Before Mitigation**: Likelihood: 3, Severity: 5, Overall: 15

**Mitigation**: Don't allow children to play with small parts; remove from setup if children can't behave. Check all components are in good working order and not broken before demonstrating. In the event of swallowing, call a first aider.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

## Risk Assessment Check History 

**Check 1**: 2019-02-04 - Grace Exley (gae23@cam.ac.uk), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2019-12-26 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2020-01-27 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk), **Check 2**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)