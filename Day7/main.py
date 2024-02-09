import random
from hangman_art import *
from hangman_words import word_list


target = []
target_word = ""

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)

for letter in chosen_word:
    target.append("_")

for i in range(len(target)):
    target_word += target[i]
    if i < len(target) - 1:
        target_word += " "
print(target_word)


live = len(chosen_word)
while live > 0:
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter in chosen_word:
        if letter == guess:
            if target[index] == "_":
                target[index] = letter
                break
        index += 1

    target_word = ""
    for i in range(len(target)):
        target_word += target[i]
        if i < len(target) - 1:
            target_word += " "
    print(target_word)

    if chosen_word == target_word.replace(" ", ""):
        live = 0
    else:
        live -= 1

if chosen_word == target_word.replace(" ", ""):
    print("You win")
else:
    print("Game Over")
