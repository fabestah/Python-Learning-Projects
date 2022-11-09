import colorgram
from turtle import *
from random import choice


def paint_row_fd():
    for x in range(24):
        t.pendown()
        t.dot(20)
        t.color(choice(colors))
        t.penup()
        t.fd(50)


colors = []
color_objs = colorgram.extract(
    "X:\\1.CODING\\Learning_Projects\\Python_Learning_Projects\\2_Intermediate\\6_turtle_art\\4_hirst_painting\\image.jpg",
    6,
)

for i in range(len(color_objs)):
    red = color_objs[i].rgb[0]
    blue = color_objs[i].rgb[1]
    yellow = color_objs[i].rgb[2]
    colors.append((red, blue, yellow))

y = 500
x = -600

s = getscreen()
t = RawTurtle(s)
s.colormode(255)

t.shape("circle")
t.speed("fastest")

for r in range(21):
    t.penup()
    t.goto((x, y))
    paint_row_fd()
    y -= 50


s.exitonclick()
