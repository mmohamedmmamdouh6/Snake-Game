from turtle import Turtle
import random

class Apple(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.move()

    def move(self):
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        self.goto(x, y)

        