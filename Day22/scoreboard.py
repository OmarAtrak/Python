from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_paddle_score = 0
        self.left_paddle_score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.left_paddle_score, align="center", font=("Courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.right_paddle_score, align="center", font=("Courier", 80, "normal"))

    def add_point_to_right_paddle(self):
        self.right_paddle_score += 1
        self.refresh_score()

    def add_point_to_left_paddle(self):
        self.left_paddle_score += 1
        self.refresh_score()
