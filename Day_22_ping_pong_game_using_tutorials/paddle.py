from turtle import Turtle
import  random
colours = ["red", "green" , "orange", "blue", "purple", "pink"]

class Paddle(Turtle):
    def __init__(self, position): # this is how we pass arguments to the class
        super().__init__()

        self.penup()
        self.color(random.choice(colours))
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.height = 100
        self.goto(position)


    def up(self):
        if self.ycor() <240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)


    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
