from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as read_score:
            self.high_score = int(read_score.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} Highscore: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as write_score:
                write_score.write(f"{self.score}")
        self.score = 0
        self.update_score()
