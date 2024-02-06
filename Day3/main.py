print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_or_right = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if left_or_right.lower() == "left":
    wait_or_swim = input("You come to a lake. There is an island in middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if wait_or_swim.lower() == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if door.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")