from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("orange")
        self.back_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)



    def back_to_start(self):
        self.goto(STARTING_POSITION)
    def has_crossed(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
        

