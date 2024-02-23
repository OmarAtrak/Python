from turtle import Turtle, Screen, colormode
from color import random_color
import random

turtle = Turtle()
turtle.speed(8)
turtle.width(10)
colormode(255)


def random_move():
    left_or_right = random.choice(['left', 'right', 'turn'])
    if left_or_right == 'left':
        turtle.left(90)
    elif left_or_right == 'right':
        turtle.right(90)
    else:
        turtle.right(180)
    move = random.randint(10, 50)
    turtle.forward(move)


for _ in range(100):
    color_rgb = random_color()
    turtle.pencolor(color_rgb)
    random_move()


my_screen = Screen()
my_screen.exitonclick()
