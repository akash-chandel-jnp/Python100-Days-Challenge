from turtle import Turtle, Screen

screen = Screen()
tim1 = Turtle()
tim1.shape("circle")
tim1.turtlesize(2)
tim1.color("orange")
tim1.penup()
tim1.setposition(x=-220, y=-100)
# print(tim1.pos())

tim2 = Turtle()
tim2.shape("turtle")
tim2.turtlesize(2)

tim2.color("green")
tim2.penup()
tim2.setposition(x=220, y=100)


# print(tim1.pos()==tim2.pos())

def has_not_touched(tim1, tim2):
    if tim1.pos()[0] + 30 > tim2.pos()[0] and tim1.pos()[1] + 30 > tim2.pos()[1] and tim2.pos()[0] + 30 > tim1.pos()[
        0] and tim2.pos()[1] + 30 > tim1.pos()[1]:
        tim1.hideturtle()
        tim2.turtlesize(4)
        tim2.color("red")
        screen.textinput("Your game is over", "Do you want to play again")
        return False
    else:
        return True


def move_fwd():
    tim1.forward(30)
    has_not_touched(tim1, tim2)


def hide_yourself():
    tim1.hideturtle()


def show_yourself():
    tim1.showturtle()

def hide_yourself(t_tur):
    t_tur.hideturtle()


def show_yourself():
    tim2.showturtle()

# turn Right
def turn_right():
    tim1.right(15)
    has_not_touched(tim1, tim2)
    # return has_not_touched(tim1, tim2)


# Turn Left
def turn_left():
    tim1.left(15)
    has_not_touched(tim1, tim2)

    # return has_not_touched(tim1, tim2)


# Move Backwards
def move_back():
    tim1.back(10)
    has_not_touched(tim1, tim2)

    # return has_not_touched(tim1, tim2)


# =======================================================================
# For second turtle
def move_fwdd():
    tim2.forward(30)
    has_not_touched(tim1, tim2)

    # return has_not_touched(tim1, tim2)


# turn Right
def turn_rightt():
    tim2.right(15)
    has_not_touched(tim1, tim2)

    # return has_not_touched(tim1, tim2)


# Turn Left
def turn_leftt():
    tim2.left(15)
    has_not_touched(tim1, tim2)

    # return has_not_touched(tim1, tim2)


# Move Backwards
def move_backk():
    tim2.back(15)
    has_not_touched(tim1, tim2)

    # return has_not_touched(tim1, tim2)


# tim.forward(30)

screen.listen()
# For first turtle

# second Turtle
screen.onkey(move_fwdd, "8")
screen.onkey(move_backk, "5")

screen.onkey(turn_leftt, "4")
screen.onkey(turn_rightt, "6")

# =====================================================
# For First Turtle
screen.onkey(move_fwd, "w")
screen.onkey(move_back, "s")

screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(hide_yourself, "z")
screen.onkey(show_yourself, "x")

# while True:
#     # call for next move
#     pass

screen.exitonclick()
