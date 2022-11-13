from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        self.load_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Highscore: {self.highscore} | Score: {self.score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.store_highscore()
        self.clear()
        self.score = 0
        self.update_scoreboard()

    def store_highscore(self):
        with open("highscore.txt", "w") as highscore_file:
            highscore_file.write(str(self.highscore))

    def load_highscore(self):
        with open("highscore.txt") as highscore_file:
            self.highscore = int(highscore_file.read())
