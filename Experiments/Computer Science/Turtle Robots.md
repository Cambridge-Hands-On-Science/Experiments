# Turtle Robots

**These turtles want to draw you shapes.** - Learn the basics of robotics by teaching simple robots to move and draw. 

Last initially checked on 2025-01-21 by Rowan Ong (rzmo2@cantab.ac.uk) and double-checked on 

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Valiant Roamer Turtle Robots (Currently have 4, one is cracked)
- Valiant Roamer Control Unit (Currently have 1 and sensors)
- Roamer Turtle Cases (I think there's two, one should be used on cracked robot)
- 6V Lantern Batteries (2 per robot) [These are available from some shops (camping ones) but are best got on Amazon or eBay]
- Custom wooden base plates (these are wooden and cover the batteries)
- Obstacles (cones)
- Roamer User Guide
- Roamer Activity Book
  
- Volty the robot (Needs 3 AAA batteries)
- 24  large double-sided circuit puzzle piece tiles
- 10 Circuit diagrams (with 20 different circuits to try)
- 40 command cards (small arrow cards)
- Instruction booklet (helpful to have)

<br/>

## Experiment Explanation 

#### TEACHING THE ROAMER
The Roamer moves forward and back, turns left and right, waits and makes sounds. You teach the Roamer to do this by pressing keys on the top of its body. There is a key for each of these functions, and a set of number keys. 

To enter an instruction press a key, followed by a number. This tells the Roamer how far to move, how much to turn, how long to wait or what sound to make. There are three other function keys: Sense, Two-State Outputs and Stepper Motor. 

#### ROAMER PROGRAMS
There are two types of program, the GO Program and Procedures. 
The GO Program is a list of instructions carried out when you press GO. 
A Procedure is a list of instructions with a name. Once you have defined the list, its name (e.g. P1) is used like any other instruction. When you enter its name in the GO Program, the Roamer will carry out the whole procedure list.

#### MEMORY
The Roamer has two types of memory, GO Memory and Procedure Memory. 
The Roamer will remember up to 59 instructions, and its powerful programming facilities enable it to carry out hundreds of actions. 
When its memory is nearly full the Roamer will sound a warning, similar to the sound you hear when you press CM. 

#### GO MEMORY
Instructions in the GO Memory are carried out when you press GO. If you add more instructions after executing the GO Program, they will be added to the GO Program and carried out the next time you press GO. 
The Roamer waits for two seconds after you press GO before executing the GO Program.

#### CLEARING THE GO MEMORY
Pressing CM then CM clears the GO Memory and allows you to enter a new GO Program. It does not clear the Procedure Memory. 
The first time you press CM a warning is sounded. Pressing CM a second time clears the GO Memory. 
If you press by mistake, press another key, or wait 10 seconds. The Roamer will then carry on with its GO Memory intact. 

#### DEMONSTRATION PROGRAM
If you press GO after you switch on the Roamer, it will carry out the Demonstration Program. This can be used to show beginners the basic Roamer functions. 
REMEMBER TO CLEAR THE DEMONSTRATION PROGRAM From THE GO MEMORY BEFORE PROGRAMMING. 

#### FORWARD AND BACK
Pressing (forward) or (back) followed by a number from 1 to 99 tells the Roamer to move forward or back that number of units. (See UNITS OF DISTANCE AND TURN). (These examples are illustrated in the style suggested on the programming sheet). 

#### RIGHT AND LEFT TURN
Pressing (right) or (left) followed by a number up to 999 turns the Roamer to the right (clockwise) or left (anticlockwise) that number of units. (See UNITS OF DISTANCE AND TURN). 

#### WAIT
Pressing (W) followed by a number from 1 to 99 tells the Roamer to be still and quiet for that number of seconds.

#### MUSIC
The Roamer has a programmable sound facility. You need to specify how long each note will last (duration) and how high or low the note will be (pitch). To play a note, press the music note button (♪) followed by a number from 1 to 8 for its duration, and another number from 1 to 13 for its pitch. If you want a rest (silent note), enter 14 for the pitch.

#### UNITS
The default units are 30cm (one robot length) for movement and 1 degree for turning. They can be changed by pressing (forward) or (right) and then ([]) and a number of cms or degrees.

#### STOPPING
Hold any key to stop the currently executing programme. 

#### CANCELLING
pressing (CE) cancels the last instruction from the programme. 

#### LOOPS
Pressing repeat, (R) followed by a number then ([]) some instructions and a closing ([]) repeats the enclosed instructions as a loop. Conditional loops aren't supported. 

#### PROCEDURES
Press (P) followed by a number to define that procedure. Then place instructions inside ([]). To use a procedure in the programme press (P) and its number and the only way to edit or delete is to redefine the procedure.

Recursion is not permitted and is implemented by procedures only being able to call procedures of strictly greater number. 99 procedures can be stored. 

#### DEMONSTRATING
Try to split the group evenly between the different robots and ensure each one has enough space to move around.

The robots are very simple to use so can be programmed with a try it and see approach. The sound feedback tells you what works and what doesn't and people will find out quickly what to do. You may wish to masking tape over some of the buttons, like the note and procedures to prevent them being used and increase the success of random button pressing.

The simplest aim is to set up some obstacles (cones or other) and ask them to navigate around the course. With sharpies one could also draw shapes on paper as an alternative. 
Obviously there are also things to learn. Roamers are procedurly programmed, one can talk about how one might try and solve a problem. A natural way is to break it into smaller problems, breaking down tasks into a set of steps to be carried out is called an algorithm and is a key part of programming.

When setting out the course think of repeatable steps you can build in so they can see they solve some problems a few times. This is where a procedure comes in. This could be something like navigate around a cone and this can be called whenever it's needed to navigate around a cone (similar to calling a function in coding). You can try this out with more advanced groups, if they seem to have a handle on the using the Go memory.

Procedures also have other advantages. For instance if we swap all the cones for different obstacles then we only have to change the cone procedure to work for the new obstacle.


The activity book has ideas for courses to build (we mostly use the maze one-easiest to set up, feel free to add some story to make it more interesting, eg. escaping a dungeon or looking fo treasure). The user guide provides more detail on how to program the roamers and what each button does, feel free to use these for reference.

Bottom up programming - using existing knowledge to solve a new problem.

Top down programming - diving a complex problem into smaller sub problems.

#### CONTROL UNIT 
We now own one Control Unit, this is in a cardboard box with lots of electronic sensors. It hasn't been used in demonstrations before.

The control unit screws into the depression on the bottom and the cable goes into the battery compartment to link to the robot. You can plug in sensors or two-state outputs (and also motors but we don't have any). In theory the button on top allows you to use these. It introduces some limited conditional elements using the sensor blocks and throwing in several loops lets you use these in more usual ways. Please use and document!


#### VOLTY ROBOT
There is also one volty robot. This comes with the power tracks set, including 10 double-sided circuit cards, tracks to build them, and direction cards to help kids plan a route. The tracks come in two types, one for the corners and one for the straights. The tiles are double sided and have a variety of sounds and lights commands Volty will do. The first three diagrams on the diagram cards are like a tutorial showing how construct the circuit.

Once the circuit is completed, the command cards come into play. This helps the kids plan out coding Volty to follow the circuit. This is especially useful when you get to the more complicated diagram examples.

When Volty completes a circuit and ends up back at the start, he does a little dance (rotates left and right) and plays a song. Slight bumps on the floor can cause Volty to move slightly off the track so he doesn’t play the sound or light up when expected. If it is on a flat surface this doesn’t happen.

You can try building these circuits and getting the kids to plan and input the routes, or let them choose the circuit to build or create their own circuits to follow. This kit is smaller scale than the turtle robots, but may be visually easier for younger children to understand, and less complex to program (as the programmed instructions are shown on Volty's screen). 

Side note: Volty needs to be used with the tracks, it can move forward and backwards without them, but requires the lines to follow to know when to stop rotating. It also reads the barcodes on the tracks to tell it when to make sounds/light up.


#### Programming Volty

- Pressing and holding the Delete (Bin) button will wipe the memory
- Press the program button (</>) to start entering a new program (up to 40 instructions)
- Press the direction button and it will appear under the current step (forward, 90 degrees right or left)
- Press the tick when you have finished editing the program and it will begin
- Pressing Bin will stop the current program
- To edit the current program press </> and use the left and right keys to move to the step you want to change, then press the tick to edit it, and enter the new instruction, followed by the tick to confirm it. Repeat for other steps you want to edit or press tick twice to exit edit mode



<br/>

## Risk Assessment

### **Hazard**: Battery covers

**Description**: Batteries may become loose/caught/punctured if improvised covering fails.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Check covering before beginning experiment. Call first aider in the event of accident.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Rain

**Description**: Batteries may react with rain due to improvised covers.

**Affected People**: Particularly demonstrator when handling batteries

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 4

**Mitigation**: Don't use in rain. Call first aider in case of injury. Check batteries for signs of corrosion before demonstrating the experiment.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Robots

**Description**: Robots may fall off table, raised surface and hit a person.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 3, Overall: 6

**Mitigation**: Use on the floor or have barriers on tables.
In the event of accident, call a first aider/mechanic.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3

<br/>

### **Hazard**: Robots

**Description**: Robots may be trip hazard if used on floor.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Don't use in thoroughfare and section off area for operation with hazard tape. Call first aider in the event of accident.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Paper and Cards

**Description**: Papercuts

**Affected People**: All 

**Before Mitigation**: Likelihood: 3, Severity: 3, Overall: 9

**Mitigation**: Laminated paper while possible, cards placed on the ground so minimal handling needed.

**After Mitigation**: Likelihood: 1, Severity: 3, Overall: 3



<br/>

## Risk Assessment Check History 

**Check 1**: 2018-07-22 - Benjamin Akrill (bja32@alumni.cam.ac.uk), **Check 2**: 2018-07-24 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-04 - Matthew Le Maitre (msl54@cam.ac.uk)

**Check 1**: 2020-01-31 - Beatrix Huissoon (beh37@cam.ac.uk), **Check 2**: 2020-02-04 - Emma Crickmore (elc75@cam.ac.uk)

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Sian Boughton (seb216@cam.ac.uk)

**Check 1**: 2023-02-17 - Emma Crickmore (elc75@cam.ac.uk), **Check 2**: 2023-02-18 - Asmita Niyogi (an637@cam.ac.uk)

**Check 1**: 2024-02-15 - Peter Methley (pm631@cam.ac.uk), **Check 2**: 2024-02-15 - Isobel Gilham (ig419@cam.ac.uk)

**Check 1**: 2025-01-21 - Rowan Ong (rzmo2@cantab.ac.uk), **Check 2**: 
