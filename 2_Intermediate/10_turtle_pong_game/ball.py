from turtle import Turtle


class Ball(Turtle):
    def __init__(self, shape="circle"):
        super().__init__(shape)
        self.x_move = 0.1
        self.y_move = 0.1
        self.color("white")
        self.penup()
        self.speed("slowest")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
