from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue = True
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while should_continue:
    total_items = menu.get_items()
    order_name = input(f"What would you like to have??? {total_items}").lower()
    if order_name == "off":
        should_continue = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        choice = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
            coffee_maker.make_coffee(choice)
