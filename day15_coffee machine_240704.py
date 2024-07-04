# Day15 final project: Coffee machine _240704
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

lack_resources = []

def enough_resources(res, choi):
    global lack_resources
    if (res["water"] >= MENU[choi]["ingredients"]["water"]) and (res["milk"] >= MENU[choi]["ingredients"]["milk"]) and (res["coffee"] >= MENU[choi]["ingredients"]["coffee"]):
        return True
    if res["water"] < MENU[choi]["ingredients"]["water"]:
        lack_resources.append("water")
    if res["milk"] < MENU[choi]["ingredients"]["milk"]:
        lack_resources.append("milk")
    if res["coffee"] < MENU[choi]["ingredients"]["coffee"]:
        lack_resources.append("coffee")


def money_cal(menu_choi):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many nickels?: "))
    total_result = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    total_result = round(total_result, 2)
    print(f"You inserted ${total_result}, and {menu_choi} is ${MENU[menu_choi]['cost']}")
    return total_result

def using_resources(res, choi):
    res["water"] = res["water"] - MENU[choi]["ingredients"]["water"]
    res["milk"] = res["milk"] - MENU[choi]["ingredients"]["milk"]
    res["coffee"] = res["coffee"] - MENU[choi]["ingredients"]["coffee"]


should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Case1. report
    if choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

    # Case2. off
    elif choice == "off":
        should_continue = False
        print("The coffee machine turned off.")

    # Case3. menu
    else:
        # Case3-1. menu & enough resources
        if enough_resources(resources, choice):
            total_money = money_cal(choice)
            # Case3-1-1. menu & enough resources & enough money
            if total_money >= MENU[choice]["cost"]:
                if total_money > MENU[choice]["cost"]:
                    change = round(total_money-MENU[choice]['cost'], 2)
                    print(f"Here is ${change} in change.")
                using_resources(resources, choice)
                profit += MENU[choice]["cost"]
                print(f"Here is your {choice} Enjoy!")
            # Case3-1-2. menu & enough resources & not enough money
            else:
                print("Sorry that's not enough money. Money refunded.")

        # Case3-2. menu & not enough resources
        else:
            print(f"Sorry, there is not enough {', '.join(lack_resources)}.")
