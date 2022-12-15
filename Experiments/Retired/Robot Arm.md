# Robot Arm

**Programme a robot using scratch!** - Learn how to programme in scratch by controlling this robotic arm, 

Last initially checked on 2021-01-22 by Polly Hooton (prh43@cam.ac.uk) and double-checked on 2021-01-22 by Grace Exley (gae23@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Computer Science**

**Programming**

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- **Electricity needed**
- Robotic arm and USB interface
- Laptop with installed software
- Something to pick up (can, lego)
- 
- Software
- Scratch 2.0 Offline (Note version 3.0 lacks support for HTTP Extensions)
- Python (2.7 defo but probs recent ones too) + pip
- Pyusb package (run pip install --pre pyusb)
- Libusb
- Http_server.py (python script)
- MaplinArm.json (scratch extension)

<br/>

## Experiment Explanation 

Set up
You'll need to check you have all the software on the laptop. If I remember there'll be a USB with it all on in the box however the internet has it available.
Firstly connect the arm and make sure it is switched on, then open a python terminal and run 'python http\_server.py' which will execute the python script. A message saying the server is running should be displayed, leave it running all the time. Then you'll need to load the arm functions into scratch, press shift, then click file while holding shift. Go to "Install experimental HTTP Extension" then select 'maplinArm.json'. In scratch you should be able to access these under more blocks, then a 'MaplinArm' drop down. There should be a green dot next to 'MaplinArm' to indicate the communication is working.
[What you've done here is start up a HTTP server in python, this receives packets from scratch saying which instruction and then it runs some python which via some reverse engineering of the arm control protocol, a robotic arm library and USB wizardry to actually control the arm. Without the whole mechanism of HTTP this is a bit like an interpreter from Scratch into Python, if you wanted to talk about this and compilers feel free...]
see https://piamble.wordpress.com/controlling-the-maplin-robot-arm-with-scratch-v2-offline-on-microsoft-windows-10/
My code for this is also on the CHaOS github.

Using it
It's like scratch but with some extra blocks that control the arm. The kids can probably figure it out simples even if you can't. Get them to pick things up, move them around and put them down again. You can talk about general robotics, what might you use this for? Problems? (I'd guess this could crush an empty can if you weren't careful) Maybe think about loops, automated processes in a factory. You could ask about improvements? Maybe fit a camera and then sort based on colour (you couldn't do this in scratch though!).

<br/>

## Risk Assessment

### **Hazard**: Moving parts of the robot arm.

**Description**: Getting hair trapped or fingers caught in movements of the arm.

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

**Mitigation**: Keep back from the arm while movements are happening.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-12-20 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-05 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2019-12-26 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2020-01-27 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk), **Check 2**: 2021-01-22 - Grace Exley (gae23@cam.ac.uk)