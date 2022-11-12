import time
from random import randint
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_man = CarManager()
scoreboard = Scoreboard()

game_is_on = True
count = 0

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:

    screen.update()
    time.sleep(0.1)

    car_man.spawn_car()
    car_man.move_cars()

    # Collision detection
    for car in car_man.all_cars:
        if player.distance(car) < 27:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        car_man.level_up()
        player.reset()
        scoreboard.increase_level()
