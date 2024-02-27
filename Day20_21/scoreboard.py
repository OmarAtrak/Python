from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
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
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 24, "normal"))
