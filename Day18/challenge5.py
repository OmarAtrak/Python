from turtle import Turtle, Screen, colormode
from color import random_color

turtle = Turtle()
turtle.speed('fastest')
colormode(255)


def random_move():
    color_rgb = random_color()
    turtle.pencolor(color_rgb)
    turtle.circle(100)
    turtle.left(5)


random_move()
current_heading = turtle.heading()
while current_heading != 0.0:
    random_move()
    current_heading = turtle.heading()

my_screen = Screen()
my_screen.exitonclick()
