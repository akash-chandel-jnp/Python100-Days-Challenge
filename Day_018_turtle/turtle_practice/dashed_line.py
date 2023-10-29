from turtle import Turtle, Screen
tt_turtle_obj = Turtle()


#method 1 : change the color of the pen from from black to white  in between and then again back to black
# for _ in range(5):
#     tt_turtle_obj.forward(20)
#     tt_turtle_obj.color("white")
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.color("black")

# Method 2 : Using penup and pendown function
for _ in range(5):
    tt_turtle_obj.pendown()
    tt_turtle_obj.forward(20)
    tt_turtle_obj.penup()
    tt_turtle_obj.forward(10)
    tt_turtle_obj.left(30)
    

screen = Screen()
screen.exitonclick()