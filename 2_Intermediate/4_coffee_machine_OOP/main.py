from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":

    menu = Menu()
    coffemaker = CoffeeMaker()
    money = MoneyMachine()
    latte = MenuItem("latte", 200, 150, 24, 2.5)
    espresso = MenuItem("espresso", 50, 18, 0, 1.5)
    cappuccino = MenuItem("cappucino", 250, 100, 24, 3.0)
    m_run = True

    while m_run:
        options = menu.get_items()
        order = input("What would you like? (espresso/latte/cappuccino):\n").lower()
        if order == "espresso" or order == "latte" or order == "cappuccino":
            order = menu.find_drink(order)
            if coffemaker.is_resource_sufficient(order):
                print(f"Please insert ${order.cost} (enter amount of coins)")
                if money.make_payment(order.cost):
                    coffemaker.make_coffee(order)
                else:
                    print("Please try again with sufficient money!")
            else:
                print(f"Sorry, not enough ingredients available, try again later!")
        elif order == "report":
            coffemaker.report()
            money.report()
        elif order == "off":
            m_run = False
