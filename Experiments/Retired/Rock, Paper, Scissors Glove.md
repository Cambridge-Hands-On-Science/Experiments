# Rock, Paper, Scissors Glove

**Can you beat a glove at Rock Paper Scissors?** - We've taught a glove to play rock paper scissors, can you beat it? Learn about AI in this quick demo.

Last initially checked on 2021-01-22 by Polly Hooton (prh43@cam.ac.uk) and double-checked on 2021-01-22 by Grace Exley (gae23@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**AI**

**Busking**

**Floating**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **Electricity needed**
- Rock Paper Scissors Glove
- Display Screen
- Code on github repo
- OPTIONAL - If you have a laptop with ipython notebook support and arduino ide you can retrain the glove

<br/>

## Experiment Explanation 

Get the volunteer to put on the glove, they can take a look at some of the electronics on the outside but we can think about how it works later.

connect the glove to the 'display', explain to the volunteer how the game works and how the display works. Then get them to play. The glove should point fairly quickly to it's choice so it'll seem like they go at the same time. 

So how come the glove wins? You can see some sensors on the glove, there's one on the second finger and one on the pinky. These sensors are flex/bend sensors and the resistance increases when the sensor is bent, which happens when you move your fingers. These feed into an Arduino via the cable from the glove which processes the signal and decides what the volunteer is going for.

If you want to go into details with the laptop then the sensors use a voltage divider to calculate the resistance of the flex sensor. This is a simple circuit with a fixed resistor then in parallel a voltage reader (analogue input on arduino) and the flex sensor. We can then use Ohm's law to calculate the resistance and therefore measure how much the sensor is flexed. We'll re-scale this into [0,1].

It uses a machine learning model to predict this, this is trained on some past uses of people throwing the different signs. What way can we confuse it? Try and do the symbols differently, maybe rock with pinky out or scissors with fingers 3 and 4.

Our model is trained on past data, this involves us repeating rock over and over and recording the value of the resistors in a data file. We then do the same for scissors and paper. We can imagine these values as points in a square where the values from our two resistors give us coordinates. As we've re-scaled this is [0,1] x [0,1]. If we put in the points as red, green and blue our aim is to divide up the square into three pieces roughly corresponding to rock, paper and scissors. In the python notebook you can see this graphed out in the plane and shaded regions. 

This is an example of supervised learning, we're giving the computer knowledge of the three categories we want it to identify. We have lots of simple ways of doing this, one is called KNN (k-Nearest Neighbours) this calculates the k points in our past data which are closest [in distance on the plot] and we look at whether the majority are from the rock, paper or scissors data examples. 

We're using here a package called tensor flow which uses linear maps, this map is calculated from our past data and uses a matrix to map our two sensor readings to three probabilities. This map is what the python notebook prints out and is what we copy across to the arduino. The probabilities represent our likelihood estimate that the reading came from rock, paper or scissors. This is linear/logistic regression. 

Other types of learning are unsupervised, here we let the code find the different clusters itself, here those would be the rock, paper and scissors ones, it wouldn't work well for the glove though as we need to know which cluster is which to be able to win. There's also reinforcement learning, for this we'd get the machine to play the game several times, at the start it would just pick it's moves at random, after each go we'd give it positive or negative feedback and then it would adjust it's strategy slightly. [This would also work well for rock, paper, scissors if we can get a green and red button and some code together we could do this in future, I'm not sure how many games you'd need to play to get it to win frequently. It could also then deal with a surprise mid-game swap to rock, paper, scissors, lizard, spock but you'd probably want more bend sensors (they're £15 each and I'd get 4" ones next time) and to work on the hand signals as paper vs spock is hard].

You should be able to train the glove yourself eventually [i.e. when I get the code working]. You'll need to do this on the laptop, I think around 30 samples of each should be fine for a quick demo. Then copy and paste the output map into the top of the arduino programme and upload it to the device. If you can leave the original programme on the device when you finish that would be great!

https://experiments.withgoogle.com/rock-paper-scissors

---------------------------------
To make this better looking you could 3D print an articulated hand and add in a second servo to control the fingers. 

<br/>

## Risk Assessment

### **Hazard**: Electronics

**Description**: Electronics could short in rain.

**Affected People**: All

**Before Mitigation**: Likelihood: 4, Severity: 2, Overall: 8

**Mitigation**: Check waterproofing before use. Don't use if any issue with rain predicted. Try to avoid demonstrating this experiment outdoors.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Cable

**Description**: People could get tangled in cable from display to glove.

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Make it easily detachable if pulled strongly, encourage people to stay still while wearing glove.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-12-12 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2018-12-15 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2019-12-26 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2020-01-27 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk)