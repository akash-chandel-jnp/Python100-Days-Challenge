import turtle
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('coral')
timmy.forward(100)
timmy.left(60)
timmy.forward(100)
timmy.left(60)
timmy.forward(100)

timmy.left(60)
timmy.forward(100)
timmy.left(60)
timmy.forward(100)
timmy.left(60)
timmy.forward(100)

my_screen = Screen()

print(my_screen.canvwidth)

my_screen.exitonclick()

from prettytable import PrettyTable # from prettytable package we are importing PrettyTable class (module) which help in creating object

table = PrettyTable()
print(table)
table.add_column("Pokeman Name", ["Pikachu", "Squirel", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])


table.align = 'r'
print(table)
