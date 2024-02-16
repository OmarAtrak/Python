import random

def check_number(guess_number, number):
    if guess_number > number:
        return "Too high."
    elif guess_number < number:
        return "Too low."

print("Welcome to the Number Guessin Game!")
print("I'm thinking of a number 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

while difficulty != 'hard' and difficulty != 'easy':
    print("You choose incorrect difficulty")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


attempts = 5
number = random.randint
guess_number = random.randint

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    print(check_number(guess_number, number))
    attempts -= 1
