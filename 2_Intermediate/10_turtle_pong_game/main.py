from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0)

    # Wall Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle Collision
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 340
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -340
    ):
        ball.bounce_x()

    # R Paddle Miss
    if ball.xcor() > 380:
        scoreboard.score("L")
        ball.reset()
    # L Paddle Miss
    elif ball.xcor() < -380:
        scoreboard.score("R")
        ball.reset()

screen.exitonclick()
