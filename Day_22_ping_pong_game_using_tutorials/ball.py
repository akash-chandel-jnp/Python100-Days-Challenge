from turtle import Turtle
import time

import random

angle_towards_left = random.randint(120,200)
angle_towards_right = random.randint(-60, +60)
initial_direction = random.randint(-30,+30)
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_move = 10
        self.y_move =10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        self.y_move *= -1





