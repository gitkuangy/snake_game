from turtle import Turtle
import random

WIDTH = 800
HEIGHT = 800


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed("fastest")
        self.relocation()

    def relocation(self):
        random_x = random.uniform(-WIDTH / 2 + WIDTH / 15, WIDTH / 2 - WIDTH / 15)
        random_y = random.uniform(-HEIGHT / 2 + HEIGHT / 15, HEIGHT / 2 - 45)
        self.goto(random_x, random_y)
