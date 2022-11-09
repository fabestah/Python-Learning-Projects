from turtle import Turtle

SCORE_POSITION = (0, 270)
AlIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(SCORE_POSITION)
        self.write(
            f"Score = {self.score}",
            False,
            align=AlIGNMENT,
            font=FONT,
        )

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(
            f"Score = {self.score}",
            False,
            align=AlIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER!",
            False,
            align=AlIGNMENT,
            font=FONT,
        )
