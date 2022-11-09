from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.ht()
        self.update_scoreboard()

    def score(self, p_scored):
        if p_scored == "L":
            self.score_l += 1
            self.clear()
            self.update_scoreboard()
        elif p_scored == "R":
            self.score_r += 1
            self.clear()
            self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Consolas", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Consolas", 80, "normal"))
