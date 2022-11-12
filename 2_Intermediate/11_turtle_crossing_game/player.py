from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.seth(90)
        self.reset()

    def move(self):
        self.fd(10)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def reset(self):
        self.goto(STARTING_POSITION)
