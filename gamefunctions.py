# CSCI 150
# Emma Braddock
# semester game project

import random

#function 1: prices, items and budgets
#purchase_item prints the number of items purchased and left over money based on user input

def purchase_item (item_price, starting_money, quantity_to_purchase = 1):
    """
    Takes inputs: item price, starting money, and quantity to purchase;
    output how many items were bought and the remaining money.
    """
    
    if item_price > starting_money:
        num_purchased = 0
        leftover_money = starting_money
        
    elif quantity_to_purchase == starting_money // item_price:
        num_purchased = quantity_to_purchase
        leftover_money = 0
        
    elif quantity_to_purchase > starting_money // item_price:
        num_purchased = (starting_money // item_price)
        leftover_money = starting_money - (num_purchased * item_price)

    elif (starting_money // item_price) > quantity_to_purchase:
        num_purchased = quantity_to_purchase
        leftover_money = starting_money - (quantity_to_purchase * item_price)
        
    return num_purchased, leftover_money

#function 2: creates a random monster in dictionary format
#defining the monster characteristics
    
def new_random_monster():
    """ Creates a random monster with no inputs and outputs a name, description, health, power, and money """

    value = random.randint(1,4)
    
    if value == 1:
        name = "kermit"
        description = "This is the wild kermit that feeds off the fear of missing a sale on athletic wear."
        health = 10
        money = 800
        power = "super singing"
        
    elif value == 2:
        name = "hulk"
        description = "So unfortunate ... you have come across the hulk!!!!!!! AHHHHHHHH!!!!!"
        health = 9
        money = 500
        power = "smash"
        
    elif value == 3:
        name = "shrek"
        description = "Watch out! The stinky shrek has crossed your path."
        health = 12
        money = 15
        power: "stinky breath"

    elif value == 4:
        name = "grinch"
        description = "The grinch is running toward you! Don't let him steal your Christmas joy!"
        health = 15
        money = 300
        power = "scarying kids"

    return {"name": name, "description": description, "health": health, "money": money, "power": power}

def print_welcome (name, width):
    """Takes inputs "name" and "width" and prints "Hello, user_name" centered by the inputed width"""

    name_formated = f"Hello, {name}"
    print(f"{name_formated:^{width}}")
    return None

def print_shop_menue(item1Name, item1Price, item2Name, item2Price):
    """Takes name and price for two items and prints a formatted sign of the names with prices"""
    price_1_format = f"${item1Price:.2f}"
    price_2_format = f"${item2Price:.2f}"
    print("/----------------------\\")
    print(f"| {item1Name:<12}{price_1_format:>8} |")
    print(f"| {item2Name:<12}{price_2_format:>8} |")
    print("\----------------------/")
    return None

