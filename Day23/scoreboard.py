from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 0
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
