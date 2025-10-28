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
colors = []

print("Moving on to the next step: Color")
singleorall= input("What color would you like your npcs to be? You may choose to make the mass of them \n one color or make them each a random color indiividually \n please type all to customize all of them at once or single for individual \n customization: ")
if singleorall == "single":
    print("You have selected single")
    for color in range(amount):
        colorinput = input("What color would you like your npc to be? ")
        colors.append(colorinput)
elif singleorall == "all":
    print("You have selected all")
    colorinput= input("What color would you like all your npcs to be? ")
    colors.append(colorinput)

