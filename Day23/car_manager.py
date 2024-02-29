from turtle import Turtle, colormode
import random

CARS_COUNT = 20
MOVE_SPEED = 0.1


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


class CarManager:
    def __init__(self):
        super().__init__()
        self.move_speed = MOVE_SPEED
        colormode(255)
        self.cars = []
        self.create_cars()

    def increase_speed(self):
        self.move_speed *= 0.9

    def create_cars(self):
        for _ in range(0, CARS_COUNT):
            self.add_car((random.randint(-280, 300), random.randint(-240, 240)))

    def move_cars(self):
        for car in self.cars:
            car.forward(-10)
            if car.xcor() < -350:
                self.cars.remove(car)
                self.add_car((random.randint(300, 550), random.randint(-240, 240)))

    def add_car(self, position):
        new_turtle = Turtle("square")
        new_turtle.color(random_color())
        new_turtle.penup()
        new_turtle.shapesize(stretch_wid=1, stretch_len=2)
        new_turtle.goto(position)
        self.cars.append(new_turtle)
