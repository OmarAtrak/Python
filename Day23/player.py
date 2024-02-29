from turtle import Turtle

START_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.go_to_start()

    def go_up(self):
        self.forward(10)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def go_to_start(self):
        self.goto(START_POSITION)
