# Python Program using Food Tip Calculator
print('''
Restaurant
                     ________
             <<<|>> |PARADISE|
               _|___|[] [] []|
              |[] []|        |
   ___________|_____|[]_[]_[]|_
  |                            |
  |   <>   CAFE  LAMOUR   <>   |
  |____________________________|
 /::::::::::::::::::::::::::::::\
/::::::::::::::::::::::::::::::::\
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
 |  _______________   _________ |\.--------.
 | |vvv|vvv|vvv|vvv|  || _ _ || | | Hotel  |
 | |   |   |   |   |  |||_|_||| | |Entrance|__
 | |%%%+%%%+%%%+%%%|  |||_|_||| |/'--------'
 | |%%%|%%%|%%%|%%%|  ||     || |
 | |%%%|%%%|%%%|%%%|  ||o    || |()         ()
 |  """""""""""""""   ||     || ||| /     \ ||
 |                    ||_____|| |||/       \||lc
 ~~~~~~~~~~~~~~~~~~~~~/_______\~~ /         \

~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.<>.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~
''')

print("Welcome to Chinnu's Restaurant")
bill = float(input("Enter the total amount of cost you have to pay: $"))
tips = int(input("Please provide tips for waiter, tips will be '10', '12' or '15'. Enter tips: $"))
people = int(input("Enter how many peoples were going to share the cost: $"))

average_tips = bill * tips /100
final_tips = bill + average_tips
total_amount = final_tips / people
print(f"Each Person should pay: {round(total_amount)}$ ")

