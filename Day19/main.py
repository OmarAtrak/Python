from turtle import Turtle, Screen, colormode
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_forward():
    forward = random.randint(1, 20)
    return forward


colormode(255)
screen = Screen()
screen.setup(width=500, height=300)
user_response = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a nomber from 1 to 6: ")

list_turtle = [
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle"),
    Turtle(shape="turtle")
]
positions = [75, 45, 15, -15, -45, -75]
turtle_winner = None

for turtle_index in range(6):
    turtle = list_turtle[turtle_index]
    color = random_color()
    turtle.color(color)
    turtle.penup()
    turtle.goto(-150, positions[turtle_index])

while turtle_winner == None:
    for turtle in list_turtle:
        turtle.forward(random_forward())
        if turtle.pos()[0] >= 150:
            turtle_winner = list_turtle.index(turtle) + 1
            break

if int(user_response) == turtle_winner:
    print(f"You've win! The turtle nomber {turtle_winner} is the winner!")
else:
    print(f"You've lost! The turtle nomber {turtle_winner} is the winner!")

screen.exitonclick()