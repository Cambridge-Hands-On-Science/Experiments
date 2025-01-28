# Cryptography 

**Learn about codes and ciphers** - Learn about codes and ciphers through a selection of demonstrations of different methods using whiteboards and padlocks. 

Last initially checked on 2025-01-27 by Rowan Ong (rzmo2@cantab.ac.uk) and double-checked on 

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
X before item indicates it is not currently in the kit and needs sourcing

Morse Code
- Morse code clicker with buzzer and LED (need to keep horizontal for buzzer to work)
- Laminated morse code chart

Semaphore
- 4 Paper Semaphore Flags on wooden sticks (2 per transmitter)
- Laminated Semaphore Sheet

Paper Telephones and Envelopes
- Two paper cups connected by string
- Third paper cup on a string
- Some envelopes

Ceaser Shifts
- X Whiteboards and pens
- Laminated alphabet wheels

Scytale
- Wrap around code strips (if more needed-excel spreadsheet on Github-under images in CompSci folder)
- Sections of pipe insulation

Asymetric Encryption (PLUS)
- X Two padlocks with keys
- X Box with two padlock holes

Public key encryption (PLUS)
- X 2 Padlocks with key (which needs a key to lock)
-  X Padlock with key (which locks WITHOUT a key)
- X Box with at least one padlock hole

Diffie-Helmann
- Two led lights
- X Transparent plastic cups
- X Food colouring (there is some but it's expired)
- Water

Quantum Cryptography (PLUS)
- x Polarisation Experiment with extra filters
- x Pollard's Kangaroo
- x Kruskal's Count Experiment

<br/>

## Experiment Explanation 

Firstly this is a large selection of small demos, each one is relatively fun and some link together well. They start off relatively easy however some of the demos at the end are really quite hard.

The main thing you'll get confused about is this technicality 

Code - converts whole words

Cipher - acts letter by letter

This means lots of things we call codes are ciphers! 

#### Morse 'code' (actually a cipher)
Press down on the morse code clicker (which should be connected to the buzzer) and make a buzz, using the morse code translation table you can transmit messages. Get one person to transmit and the others to try and transcribe the message.
The clicker conrols a buzzer and an LED at the same time (though if the buzzer is getting annoying, the circular switch turns it off so only the LED is triggered).

Most competent transmitters can manage 40 words per minute and the record is 75.2wpm. However as words and characters have different lengths this is just an average!

#### Semaphore
Display the flags in the patterns for each letter. Similarly to Morse one group transmits and one transcribes. Semaphore was used pre-telegraph and Morse code to transmit messages long distance, using towers and spyglasses to relay messages faster than horse and rider. You can easily split the groups into two, with one group transmitting Morse and receiving semaphore, and vice versa.

#### Paper Telephones and Envelopes 
These phones allow you to communicate like a telephone, it works by vibrating the string to transmit. If you loop on the third cup to the first two, there's now an eavesdropper (a wire tap)!!. Therefore you can see that this transmission is not secure.

Similarly if two people pass envelopes between a third postman they can communicate. However the postman can open and read letters, or even change them completely. This isn't a secure transmission either.

Try both of these ideas out.

We can think about what properties we want when sending messages - there are a few contenders:

Confidentiality - only the person meant to receive the message does. 

Integrity - the message has not been altered in sending. 

Authenticity - the message comes from the right person. 

How can we fix these? Let people come up with ideas.

Some ideas for discussion: Seal envelopes to make it harder to open and close. Sign letters. Talk in code/cipher.

#### Caesar Shifts
These are named after Julius Caesar even though they've existed long before him. They work by rotating the alphabet by a certain amount and replacing letters like this. The code wheels are very useful to do this, they can do both the encryption and decryption. This code is really easy to break, as there are only 26 options for the code, so we just have to try a few. You can even get people to try this. Just by trying a few letters you can decide to move on and try the next rotation, e.g. it's very unlikely the message starts 'zm'.

This encryption sees only one common use, since it's so insecure it's mainly used for spoilers (security vunerability on CPU). 

Spoilers commonly use a form called ROT13 which rotates 13 places, try it and try encrypting something twice! You'll find it's self inverting which saves on code. I.e. you decode the message by doing the same thing as encoding it!

In a generic caesar shift, for someone else to decrypt it they just need to know the number you've rotated by. 
Because it's so simple, one way to add complexity is by also agreeing a word, write this under the start of the alphabet and then write out the remaining letters of the alphabet which haven't been used in the word in order. This makes it harder for someone to decode your message, as there are many more options for the encryption - they need to guess your word.

Can we still break this code? Yes, quite easily, write a long message in English, count up how many times each letter appears, are they all equal? Which letters appear most often? If we find these in a long coded message we can see which letter is most common and try and match them up. E, T, A and O are the most common, while Z, Q and X are rarest. We can also do this looking at pairs and find TH, ER, ON, and AN are the most common pairs of letters (termed bigrams or digraphs), and SS, EE, TT, and FF are the most common repeated letters.

Split the kids into two teams, get one to encode a word, and the other to try and decode it (with both knowing the rotation number).

#### Scytale - wrap around codes
These codes are written on strips of paper. To read them you need to wrap them around a piece of pipe insulation and read downwards. The hidden key is the diameter (width) of the insulation, only one diameter will give the message, the other diameters will give nonsense.

Get the kids to try wrapping the strips around the different cylinders, get them to guess which strip matches with which tube and what the encrypted word on each is.

The 38mm tube says CAKES (or both CAKES and SMILE), the 62mm tube says GOAT and the 68mm tube says DUCK.

## Advanced Experiments (missing equipment for it-so NOT IN USE)
#### Key Exchange (becomes a bit harder from now on)

In this section, we'll look at sharing information between two people Alice and Bob. They want to pass messages to each other without them being read by their nosy friend Eve the Eavesdropper. We've got a box they can post messages between them in as well as an assortment of padlocks and keys, ask the children how they might send a message between them? You can act as the post, taking things between them, but also as Eve, reading and copying all the post they send in the box.

The simplest way is having one padlock and giving Alice and Bob each a key that opens it. This works well but imagine Alice and Bob live on opposite sides of the world and can't meet in person - how can they both get a copy of this key? Whenever you're using the internet you need to do frequent key exchanges. If you're making a payment you need to send that information to the company, but don't want anyone else stealing your bank information, so you need to exchange keys.

The next idea might be for Alice to post a key to Bob however if Alice puts a key in the post, Eve can intercept it and copy it. Now Alice, Bob and Eve all have keys so it isn't secure and everything is ruined. You'll have to think of ways to pass the boxes so Eve can't open them.

One way to exchange is as follows, each person has their own padlock and key. Person A wants to send a message to B, do so they follow this process:
- They lock the message in a box using their own padlock and send it to B,
- B receives the box but can't open it as they don't have A's key, they padlock it with their own lock and send it back to A,
- A now can't open it either but they unlock their padlock and send it back to B,
- B can now open the box and read the message.
This can be demonstrated using the padlocks which need keys to lock, and two groups.

This system is a private (asymmetric) key system, with both keys and padlocks only known to A and B. 

In modern cryptography, lots of systems rely on public keys. These allow individuals to be able to send messages easily, as to send a message to A you get A's public key (an unlocked padlock with no key) you then lock this and send it to A. A is the only person with the key so only A can open it, but anyone can send the messages (no guarentee of the origin of a message). 
This can be demonstrated using the padlock which doesn't need a key to lock (anyone can lock a message in a box, but only A can open the box to read it.


More complex bit:

In public-key cryptography, keys are often exchanged using ElGammel or Diffie-Helmann, both of which work on a similar "double-lock" process. The process given above is actually insecure and vulnerable to a man-in-the-middle attack in a public key system, for this example it can be broken as follows:
- E intercepts the box A sends (box 1) to B, 
- E copies the box (which will be empty as E doesn't know the contents and B can't open) to get box 2 which she padlocks sends to B,
- B padlocks the fake box 2 and returns it,
- E intercepts box 2, then adds her padlock to box 1 and returns this to A, 
- A receives box 1, removes his padlock then sends to B. 
- E intercepts box 1 and views the contents,
- E creates a new box 3 with the contents and locks this with B's padlock (as padlocks are public keys)

### Diffie-Helmann (PLUS-NOT IN USE)

One can create a valid model for Diffie-Helmann using lights. Optionally place the two led lights under the cups for darkroom use. Make up a private key which will be your own special colour. Between you make a public key which you can show everyone. Each take equal amounts of public and private keys and mix, you can share this with Eve while passing it between you. Then to the swapped colours add a shot of your private key to the new mixture. You'll find there's now a shot of each private key and a shot of public key in both A and B's mixture however E can't recreate it as she's only seen the following mixtures: public key, public+A private, public+B private. Any mix of these is going to have too much public key in! This works best if the colours are all different and very light, otherwise you end up with black as your secret colour and its hard to show Eve not getting it (they've not got the same shade of black but its hard to tell). 

One more modern encryption scheme is RSA, this is also an asymmetric scheme. Its a public key scheme, a public key here is an unlocked padlock which we leave them with a central repository, anyone wanting to send A a message goes and gets an unlocked A padlock uses it to seal the message to A and then only A can unlock it. There is one weakness with this, if the person in the repository is dodgy then they can read all messages, they give out their own padlocks, open the message then attach the correct padlock.

#### Quantum Cryptography (PLUS-NOT IN USE)
Digitally we encode using binary, we can represent this in any way punched holes, magnetism. However we've seen photons have a polarisation and we could use this.
Alice has a light and polarizer and Bob has a polarizer and screen. On the screen the difference in brightness should be apparent between the filters being aligned, off by 45 or opposite.
A simple way of transmitting messages is for Alice to rotate her filter horizontal for 0 and vertical for 1. Bob leaves his filter horizontal and can observe. This has all the same problems as paper telephones. You may wonder why polarisation is used, it turns out its a really robust property of photons.
Now we move onto the full quantum scheme, we need to set up some random shared information. Alice and Bob both flip coins to generate this. Alice picks a string of test bits to send. 
Alice flips her coin and heads mean she uses the convention before of horizontal 0 and vertical 1, tails means she rotates this by 45 degrees and diagonal is 0 and antidiagonal(135) is 1.
Bob sets his polarizer horizontal with a head and diagonal at tails.
Bob records as before however if its intermediate he flips a coin and records that. 
Alice then reads her coin toss results to Bob and anyone else that wants to listen in. Bob knows anytime he flipped the same he can trust what he saw (this should be roughly half the string) To check there's no eves dropper he confirms some of the successes with Alice, if they don't agree they've outed an eves dropper.
Eve to listen in needs a set up like Bob and then Alice. She tries to read Alice's message then re-transmit to Bob. So she needs to flip coins for both Alice and Bob. This means half the verification is expected to go wrong as she'll disagree. However anything that did get through can be used.
In real quantum you'd want to use single photons, this method is vulnerable to slightly dimming the light in the middle but this isn't possible for single photons. 
https://spookyactionbook.com/2016/04/12/demonstrate-quantum-encryption-with-a-flashlight-and-pair-of-sunglasses/


<br/>

## Risk Assessment

### **Hazard**: Paper

**Description**: Paper cuts

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: Make sure children don't get too over excited and call a first aider in the event of an incident.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Morse Code Buzzer

**Description**: Electrocution from Morse code buzzer

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 4, Overall: 8

**Mitigation**: Make sure power is low (i.e. small battery) and people don't try and make connection using a finger (especially not when wet).

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

### **Hazard**: Stick Flags

**Description**: Someone coild be poked by the sticks in the semaphore flags

**Affected People**: All

**Before Mitigation**: Likelihood: 2, Severity: 4, Overall: 8

**Mitigation**: Sand down the points on the flags, encourage people using them to be careful

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

### **Hazard**: Persons padlocked together.

**Description**: Persons padlocked together indefinitely.

**Affected People**: Public

**Before Mitigation**: Likelihood: 3, Severity: 4, Overall: 12

**Mitigation**: Make sure padlocks have working keys before use. Make sure kids don't mess with them.

**After Mitigation**: Likelihood: 1, Severity: 4, Overall: 4

<br/>

### **Hazard**: Padlock.

**Description**: Fingers caught in padlock.

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: Ensure padlocks not messed with: keep hold of them when not being used.

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-12-12 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2020-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2020-02-04 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2021-01-17 - Sian Boughton (seb216@cam.ac.uk), **Check 2**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Sian Boughton (seb216@cam.ac.uk)

**Check 1**: 2024-02-15 - Peter Methley (pm631@cam.ac.uk), **Check 2**: 2024-02-15 - Isobel Gilham (ig419@cam.ac.uk)

**Check 1**: 2025-01-27 - Rowan Ong (rzmo2@cantab.ac.uk), **Check 2**:


