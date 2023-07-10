from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Requirements.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Requirements.txt", 'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.updateScoreboard()
