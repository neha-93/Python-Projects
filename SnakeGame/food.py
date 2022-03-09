from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_cord = random.randint(-330, 330)
        self.y_cord = random.randint(-330, 290)
        self.refresh()

    def refresh(self):
        self.x_cord = random.randint(-330, 330)
        self.y_cord = random.randint(-330, 330)
        self.goto(self.x_cord, self.y_cord)
