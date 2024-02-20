machine_stock = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}

coffee_stock = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "money": 1.50
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "money": 2.50
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "money": 3.00
    },
}


def check_available(coffee):
    coffee_available = True

    for _coffee_item in coffee_stock[coffee]:
        if _coffee_item != "money":
            if coffee_stock[coffee][_coffee_item] > machine_stock[_coffee_item]:
                coffee_available = False

    return coffee_available


def coffee_out_of_machine_stock(coffee):
    global machine_stock
    for stock_item_key in coffee_stock[coffee]:
        if stock_item_key != "money":
            machine_stock[stock_item_key] -= coffee_stock[coffee][stock_item_key]
        else:
            machine_stock[stock_item_key] += coffee_stock[coffee][stock_item_key]


def report():
    global machine_stock
    for _coffee_item in machine_stock:
        print(f"{_coffee_item}: {machine_stock[_coffee_item]}")


is_program_stop = False

while not is_program_stop:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if response == 'report':
        report()
    elif response == 'stop':
        is_program_stop = True
    elif check_available(response):
        print("Please insert coins.")
        pennies_coins = int(input("How many pennies? ")) * 0.01
        nickles_coins = int(input("How many nickles? ")) * 0.05
        dimes_coins = int(input("How many dimes? ")) * 0.10
        quarters_coins = int(input("How many quarters? ")) * 0.25
        total = pennies_coins + nickles_coins + dimes_coins + quarters_coins
        if total >= coffee_stock[response]['money']:
            change = total - coffee_stock[response]['money']
            coffee_out_of_machine_stock(response)
            print(f"Here is ${change} in change.")
            print(f"Here is your {response} ☕ Enjoy!")
        else:
            print("Sorry, you don't have enough Money, Money refunded")
    else:
        print("Sorry, this coffee not available")