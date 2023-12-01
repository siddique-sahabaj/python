from turtle import Turtle

with open("./data.txt", mode="r") as file:
    high_score = int(file.read())

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score = {self.high_score}", align="center", font=("monospace", 18, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display_score()
