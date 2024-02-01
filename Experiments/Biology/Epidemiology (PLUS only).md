# Epidemiology (PLUS only)

**Show kids how disease dynamics, with a model of Citrus Canker spreading through a population of orange trees** - Exploring the concept of disease spread and biological modelling. 

Last initially checked on 2024-02-01 by Margaret Johncock (mllyj2@cam.ac.uk) and double-checked on 2023-02-14 by Asmita Niyogi (an637@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Biology**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **Electricity needed**
- 2 CHaOS laptops
- WiFi access - ask a committee member and or one of the teachers present
- Http://www.webidemics.com/ - NEW WEBSITE - https://plantepidemics.github.io/interactive/ - we are awaiting it to be built! This computer model was developed by Nik Cunniffe’s group http://www.plantsci.cam.ac.uk/research/nikcunniffe) in Plant Sciences. It models the spread of Citrus Canker under a variety of weather conditions, disease parameters and control efforts, allowing you to set initial conditions then watch the model run to a determined end point.
- *** Requires Adobe Flash which is no longer available, hence not working label added 12/01/21 by Miffles. I have found the website, and am hoping they will actually develop their new version - https://plantepidemics.github.io/interactive/ - there is a working game there, but the instructions below give all the theory without going through the game - it is really good though. Changed back to actibe ***
- Envelope with model component cards (maybe in Tree's box...)
- Collection of duplo blocks with eyes (for the population, stolen from maths and engines)

<br/>

## Experiment Explanation 

Much of this is taken from the Citrus Canker RA which explains how to set it up and how the model functions. For Plus the equipment and concepts are basically the same but it is more maths heavy and takes things from first(ish) principles. 

Intro to modelling
Welcome, welcome! For the next 20 minutes or so you are going to be epidemiologists and are tasked with understanding and preventing or mitigating the spread of diseases. 

So, before we get started, what do you think are the different ways epidemiologists can help fight against the spread of disease?
 - understanding of the disease causing organism (lifecycle, habitat)
 - understanding the population (who is vulnerable, what section of the population are most at risk)
 - from these can work out what might slow/stop disease spread
 - look at historical cases to understand how similar diseases have spread in the past 
 - model the spread of diseases to estimate best and worse case scenarios
 - vaccinations, improved sanitation, improved diets/lifestyle

This morning we're going to zoom in on the modelling work; how would you define a computer model?
 - simplification of some function of the real world, built to help understand how the world works
 - all models are wrong, some are useful

Why do you think that models might be useful for epidemiologists? 
 - can't carry out these experiments in real life (unethical...)
 - can test many scenarios; what ifs...
 - allows you to test how well theory matches up with reality
 - computers allow us to do this on a big scale quickly and cheaply

We now have a population which is starting to get sick. There are some broad categories which we can break the population down into to help us to start to build our model - not every individual is equally likely to get sick and these categories help us to see this.
S Susceptible, not yet sick and can get sick
I Infected, currently ill and infectious
R Removed, either recovered or dead

Now we can use these three categories to build up our model

What do we need to know to understand how fast this disease will spread? How fast it is transmitted (beta). How fast is recovery (gamma). [expect lots of biological detail here]

Now we need to represent this mathematically (in order to get the computers to do all the hard work of calculation)
Talk about change in one category depends on the number of organisms arriving in it and leaving it, talk through each. 

R0 ("R naught") is the measure of the number of secondary infections caused by a single infected organism in a totally susceptible population
for an epidemic to occur R0 > 1 (then the disease will spread)
R0 = beta/gamma, for extent of spread depends on the number of organisms infected and the (inverse of) the rate of recovery 

Useful info and set up
----------------------


 **What is it?**
"Here I have a model of disease spreading between trees. We can see how quickly it spreads in different conditions and if our efforts to control it actually help."

**Set up** 
[Read through the descriptions of the parameters and get a feel for how changes to each parameter affects the spread of the disease, you can also hover over any of the text within the model for a short description. Don't forget to accept the changes before running a new simulation, or else nothing will change!]

Set up a fairly basic run of the model

Epidemiology
 - Model type = non cryptic infection, no death 
 - Expected primary infections = 0 
 - Expected exposed period = 100 days 
 - Expected cryptic period = 100 days 
 - Landscape type = random 
 - Dispersal kernel =100m 
 - Kernel type = exponential 
 - Stopping condition = epidemic eradicated (this can take a long time but you actually see the infection end (you can speed up running time)

Weather
 - low weather severity 

Control 
 - Disable Control 
(second time around) 
 - Cull radius = 100m 
 - First survey = 0 days 
 - Fraction unsurveyed = 0 
 - Detection probability = 80% 
 - Survey interval = 90 days 
 - Expected notice period = 60 days 
 - Notice variability = 0

**Start by talking about the spread of diseases:** 
 
"How do diseases spread?" - will probably get animal/human centred answers: sneezing, coughing, dirty hands, bad food, bad water, insects, bodily fluids 

"What about how diseases spread between plants?" - insects (vectors) are more important, moving the bacteria/viruses/parasites between plants, humans move infected plant material between fields (on farm equipment etc) 

[on computer] Here we can see a disease spreading between a bunch of orange/citrus trees: Green = healthy, orange = exposed, yellow = infected without symptoms, red = infectious, black = culled. "Can you see any pattern to how the disease is spreading?" - the disease doesn't spread randomly, but trees closer to a diseased tree are more likely become infected. With our model we can change how quickly the disease spreads [run the model with basic parameters (without cryptic infection), run it again with more initially infected trees, run again changing parameters to speed up spread of disease] Get the children to change the disease parameters (can split the group into two and use both laptops), trying to spread the disease the fastest. Ask them why they think the model is useful? - can see when the disease spreads fastest/which aspects of it make it most contagious, can see how it spreads through a landscape (which trees are most vulnerable to infection as the disease spreads)

[on computer] We can also try out different ways of stopping the disease spreading. "How would you stop a disease spreading?" Vaccination (doesn't work as plants don't have active immune systems like animals) Quarantine (you can't move trees away from each other, and it would be a lot of effort to seal the trees off from each other) Stopping insects (herbicides, this is one of our main ways of slowing the spread of diseases) Culling (killing/removing the trees, stopping the disease spreading away from trees which are known to be infected). Culling is the only effective way of controlling the spread of Citrus Canker, but there are different ways of doing it [run with control parameters, then run again with new parameters, chat through the differences] Get the children to change the control parameters, trying to save as many trees as possible, you can make it a competition between the two groups. Ask them why they think the model is useful? - can test how effective different control options are, then can use the results to find the optimal control mechanism, can run the same control plan many times to see how it is most likely to turn out.

**Team Disease vs Team Control** 
You can split the children into two teams; Team Disease; who are trying to kill as many of the trees as possible, and Team Control; who are trying to contain the spread of the disease (they tend to enjoy this challenge!)

[on computer] We can't always tell when trees are infected. This is called a cryptic infection and makes it more difficult to control the spread of the disease as the infected trees can infect other trees, without being infected. [run model with cryptic infection - should take longer to bring the infection under control]
 
 **Explaining the point of computer models:**

[ probably for older children] Computers are really useful for biologists. They make it easier to do calculations, work out statistics and can help us predict how a disease will spread. 

"Why do we want to know how a disease will spread?" Work out who/what might get infect next, how we can slow the spread of a disease. 

"Why is it good to have a computer to do this for us?" Makes it easier (not having to do the sums ourselves), don’t have to infect animals or plants in real life, can put in specifics about our outbreak of disease (where it started, how many people/animals/plants [organisms, depending on age of child]) to make it more accurate. 

Models simplify reality. To make it easier to understand the disease we can split all of our trees into different 'disease states/compartments', the most simple has just three compartments - Susceptible, Infected and Removed. More complicated models include Exposed and Cryptic Infections (like this model). Mathematical equations describe the movement of plants between the different compartments, the more compartments, the more complicated the equations get, but the more accurate the model gets.
 
Multiple Runs - [only for older, keen, kids who want to know more about modelling]. Each time the model is run (run new simulation) the results are different, partially because the initial conditions are different (two different trees are initially infected) even if the same trees were infected each time, the results would still be different as there are many variables not quantified in the model (e.g. precise landing spot of individual raindrops, wind speed and direction etc) we end up with a different result each time - chaos!(theory). 
To get a better grasp on the system you can run the simulation multiple times and watch the results of 100, 200 or 500 simulations run on a series of graphs which show the number/percentage of trees in each category (healthy, infectious and dead) change over time. You can see the typical pattern of infection e.g. that (given the initial conditions that you have set) most times about 250 trees will have to be culled, but that about 5% of the time only 600 trees will be left alive and the disease will run for over 8 years. 


 Demonstrator background info:
-----------------------------


This is a computer model for a disease called Citrus Canker. It is caused by a bacteria (Xanthomonas axonopodis) and infects orange and lemon trees causing them to drop their leaves and fruit early. The fruit is safe to eat, but too ugly to be sold. It can be easier to model plant diseases because unlike animals plants aren’t going to move around and spread the disease further themselves. The only way that the disease can be controlled is by cutting down infected trees. 

**Parameters**

[Read through these descriptions and work out how the changes to each parameter affects the spread of the disease, you can also hover over any of the text within the model for a short description. Don't forget to accept the changes before running a new simulation, or else nothing will change!] 

Talk through the model parameters in as much detail as you like. Less is more, probably chat through them in stages - run the model without controls to look at the epidemiology parameters, then keeping those parameters the same, introduce controls. 
 
**Epidemiology** 
(change how the disease spreads)
 
Initial infection – how many trees are infected right at the start (in real life this will depend on when the farmers spots that some of his trees are diseased) 

Secondary infection rate – how quickly the disease will spread from an infected to an uninfected tree 

Typical kernel range – a dispersal kernel is the area around an infected tree which the disease is likely to spread into, shows us which other trees are in danger, the type (either exponential or cauchy (apparently a better model for describing long distance dispersal)) probably doesn't make much difference. 

Initial infections - number of trees infected at the beginning of the trial 

Model type - different disease scenarios e.g. can it spread before it has been detected (cryptic infection) or not (probably easier to start off without cryptic infection or death) 

Expected primary infections - the number of new infections which come from outside the trial (i.e. not from trees that you can see on screen, but the 'external environment') best to keep this at zero to avoid confusion 

Expected exposed period - length of time that it takes for a tree to become infected (or how long it needs to be exposed for before becoming infected), once infected the tree can be discovered (as infected but not causing other infections) or start infecting other trees (if there is a cryptic infection period) 

Expected detectable period - length of time a tree will be detectable for before becoming infectious 

Landscape type - can simulate two neighboring plots of orange trees in a grove or citrus trees across a large landscape 

Stopping condition - the simulation can either stop after a set period of time or once the disease has been bought under control (it's more satisfying to let it run until either you or the disease have 'won') 
 
**Weather** 
Citrus canker is spread by in water droplets so it spreads more quickly between plants in high severity (wetter and windier) weather. It 'll be easier to start by keeping the weather the same throughout the trial (go for low severity throughout, you'll have a greater chance of 'beating' the disease) 

Probability that a low/high weather severity index - these two parameters alter the changeability of the weather, if the cursor is to the right for both then the weather will remain constant throughout the experiment, if to the left then the weather will oscillate between high and low 

Weather change interval - how often the weather status could change severity 

Weather low severity factor - controls the difference in rate of infection spread between low and high severity weather conditions 
 
**Controls**
The main method for controlling Citrus Canker is culling visibly infected trees and a number of the surrounding trees. 

Cull radius - all of the trees within this area are culled at the same time as the infected tree. The larger that this area is, the more likely you are to locally eradicate the disease, but you might end up killing all of your trees! 

Detection probability - likelihood of spotting the symptoms of diseased trees 

First survey - the time point at which the trees are first checked for disease 

Survey interval - how often the trees are checked for disease 

Fraction unsurveyed - proportion of trees which can't be accessed to check for disease (since they are on private property or are physically inaccessible), these trees will still be culled if within the cull radius of another tree 

Expected notice period - average time between finding a diseased tree and culling it 

Notice variability - standard deviation of time between finding and culling a given tree (makes the model more realistic - as you can't guarantee to remove all trees exactly 20 days after finding them) 

Cull together - remove all trees simultaneously 

Disable control - no intervention, watch spread of unopposed disease

<br/>

## Risk Assessment

### **Hazard**: Laptop cable

**Description**: Trip hazard

**Affected People**: All

**Before Mitigation**: Likelihood: 4, Severity: 2, Overall: 8

**Mitigation**: Set up close to power source, avoid cables crossing walkways and tape down cables.
Call a first aider in the event of an emergency.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Duplo on floor

**Description**: Trip hazard

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: Set up on a table or away from walk ways, making sure to pick up duplo if it gets knocked off table. Call a first aider in the event of an emergency.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Duplo

**Description**: Choking hazard

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: Do not let students eat duplo (should not be a problem with older students). Call a first aider in the event of an emergency.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

## Risk Assessment Check History 

**Check 1**: 2014-12-27 - Sarah Wiseman (sw628@cam.ac.uk), **Check 2**: 2015-01-23 - Kym Neil (kym.e.neil@gmail.com)

**Check 1**: 2016-01-04 - Sarah Wiseman (sw628@cam.ac.uk), **Check 2**: 2016-01-07 - Natalie Cree (nc434@cam.ac.uk)

**Check 1**: 2017-02-09 - Matt Worssam (mdw47@cam.ac.uk), **Check 2**: 2017-02-12 - Joanna Tumelty (jt574@cam.ac.uk)

**Check 1**: 2017-12-04 - Sarah Wiseman (sw628@cam.ac.uk), **Check 2**: 2018-02-02 - Richard "Miffles" Mifsud (rwm41@cam.ac.uk)

**Check 1**: 2019-01-09 - Amanda Buckingham (abb53@cam.ac.uk), **Check 2**: 2019-01-13 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2020-01-08 - Matt Worssam (mdw47@cam.ac.uk), **Check 2**: 2010-01-25 - Bryony Yates (by250@cam.ac.uk)

**Check 1**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk), **Check 2**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2022-02-01 - Andrew Sellek (ads79@cam.ac.uk), **Check 2**: 2021-02-09 - Sian Boughton (seb216@cam.ac.uk)

**Check 1**: 2023-01-18 - Jessica Trevelyan (jet81@cam.ac.uk), **Check 2**: 2022-02-14 - Asmita Niyogi (an637@cam.ac.uk)

**Check 1**: 2024-02-01 - Margaret Johncock (mllyj2@cam.ac.uk), 
