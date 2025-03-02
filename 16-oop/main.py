from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker() # Create object
money_machine = MoneyMachine() # Create object
menu = Menu()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What beverage would you like? ({options}): ")
    print(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



        
        


