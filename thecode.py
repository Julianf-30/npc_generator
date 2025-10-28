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

print("Welcome to the Generator section")
time.sleep(1)
amount_y_or_n = ""
amount = int(input("To start, how many npcs would you like to generate?(must be at least 10) "))

while amount_y_or_n != "yes" or "no":
    print(f"You are generating {amount} npcs")
    amount_y_or_n = input("Is this number correct? ")
    if amount_y_or_n == "yes" and amount >=  10:
        print("Moving on to the next step")
        break
    elif amount_y_or_n == "no":
        new_amount = int(input("Please type in another number (at least 10) "))
    else:
        print("Sorry this number is invalid")
        time.sleep(1)
        int(input("Please type in a number that is at least 10: "))
    
listofnames = []

for name in range(amount):
   namesofnpcs = input("Name of npc: ")
   listofnames.append(namesofnpcs)

print(listofnames)
print(listofnames[5])
