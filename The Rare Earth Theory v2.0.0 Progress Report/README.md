# The Rare Earth Theory v2.0.0

Hello everyone,

It has been almost two whole months since this project started. It has taken significantly more time than I expected. I anticipated this game to finish maybe by the end of february so I can pursue a different project involving robotics this time so I can put python into its intended use instead of making a video game off it. However, I am currently in junior high school, and the exams and assignments matter significantly towards university. Also, I am very committed to the gym, and coupled by the fact that I live in a dormitory, it leaves me with little time to work on this project other than the weekends.

However, I am very proud to say that I have made progress on the game, and I am a little proud that a small spark of interest back during winter break has still been continuing to this day, as most people’s passion dies out easily within such a span.

I am happy to announce that I am around half way finished with the project. Here is what I have been working on.

---

## Graphical User Interface

As promised in the last version of the game, a graphical user interface has now been implemented using Pygame. A screen is created with pygame.display, and from there I can set it to any image that I load. This allows a background image to be displayed, although it does not yet support placing regular images onto specific positions of the screen in a flexible way.

To solve this, I created a class called Button in a separate file named TRETStar. Inside the class, I defined functions such as draw(self, surface), which include mouse logic that checks the mouse position and whether the image is being clicked. This allows any image to function as a button by using that built in mouse detection to trigger actions.

Using this system, I was able to create a main menu. The texts were generated using a website named CoolFontGenerator, and the letters drop from the top of the screen for visual effect. The Start button begins the game, while the Exit button closes it.

---

## Choosing the Temperature of the Star

After clicking Start, the player must enter the temperature of their star by typing it in the box. The allowed range is 2,000 K to 50,000 K. While certain stars such as WR 102 can go beyond 200,000 K, main sequence stars generally fall within this range. These limits were intentionally chosen to make sure that every category in the Harvard spectral classification system can be chosen.

To make the temperature input feel more interactive, I added a function called StarTempRGB(t) that changes the color of the number inside the input box based on the temperature the player types. In other words, the star temperature text itself becomes a visual indicator of heat. Cooler temperatures appear more orange, and as the value approaches 50,000 K, the text shifts toward a deeper, hotter looking red. This creates a smooth gradient effect that makes the input screen feel more alive and readable at a glance.

The player does not directly choose the star’s radius. Instead, the radius is calculated programmatically. Each spectral class is assigned a constant that represents the average stellar size in that category relative to the Sun. The system then multiplies this constant by the star’s temperature relative to the minimum and maximum temperatures of its spectral class.

For example, if a player selects 4,500 K, the system identifies the star as a K-type star using the Star class in TRETStar.py. K-type stars range approximately from 3,500 K to 5,000 K. The midpoint of that range is used as a reference, and the class constant for K-type stars, which is 0.8, is multiplied. While this method is not necessarily scientifically accurate, the constants were chosen to attempt to make the stellar sizes as accurate as possible. Most of the scientific accuracy in this game will likely come from the physical equations that will be introduced later in development.

Finally, each spectral type also has its own visual design. The color of the star dynamically changes based on the temperature entered by the player. That's about it… nothing special, really. Just a static image.

---

## Planet placement and the habitable zone

After the player selects a temperature within the acceptable range, a new screen appears displaying the chosen star at the center, surrounded by a green ring. This green ring represents the habitable zone.

For visual consistency, the outer boundary of the habitable zone is always fixed at a radius of 150 pixels. Due to this, the apparent size of the star must be adjusted relative to that boundary. This is why in the game, M-type stars appear larger than O-type stars in the game. In reality, O-type stars are astronomically larger than M-type stars. However, since O-type stars would have habitable zones located extremely far away (or any star for that matter), scaling everything proportionally would make the star itself nearly invisible on screen. To avoid this, scaling constants were chosen for each spectral class to control how large the star appears visually. Yes, they are also arbitrary numbers, but I made sure that the fundamental scaling are still accurate.

The habitable zone itself is determined using the star’s relative luminosity. Luminosity follows the Stefan–Boltzmann relationship:

L ∝ R²T⁴

For our game, the star’s radius and temperature are taken relative to the Sun, which is rounded up to 5,800 K. The calculated relative luminosity, Lrel, is then used to estimate the habitable zone boundaries.

The inner and outer limits of the habitable zone are derived by multiplying Lrel by 0.75 for the cooler boundary and 1.25 for the hotter boundary. These values are simplified approximations used to create a reasonable visual range rather than a strictly precise astrophysical model.

Because the outer boundary is always fixed at 150 pixels, what changes visually is the inner boundary of the habitable zone.

Once the player clicks anywhere within the green ring, a rocky planet is generated at that position and begins orbiting the star.

---

## Conclusion

To conclude, I believe this project will be completed in the near future. My goal is to finish it by the end of March, especially since I have spring break to put time into development.

(Anything beyond this point is completely useless information and just me talking about life and venting. Please feel free to skip to section 5 if you wish.)

To be honest, spring break has been far more boring than I anticipated. I expected to meet up with friends, but I never actually made plans, and now I find myself looking forward to summer instead. I thought there would be more to do, but there really is not. Hobbies like weight lifting take maybe a few hours of your day at most, and I want to put the rest of the day to use instead of rotting in bed.

Naturally, my first instinct when I arrived was to play video games, since I cannot play them while living in a dorm during the school trimester. However, I became bored after only a few days. To be honest, video games feel like something I am moving past, which is part of the reason I started working on projects like this in the first place.

I am already bored, and I already feel the urge to work on this project instead of doing anything else. Because of that, I expect to make significant progress during this break. I want to innovate… create something new. I believe this curiosity and urge to explore are what make humanity so great.

---

## Files

### The Rare Earth Theory v2.0.0 UNFINISHED.py
The main game file.

### TRETStar.py
Handles calculations related to star temperature, radius, luminosity, and habitable zone boundaries.

### TRETButton.py
Contains the Button class and manages interactive image based buttons.
