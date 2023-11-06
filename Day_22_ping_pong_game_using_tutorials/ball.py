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

    def move(self):
        new_x = self.xcor() +10
        new_y = self.ycor() +10
        self.goto(new_x, new_y)


    # def ball_initial_move(self):
    #     self.setheading(initial_direction)
    #     self.keep_moving()


