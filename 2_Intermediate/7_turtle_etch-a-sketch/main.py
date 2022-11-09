from turtle import *

t = Turtle()
s = getscreen()


def move_fwd():
    t.fd(10)


def move_bwd():
    t.bk(10)


def turn_right():
    t.right(90)


def turn_left():
    t.left(90)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(key="w", fun=move_fwd)
s.onkey(key="s", fun=move_bwd)
s.onkey(key="d", fun=turn_right)
s.onkey(key="a", fun=turn_left)
s.onkey(key="c", fun=clear_screen)

s.exitonclick()
