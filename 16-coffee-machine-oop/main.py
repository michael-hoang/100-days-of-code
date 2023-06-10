from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# # This part is unnecessary. All of these coffee objects and its attributes are
# # already defined in menu.py
# espresso_object = MenuItem("espresso", 50, 0, 18, 1.50)
# espresso_object.name = "espresso"
# espresso_object.cost = 1.50
# espresso_object.ingredients = {
#     "water": 50,
#     "coffee": 18,
#     }
# latte_object = MenuItem("latte", 200, 150, 24, 2.50)
# cappuccino_object = MenuItem("cappuccino", 250, 100, 24, 3.00)


menu_object = Menu() # create menu object
coffee_maker_object = CoffeeMaker() # create coffee maker object
money_machine_object = MoneyMachine() # create money machine object

coffee_machine_running = True
while coffee_machine_running:
    # Customer picks coffee from menu and stores it in a variable as a string. The 
    # .get_items() method will display the coffee options.
    selection = input(f"What would you like? ({menu_object.get_items()})")

    if selection == "report":
        coffee_maker_object.report()
        money_machine_object.report()
    elif selection == "off":
        coffee_machine_running = False
    else:
        # Selection string is passed through .find_drink() method to see if drink is
        # available on the menu. Returns object and stores it in a variable called 
        # 'on_menu' if drink is available. Else the method .find_drink() will print 
        # "Sorry that item is not available."
        on_menu = menu_object.find_drink(selection)

        # If coffee is on the menu, check if there is enougoh resources to make the drink
        # by passing coffee object (on_menu) into the method called 'is_resource_sufficient'.
        # Returns True if there is sufficient resources, else returns False.
        enough_resources = coffee_maker_object.is_resource_sufficient(on_menu)

        # If and only if there is enough resources to make the coffee, ask customer 
        # to put in coins into the vending machine. Pass the cost attribute for the 
        # coffee object (on_menu) into the method .make-payment(). Returns True 
        # if enough money is inserted and keeps track of profits. Else returns 
        # False and refunds the money. Store this return boolean value in a variable 
        # called enough_money.
        if enough_resources:
            enough_money = money_machine_object.make_payment(on_menu.cost)

            # If enough money is inserted, make the drink! Pass the coffee object (on_menu) 
            # into the method .make_coffee(). It will deduct resources needed from the
            # available resources and gives coffee to customer.
            if enough_money:
                your_coffee = coffee_maker_object.make_coffee(on_menu)


# ## ALTERNATIVELY...    

#         # The second operand (money_machine_object.make_payment(on_menu.cost)) won't
#         # evaluate if the first operand (coffee_maker_object.is_resource_sufficient(on_menu)) 
#         # is False. This is called Short Circuit Evaluation. 
#         if coffee_maker_object.is_resource_sufficient(on_menu) and money_machine_object.make_payment(on_menu.cost):
#             # If there is enough resources and money, make the drink! Pass the 
#             # coffee object (on_menu) into the method .make_coffee(). It will deduct 
#             # resources needed from the available resources and gives coffee to customer.
#             your_coffee = coffee_maker_object.make_coffee(on_menu)