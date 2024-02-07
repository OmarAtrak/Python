#Password Generator Project
import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
]
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for count_letter in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for count_symbol in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for count_number in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""
characters = [letters, symbols, numbers]
nr = [nr_letters, nr_symbols, nr_numbers]
count = [1, 1, 1]

for i in range(1, nr_letters + nr_numbers + nr_symbols + 1):
    random_character_type = random.randint(0, 2)
    
    while count[random_character_type] > nr[random_character_type]:
        random_character_type = random.randint(0, 2)

    count[random_character_type] += 1
    index_random = random.randint(0, len(characters[random_character_type]) - 1)
    password += random.choice(characters[random_character_type])

print(password)