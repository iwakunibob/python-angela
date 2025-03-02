# import turtle
# timmy = turtle.Turtle()
# OOP classes used Title Case

# Pretty Table demo
from prettytable import PrettyTable
table = PrettyTable()  # Created table object
table.field_names = ["Pokeman", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)
