from turtle import Turtle,  Screen
import  random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.turtlesize(.8)
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.setposition(random_x, random_y)












