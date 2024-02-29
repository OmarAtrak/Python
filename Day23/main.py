from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "Up")

is_game_over = False
while not is_game_over:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.move_cars()

    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.increase_speed()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_over = True

screen.exitonclick()
