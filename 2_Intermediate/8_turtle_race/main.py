from turtle import Turtle, Screen
from random import randint


def gen_turtles():
    y = 90
    for _ in range(6):
        t = Turtle(shape="turtle")
        turtles.append(t)
        t.penup()
        t.color(colors[_])
        t.goto(x=-235, y=y)
        y -= 30


if __name__ == "__main__":
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    s = Screen()
    s.setup(width=500, height=400)
    user_bet = s.textinput(
        title="Make you bet", prompt="Which turtle will win the race? Enter a color: "
    )
    turtles = []

    if user_bet:
        is_race_on = True

    gen_turtles()

    while is_race_on:
        turtle.fd(randint(1, 10))
        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                is_race_on = False
                if winning_color == user_bet:
                    print(f"You've won!\nThe {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost!\nThe {winning_color} turtle is the winner!")
