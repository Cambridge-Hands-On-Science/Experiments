# Evolution Games (PLUS only)

**Modelling Evolution by Game Theory** - Simulate populations and explore stable and unstable equilibrium by using Game Theory to model animal behaviour in sharing a food supply.  

Last initially checked on 2024-02-17 by Lauren Mason (llm34@cam.ac.uk) and double-checked on 

## Tags
<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->

**Evolution**

**Maths**

**Active** (Experiment has working equipment at the time of last update, and is available for events.)

**Demo only** (Demonstration type experiments and lectures, not suitable for assignment for standard events.)

**CHaOS+**
<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->

<br/>

## Equipment Needed 
- A selection of strategy cards with various bird pictures
- A whiteboard and pen (optional)
- Some lego brick success counters
- A photocopy of Chapter 5 of the Selfish Gene by Richard Dawkins (source of experiment)

<br/>

## Experiment Explanation 

Talk about people’s ideas about evolution. Try and say how most competition is in between members of the same species. Competition for mates etc. We can model that with maths.

Moles and blackbirds compete for worms; blackbirds and blackbirds compete for worms and everything else. Why don't blackbirds just kill off their competition (and eat them)? There's a risk attached to it, and it might end up help other animals to the detriment of the blackbirds.

A good example is that of elephants being hunted for their tusks. Those with larger tusks die, so tusk size decreases. (I introduced genes as parts of the DNA encoding some feature, you could go into more detail if you wanted.)

First, talk about how science works: we observe something and try and create a model of how it works. This can be linked nicely to Hand Model and Handy Engineering. It's often best to start with a simple model and add in more elements to improve it. That's what we do here for evolution. You could ask why they think a game is a good model for evolution/whether they think it's a good model. Some people win (propagate genes), there's the element of chance, making decisions/moves etc. Thankfully the mathematical and normal notion of games match well.

Give everyone 10 Lego/Duplo bricks; these are a measure of how 'successful' you have been at life. The game works by two people in the population 'randomly' meeting and competing over a resource (this could be a mate, food, nest). The resource is worth 5 blocks to whoever gets it, but only one can get it (no sharing). How can we decide who gets it? 

Two ways: we either have a fight (this is risky, as the loser will come out badly hurt so takes a -10), or we can have an argument/show off/staring contest (think peacocks with their tails over mates or pacing in circles in cats). The latter is risk free, but in the time it takes to do this we could have found the object of the competition elsewhere - so there's a -1 score for losing the display. If someone tries to fight you, you're able to run away so you don't get injured. If there is a fight/stare-off/display etc., then flip a coin or do rock-paper-scissors for who wins.

We consider individuals behaving in a very simple way. They are either an aggressive hawk or a peaceful dove (this is untrue as doves are aggressive, and unhelpful as this is inter-species competition...). Hawks always fight and never run away, whilst doves never fight and will just stare off or run away when challenged to a fight. 

We can now consider various different encounters...
- Between a hawk and a dove, it's obvious a hawk does well and a dove doesn't do badly.
- Between a dove and a dove, one gets a win and the other a slight loss. On average though across two fights both are in profit.
- Between a hawk and a hawk, one does well and one takes a massive loss. On average neither is doing too well.

You can now ask what would happen if...
- We had one hawk in lots of doves => the hawk would always win and the number of hawks would increase (they have lots of offspring).
- We had one dove in lots of hawks => slightly trickier as the dove would never win and would always score zero, but the hawks lose 2.5 points a fight on average, so the dove is actually winning by not suffering major injuries.

So from all hawks we're pushed towards more doves and all doves pushes towards more hawks. We can convince them this might have a stable point in the middle which both these push against. In fact it does when the population is 7/12 hawks and 5/12 doves. 

With 6 people you can simulate this using one of the random cards (explaining it's like half hawk half dove) this also leads into the idea of polymorphism, not that individuals are intrinsically a hawk but they sometimes decide to act like one.

Phase plane diagram
|->->->->->->->->->->!<-<-<-<-<-<-<-<-<-<-<-<-<-<-|
0%doves Stable 100%doves

Now they've seen a simple model ask them how they think you could change it, thinking about how they see animals and themselves behaving:

- You could vary the rewards, this only really shifts the equilibrium - we pick them with a reasonable weighting. In fact we can actually back calculate these numbers from observing populations too. Increasing penalty for wasting time favours hawks, who never waste time, whilst increasing the penalty for losing a fight favours doves for the same reason. Changing the win value is more complicated. We could also make these random but we can take the expectation and it turns out to be equivalent in the long run. We can observe this in populations of very venomous snakes - they're very unlikely to attack as the risks are high.

- We can introduce new strategies - ask them for ideas. The simpler the better (we don't want to make our model too complicated). The next ones we normally consider are conditional strategists. They make decisions based on what the other person is doing. For example the retaliator stares off like a dove against a dove and fights like a hawk if fought against. Strategies like retaliator and prober-retaliator form a (nearly) Evolutionary Stable Strategy (ESS). They're vulnerable to slight invasions by each other and doves, and we get a polymorphism between them.

- We can also "break the symmetry" of the game. So far all fights are 50-50 who wins, but in reality this is really not the case. Some members of the species are bigger, more experienced fighters or are in home territory giving them an advantage in the fight. The idea of "bigger animal acts like a hawk, smaller a dove" is a stable strategy. Weirdly so is the reverse "smaller acts like a hawk, bigger like a dove" as anyone who chooses to break it is going to end up in lots of fights. Mexican Social Spiders are a species stuck in one of these paradoxical strategies, "if your nest is invaded, act like a dove; if you're invading, act like a hawk". One invasion leads to many, which is very costly. However, the risk of fighting manages to outweigh it in this species. Also rewards might be worth different amounts to different individuals: older ones might take more risks as they have less to lose, but if you have a large stash of food you're less likely to risk much on getting more.

- Memory. Crickets have past memory but can't identify individuals. They remember how well they've done previously and rank themselves on this (I lose 30% of fights). Monkeys can start doing individual rankings, I always lose to Frank, and Phil always runs away. This gives you ideas of what strategy other players are using.

We can work out optimal values for these games too. At the simple equilibrium in the original game on average everyone gets 0.625 points/encounter. We can now talk conspiracy theories. If everyone agreed to be a dove they'd average a reward of 1.5 which is much better, however individuals have no incentive to stick to it - become a hawk in this group and they rake in the points. "Stable not because it's good for the individuals within but because it's immune to treachery". (There are actually even better conspiracies to have)

If we want somewhere to go next we can go for wars of attrition. Like an auction but all bidders pay their bid and only the highest bidder gets the item. E.g. staring competition for a piece of food, both waste time staring and the loser gets nothing. Lots of things are unstable. An animal that values how much a piece of food is worth, stares as for as long as it thinks the food's worth, then gives up is outdone by someone who stares a second longer than the food is worth staring for. If you're not going to win ever you might as well never try so max bid population infiltrated by immediate quitters, then infiltrated by people who wait a second longer etc.

Imagine there was an indication you might give up, e.g. a whisker flicker when you'll give up in a minute. The strategy where you continued as you would but as soon as your opponent's whisker flickered you wait 61 seconds is optimal, but if you're going to give up in a minute and they haven't flickered it's best to give up sooner (without flicking your whiskers!) because you weren't going to win. Hence evolution of the poker face. Lying is unstable. Imagine people sitting down if they were in for the long game - people would give up if their opponent sat down, then liars emerge who sit down anyway, the people emerge to call the bluff. Lies and truth both unstable.

There's also competition inter species. A lion wants to eat an antelope. An antelope would prefer to not be eaten by a lion. These are mutually incompatible. Obviously lions could instead try to eat other lions but there's no much risk of retaliation. Antelopes don't fight back as it's too risky to attack the lion so they try and improve their running away. This is really just an example of (a rather large) asymmetry in participants.

There are often questions which actually highlight the one major flaw in this model. Humans are actually very bad at following it. There are various good examples in the Public Goods Game, Ultimatum game, Dictator (Trust) 'game' which give very counter intuitive results.


<br/>

## Risk Assessment

### **Hazard**: Duplo/Lego/Coins

**Description**: Children swallowing Duplo or Lego pieces, choking hazard.

**Affected People**: Public

**Before Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

**Mitigation**: The Duplo pieces should be sufficiently large to discourage swallowing. Do not use Lego with very small children and keep a close eye on the box of Lego. This experiment is designed for CHaOS+ (i.e. 16+), so the risk of participants trying to eat the experiment should, hopefully, be very slim anyway when used for this.
Call first aider if child swallows, if choking encourage child to cough. If the situation gets worse, i.e. child is suffocating and unable to cough the object out, call an ambulance immediately

**After Mitigation**: Likelihood: 1, Severity: 5, Overall: 5

<br/>

### **Hazard**: Duplo/Lego

**Description**: People falling/slipping on dropped pieces of Lego/Duplo

**Affected People**: All

**Before Mitigation**: Likelihood: 3, Severity: 2, Overall: 6

**Mitigation**: The pieces should be large enough that they don't present a large slip hazard. Be careful to keep pieces on the table and pick up anything that is dropped. Only use as many pieces as you need and keep the rest in the box.
Call a first aider in case of accident.

**After Mitigation**: Likelihood: 1, Severity: 2, Overall: 2

<br/>

### **Hazard**: Coins

**Description**: Tossed coins flying off and hitting someone.

**Affected People**: All

**Before Mitigation**: Likelihood: 1, Severity: 1, Overall: 1

**Mitigation**: Check you can flip a coin without losing control of it, otherwise just spin it on the table. It's perfectly fine to let the children toss the coin themselves, but make sure they're capable of doing it safely with a trial flip first.
In case of injury call first aider.

**After Mitigation**: Likelihood: 1, Severity: 1, Overall: 1

<br/>

## Risk Assessment Check History 

**Check 1**: 2016-12-07 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2017-02-06 - Mithuna Yoganathan (my332@cam.ac.uk)

**Check 1**: 2018-01-02 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2018-01-12 - Josh Garfinkel (jlg70@cam.ac.uk)

**Check 1**: 2019-01-01 - Thomas Webster (tw432@alumni.cam.ac.uk), **Check 2**: 2019-02-04 - Conor Cafolla (ctc43@cam.ac.uk)

**Check 1**: 2020-02-05 - Conor Cafolla (ctc43@cam.ac.uk), **Check 2**: 2020-02-05 - Grace Exley (gae23@cam.ac.uk)

**Check 1**: 2020-12-12 - Yian Aaron Koh (yak23@cam.ac.uk), **Check 2**: 2020-12-28 - Esmae Jemima Woods (ejw89@cam.ac.uk)

**Check 1**: 2022-02-09 - Joshan Parmar (jp862@cam.ac.uk), **Check 2**: 2022-02-09 - Margaret Johncock (mllyj2@cam.ac.uk)

**Check 1**: 2023-02-15 - Emma Crickmore (elc75@cam.ac.uk), **Check 2**: 2023-02-16 - Lauren Mason (llm34@cam.ac.uk)

**Check 1**: 2024-02-17 - Lauren Mason (llm34@cam.ac.uk),
