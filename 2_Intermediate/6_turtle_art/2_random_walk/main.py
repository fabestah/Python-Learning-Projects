from turtle import *
from random import randint, choice


def random_forward():
    direction = choice([50, -50])
    t.fd(direction)


def random_turn():
    direction = choice([0, 90, 180, 270])
    t.setheading(direction)


def gen_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    r_color = (r, g, b)
    return r_color


if __name__ == "__main__":
    s = getscreen()
    t = RawTurtle(s)
    s.colormode(255)
    t.pensize(10)

    for _ in range(500):
        t.pencolor(gen_random_color())
        random_forward()
        random_turn()
