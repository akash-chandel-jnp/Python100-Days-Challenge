from turtle import Turtle
import random
colours = ["red", "green" , "orange", "blue", "purple", "pink"]

class Car(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.setheading(270)
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=2.5, stretch_len=1)
        self.color(random.choice(colours))

    def car_move(self):
        new_x = self.xcor() -10
        self.goto(new_x, self.ycor())
