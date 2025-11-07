# CSCI 150
# Emma Braddock
# semester game project

"""A module that contains functions for budgets, monsters, and menues.

There are 4 functions in this module. The purchase_item function takes
three conditions, item_price, starting_money, quantity_to_purchase, then
outputs the number_purchased and remaining money. The new_random_monster function
takes no inputs, but when called, returns a random monester out of four choices
and contains the name, description, health, money and power. The print_welcome function
take 2 paramiters, user_name and width, and formats "Hello, user_name" centered
to the desired width and returns None. The print_shop_menue function takes in
the price and name of 2 items and makes formated menue, also returning none."""

import random

def purchase_item (item_price, starting_money, quantity_to_purchase = 1):
    """
    Items purchased and remaining money.

    Parameter:
        item_price(str): price of item
        starting_money(str): budget
        quantity_to_purchase(int): how many items you want to purchase

    Returns:
        num_purchased(int), leftover_money(int)

    Example:
        purchase_item(3, 35, 10)
        10, 5
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


def new_random_monster():
    """
    Creates a random monster.

    Parameters:
        None

    Returns:
        name, description, health, power, and money

    Example:
        new_random_monster()
        'name': kermit, 'description': This is the wild kermit that feeds off the fear of
        missing a sale on athletic wear., 'health': 100, 'money': 800, 'power': super singing
        
    """

    value = random.randint(1,4)
    
    if value == 1:
        name = "Gleb"
        description = "Gleb is a three time mirror ball champion."
        health = 10
        money = 800
        power = "samba"
        
    elif value == 2:
        name = "Val"
        description = "Known for pushing his partners to sucess!"
        health = 9
        money = 500
        power = "choreography"
        
    elif value == 3:
        name = "Pasha"
        description = "The silent winner."
        health = 12
        money = 15
        power = "lifts"

    elif value == 4:
        name = "Jan"
        description = "The new pro that is steeling the show!"
        health = 15
        money = 300
        power = "spins"

    return {"name": name, "description": description, "health": health, "money": money, "power": power}


def print_welcome (name, width):
    """
    Center-formatted user welcome.

    Parameteres:
        user_name(str): enter a name
        width (int): the width for the name to be centered in

    Returns:
        None

    Example:
        print_welcome(Emma, 30)
                 Hello, Emma          
    """

    name_formated = f"Hello, {name}"
    print(f"{name_formated:^{width}}")
    return None


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Formatted shop menue for 2 items.

    Parameters:
        item1Name(str): name of item
        item1Price(int): cost of item
        item2Name(str): name of item
        item2Price(int): cost of item

    Returns:
        None

    Example:
        print_shop_menue("Shoes", 45, "Socks", 3.59)
        /----------------------\
        | Shoes         $45.00 |
        | Socks          $3.59 |
        \\----------------------/
     """
    
    price_1_format = f"${item1Price:.2f}"
    price_2_format = f"${item2Price:.2f}"
    print("/----------------------\\")
    print(f"| {item1Name:<12}{price_1_format:>8} |")
    print(f"| {item2Name:<12}{price_2_format:>8} |")
    print("\\----------------------/")
    return None

def test_functions():
    print("Testing purchase_item function by calling three times:")
    purchaseTest1 = purchase_item(3, 35, 10)
    purchaseTest2 = purchase_item(341, 2112)
    purchaseTest3 = purchase_item(123, 201, 3)
    print (purchaseTest1)
    print (purchaseTest2)
    print (purchaseTest3)
    
    print("Testing new_random_monster funtion by calling three times:")
    monsterTest1 = new_random_monster()
    monsterTest2 = new_random_monster()
    monsterTest3 = new_random_monster()
    print(monsterTest1)
    print(monsterTest2)
    print(monsterTest3)

    print("Testing print_menu funtion by calling three times:")
    print_welcome("Emma", 30)
    print_welcome("Eli", 45)
    print_welcome("Milo", 20)

    print("Testing print_shop_menu funtion by calling three times:")
    print_shop_menu("Shoes", 45, "Socks", 3.59)
    print_shop_menu("Eggs", 9.99, "Butter", 2)
    print_shop_menu("Skis", 1000, "Gloves", 45)

if __name__ =='__main__':
    test_functions()


