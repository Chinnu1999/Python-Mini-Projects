import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
letters1 = int(input("How many letters would you like in your password? "))
symbols1 = int(input("How many symbols would you like? "))
numbers1 = int(input("How many numbers would you like? "))
password = ""
for char in range(1, letters1 + 1):
    password += random.choice(letters)
for char in range(1, symbols1 + 1):
    password += random.choice(symbols)
for char in range(1, numbers1 + 1):
    password += random.choice(numbers)   
print(password)
