# Robotics on tour! & CBS Workshops

**Challenges that can be done with robots in a relatively short time period. Robotics workshops run during CBS.** - Learn to programme LEGO Mindstorms and learn about IF statements and LOOPs.

Last initially checked on 2023-12-31 by Chiara Delpiano-Cordeiro (cd796@cam.ac.uk) and double-checked on 2024-01-11 by Asmita Niyogi (an637@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **Electricity needed**
- Lego Mindstorms EV3 Robot kit (There are four robots in two cases)
- 18 x AA Batteries  (Currently there are 16 rechargeable and 2 non rechargeable)
- 2 x Recharge stations
- 1 x Green fabric with blue fabric "pond" sewn on
- Worshops:
- 8 x Robotics Kits, consisting of Lego Mindstorms NXT brick, motors, assorted sensors, associated connectors, structural lego components and moving parts (i.e. gears) - On loan from University of Cambridge Engineering Department
- 8 x laptops with software installed to program Mindstorms NXT bricks - On loan from Cambridge Engineering Department
- Assorted paper and pens
- As many charged batteries as possible for CBS

<br/>

## Experiment Explanation 

**On Tour**
**Set up:**

**For the computer:**

Turn on the CHaOS laptop (currently 2,3 and 4 have the software installed but it is free to download from the lego website)
To login the password is CHaOS (capitalised correctly) 
Start the lego mindstorms program
Go to file -> new project. If you want to be able to find programs you have created more easily I recommend you go file -> save as.
It is also possible to double click on the program name to rename it. At public events I like to ask children their names and name it that so which program is theirs can be easily seen. 

**For the robot:**

If you aren't sure of the level of charge immediately start charging its batteries.

If you are confident the batteries are suitably charged, put the batteries into the EV3 Brick.

If the robot is damaged, fix it (I need to take pictures so everybody knows what it looked like).

The Ev3 Brick should be put onto the robots base. 

Connect the colour sensor to port 3, and the motors to ports B and C. The motor wires **should** cross due to way the steering works.

**The programming**

Ideally you should experiment with the robot before you start demonstrating. All programs consist of series of blocks that contain instructions which the robot will follow in order.

There are four blocks that I use more than the others:

Green Tab, 3 along. This is "Move Steering" with this you can control which direction the robot turns and how tightly, which direction it will travel and how fast and how long it will do so for. Alternatives to this would be the "Move Tank" and "Large motor" Blocks which I feel are less intuitive.

Green Tab, 7 along. This is "Brick Status Light". It can be set to three different colours and be on continuously or flash. It is useful for identifying sensor inputs easily. An alternative to this would be the "Sound" block which I find is too quiet too be heard in a room full of children. The "Display" block can also be used too.

Orange Tab, 3 along. This is the "Loop" Block. Loops are an important concept in programming and quite simple. It works especially well in combination with the next block.

Orange Tab, 4 along. This is the "Switch" block and is the most interesting block I frequently use as it allows the robot to make decisions based on inputs. I use the colour sensor but if you wanted to make modifications there is potential for other sensors to be used. If you want to follow the edge of a colour I would recommend using compare colour. If you wanted to stay with in a coloured area separated by two different colours you would use measure colour. Compare is more reliable as it can tell whether or not something is a certain colour quite well, but with measure it can be hard to determine what the robot will decide it is e.g. purple when you are asking it to choose between red and blue. The two 'paths' of the switch should have the robot turning different directions or travelling in different directions in order for something interesting to be observed.

There's full support for variables (but that doesn't mean you want to use them and it's easier if you don't however for advanced groups) you drop a variable box to create a variable ad it's name is in the upper right and it's data type in the lower left. Operations performed using maths boxes and the lower left box sets the operation and the next two boxes the arguments, these can be variables connected via a data wire. The output can be saved as a variable using a data wire and setting data type as write number.

**Demonstrating:** 

I start off by asking them their names so that we have an easily identifiable program (In schools the groups will likely be too large for this. I then ask them, what do robots do? You will get a range of different responses, sometimes close to the answer of "they follow instructions". I then introduce the program to them and tell them that the blocks are just instructions for the robot. 

Depending on the age of the children you can ask them what they want it to do e.g. "Do you want it to turn left or right?" and program it yourself or tell them "this slider controls how it will turn" and let them do it. After they have made their block they need to download the program to the robot. 

Connect the cable to the computers USB port and the pc port on the output side of the robot. Press the download arrow in the bottom right of the screen. It may be grayed out if you have just connected the robot. After you have pressed download the robot will make a noise. This means it has downloaded. You will now need to look for your program on the robot. Go to the file tab, pick the correct project, then scroll down to the correct name. Get the child to verify that that is their name on the program that is about to be run. Place the robot in a suitable space and let them press the middle grey button.

You can then move on to making the program more complex, normally by making lights flash and a second movement block. If you think they are mature enough move on to using the sensor. Delete the previous program and put the loop and switch in place. Let them chose what they want in each option but give hints so that it ends up doing something interesting.

If they really want to do more let them, but I normally end by discussing in which jobs are robots most useful. The boring ones (painting cars), and the dangerous ones (missions to mars).

To get ready for the next child create a new program and keep the old ones as some may do interesting things which take time to program. However keeping too many programs can resulting in downloading taking more time.

Advice for demonstrating in Schools:

- It is more important that you don't keep the children for too long, this experiment can easily take 20 minutes if you try to get them to do the line following even with significant prompting.
- Try to ensure that all students make an input to the program, this becomes more difficult with larger groups
- For primary school students it is probably fine to ignore the sensor completely and just let them play around making a basic program with flashing lights, sounds and movement.
- For older secondary age (Y9+) students you should try to get them to do line following.
- For children in Y7&Y8 ask them whether they want a challenge (line following) or just to play around. 

**Braitenberg Vehicles - fast to demonstrate, easy to explain, but still produces complex behaviour**

A possible easy way to demo robots is to teach the kids about some of the earliest robots - things called “Braitenberg Vehicles”. To set this up, just hook up some light sensors to output numbers straight to the motors. If we have two light sensors, each outputting light-intensity, and we just whack those numbers into the motors, we can create some “life-like” behaviour. Setting this up means you have to have a light sensor on either side of the robot, and feeding that number to the “move tank” block by using the variable drag and drop lines on Mindstorms:

![](/sites/default/files/Screenshot 2019-08-31 at 15.19.14.png)

There are two possible behaviours, where the robot will speed towards lights, or speed until they’re facing away from them, “aggressive” (charges towards lights in a search-and-destroy fashion - this might be part of the reason Moths fly towards lights, I think I read that they have a biological feedback similar to this) and “cowardly” (runs like crazy to get away from light):

![](/sites/default/files/Screenshot 2019-08-31 at 15.02.45.png)
![](/sites/default/files/Screenshot 2019-08-31 at 15.02.40.png)

If we multiply the sensor output by -1 (use an arithmetic block), then another two behaviours are possible, “explorer” (goes all over the place), and “loving” (lovingly and slowly approaches the lights). You can let the kids fiddle with the numbers and rewire the sensors to other motors.

![](/sites/default/files/Screenshot 2019-08-31 at 15.02.59.png)
![](/sites/default/files/Screenshot 2019-08-31 at 15.02.51.png)

Depending on age and time, you can use the Braitenberg vehicles to talk about perception-action loops - what's the loop going on here, what about if we wanted to give it instructions, what about if the robot is now on the moon and we want to give it instructions, what problems are there now (the moon is 1 light second away...). Could also talk about reactive vs deliberative behaviour - are the vehicles reactive or deliberative, why? (reactive because there's no planning going on, you could mention that they don't need to remember anything). 

For people who really know what's going on, you could talk about vehicles with more sensors - you can combine them in lots of different ways, even having multiple sensors wired to each (motor) output... if the outputs are a linear combination of the inputs, we have a complicated Braitenberg vehicle. But... if we want a *non-linear* combination of the input variables, then we can use a *neural network* to add up inputs in any which way we want. Now you could get them thinking about their bodies... we have a series of inputs (feel, smell, sight etc.), which go through something inside our skull which is a bit like a neural network... which outputs to a series of *actuators* (muscles). Proceed into philosophical discussion about consciousness until the kids are either forced to leave by terror or boredom.

PLUS Explanation
----------------

The line following works well for this age as most have not done significant amounts of programming so it will still be a challenge. For students who complete that quickly you can push them further. Instruct them to start far from the blue and travel in a straight line until they hit the pond then follow it around, stopping when they get to a red piece of card. 

You should not let yourself be restricted by these instructions if you have other ideas of how to run this. There is a huge potential of things that could be done.

The below sections are not part of a demonstration but are retained as they could be used in future designs

 Maze
-----

A simple maze can be created with the wooden blocks or cardboard. The challenge is to program the robot so that it can navigate its way through the maze without any outside influence once it has started. This can be be done in several ways that progressively advance in difficulty:

1. Dead reckoning: the robot is programmed to move forward a certain angle, turn, move forward another certain amount and so on. This requires no sensor use and the robot is likely to generate errors in its positioning as it moves further. The robot could potentially fitted with a missile to try and hit targets once it has been through the maze.
3. Sensors with knowledge of the maze: The robot is equipped with touch/light sensors on its front and detects when it hits an obstacle. With knowledge of the maze, it will be possible for children to have set the correct direction for the robot to turn. The robot should be able to progress through the maze with smaller errors.
4. Sensors and a generic maze: The robot will be programmed to turn whenever it hits an obstacle and if that turn leads to another obstacle it will turn the other way. Through use of counters it could even find its own way back through the maze with little crashing. Sensors on the sides could be used to correct its course if it has a glancing impact with the wall.
5. Maze with coloured tiles. Using the ability of the robots to detect colours we can tell them to perform certain actions when they see a certain colour. 
This compares well with the simple Turtle Robots which are often used like this and you can read the RA for that to find information about programming them in this style.

Robot Writer
------------

The A3 sheet will be placed under the wooden blocks used for the maze so that it does not slide. The robot will be equipped with a pen holder arm that will be raised or lowered as necessary. This arm could be stationary relative to the robot or could move, allowing more effective writing to be used. The movements are likely to be by dead reckoning.

Children could be instructed to program the robot to make letters of the alphabet and write words. A simple task could be for them to write the word CHaOS. They would create a sub-program for the letter "H" and then add it to to subprograms created by the demonstrator that write the other letters.

Potential inputs could be morse code claps to be picked up by a microphone and subsequently written down by the robot. This bit is likely to be too advanced for the time we have but could be used in less time sensitive places such as public events.

<br/>

## Risk Assessment

### **Hazard**: Power cables

**Description**: Trip hazard.

**Affected People**: All

**Before Mitigation**: Likelihood: 4, Severity: 3, Overall: 12

**Mitigation**: Ensure wires are either taped securely to surfaces, or are placed behind tables, so no one walking past will catch themselves on the wires. 

In case of an accident, turn off power at the mains, do not touch any other components, such as the laptop or its battery. Call first aider.

**After Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

<br/>

### **Hazard**: Electrical components

**Description**: Various risks associated with electrical components.

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 5, Overall: 15

**Mitigation**: All laptop chargers will be PAT checked for safety and will be kept out of reach of children. See electrical parts RA.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Small Lego parts

**Description**: Choking hazard for small Lego components.

**Affected People**: Mainly young children

**Before Mitigation**: Likelihood: 3, Severity: 5, Overall: 15

**Mitigation**: All participants will be monitored regularly by demonstrators to ensure they do not put Lego in their mouths. The robots are largely pre-built, minimising visitors’ use of individual parts, and any modifications will be supervised by a demonstrator. Particularly young children will be supervised closely and if at CBS, will also be under parental supervision, though it is unlikely that very young children will be present as the workshop is targeted at older children. 

Call a first aider if choking occurs.

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Robots and laptops

**Description**: Robots/laptops falling off tables and hitting small
children/sitting children.

**Affected People**: Children

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Robots should be used on the floor unless they are immobile or all children present are standing and have their heads above the edge of the table. Laptops if used on tables shouldn’t be moving around, and should be far enough away from table edges. 

Call a first aider if required.

**After Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

<br/>

### **Hazard**: Motors

**Description**: Short circuits.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 4, Overall: 8

**Mitigation**: Motors are sealed in a robust manner, so any short circuits will result in a simple failure, with no risk to users. In the very unlikely event of an exposed short, voltages and currents used are very low (powered by 4 AA batteries), so present no significant risk to users. 

If short circuit occurs, power down the robot and do not use the kit further. Call a first aider if required.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Gearing system

**Description**: Things like hair wrapping around moving motors.

**Affected People**: All, particularly those with long hair

**Before Mitigation**: Likelihood: 4, Severity: 2, Overall: 8

**Mitigation**: Motors are sealed, so hair is unlikely to be caught, though it may be caught by gearing systems. All visitors will be made aware of the risk and asked to ensure any dangling objects on their person are kept out of the way and advised to tie long hair up if they might lean near the gearing system. They will also be made aware of the emergency stop, which will shut off all motors instantaneously. 

Immediately stop robot if anything is caught in motors. Call a first aider if required.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

## Risk Assessment Check History 

**Check 1**: 2015-10-23 - Tim Morgan Boyd (tmb58@cam.ac.uk), **Check 2**: 2015-10-23 - Robert Gayer (rg478@cam.ac.uk)

**Check 1**: 2017-01-22 - Robert Gayer (rg478@cam.ac.uk), **Check 2**: 2017-02-06 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2018-02-06 - Jared Jeyaretnam (jaj55@alumni.cam.ac.uk), **Check 2**: 2018-02-06 - Joanna Tumelty (jt574@cam.ac.uk)

**Check 1**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk), **Check 2**: 2019-02-05 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2019-08-31 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2019-09-01 - Benjamin Akrill (bja32@alumni.cam.ac.uk)

**Check 1**: 2020-01-30 - Conor Cafolla (ctc43@cam.ac.uk), **Check 2**: 2020-01-30 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2021-01-19 - Jared Jeyaretnam (jaj55@alumni.cam.ac.uk), **Check 2**: 2021-01-20 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Margaret Johncock (mllyj2@cam.ac.uk)

**Check 1**: 2023-01-21 - Asmita Niyogi (an637@cam.ac.uk), **Check 2**: 2023-01-30 - Jamie Barrett (jb2369@cam.ac.uk)

**Check 1**: 2023-12-31 - Chiara Delpiano-Cordeiro (cd796@cam.ac.uk), **Check 2**: 2024-01-11 - Asmita Niyogi (an637@cam.ac.uk)
