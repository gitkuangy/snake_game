from turtle import Turtle

WIDTH = 800
HEIGHT = 800
ALIGNMENT = "center"
FONT = ("Arial", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("blue")
        self.goto(0, HEIGHT / 2 - 40)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
