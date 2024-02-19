from art import logo, vs
from game_data import data
import random

print(logo)

is_program_stop = False
score = 0

def plus_point():
    global score
    score += 1
    print(f"You're right! Current score: {score}")

def check_response(a_follower_count, b_follower_count, response):
    if response == "A":
        return a_follower_count['follower_count'] > b_follower_count['follower_count']            
    elif response.upper() == "B":
        return b_follower_count['follower_count'] > a_follower_count['follower_count']
    else:
        return False

first_data = random.choice(data)

while not is_program_stop:
    second_data = random.choice(data)
    print(f"Compare A: {first_data['name']}, a {first_data['description']} from {first_data['country']}")
    print(vs)
    print(f"Against B: {second_data['name']}, a {second_data['description']} from {second_data['country']}")
    response = input("Who has more followers? Type 'A' or 'B': ").upper()

    if check_response(first_data, second_data, response):
        plus_point()
        first_data = second_data
        print("-" * 70)
    else:
        is_program_stop = True
        print(f"Sorry, that's wrong. Final score: {score}.")