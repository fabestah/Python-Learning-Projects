import time
from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def spawn_car(self):
        n_car = Turtle("square")
        car_spawn_y = randint(-250, 250)
        car_spawn_x = 310
        spawn_frequency = randint(1, 6)

        if spawn_frequency == 6:
            n_car.shapesize(stretch_wid=1, stretch_len=2)
            n_car.penup()
            n_car.color(choice(COLORS))
            n_car.goto(car_spawn_x, car_spawn_y)
            self.all_cars.append(n_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
