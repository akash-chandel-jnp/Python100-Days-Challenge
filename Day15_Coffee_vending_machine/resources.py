from menu_and_ingredients import ingredients_list
from money_and_coins import money_balance

resources_rem = {
    "water": 400,
    "milk": 300,
    "coffee": 200,
}

# Checking whether resources are sufficient or not
# TODO 4: Check resources sufficient?
"""a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""


def check_resources_sufficiency(drink_name):
    # print("checking resources")
    is_resource_sufficient = True
    for ingrd_name in ingredients_list[drink_name]["ingredients"]:
        ingr_needed = ingredients_list[drink_name]["ingredients"][ingrd_name]
        if resources_rem[ingrd_name] < ingr_needed:
            print("enough is")
            is_resource_sufficient = False

    return is_resource_sufficient


def print_report():
    print("The current resource values are : ")
    print(f"Water: {resources_rem['water']}ml")
    print(f"Milk: {resources_rem['milk']}ml")
    print(f"Coffee: {resources_rem['coffee']}g")
    print(f"Remaining Resources: {resources_rem}")
    print(f"Money balance : ${money_balance}")


def update_resources(drink_chosen):
    for ingrd_name in ingredients_list[drink_chosen]["ingredients"]:
        resources_rem[ingrd_name] -= ingredients_list[drink_chosen]["ingredients"][ingrd_name]

    print_report()
