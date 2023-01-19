# Spaghetti Loading

This experiment uses uncooked spaghetti to explore elastic buckling of vertical columns and 3-point bending of horizontal beams.

Last initially checked on 2023-01-19 by Toni Renz (ir331@cam.ac.uk) and double-checked on 2022-02-09 by Conor Cafolla (ctc43@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Materials Science**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Materials Science**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- 1 pack of spaghetti (will need replacing periodically)
- 2 wooden blocks to hang spaghetti across
- 9 steel nuts
- 1 pack of elastic bands
- 1 tray to catch spaghetti fragments
- 1 hollow cylindrical beam (pending)
- 1 small I-beam (pending)
- Photos of the Pantheon/Acropolis, crushed concrete column, and wooden roof beams.

<br/>

## Experiment Explanation 

This demonstration uses a spaghetti model to demonstrate elastic buckling and 3-point bending. I personally like to put it into the context of building a house out of equal-sized wooden logs. You can start by discussing use of spaghetti as a building material, because the more materials science we put into this experiment, the less likely it is that the engineering coordinators will try and claim it. Spaghetti would not make a good building material because it goes soft when wet. It is also quite brittle so may not fare well in heavy wind. Some people may suggest that it is weak, but large bundles of spaghetti are probably surprisingly strong.

**Axial Loading:**

How will we hold the ceiling up? Most students will say using a wall or pillar. Try to guide them towards pillars/columns since this is what you're actually going to be talking about. The job of a column is to keep the ceiling up. Hold up an intact piece of spaghetti by the palms of your hands, as this will enable you to load it under compression and demonstrate buckling. Buckling is bad as it allows the ceiling to move downwards, which could warp it and cause it to fail.

Push your hands together gently with your palms flat to demonstrate elastic buckling in the spaghetti. It is elastic because removing the force allows the spaghetti to return to its original shape. Ask the students how we can make the column stiffer i.e. resist buckling. 

$$\ σ_{EB} = \frac{cπ^2E}{4(L/R)^2} $$

The above expression tells us that a smaller stress (force) is required to cause buckling if the aspect ratio, the ratio of the column length to its radius is larger. The column can be made stiffer in two ways: by making it shorter, or by making it wider. This can be demonstrated by giving the students pieces of spaghetti of different lengths and getting them to feel how much force it takes to make them buckle. Shorter pieces should be much more difficult to buckle.

The problem with making it shorter is that it has to span the distance between the floor and ceiling in order to hold up the ceiling. So the column length isn't easily customisable.

If you don't explain the aspect ratio thing to students, most of them will probably say that adding more logs to the column will make it stiffer. By adding more logs you make the column wider which also decreases the aspect ratio, thus making the column more resistant to buckling.

By this logic, we want an infinitely thick column. There are a couple of problems with this. Firstly, the wider the column, the more space it takes up. So we want an optimal thickness which will hold the ceiling up without using too much space. The other problem is that if the buckling stress is too high, the column will instead fail by crushing. A crushed column cannot bear any weight, but a column which is buckling still can provided it doesn't break. Therefore, it is better for a column to buckle slightly than break, and short fat columns may not be desirable.

**3-Point Bending:**

In the context of house-building, I claim that roof beams are loaded under a 3-point bend. To be honest, I have no idea if this is the case. So if someone has a better way to put it into context then let me know.

First, ask the student if you can make stronger roof beams by laying them out individually or bundling them up. Hopefully they will say bundling up. There are two reasons why bundling them up is better. Firstly, The more logs you have in the roof beam, the more weight they can bear since the weight is shared between the logs. Laying them out side by side means that you can't fit as many logs along the length of the ceiling that if you bundle them up, and make use of the vertical space.

Secondly, by bundling them up, you increase the second moment of area of the roof section. This makes the beam stiffer under a 3-point bend, and it can therefore take more weight without flexing. The equation for 3-point bending is shown below:

$$ y = \frac{Fx}{48EI} (3L^3 - 4x^2) $$

Place a piece of spaghetti so that it is resting horizontally on top of the two wooden blocks. To make this part more interesting (if that's even possible), you can ask the students to take bets on how many of the steel nuts it will take (threaded onto the centre of the spaghetti beam) to break it. Usually, two or three is enough. After this, take a bundle of 5 pieces of spaghetti, and wrap an elastic band around one end to hold it all together. Ask the students whether it will take more or less weight to break the bundle (they should say more) and then ask how many nuts they want you to put on. Even with all 9 of the provided nuts, the bundle will not break. But you can show that however many they select, the bundle doesn't flex that much. **note:** it is difficult to demonstrate the effect of bundling vs. loose because loose spaghetti tends to bundle up when threaded through the nuts.

When bending the spaghetti bundle, the bottom surface ends up under tension while the top surface gets put under compression. Just like many materials, spaghetti is much stronger under compression than tension. This discrepancy is especially pronounced in concrete, which is extremely strong in compression and weak in tension, hence they are used for support columns rather than cables. You can show this using spaghetti by loading it in compression (trying to crush a piece between your fingers by pressing across its diameter) and then in tension (by pulling from opposite ends). Students should find that it is impossible to crush the spaghetti, but quite easy to pull it apart. If anyone does manage to crush the spaghetti, send them my way as I may have a job for them.

What this means is that the piece of spaghetti at the bottom of the bundle, which is under the most tension, will fail first. This is followed by the rest of the bundle as the stress is redistributed. The bundle fails in a 'chain reaction' as the fracture propagates from the bottom to the top surface of the bundle, with each piece of spaghetti breaking in sequence. This failure happens very suddenly and catastrophically. Macroscopically, there are no early warning signs as the failure of one log in the bundle leads to the instant failure of the entire bundle. Spaghetti is also brittle, meaning it will fail suddenly without plastic deformation. Therefore, this is something we want to try and avoid.

**Hollow sections and I-beams (CHaOS+)**

Hopefully by now someone has acquired a hollow beam and an I-beam. While these won't be loaded or broken in the demonstration, it is interesting to discuss how engineers can save on materials without sacrificing much strength.

Hollowing out a beam will decrease its mass significantly, with a less than proportionate loss in strength. This is because the larger the second moment of area of a beam (effectively a measure of the distribution of mass away from the central axis of the beam), the greater the 'beam stiffness' which is a product of second moment of area and young's modulus. A hollow beam will be much stiffer than a solid beam of the same mass.

Solid Beam

$$ I = \frac{wh^3}{12} $$

Hollow Beam

$$ I = \frac{wh^3 - w_{in}h_{in}^3}{12} $$

An I-shaped beam is used by engineers because it can achieve a similar strength to a beam with a solid cross section but requires less material to make and is also lighter. Some manufacturers even go as far as to cut holes in the stem of the 'I'. The further away material is from the central axis of the beam, the more it contributes to the stiffness of the beam. This is why cross sections with a greater second moment of area give stiffer beams. The beam is an 'I' rather than an 'H' because this orientation of the beam provides the most resistance to elastic deformation when the beam is under a vertical load, which it usually is in service.

<br/>

## Risk Assessment

### **Hazard**: Uncooked spaghetti

**Description**: Public

**Affected People**: Sharp ends from spaghetti fracture scratching or stabbing people.

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: Clear spaghetti debris from table throughout the experiment. Instruct kids to throw away spaghetti pieces as the experiment progresses rather than at the end. Also make sure fractured pieces are not held near the face. Do the experiment in a tray.
Call a first aider in event of injury.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Slippy spaghetti

**Description**: All

**Affected People**: Spaghetti debris on the floor could be "slippery" if stepped on.

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Clear spaghetti debris as much as you can throughout the experiment. As above, do the experiment in a tray to try to contain most of the shards.
Call a first aider in event of injury.

**After Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

<br/>

### **Hazard**: Spaghetti shards

**Description**: All

**Affected People**: Loose pieces of spaghetti flying into eyes when bent and fractured.

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Forewarn students and when bending spaghetti, bend away from self and away from others.
In case of injury call first aider.

**After Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

<br/>

### **Hazard**: Masses

**Description**: Public

**Affected People**: Masses falling onto feet or fingers.

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Set-up on table to avoid toes. Have ‘drop zone’, no fingers under masses. Use light masses (10-50g) to avoid heavy masses hurting fingers.
Call a first aider in event of injury.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Spaghetti

**Description**: Public

**Affected People**: Transfer of bacteria if students try to eat spaghetti that others have touched.

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

**Mitigation**: Instruct students to not eat the spaghetti. Use different strands for each student, and for each group.
In case of contact, advise parents to take children to GP if illness develops.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-01-18 - Laura Wells (lbw28@cam.ac.uk), **Check 2**: 2018-02-06 - Andrew Sellek (ads79@cam.ac.uk)

**Check 1**: 2018-08-11 - Yaron Bernstein (yb258@cam.ac.uk), **Check 2**: 2018-08-11 - Matthew Le Maitre (msl54@cam.ac.uk)

**Check 1**: 2019-01-09 - Grace Exley (gae23@cam.ac.uk), **Check 2**: 2019-01-27 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2020-01-18 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2020-01-20 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2021-01-20 - Conor Cafolla (ctc43@cam.ac.uk), **Check 2**: 2021-01-20 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2022-02-09 - Andrew Sellek (ads79@cam.ac.uk), **Check 2**: 2022-02-09 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2023-01-19 - Toni Renz (ir331@cam.ac.uk), 
