from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

my_menu = Menu()
coffee_marker = CoffeeMaker()
money_machine = MoneyMachine()
is_program_stop = False

while not is_program_stop:
    response = input(f"What would you like? ({my_menu.get_items()}): ").lower()

    items = []
    for menu_item in my_menu.menu:
        items.append(menu_item.name)

    if response == 'report':
        coffee_marker.report()
        money_machine.report()
    elif response == 'stop':
        is_program_stop = True
    elif response in items:
        order = my_menu.find_drink(response)
        if coffee_marker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                print("In progress", end="")
                for i in range(1, 4):
                    time.sleep(1)
                    print(".", end="")
                print()
                coffee_marker.make_coffee(order)
    else:
        print("Sorry, this coffee not available")