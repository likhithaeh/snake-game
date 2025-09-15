from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(x = 0, y = 270)
        self.score = 0
        with open("highscore.txt", "r") as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))

