MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ressources(order, m_status):
    if MENU[order]["ingredients"]["water"] > m_status["water"]:
        return "water"
    elif MENU[order]["ingredients"]["coffee"] > m_status["coffee"]:
        return "coffee"
    try:
        if MENU[order]["ingredients"]["milk"] > m_status["milk"]:
            return "milk"
    finally:
        return False


def sum_coins(q, d, n, p):
    q *= 0.25
    d *= 0.10
    n *= 0.05
    p *= 0.01
    return q + d + n + p


def process_coins(total, order, m_status):
    if total == MENU[order]["cost"]:
        m_status["money"] += total
        print(f"---\nYou inserted ${round(total, 2)}\nOrder is getting processed\n---")
        return True
    elif total > MENU[order]["cost"]:
        m_status["money"] += MENU[order]["cost"]
        print(
            f"---\nYou inserted ${round(total, 2)}\nOrder is getting processed\nChange of {round(total - MENU[order]['cost'])} will be refunded\n---"
        )
        return total - MENU[order]["cost"]
    print(
        f"---\nYou inserted ${round(total, 2)}\nNot enough money inserted\nMoney will be refunded\n---"
    )
    return False


def process_order(order, m_status):
    m_status["water"] -= MENU[order]["ingredients"]["water"]
    m_status["coffee"] -= MENU[order]["ingredients"]["coffee"]
    try:
        m_status["milk"] -= MENU[order]["ingredients"]["milk"]
    except KeyError:
        pass
    finally:
        print(f"Order has been processed\nEnjoy your {order.capitalize()}!")


m_run = True
m_status = {"water": 300, "milk": 300, "coffee": 300, "money": 0}
machine_status_list = [
    m_status["water"],
    m_status["milk"],
    m_status["coffee"],
]


if __name__ == "__main__":
    while m_run:
        order = input("What would you like? (espresso/latte/cappuccino):\n").lower()
        if order == "espresso" or order == "latte" or order == "cappuccino":
            if check_ressources(order, m_status):
                print(f"Sorry there is not enough {check_ressources(order, m_status)}")
            else:
                print(f"Please insert ${MENU[order]['cost']} (enter amount of coins)")
                quarters = int(input("Quarters: "))
                dimes = int(input("Dimes: "))
                nickles = int(input("Nickles: "))
                pennies = int(input("Pennies: "))
                total = sum_coins(quarters, dimes, nickles, pennies)
                if process_coins(total, order, m_status):
                    process_order(order, m_status)
                else:
                    print("Please try again with sufficient money!")
        elif order == "report":
            for k, v in m_status.items():
                if k != "money":
                    print(f"{k.capitalize()}: {v}")
                else:
                    print(f"{k.capitalize()}: ${v}")
        elif order == "off":
            m_run = False
