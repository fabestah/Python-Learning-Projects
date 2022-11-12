import time
from random import randint
from turtle import Screen

from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_man = CarManager()

game_is_on = True
cars_list = []
count = 0

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:

    screen.update()
    time.sleep(0.1)

    car_man.spawn_car()
    car_man.move_cars()

    if player.ycor() > 270:
        player.reset()
