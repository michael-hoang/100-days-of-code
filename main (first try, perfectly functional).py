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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cash_drawer = 0

def check_resources(coffee_selection, menu_recipes, ingredients_available):
    """Function that passes customer's coffee selection, checks and returns if 
    resources are sufficient. Also returns unavailable ingredients if any."""
    for coffee in menu_recipes:
        if coffee == coffee_selection:
            num_ingredients_needed = len(menu_recipes[coffee]["ingredients"])
            num_ingredients_avail = 0
            insufficient_ingredients = []
            for ingredient in menu_recipes[coffee]["ingredients"]:
                if ingredients_available[ingredient] >= menu_recipes[coffee]["ingredients"][ingredient]:
                    num_ingredients_avail += 1
                else:
                    insufficient_ingredients.append(ingredient)
            if num_ingredients_needed == num_ingredients_avail:
                return True, "none"
            else:
                return False, insufficient_ingredients

def process_coins(coffee_selection, quarters, dimes, nickels, pennies, menu_prices):
    """Function that processes coins and returns change if successful."""
    # Convert number of coins to its dollar value, and then calculate total.
    quarters_value = quarters * .25
    dimes_value = dimes * .10
    nickels_value = nickels * .05
    pennies_value = pennies * .01
    total_dollars = quarters_value + dimes_value + nickels_value + pennies_value
    coffee_cost = menu_prices[coffee_selection]["cost"]
    if total_dollars >= coffee_cost:
        change = round(total_dollars - coffee_cost, 2)
        return change, coffee_cost
    else:
        return 0, 0

coffee_machine_running = True
while coffee_machine_running:
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "report":
        for resource in resources:
            if resource != "coffee":
                print(f"{resource.title()}: {resources[resource]}ml")
            else:
                print(f"{resource.title()}: {resources[resource]}g")
        print(f"Money: ${cash_drawer}")
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        resources_availability, insufficient_ingredients = check_resources(selection, MENU, resources)
        if resources_availability:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))
            change, revenue = process_coins(selection, quarters, dimes, nickels, pennies, MENU)
            # If transaction is successful (revenue is not zero)
            if revenue != 0:
                # Add customer's money inside cash drawer.
                cash_drawer += revenue
                # Make coffee. Subtract ingredients used for making coffee from available resources.
                for ingredient in MENU[selection]["ingredients"]:
                    ingredient_remaining = resources[ingredient] - MENU[selection]["ingredients"][ingredient]
                    resources[ingredient] = ingredient_remaining
                print(f"Here is ${change} in change.")
                print(f"Here is your {selection} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            for ingredient in insufficient_ingredients:
                print(f"Sorry there is not enough {ingredient}.")      
    elif selection == "off":
        coffee_machine_running = False
