NPC Generator
Julian Fechner

## Highlights
Hello! This is an npc generator I created for all of your npc needs! It generates npcs for you with random attributes. You may choose how many you would like to generate as well, but it must be over 10.

## Overview

My name is Julian and I made this generator for roleplay/openworld games. The attributes that will be generated with the npc's are specifically designed for those kinds of games. The attributes that come with the npc's are:
- Gender
- Style
- Age
- Race
- Name

As you can see, those are the kinds of attributes that differentiate the npc's in openworld games. 

## How it works

When starting the code, you will be greeted with a main menu. You may choose to continue to the generator or type help to see a sentence or two that will hopefully answer whatever questions you may have. Once you continue, you will input the amount of npcs you would like to generate. After that a final statement will be printed with the attributes of all the npcs you asked for. And that's it! 

## Technical details

1. When on the main menu section you have two options:
    - Type continue 
    - Type help
If this doesn't work try again because you probably made a typo. Typing anything in wrong will restart the main menu.

2. Age is chosen between 1 and 90, not off of a list. I used: 
```py 
import random
random.randint(1, 90)
```
I feel like this covers babies to old people 

3. Gender is chosen randomly and a name is chosen based on the gender so don't worry about getting a boy's name for a girl

4. Generator will not work if any number under ten is printed. If you are upset about this, look on the bright side: You have more options to choose from. 


I hope this explanation helped and answered any questions you may have had. 

Thank you! 
Julian Fechner



