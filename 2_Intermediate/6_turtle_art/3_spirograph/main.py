from turtle import *
from random import randint, choice


def gen_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    r_color = (r, g, b)
    return r_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(gen_random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


if __name__ == "__main__":
    s = getscreen()
    t = RawTurtle(s)
    s.colormode(255)
    t.speed("fastest")

    draw_spirograph(5)
