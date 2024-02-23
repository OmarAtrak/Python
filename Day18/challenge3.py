from turtle import Turtle, Screen, colormode
from color import random_color


turtle = Turtle()
turtle.left(180)
turtle.forward(50)
turtle.right(180)
colormode(255)

for i in range(3, 10):
    color_rgb = random_color()
    turtle.pencolor(color_rgb)
    for _ in range(0, i):
        turtle.forward(100)
        turtle.right(360 / i)


my_screen = Screen()
my_screen.exitonclick()
