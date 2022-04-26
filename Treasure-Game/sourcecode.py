# Treasure Game Project

print("Welcome to treasure island")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("I Welcome you again to the treasure island, your mission is to find the treasure using right path")
print("Have a fun to play the game")
name = input("Please enter your name for playing the game: ").upper()
choice1 = input('You\'r are in the island now, choose "left" or "right" to continue the game: ').lower()
if choice1 == str("left"):
    choice2 = (input('''Welcome, You successfully completed Level-1. 
                    Now you are in middle island:- Choose 'swim' or 'wait' to complete level-2: ''')).lower()
    if choice2 == str("wait"):
        choice3 = input('''Congrats, you crossed level-2. Its time to choose the door in front of you.
                 Choose any one colored door "Red" or "blue" or "Yellow" to get the treasure: ''').lower()
        if choice3 == 'red':
            print("The red color room full of fire, Game Over")
        elif choice3 == "blue":
            print("The blue colored room full of water, Game Over")
        elif choice3 == 'yellow':
            print(f"Wow, {name} Excellent You find the treasure. Congrats.........................")
        else:
            print("you choosen door not exit.")
    else:
        print("Oh, oh you choose wrong decision. You are hunted by sea animals. Game Over!.....")
else:
    print("Oh, oh you choosen a wrong direction. You fellow down in to the hole :--: Game Over!....")
