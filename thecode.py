#Main menu section
import time
main_menu = ""
while main_menu != "help" or "continue": 
    print("Hello, welcome to the npc generator, a generator for all your npc needs")
    time.sleep(1)
    main_menu = input("Welcome to the main menu, for any questions \ntype help, to continue on to making your npc type continue: ")
    if main_menu == "help":
        print("Welcome to the help forum, we hope this will answer any questions you have")
        print()
        time.sleep(1)
        print("This npc generator will allow you to customize the attributes of your npc, or make a random one")
        time.sleep(4)
        print()
        print("You will not be able to see a physical copy of your npcs, just what their attributes are. \n You must make at least ten")
        time.sleep(4)
        print()
        print("We hope this answered all of your questions about this generator")
        help_input = input("Type continue to continue to the generator: ")
    elif main_menu == "continue":
        break 

#Generator section
print("Welcome to the Generator section")
time.sleep(1)
amount_y_or_n = ""
amount = int(input("How many npcs would you like to generate? Must be at least ten: "))
while amount_y_or_n != "yes" or "no":
    print(f"You are generating {amount} npcs")
    amount_y_or_n = input("Is this number correct? ")
    if amount_y_or_n == "yes" and amount >=  10:
        print("Moving on to the next step")
        break
    elif amount_y_or_n == "no":
        amount = int(input("Please type in another number (at least 10) "))
    else:
        print("Sorry this number is invalid")
        time.sleep(1)
        amount = int(input("Please type in a number that is at least 10: "))

 #naming section  

listofnames = []

for name in range(amount):
   namesofnpcs = str(input("Name of npc: "))
   listofnames.append(namesofnpcs)

#Color section
import random
color = []
randomcolorchoice = 0
randomcolorlist = ["Red", "Orange", "Green", "Blue","Yellow", "Indigo", "Violet", "Pink", "Cyan"]
colorchoice = input("What color would you like your npc to be? you may choose a color or leave it to choice.\ntype choice to choose a color for all of your npcs or type random to leave it up to chance ")
if colorchoice == "choice":
    whatcolor = input("What color? ")
    color.append(whatcolor)
elif colorchoice == "random":
    randomcolorchoice = random.choice(randomcolorlist)
    print(f"Your color is {randomcolorchoice}")
time.sleep(1)
print("The rest of your npc's characteristics will be auto generated and then printed to you")
time.sleep(1)
#Height section
heightchoices = ["5'10", "5'11", "6'0", "6'1", "6'2", "6'5" "6'7", "6'9", "5'3", "5'4", "5'7", "5'5", "5'1", "4'11", "4'10", "2'2", "0'5", "5'10", "5'11", "6'0", "6'1", "6'2", "6'5" "6'7", "6'9", "5'3", "5'4", "5'7", "5'5", "5'1", "4'11", "4'10", "2'2", "0'5"]
height = random.choice(heightchoices)

#style section t or f
stylechoices1 = ["Cool", "Grunge", "Elegant", "Casual"]
stylechoice2 = ["Emo", "Serious", "Preppy", "Chill"]
styleselected = 0
stylehelp = int(input("To influence your npc a little type any postiive number "))
if stylehelp%2 == 0:
    styleselected = random.choice(stylechoices1)
elif stylehelp%2 == 1:
    styleselected = random.choice(stylechoice2)
    

