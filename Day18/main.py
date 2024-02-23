from turtle import Turtle, Screen, colormode
from color import choice_color


def new_line(step):
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(step * 10)
    turtle.left(180)


colors_list = [
    (223, 236, 228),
    (236, 230, 216),
    (140, 176, 207),
    (25, 32, 48),
    (26, 107, 159),
    (237, 225, 235),
    (209, 161, 111),
    (144, 29, 63),
    (230, 212, 93),
    (4, 163, 197),
    (218, 60, 84),
    (229, 79, 43),
    (195, 130, 169),
    (54, 168, 114),
    (28, 61, 116),
    (172, 53, 95),
    (108, 182, 90),
    (110, 99, 87),
    (193, 187, 46),
    (240, 204, 2),
    (1, 102, 119),
    (19, 22, 21),
    (50, 150, 109),
    (172, 212, 172),
    (118, 36, 34),
    (221, 173, 188),
    (227, 174, 166),
    (153, 205, 220),
    (184, 185, 210)
]

turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.left(225)
turtle.forward(300)
turtle.left(135)
colormode(255)

forward = 50
for _ in range(10):
    for _ in range(10):
        turtle.dot(20, choice_color(colors_list))
        turtle.forward(forward)
    new_line(forward)

screen = Screen()
screen.exitonclick()
