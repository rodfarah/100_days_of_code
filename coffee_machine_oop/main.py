from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

def operate():
    """Starts Coffee Machine operations"""
    global is_on
    while is_on:
        drinks = menu.get_items()
        order = input(f"What would you like? ({drinks}): ")
        if order == "off":
            return "Coffee Machine is now off."
            is_on = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            
print(operate())


