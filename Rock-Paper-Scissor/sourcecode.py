import random

scissor = '''
        ___________
_______'        ___)_______
                   ________)
               ____________)
               (______)
----------._____(_____)
'''
rock = '''
        __________
_______'      _____)
            (______)
            (______)
            (______)
-------._____(____)
'''
paper = '''

        ______
_______' _____)___
            ______)
            _______)
            ______)
-------.________)

'''

print("Hi Welcome to Rock Paper Scissor Game")
name = input("enter your name to play the game: ")
game = [rock, paper, scissor]
user1 = int(input("Please select any 1 option to play the game: \noptions:- \nType 0 as Rock, 1 as Paper or 2 as Scissor: "))
print(f"user choosed: {game[user1]}")
computer = random.randint(0, 2)                # computer will generate random number..
print(f"computer choosed: {game[computer]} ")
if user1 >= 3 or user1 < 0:
  print("you entered invalid number. Restart the game!....")
elif user1 == 0 and computer == 2:
  print(f"{name} you win!..")
elif computer == 0 and user1 == 2:
  print(f"{name} you lose!")
elif computer > user1:
  print(f"{name} You lose")
elif computer < user1:
  print(f"{name} You win!...")
elif user1 == computer:
  print(f"{name} Game Draw!..")
else:
  print("NA")
