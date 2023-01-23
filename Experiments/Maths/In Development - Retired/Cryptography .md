# Cryptography 

**Learn about codes and ciphers** - Learn about codes and ciphers through a selection of demonstrations of different methods using whiteboards and padlocks. 

Last initially checked on 2022-02-09 by Joshan Parmar (jp862@cam.ac.uk) and double-checked on 2022-02-09 by Sian Boughton (seb216@cam.ac.uk)

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Standard** (A standard CHaOS experiment, useable for all hands-on events.)

**Computer Science**

**In development** (This experiment doesn't actually exist yet, but might in the future!)
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- Morse code
- Morse buzzer and clicker
- Morse code chart
- 
- Semaphore Flags (2 per transmitter)
- Semaphore Sheet
- 
- Paper Telephones and Envelopes
- Two paper cups connected by string
- Third paper cup on a string
- Some envelopes
- 
- Ceaser Shifts
- Whiteboards and pens
- Laminated alphabet wheels
- Laminated alphabets
- 
- Wrap around codes
- Sections of pipe insulation
- Code strips
- 
- Asymetric Encryption
- Two padlocks with keys
- Box with two padlock holes
- 
- Public key encryprion
- Padlock with key (needs to lock without key)
- Box with at least one padlock hole
- Two led lights
- Transparent plastic cups
- Food colouring
- Water
- 
- Quantum Cryptography
- Polarisation Experiment with extra filters
- 
- Pollard's Kangaroo
- Kruskal's Count Experiment

<br/>

## Experiment Explanation 

Firstly this is a large selection of small demos, each one is relatively fun and some link together well. They start of relatively easy however some of the demos at the end are really quite hard.

The main thing you'll get confused about is this technicality 
Code - converts whole words
Cipher - acts letter by letter
This means lots of things we call codes are ciphers! 

Morse 'code' 
Press down and make a buzz, using the translation table you can transmit messages. Get one person to transmit and the others to try and transcribe the message.
Most competent transmitters can manage 40 words per minute and the record is 75.2wpm. As words and characters have different lengths this is just an average though.

Semaphore
Display the flags in the patterns for each letter. Similarly to Morse one group transmits and one transcribes. It was used pre-telegraph and Morse code to transmit messages long distance, using towers and spyglasses to relay messages faster than horse and rider. You can easily split the groups with one transmitting Morse and receiving semaphore and vice versa. 

Paper Telephones and Envelopes 
These phones allow you to communicate like a telephone, it works by vibrating the string to transmit. If you loop on the third cup there's now an eves dropper (a wire tap). This transmission is not secure due to this.
Similarly if two people pass envelopes between a third postman they can communicate. However the postman can open letters, or even just change them. 
We can think about what properties we want when sending messages there are a few contenders.
Confidentiality - only the person meant to receive the message does. 
Integrity - the message has not been altered in sending. 
Authenticity - the message comes from the right person. 
How can we fix these? Let people come up with ideas.
Seal envelopes to make it harder to open and close. Sign letters. Talk in code/cipher.

Caesar Shifts
These are named after Julius Caesar even though they've existed long before. They work by rotating the alphabet and replacing letters like this. The code wheels are very useful to do this, they can do both the encryption and decryption. This code is really easy to break, there's only 26 options so we just have to try a few, you can even get people to do this. Just by trying a few letters you can decide to move on and try the next rotation, it's very unlikely the message starts 'zm'.
This encryption sees only one common use, since it's so insecure it's mainly used for spoilers. They use a form called ROT13 which rotates 13 places, try it and try encrypting something twice! You'll find it's self inverting which saves on code.
In these for someone else to decrypt they just need to know the number you've rotated by. 
Because it's so simple one way to add complexity is by also agreeing a word, write this under the start of the alphabet and then write out the remaining letters in order. This makes it harder for someone to guess as they need to get your word.
Can we still break this code? Yes quite easily, write a long message in English, count up how many times each letter appears, are they all equal? Which letters appear most often? If we find these in a long coded message we can see which letter is most common and try and match them up. E, T, A and O are the most common, while Z, Q and X are rarest. We can also do this looking at pairs and find TH, ER, ON, and AN are the most common pairs of letters (termed bigrams or digraphs), and SS, EE, TT, and FF are the most common repeated letters.

Wrap around codes (I can't remember the name) Scytale
These codes are written on strips of paper to read them you need to wrap them around a piece of pipe insulation and read downwards. The hidden key is the diameter of the insulation, try a different size and the message doesn't make sense. 

Key Exchange

In this section, we'll look at sharing information between two people Alice and Bob. They want to pass messages to each other without them being read by their nosy friend Eve. We've got a box they can post messages between them in as well as an assortment of padlocks and keys, ask the children how they might send a message between them? You can act as the post, taking things between them, but also as Eve, reading and copying all the post they send.

The simplest way is having one padlock and giving Alice and Bob each a key that opens it. This works well but imagine Alice and Bob live on opposite sides of the world and can't meet in person? How can they both get a copy of this key? Whenever you're using the internet you need to do frequent key exchanges, if you're making a payment you need to send that information to the company, but don't want anyone else stealing your bank information, you need to exchange keys.

The next idea might be for Alice to post a key to Bob however if Alice puts a key in the post, Eve can intercept it and copy it. Now Alice, Bob and Eve all have keys so it isn't secure and everything is ruined. You'll have to think of ways to pass the boxes so Eve can't open them.

One way to exchange is as follows, each person has their own padlock and key. Person A wants to send a message to B, do so they follow this process:
• They lock the message in a box using their own padlock and send it to B,
• B receives the box but can't open it as they don't have A's key, they padlock it with their own lock and send it back to A,
• A now can't open it either but they unlock their padlock and send it back to B,
• B can now open the box and read the message.

This system is a private key system, with both keys and padlocks only known to A and B. In modern cryptography, lots of systems rely on public keys, these allow individuals to be able to send messages easily as to send a message to A you get A's public key (an unlocked padlock with no key) you then lock this and send it A. A is the only person with the key so only A can open it.

In public-key cryptography, keys are often exchanged using ElGammel or Diffie-Helmann, both of which work on a similar "double-lock" process. The process given above is actually insecure and vulnerable to a man-in-the-middle attack in a public key system, for this example it can be broken as follows:
• E intercepts the box A sends (box 1) to B, 
• E copies the box (which will be empty a E doesn't know the contents and B can't open) to get box 2 which she padlocks sends to B,
• B padlocks the fake box 2 and returns it,
• E intercepts box 2, then adds her padlock to box 1 and returns this to A, 
• A receives box 1, removes his padlock then sends to B. 
• E intercepts box 1 and views the contents,
• E creates a new box 3 with the contents and locks this with B's padlock (as padlocks are public keys)

One can create a valid model for Diffie-Helmann using lights. Optionally place the two led lights under the cups for darkroom use. Make up a private key which will be your own special colour. Between you make a public key which you can show everyone. Each take equal amounts of public and private keys and mix, you can share this with Eve while passing it between you. Then to the swapped colours add a shot of your private key to the new mixture. You'll find there's now a shot of each private key and a shot of public key in both A and B's mixture however E can't recreate it as she's only seen the following mixtures: public key, public+A private, public+B private. Any mix of these is going to have too much public key in! This works best if the colours are all different and very light, otherwise you end up with black as your secret colour and its hard to show eve not getting it (they've not got the same shade of black but its hard to tell). 

One more modern encryption scheme is RSA, this is also an asymmetric scheme. Its a public key scheme, a public key here is an unlocked padlock which we leave them with a central repository, anyone wanting to send A a message goes and gets an unlocked A padlock uses it to seal the message to A and then only A can unlock it. There is one weakness with this, if the person in the repository is dodgy then they can read all messages, they give out their own padlocks, open the message then attach the correct padlock.

RSA (PLUS)
For really competent groups who've probably already seen group theory you can go into detail of how RSA actually works. It's quite complicated though. You can link in Hexaflexagons to solve some equations.

Quantum Cryptography (PLUS)
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

Pollard's Kangaroo (PLUS)
http://faculty.uml.edu/rmontenegro/research/kruskal\_count/kangaroo.html
So you can solve some discrete log stuff (which is used in DiffieHelam and ElGammel) using basically Kruskal's count with some fancy number theory rules...

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

**Mitigation**: Make sure power is low (i.e. small battery) and people don't try and make connection using a finger.

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

**Mitigation**: Ensure padlocks not messed with

**After Mitigation**: Likelihood: 2, Severity: 2, Overall: 4

<br/>

## Risk Assessment Check History 

**Check 1**: 2018-12-12 - Matthew Le Maitre (msl54@cam.ac.uk), **Check 2**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk)

**Check 1**: 2020-02-04 - Esmae Jemima Woods (ejw89@cam.ac.uk), **Check 2**: 2020-02-04 - Beatrix Huissoon (beh37@cam.ac.uk)

**Check 1**: 2021-01-17 - Sian Boughton (seb216@cam.ac.uk), **Check 2**: 2021-01-22 - Polly Hooton (prh43@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Sian Boughton (seb216@cam.ac.uk)