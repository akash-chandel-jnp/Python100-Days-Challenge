from turtle import Turtle
# POSITIONS = [ (850, -20),  (850, -40), (850, 0), (850, 20), (850, 40)]
POSITIONS2 = [(-850, -20), (-850, -40), (-850, 0), (-850, 20), (-850, 40)]

SLIDER_LENGTH = 5
STARTING_POSITION_OF_FIRST_SEGMENT = SLIDER_LENGTH * 20 / 2


class Slider:
    def __init__(self):
        self.segment = []
        self.create_body()
        self.head = self.segment[0]
        self.tail = self.segment[-1]


    # TODO create body by creating new_segement (which is a turtle) and in appending it to the segment list and then repeat the same steps for n times to increase the length of the slider
    def create_body(self):
        uppermost_position = STARTING_POSITION_OF_FIRST_SEGMENT
        for i in range(SLIDER_LENGTH):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(870, uppermost_position)
            self.segment.append(new_segment)
            uppermost_position -= 20
        print("body complete")

    def up(self):
        if self.head.ycor() < 380:
            self.head.setheading(90)
            self.head.forward(30)
            print(self.head.ycor())
            for seg in self.segment[1:] :
                new_x = seg.xcor()
                new_y = seg.ycor() + 30
                seg.goto((new_x,new_y))

    def down(self):
        if self.tail.ycor() > -390:
            self.tail.setheading(270)
            self.tail.forward(30)
            for seg in self.segment[-2: :-1] :
                new_x = seg.xcor()
                new_y = seg.ycor() -30
                seg.goto((new_x,new_y))




