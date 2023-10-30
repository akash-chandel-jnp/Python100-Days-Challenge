from turtle import Turtle, Screen

screen = Screen()
tim1 = Turtle()
tim1.shape("turtle")
tim1.color("orange")

tim2 = Turtle()
tim2.shape("turtle")
tim2.color("green")

# For first turtle
def move_fwd():
    tim1.forward(10)


# turn Right
def turn_right():
    tim1.right(15)


# Turn Left
def turn_left():
    tim1.left(15)


# Move Backwards
def move_back():
    tim1.back(10)

# =======================================================================
# For second turtle
def move_fwdd():
    tim2.forward(10)


# turn Right
def turn_rightt():
    tim2.right(15)


# Turn Left
def turn_leftt():
    tim2.left(15)


# Move Backwards
def move_backk():
    tim2.back(10)



# tim.forward(20)

screen.listen()

#second Turtle
screen.onkey(move_fwdd, "i")
screen.onkey(move_backk, "k")

screen.onkey(turn_leftt, "j")
screen.onkey(turn_rightt, "l")

# =====================================================
# For First Turtle
screen.onkey(move_fwd, "w")
screen.onkey(move_back, "s")

screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.exitonclick()
