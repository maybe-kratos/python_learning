from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Blue")
        self.speed("fastest")
        random_x = random.randint(-370, 370)
        random_y = random.randint(-270, 270)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        random_x = random.randint(-370, 370)
        random_y = random.randint(-270, 270)
        self.goto(x=random_x, y=random_y)
