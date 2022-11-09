from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, s_color="white"):
        self.s_color = s_color
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_seg(pos)

    def add_seg(self, pos):
        new_seg = Turtle("square")
        new_seg.color(self.s_color)
        new_seg.penup()
        new_seg.goto(pos)
        self.segs.append(new_seg)

    def extend(self):
        self.add_seg(self.segs[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move(self):
        for snake_seg_num in range(len(self.segs) - 1, 0, -1):
            new_x = self.segs[snake_seg_num - 1].xcor()
            new_y = self.segs[snake_seg_num - 1].ycor()
            self.segs[snake_seg_num].goto(new_x, new_y)
        self.segs[0].fd(MOVE_DISTANCE)
