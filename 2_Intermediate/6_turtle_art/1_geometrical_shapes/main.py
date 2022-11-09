from turtle import *
from random import randint

s = getscreen()
t = RawTurtle(s)

s.colormode(255)

for f in range(3, 9):
    factor = 360 / f
    lines = int(360 / factor)
    t.pencolor((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
    for _ in range(lines):
        t.right(factor)
        t.forward(100)
