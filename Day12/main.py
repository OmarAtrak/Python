import random
from art import logo

def check_number(guess_number, number):
    if guess_number > number:
        return "Too high."
    return "Too low."

print(logo)

print("Welcome to the Number Guessin Game!")
print("I'm thinking of a number 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

while difficulty != 'hard' and difficulty != 'easy':
    print("You choose incorrect difficulty")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


attempts = 5
if difficulty == 'easy':
    attempts = 10

number = random.randint(1, 100)
guess_number = 0

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    
    
    if(guess_number ==  number):
        print("You win")
        attempts = 0
    else:
        print(check_number(guess_number, number))
        attempts -= 1

if guess_number != number:
    print("Game over!")