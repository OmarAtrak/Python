from turtle import Turtle, Screen
import time
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.init_food()

    def init_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        file = open("data/my_data.txt")
        self.high_score = int(file.read())
        file.close()

        self.init_score_text()

    def init_score_text(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.refresh_score()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

        if self.high_score > self.score:
            with open("data/my_data.txt", "w") as file:
                file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_score()


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(0, 3):
            self.add_segment()

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        if len(self.segments) > 0:
            last_segment = self.segments[len(self.segments) - 1]
            new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game_over = False
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.add_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280) or (snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
