# The Rare Earth Theory v2.0.0 Complete

Hello everyone,

It has been a long two weeks or so. I only expected myself to be halfway finished by the end of spring break, but I ended up finishing the entire project before it even ended. I initially thought it wouldn't take that much time when I finished the progress report, but I was mistaken. Over the past 10 days, I put several hours into this project every single day. There would be days where the first thing I do when I wake up is open my computer to work on this project.

Hindsight is 20/20, and I realized that many aspects of the code are similar in nature, so it's not like I was discovering and using a new function every single line. Even though that meant I was using the same functions over and over again, it actually made things much easier. By the 3rd or 4th day, I didn’t even need to look back at my old projects to relearn how to use them. I could instantly tell what needed to be done to create a new function or make something work. It made me feel much more independent, and it really proves that practice makes progress.

Although Python is known as a beginner friendly coding language and it definitely lives up to that reputation, I’m still wondering why I chose to make a game with it. Python is usually used for things like robotics, automation, and programming hardware. It’s almost never used for video games because it’s not really designed for that, which makes it pretty unoptimal, especially considering how slow it can be. Because of this, the most pygame can really offer are 2D platformer type games. That still can be very impressive though. Developers like the YouTuber DaFluffyPotato make games that honestly have potential to be semi-popular on Steam. Still, pygame still cannot really handle proper 3D games, so you definitely cannot have your own GTA 6 in pygame.

To be fair, when you make a game using engines like Unity, Unreal Engine, or even Roblox Studio, they at least give you a 3D world and a camera system to start with. In pygame, you literally have to start by creating the screen yourself and defining your own dimensions. Even though Python has a lot of built in functions and sometimes almost feels like plain English instead of coding, making a game in pygame still felt like trying to make a chicken sandwich where I had to raise the chicken and grow the wheat myself first, instead of just going to the supermarket.

At the same time, I’m almost glad that I chose pygame. Since most pygame games are simple 2D projects and not something like Elden Ring level quality, it lowered the bar a lot for me. It made my game feel more justified as a first project, especially since it’s technically my very first real coding project and it's… Python.
Maybe I’m talking too much right now. Anyways, let’s take a look at the code.

---

## Planet orbit, Time Elapsed and Year length

After PlanetPlaceChooser, I made MainGame, which basically contains everything in the main game (wowzers). The first thing coded in MainGame is how fast the planet orbits the star. Originally, I had a whole system with research backing up how fast planets orbit stars. I looked into how long planets take to orbit depending on the size and mass of the star. Since my game doesn’t actually calculate star mass, I had to research ways to estimate mass using radius and similar values.

However, not only were those methods basically just educated guesses, but if I made the planets visibly orbit a star using realistic values, it would look way too slow in game. For bigger stars, the planet would basically not look like it’s moving at all, and for smaller stars it would be the opposite, where they are orbiting the star hundreds of times every second. I also considered adding arbitrary categories where certain temperature ranges would multiply the orbital speed so it would be visible, but that would make the speed look inconsistent depending on the star. P.S. I forgot to mention that I actually tried doing this, and yeah, it ended up being incredibly inconsistent. 

In the end, I just simplified it. The allowed star temperatures in the game range from 2000 K to 50000 K. I convert that range into a fraction so the orbital speed goes from a fastest orbit of 1 second to a slowest orbit of 10 seconds, depending on how hot the star is relative to that temperature range.

I also made it so time elapsed is tracked. This was slightly difficult to implement. The reason is that ```pygame.time.get_ticks()``` only works from the moment the program starts running, and there isn’t really a built-in way to start it later. Because of this, I had to find a way to measure how many milliseconds had passed between the start of the program and when MainGame actually begins. I solved this by introducing a variable called ```initialelapsedtime```. It starts as None, but right before MainGame begins, it gets set equal to ```pygame.time.get_ticks()``` at that exact moment. Then I subtract initialelapsedtime from the current ```pygame.time.get_ticks()```, which gives me how many milliseconds have passed since MainGame started.

Once elapsed time was working, I needed a way for MainGame to end, which happens when the star goes supernova. This is calculated using the fourth value stored in TRETStar, where I researched the approximate lifetimes of stars. Some stars, like M type stars, can last over 200 billion years, but that would make the game basically last forever, so I shortened it to 8 billion years for gameplay reasons. On the other hand, O and B type stars last less than a billion years. Because the game simulates about 10 million years every second, choosing one of those stars will make the star go supernova very quickly, sometimes within seconds. That is not necessarily ideal for gameplay, but it is realistically what would happen.

I also needed to visually show the elapsed time. I added images that indicate how many million years have passed. If the elapsed time reaches or exceeds 1000 million years, which equals one billion years, the image switches to display giga years instead.

Finally, YearLength was very easy to implement. The equation was written in TRETEquations.py by defining YearLengthCalculator, which calculates the orbital period using the planet’s distance in AU and the star’s luminosity relative to the Sun.

### Flaws and Limitations

The orbital period (and this year length) can be inaccurate. This is because the mass of the star can affect the gravitational pull it has through Kepler’s Third Law. Since the game does not calculate stellar mass directly and instead uses the sun’s mass as a reference to build simplified relationships based on temperature and luminosity, the orbital period ends up being an approximated guess.

Another flaw is stellar evolution. In reality, stars gradually become hotter and more luminous as they age. For example, the Sun is estimated to have been roughly 25 to 30 percent dimmer several billion years ago. This is why scientists theorize Venus could have been habitable for a short period of time. However, if I wanted to calculate this, I needed information regarding stellar mass, metallicity, and internal fusion processes. Due to this complexity and the lack of methods to find out all of this information, the game assumes that a star’s temperature and luminosity stay the same.

---

## Atmosphere

The atmosphere in this game consists of several major gases that are also common in planetary atmospheres. These include water vapor (H₂O), carbon dioxide (CO₂), methane (CH₄), molecular nitrogen (N₂), ammonia (NH₃), molecular oxygen (O₂), and molecular hydrogen (H₂). These gases are supplied mainly by asteroid and planetesimal impacts. This system will be explained in more detail later.

The game tracks the total atmospheric supply and uses it to determine what percentage of the atmosphere is made up of each gas. This allows the player to see the composition of the atmosphere, for example what percentage is carbon dioxide or water vapor.

When an atmosphere exists, greenhouse warming can occur. The greenhouse gases included in the game are carbon dioxide, methane, water vapor, and ammonia. In TRETEquations, the greenhouse effect is calculated using a logarithmic function:
```
math.log(1 + (1.0 * CO2 + 2.5 * CH4 + 0.8 * H2O + 2.0 * NH3))
```
Each gas is multiplied by a constant that represents how strongly it contributes to the greenhouse effect. These values are not exact scientific measurements. They are simplified approximations meant to reflect that methane and ammonia tend to be stronger greenhouse gases than carbon dioxide, while water vapor also plays a significant role.
The greenhouse value is then used together with stellar radiation to estimate the planet’s surface temperature. The formula is defined as PlanetTemp. Stellar radiation relative to the Sun is raised to the power of 0.25, which comes from the Stefan–Boltzmann relationship used in planetary equilibrium temperature calculations. 288 K represents Earth's average surface temperature. SR is the star’s radiation relative to the Sun, and Gg represents the calculated greenhouse strength. The ```(SR ** 0.25)``` term comes from the physics relationship between incoming radiation and equilibrium temperature, while the ```(1 + 0.2 * Gg)``` term is a simplified way to allow greenhouse gases to increase the planet’s temperature.

Finally, the game includes a simplified escape velocity model to determine whether certain gases can remain in the atmosphere. It is defined as EscapeVelocity. This uses Earth’s escape velocity of 11.2 km/s as a reference and scales it using the planet’s mass. This approximation attempts to account for the fact that more massive planets can retain lighter gases more easily, although the exact relationship is simplified.

### Flaws and Limitations

The greenhouse calculation is entirely arbitrary. The constants used for each gas are chosen for gameplay purposes rather than being derived from detailed atmospheric physics. It's really an attempt to make it seem realistic rather than making it scientifically accurate

Second, the model does not include the water vapor feedback effect. On real planets, when carbon dioxide raises global temperature, more water evaporates into the atmosphere. Since water vapor itself is a strong greenhouse gas, this amplifies the warming. Because this feedback loop is not included in the game, water vapor often stays near 0 percent unless the planet is already relatively hot.

Finally, the planet temperature model itself is highly simplified. Many real factors such as atmospheric pressure, cloud cover, albedo, and detailed radiative transfer are not included. While the system can produce accurate results in Earth like scenarios, such as a Sun like star at around 5800 K with a planet located in the middle of the habitable zone, the model is still only a rough approximation.

---

## H2O Logic and TRETH2OBehavior
Water is known as the essence, source, elixir, and even the medium of life. It is safe to say that water is absolutely necessary for life, at least on Earth. However, when it comes to extraterrestrial life, that is still speculative science. Life could theoretically use a different solvent, such as ammonia or even methane. Because of this uncertainty, I chose to make water necessary for life in my game.

Since the atmosphere system only includes water in vapor form, I made it so total H2O on a planet can instead exist in three states: ice, liquid water, and vapor. This makes it possible to create different types of planets, such as ice worlds, water worlds like Earth, and steam worlds like Venus. What determines how much water exists in each state is the planet’s temperature.

To model this, I used Earth as a rough reference by comparing how much colder or hotter different regions are relative to the global average temperature, such as the poles compared to the equator. I then created TRETH2OBehavior, which contains the functions ```H2OProximity```, ```H2OSimilarity```, and ```H2OSimilarityPercentage```.

Each state of H2O has a temperature range in which it can exist. I also introduced a MidRange, which is simply the midpoint of each temperature range. Using ```H2OProximity```, the game checks how close the planet’s temperature is to the midpoint of each H2O state. Based on this, it estimates how much of the planet’s total H2O supply exists as ice, liquid water, or vapor.

For ice, I used a range of -150°C to 30°C. Realistically, ice could exist all the way down to absolute zero, but if I allowed that, the midpoint would be far too cold compared to the temperatures players usually get in game, which are more around -10°C to 40°C. Because of that, I had to set a reasonable lower limit so the system would actually behave properly in gameplay.

The same idea applies to vapor, which uses a range of 25°C to 350°C. Even though pure water only boils at 100°C under standard pressure, Earth still has small amounts of water vapor in the atmosphere at temperatures far below that. Because of this, I needed vapor to begin appearing even on planets that are only somewhat hotter than Earth, instead of only on extremely hot planets.

```H2OSimilarity``` converts the proximity value into a similarity value. Its purpose is to make temperatures closer to the midpoint of a state give a higher score, while temperatures farther away give a lower score. If a given H2O state can exist at that temperature, the function returns a value based on how close the temperature is to that state’s midpoint. The closer it is, the smaller the proximity, and the closer the result gets to 1. If that state cannot exist at that temperature, it just returns 0.

Finally, ```H2OSimilarityPercentage``` converts the similarity values of ice, liquid water, and vapor into percentages. This allows the player to see what percentage of the planet’s total H2O supply exists in each state. Using this system, the game has slightly more complex requirements for life. For example, planets dominated by liquid water are much better suited for complex life, while ice worlds and steam worlds are much less favorable.

### Flaws and Limitations

One flaw is that the temperature ranges are arbitrary. They were chosen mainly so the mechanic would behave reasonably in gameplay, not because they perfectly represent real planetary science. Again, realism was prioritized over scientific accuracy here, which is not a good thing.

Another flaw is that water can still evaporate even when the temperature is far below its boiling point. The game just assumes that planetary conditions, especially atmospheric pressure, are suitable enough for some evaporation to occur. It basically comes with a starter pack full of Earth-like conditions. This is a simplification, since in reality the amount of evaporation depends heavily on pressure, humidity, and other environmental factors that the game does not calculate.

Finally, the model is only based on temperature. In reality, atmospheric pressure has a significant effect on water state. For example, liquid water can exist above 100°C if the pressure is high enough, and it can disappear at much lower temperatures if the pressure is too low. This is why blood will boil on Mars- the pressure is so low that even at cold temperatures it's enough for it to turn to gas. Since pressure is not fully modeled here, the water behavior is only an approximation rather than a fully realistic simulation. It is only assumed that the pressure is the exact same as Earth.

---

## Drawing Boxes

After that, there is a long repetition of RegularImage and DrawCoreBox. I’ll give one example:
```
       RegularImage(PlanetTempText)
       DrawCoreBox(0,f"{PlanetTemperatureCelsius:.3g}°C",60,20)
       RegularImage(BOX4)
```
This is used for the visual indicator of the planet’s temperature in the game. ```RegularImage``` is a function that creates a button, like in ```TRETButton.py```, but it is not actually used as a button unless I give it a function. So technically it is still a button object, but since it is only being used visually, it does not behave like a real button. ```RegularImage``` just makes whatever is inside the brackets appear on the screen.

In this case, ```PlanetTempText``` is defined like this:

```PlanetTempText = TRETButton.Button(80, 75, PlanetTempTextText, 0.20)```

Using ```TRETButton```, the values 80, 75 are the coordinates (x, y), ```PlanetTempTextText``` is the image file being used, and 0.20 is the image scale from 0 to 1.

After that, ```DrawCoreBox``` is basically a copy of what I used earlier when the player was choosing the star temperature, except now the box displays output text instead of user input. In this example, it displays ```f"{PlanetTemperatureCelsius:.3g}°C"```. The ```:.3g``` part rounds the value to 3 significant figures.

Finally, ```RegularImage(BOX4)``` is just the image used as the border or background for the text display box so it does not look ugly.

### Flaws and Limitations

I don’t know man there's so many boxes on the screen, and sometimes it just looks like a spreadsheet more than a simulation/game.

Also, ```RegularImage()``` is way too many times. It took up almost a hundred lines, and it's mostly copy paste.

---

## Asteroids and Planetesimals

When planets form, elements do not just appear out of nowhere. In my game, I made it so that asteroids and planetesimals bombard the planet and deliver materials to it over time. These impacts happen much more frequently early on, but the frequency decreases exponentially as time passes. Eventually, the probability becomes so small that it stabilizes at a minimum 1 percent chance every random 0.5 to 1.5 seconds. This was done to reflect how bombardment is much heavier in the early stages of a planet’s history and much less common later on.

Planetesimals are larger and rarer than asteroids. Their compositions are determined in ```TRETImpactObjects```, where I created categories such as rocky, icy, and carbon rich impactors. Each type contains different amounts of materials and gases that can be delivered to the planet. The total amount delivered is then scaled by the size of the asteroid or planetesimal, which is determined by a random number. For planetesimals, this size ranges from 3 to 5, while for asteroids it ranges from 1 to 5.

The game first checks whether enough time has passed since the last impact. Specifically, it checks if the current elapsed time is greater than the previous impact time by a random interval between 0.5 and 1.5 seconds. If that condition is met, the game rolls a random number to determine whether an asteroid or planetesimal hits the planet.

If a planetesimal hits, the planet’s mass increases by an amount proportional to the size of that planetesimal. The planet image is then recreated so that the change in planetary size is shown visually in the game. After that, the impact delivers atmospheric materials such as water, carbon dioxide, methane, nitrogen, ammonia, oxygen, and hydrogen. However, these gases are not all guaranteed to remain in the atmosphere. They are passed through the ```Retention``` function, which checks whether the planet is capable of holding onto them based on factors such as temperature, molar mass, escape velocity, and total atmosphere.

Asteroids work in almost the same way, but they increase planetary mass by a much smaller amount. Like planetesimals, they also deliver gases depending on their composition and size, and those gases are then tested through the same atmospheric retention system.

After each impact, the total atmosphere is recalculated by summing all the gases currently retained. Then, the percentage of each gas is calculated relative to the total atmosphere, allowing the player to see the atmospheric composition of the planet at any given time. This means the planet’s atmosphere is not static, but instead changes over time depending on the number, type, and size of impacts, as well as the planet’s ability to retain the delivered gases.

### Flaws and Limitations

A flaw is that the asteroid and planetesimal impacts happen only based on simple probability rather than being tied to a full planetary formation model. In reality, the rate of impacts depends on many factors like the structure of the protoplanetary disk, nearby planets, and gravitational interactions. The game instead uses random intervals and probabilities to approximate the general idea of early heavy bombardment followed by a slower rate of impacts. So yeah, this part is really just for gameplay purposes. Almost no science here, which is a shame.

Another flaw is that the composition of asteroids and planetesimals is simplified. In reality, they can have many different minerals and compounds, and their compositions can vary. In the game, they are grouped into only a few types such as rocky, icy, or carbon rich, which makes the system easier to implement and easy to program but very scientifically vague.

Also, the amount of mass added to the planet from impacts is also simplified. The game increases planetary mass using arbitrary scaling factors based on the size of the asteroid or planetesimal, rather than calculating mass from realistic densities, volumes, or impact energies. They add significant mass to the planet, almost as if an entire moon were hitting it. In reality, most asteroids barely change a planet’s mass. It was just a poor attempt to find a somewhat realistic way for the planet to “grow” and get bigger.

The atmospheric retention formula does take into account factors such as molar mass and escape velocity, which are real physical variables that influence whether gases remain in an atmosphere. However, the formula still uses Earth as a reference point and includes arbitrary scaling constants to produce values that behave realistically in the game rather than being scientifically accurate.

Another limitation is that the numerical amounts of gases delivered by asteroids and planetesimals do not represent real physical quantities. For example, values such as 0.005 units of CO₂ are not meant to correspond to actual masses or pressures. These values only exist to determine the relative proportions of gases in the atmosphere so that the game can calculate atmospheric composition as percentages. As a result, the numbers themselves do not have real physical meaning and are mainly used for gameplay calculations. They were originally going to have a purpose, but ended up having a change of heart once I realized how difficult it was going to be to make those values useful.

---

## Life Stage Classification

Finally, the most important part of my game; life. In my game, life is determined in ```TRETLife.py```, where the system checks the planet’s temperature, H₂O distribution, and probability. I chose probability to play a major role because, at the end of the day, the emergence of life is not guaranteed just because a planet is habitable. Earth itself needed many favorable conditions for life to appear and persist. Even after Earth became habitable, it still took a very long time for more complex life to evolve.

Because of this, I made life progression in the game depend not only on environmental conditions, but also on chance. This is especially true for advanced and intelligent life. Scientifically, intelligence is not simply random luck, but it is also not an inevitable outcome of evolution. Evolution does not aim toward intelligence. It only favors traits that help organisms survive and reproduce in a given environment. On Earth, oxygen producing photosynthesis eventually transformed the atmosphere, and major evolutionary transitions took billions of years. Even then, complex and intelligent life only emerged much later, which shows that habitable conditions alone are not enough.

In the game, I represent this uncertainty using probability. If a planet meets the environmental requirements for the next stage of life, there is still only a certain chance that life will actually progress to that stage. This was my way of reflecting that major evolutionary transitions are rare, slow, and dependent on many factors that are impossible to fully simulate in a simple game system.

The life stages in the game are: ```Habitable```, ```Single-Celled```, ```Multicellular```, ```Complex```, and ```Intelligent```. Each stage has its own requirements for temperature, ice percentage, liquid water percentage, vapor percentage, and probability of advancement. For example, more advanced stages require a narrower temperature range and a stronger dominance of liquid water, while extremely icy or vapor dominated planets are less favorable.

The code works by checking the next life stage only. If the planet’s temperature and H₂O distribution fall within the required ranges, the game rolls a random number. If that random number is below the required probability, the planet advances to the next stage. Otherwise, it stays where it is. This makes life progression gradual and uncertain instead of automatic.

I also made it so oxygen begins to appear once life emerges. This was done because oxygen on Earth is strongly linked to life, especially photosynthetic organisms. However, this is still a simplification, because not all life produces oxygen. Early Earth had life long before it had an oxygen rich atmosphere, and oxygen only became abundant after oxygen producing photosynthesis evolved.

### Flaws and Limitations

One flaw is that the probabilities for each life stage are arbitrary. They are not based on exact scientific values, because there is no reliable way to assign a real probability to the emergence of single celled, multicellular, complex, or intelligent life

Another limitation is that life is determined using only temperature, H₂O distribution, and probability. In reality, life would also depend on many other factors such as atmospheric composition, energy sources, planetary stability, chemistry, radiation, and time. The game ignores most of these for simplicity, and assumes photosynthesis is their main source of energy.

Also, intelligent life is assumed to be an evolutionary stage that comes after complex life. In reality, intelligent life exists within complex life, and intelligence is not a fixed goal of evolution. It's purely for progression in the game.

Finally, oxygen production is simplified. The game makes oxygen appear once life emerges, but in reality not all life produces oxygen, and Earth’s atmosphere remained oxygen poor for a very long time even after life already existed. This again is only possible with photosynthesis, and if life uses chemosynthesis as a main source of energy, this won't be possible.

---

## Supernova Event

Once the star reaches the end of its lifetime, the game enters the supernova event. At this point, the normal screen is replaced with a supernova image that rapidly increases in size, then sharply decelerates until it stops growing. This creates the effect of a sudden explosion that quickly expands and then settles.

To do this, the game first records the moment the supernova event begins using ```endelapsedtime```. It then measures how many milliseconds and seconds have passed since the event started. The growth of the supernova image is controlled using an exponential function:
```
       exponentialgrowtheffect = 1 - math.exp(-5 * endelapsedtimeseconds)
       SupernovaImageSizeConstant = 0.05 + 0.25 * exponentialgrowtheffect
```
This makes the image grow very quickly at first, then slow down more and more over time. The size is also capped at 0.3 so it does not keep growing forever. After calculating the size, the supernova image is drawn on the screen.
After 5 seconds, the supernova event ends and the game moves into the outro sequence. During the outro, the supernova image moves downward off screen. Once it has fully moved past the screen, the game resets all major variables and returns the player to the main menu.

This reset includes clearing planet related values such as mass, atmosphere, H₂O distribution, life stage, and impact counts. It also resets screen states like ```MainGame```, ```PlanetChooser```, and ```StarTempChooser```, so the next run starts from the beginning. At the same time, MainMenu becomes True, which allows the main menu title and buttons to move back in smoothly, creating a smooth transition from the end of the game, back to the beginning of the game. In a poetic sense, the death of a star can lead to a new beginning, where the player starts another playthrough.

---

### Conclusion

WOW. That was long. Over 4000 words. You can probably notice that there is a clear pattern of me sometimes getting too lazy to the point where I just stop even pasting the code that I am talking about. Even then, I hope you understood my process and code.

I think you can notice that, yeah, this game is flawed. Gameplay-wise, after you set your planet temperature, all you can do is wait for the supernova while you pray that intelligent life emerges out of pure luck. What am I trying to say? It's not fun. It's more of a simulation, but simulations are at least scientifically accurate, because that's their point. Mine isn't. Now that I think about it, I basically tried to recreate this universe into a Python game, which is way too ambitious. People will usually make games like the snake game or maybe a typing game for their first project, but I literally tried to make a universal sandbox or Space Engine in Pygame. It's way too ambitious… but to an extent it did kind of work. Yeah, it's scientifically inaccurate in SOOO MANY WAYS, and it's basically just a simulation that's not accurate. However, I think I was successful at making a retro fantasy style to it, with all the fonts and images.

It's weirdly difficult to make a game that's… fun. It's easy to imagine a fun game, but often it's either too simple, already made, or you just don't have the resources or skill required. Yeah, I want to play a game where you can do anything, like robbing cars or robbing banks, but I would need a whole team for that. Hell, Rockstar has been working on it for over a decade and they still haven't released it (GTA VI).
However, I am proud that I actually finished this project. I've had so many unfinished projects it's crazy. Every time I start a new project thinking this would be the one… just to end up failing, and getting saved by the hope of a new game in mind.

This game was fun to make. Coding is no longer a foreign concept to me, albeit I am still a beginner. I've always tried avoiding it knowing I'm terrible at it, but I've finally faced that fear. This is kind of a tragic tale, but just over two years ago, I started my Roblox development journey in hopes of making a game. I remember having this idea and a dream at an onsen hotel, where I remember writing my first Hello World in Luau. For two whole years I've avoided programming and just settled for only doing animation work or modelling work, and just yesterday, over two years later, I went to the same hotel… still as a beginner. In those two years I could have been a professional at programming, and honestly probably would have made a Roblox game that's played by many by now, but my fear and cowardice of learning programming hindered me and now I'm here, still a beginner… but I wasn't really that sad. I'm more surprised that even after two years my dreams to innovate still stood strong, and that I haven't given up. And this time around, I'm actually programming for real now.

The Rare Earth Theory was a fun project. I ended up making a simulation that fails to fulfill its purpose, which is to be scientifically accurate, but I'm still glad I finished it considering how I half expected myself to just quit halfway through. I'm glad I made it in Pygame, and it's time for me to try something new.

---
## Future projects

For my next project, I want to make a solar clock. The idea is a clock that shows the time on different planets or moons. I haven’t started it yet, but I’ll start very soon. I don’t think it will take too long… which is exactly what I said about this project, and it ended up taking three whole months with long breaks in between. Still, I don’t think this one will take that long, since time is already implemented in Python. I mainly need to convert it for other planets and decide how the system will work, including things like latitude and longitude. It will probably be more of a hardware challenge because I want to build an actual physical timer and display it using something like an Arduino Uno and digital displays.

After that, I will probably switch back to Luau and challenge Roblox development again. Yup, back to square one. It almost feels like it has been calling my name the entire time and I was just in denial. This time I want to focus on building mechanics that I am actually passionate about. If they turn out well, those systems could be reused to build many different games.

---
## Files

### The RareEarth Theory v2.py
 The main game file.
### TRETStar.py
 Handles calculations related to star temperature, radius, luminosity, and habitable zone boundaries.
### TRETButton.py
 Contains the Button class and manages interactive image based buttons.
### TRETEquations.py
 Handles calculations and equations for atmosphere, greenhouse effect, and year length.
### TRETImpactObjects.py
 Handles values such as the mass and elements delivered by asteroids and planetesimals.
### TRETH2OBehavior.py
 Handles calculations related to H₂O state distribution.
### TRETLife.py
 Handles calculations related to life progression.
### Image Files
Contains all the images required for the game to load properly.

---

#### “rage, rage against the dying of the light.”
##### - Dylan Thomas
