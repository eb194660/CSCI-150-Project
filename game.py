#Emma Braddock
#10/13/25
#CSCI 150

"""Imports gamefunctions.py and uses those functions to create a user-engaging game.

4 functions are called from gamefunctions.py to take a user from being welcomed, to being
assigned a monster, viewing a menu, and purchasing items from that menu.
First, the user is prompted for their name and favorite number and a welcome statement is
printed using the gamefunctions.py print_welcome function.
Second, the user is assigned a random monster through the gamefunctions.py new_random_monster function
Third, user purchases items from the shop.
"""

from gamefunctions import *

#first, welcoming the user with print_welcome funtion
user_name = input("What is your name?:")
format_width = input("What is your favorite number between 10-50?:")
print()
print_welcome(name = user_name, width = format_width)
print()

#second, assigning user a random monster using new_random_monster_function
my_monster = new_random_monster()
print(my_monster["description"])
print()
print("Your character is the . . .")
print(my_monster["name"])
print()
print("Here is a little more information . . .")
print(f"health: {my_monster["health"]}")
print(f"money: {my_monster["money"]}")
print(f"power: {my_monster["power"]}")
print()

#third, user purchase items from the shop using print_shop_menu and purchase_item functions
print("Now, to prepair for battle  . . . Let's go shopping!")
print()
print("Let's take a look at the shop menu.")
print_shop_menu(item1Name = "Extra Health", item1Price = 100, item2Name = my_monster["power"], item2Price = 200)
print()
print("Use your money to purchase some Extra Health.")
user_purchase = input("How much extra health would you like to purchase:")
print("Your items purchased and remaining money are shown bellow:")
print(purchase_item(item_price = 100, starting_money = int(my_monster["money"]), quantity_to_purchase = int(user_purchase)))
