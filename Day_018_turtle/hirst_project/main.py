
# tim.width(5)
def hirst_paint(x_coord, y_coord, rows, col, thick, gap):
    from colours import colours
    # print(colours)
    from random import choice
    # import random
    import turtle
    from turtle import Turtle, Screen

    tim = Turtle()
    turtle.colormode(255)  # so that the color of the turtle can be changed from mode 0-1 to mode 1-255

    x = x_coord;
    y = y_coord
    for i in range(rows):
        for j in range(col):
            tim.penup()
            tim.hideturtle()

            tim.setposition(x, y)
            tim.isvisible()
            tim.color(choice(colours))
            # print(tim.color())
            tim.dot(thick)
            x += gap

        y += gap
        x = x_coord

    screen = Screen()
    screen.exitonclick()


hirst_paint(-200, -200, 6, 10, 30, 50)
