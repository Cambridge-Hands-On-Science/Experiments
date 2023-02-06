# Radiotherapy Statistics

**Statistics in the hospital** - Explore how statistics get used within a hospital with a model of radiotherapy treatment for cancer. Try and damage the tumour while minimising the effects to nearby healthy cells.

Last initially checked on 2020-12-12 by Yian Aaron Koh (yak23@cam.ac.uk) and double-checked on 2021-01-22 by Andrew Sellek (ads79@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Medicine**

**Stats**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Maths**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Lots of Dice [lots = at least 30]
- Radiotherapy Board

<br/>

## Experiment Explanation 

Ask people about statistics, we have lots of dice. We're going to be considering probabilities when rolling the dice, can they work out the chances of rolling different numbers? What about rolling greater than a 3,4,5? What about rolling at least 3 but not more than 5? 

Our game is going to involve us moving across various hexagons in a straight line. Each hexagon has a number (x+) on it, this means it will absorb any dice with x or greater and any lower dies will pass through to the next hexagon and be re-rolled, where they might get absorbed again. You can then talk about independence, we keep re-rolling so we have that!

We'll now talk about cancer and our model. One hexagon will be our tumour cell, the other hexagons are healthy body cells. Our dice will be the rays of radiation we're going to try a destroy the tumour cell with. A healthy cell will be destroyed when it's absorbed 3 dice, we'll aim to maximise the number of dice the tumour cell absorbs. We have 6 possible directions to send radiation from and the goal is to destroy the tumour. The dose is going to be the number of dice we roll and we'll also need to choose a direction, later we'll get more complicated and can choose to split our dose between several directions.

This is basically a simulation study. We can calculate with effort the 'best' dose for a given direction, however it's much more complicated with multiple directions. You can work out the expected damage a dice in a given direction causes to different cells if you want, that's fairly easy. The number of destroyed healthy cells is non-trivial.

Compare total damage to tumour vs destroyed healthy cells from different directions. You can also think of variance. Is the variance in both of these the same? What might our concern be with the variance? High variance of destroyed healthy cells means there's a chance this goes very badly.

While this model seems very simple (it is) you can see how hard it is to calculate the best option. It uses simulations to estimate as the algebra is too complicated. We can do similar more complicated simulations on a computer, and run them thousands of times to account for the variance.

Monte Carlo methods use similar ideas of simulating things, in fact there doesn't even need to be any randomness in the original problem. 

<br/>

## Risk Assessment

### **Hazard**: Dice

**Description**: Dice on floor could cause slips and trips.

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Roll dice sensibly, into tupperware or similar to contain them. Pick up any dropped dice immediately.

**After Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

<br/>

### **Hazard**: Dice

**Description**: Choking hazard

**Affected People**: Public

**Before Mitigation**: Likelihood: 2, Severity: 5, Overall: 10

**Mitigation**: Do not give the dice to small children. Keep an eye on the dice and pick up any dropped ones immediately. If choking, encourage the child to cough and call a first aider.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Cancer

**Description**: This topic may cause distress to some people

**Affected People**: All

**Before Mitigation**: Likelihood: 4, Severity: 2, Overall: 8

**Mitigation**: This game is a radical simplification and is nothing like modern oncology. Warn the group that this group is about modelling cancer treatment (i.e. tell a teacher or parent) and move group on to different experiment if affected.

**After Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-12-15 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2020-02-05 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2020-02-05 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2020-12-12 - Yian Aaron Koh (yak23@cam.ac.uk), **Check 2**: 2021-01-22 - Andrew Sellek (ads79@cam.ac.uk)