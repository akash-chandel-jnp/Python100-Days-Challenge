from turtle import Turtle,  Screen
import  random

colours = ["red", "green" , "orange", "blue", "purple", "pink"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.turtlesize(.8)
        self.refresh_food()

    def refresh_food(self):
        self.color(random.choice(colours))
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)

        self.setposition(random_x, random_y)












