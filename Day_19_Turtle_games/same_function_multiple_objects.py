from turtle import Turtle, Screen

screen = Screen()
tur1 = Turtle()
tur1.shape("turtle")
tur1.shape("turtle")
tur1.penup()
tur1.setposition(x=-200, y=-100)

tur2 = Turtle()
tur2.shape("turtle")
tur2.penup()
tur2.setposition(x=200, y=100)


def move_fwd(turtle_name):
    turtle_name.forward(20)


screen.listen()

screen.onkey(lambda : move_fwd(tur1), "w") # how to tell that this is to be called for tur1 ---ans: using a lambda function
screen.onkey(lambda : move_fwd(tur2), "i") # how to tell that this is to be called for tur2
screen.onkey(lambda :print("hello"),key='m')
# soution :
""" Use a lambda

screen.onkey(lambda: move_fwd(tur1), "w")
screen.onkey(lambda: move_fwd(tur2), "i")
"""

screen.exitonclick()
