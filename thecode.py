#Main menu section
import time
main_menu = ""
while main_menu != "help" or "continue": 
    print("Hello, welcome to the npc generator, a generator for all your npc needs")
    time.sleep(1.01)
    main_menu = input("Welcome to the main menu, for any questions \ntype help, to continue on to making your npc type continue: ")
    if main_menu == "help":
        print("Welcome to the help forum, we hope this will answer any questions you have")
        print()
        time.sleep(1.01)
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

#lists for randomly generating
gender = ["Male", "Female"]
heightchoices = ["5'10", "5'11", "6'0", "6'1", "6'2", "6'5" "6'7", "6'9", "5'3", "5'4", "5'7", "5'5", "5'1", "4'11", "4'10", "2'2", "0'5", "5'10", "5'11", "6'0", "6'1", "6'2", "6'5" "6'7", "6'9", "5'3", "5'4", "5'7", "5'5", "5'1", "4'11", "4'10", "2'2", "0'5"]
randomracelist = ["White", "Spanish", "Middle Eastern", "Black", "Asian"]
stylechoices = ["Cool", "Grunge", "Elegant", "Casual", "Emo", "Serious", "Preppy", "Chill", "Muscular"]
listofboynames = ["Julian", "James", "Nathan", "Grayson","Ethan","Michael","Liam","Logan","Alan","Alfonso"]
listofgirlnames = ["Joana", "Isabella", "Sofia", "Lily", "Lila", "Cassidy", "Renee", "Grace", "Madeline", "Maya",]


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
        time.sleep(1.01)  #float
        amount = int(input("Please type in a number that is at least 10: ")) 


#selecting everything from the lists
import random

for each_npc in range(amount): #amount is the number of npcs being printed 
    age = random.randint(1, 90)     #age 
    true_gender = random.choice(gender)
    name = 0
    if gender == "Male":                    #naming
        name = random.choice(listofboynames)
    elif gender == "Female":
        name = random.choice(listofgirlnames)               
    styleselected = random.choice(stylechoices)      #style
    race = random.choice(randomracelist)        #Race choice
    height = random.choice(heightchoices)       #Height choice
    #Final print statement
    print(f"\nYour npc is {age} and {height} tall, is {race} and has a {styleselected} style.\n Their name is {name} and their gender is {true_gender}")