from turtle import Turtle, Screen

# from screen_listener import head_east, head_west, head_north, head_south

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Feed The SNAKE")
screen.listen()

# positions
positions_of_all_turtles = []

# TODO 1: create 3 turtles
initial_x = 0
initial_y = 0
all_turtles = []
for i in range(3):
    tur = Turtle(shape="square")
    tur.color("white")
    tur.penup()
    tur.setposition(initial_x, initial_y)
    all_turtles.append(tur)
    initial_x -= 20
    positions_of_all_turtles.append((tur.pos()[0], tur.pos()[1]))

print(positions_of_all_turtles)

all_turtles[0].shape("circle")


def follow_head(all_turtles_list):
    for i in range(1, len(all_turtles_list) + 1):
        current_turt = all_turtles_list[i]
        prev_turt = all_turtles_list[i - 1]
        current_turt.setposition(positions_of_all_turtles[i - 1])
        positions_of_all_turtles[i - 1] = prev_turt.pos()


def head_east(all_turtles_list):
    all_turtles_list[0].setheading(0)
    all_turtles_list[0].forward(10)

    follow_head(all_turtles_list)

    # for i in range(1,len(all_turtles_list)+1):
    #     current_turt= all_turtles_list[i]
    #     prev_turt = all_turtles_list[i-1]
    #     current_turt.setposition(positions_of_all_turtles[i-1])
    #     positions_of_all_turtles[i-1] = prev_turt.pos()


def head_north(all_turtles_list):
    all_turtles_list[0].setheading(90)
    all_turtles_list[0].forward(10)
    follow_head(all_turtles_list)


def head_west(all_turtles_list):
    all_turtles_list[0].setheading(180)
    all_turtles_list[0].forward(10)
    follow_head(all_turtles_list)


def head_south(all_turtles_list):
    all_turtles_list[0].setheading(270)
    all_turtles_list[0].forward(10)
    follow_head(all_turtles_list)


screen.onkey(lambda: head_west(all_turtles), "Left")
screen.onkey(lambda: head_east(all_turtles), "Right")
screen.onkey(lambda: head_south(all_turtles), "Down")
screen.onkey(lambda: head_north(all_turtles), "Up")

screen.exitonclick()
