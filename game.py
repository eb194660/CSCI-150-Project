#Emma Braddock
#10/23/25
#CSCI 150

"""Imports gamefunctions.py and uses those functions to create a user-engaging game.

4 functions are called from gamefunctions.py to take a user from being welcomed, to being
assigned a monster, viewing a menu, and purchasing items from that menu.
First, the user is prompted for their name and favorite number and a welcome statement is
printed using the gamefunctions.py print_welcome function.
Second, the user is assigned a random monster through the gamefunctions.py new_random_monster function
Third, user purchases items from the shop.

Then, function town_start_loop is the main page loop.The user can either fight, sleep, or quit. If fight is chosen,
user_battle_loop is started and ends when the user flees or dies, return user to the town_start_loop.
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

#loops section starts, main loop and fight scene loops

def user_battle():
    user_health = 10
    bruno_health = 10
    all_damage = 5
    user_gold = 10
    print("You have chosen to enter into battle")
    print("With each perfected samba roll, you decrease your opponents health by 5.")

    while user_health > 0 and bruno_health > 0:
        user_action = input("You can 3)samba roll or 4)chasse away :")

        if user_action == "3":
            user_health -= all_damage
            bruno_health -= all_damage

        elif user_action == "4":
            print("Better luck next time, you chassed away.")
            break

        else:
            print("Unrecognized command, You can 3)samba roll or 4)chasse away")

    if user_health <= 0:
        print("You passed out on the dance floor :(")
        
        
    if bruno_health <= 0:
        user_gold += 3
        

    
    
def town_start():
    """Prints the home page as the main loop"""
    my_health = my_monster["health"]
    print()
    print("You are in town.")
    print(f"Current Health: {my_health}, Current Gold: 10")
    print("What would you like to do?")
    print(f"1) Leave town (fight monster)")
    print(f"2) Sleep (Restore Health for 5 Gold)")
    print(f"3) Quit")
    print()
    user_choice = input("What do you choose?:")
    user_choice_int = int(user_choice)

    if 1 < user_choice_int > 3:
        print("That is not an option, please choose 1, 2, or 3.")
        town_start()

    elif user_choice_int == 3:
        return None
    
    elif user_choice_int == 2:
        print("Your health is:", my_health + 5)
        my_health = my_monster["health"] + 5
        town_start()

    elif user_choice_int == 1:
       user_battle()
        

town_start()

    




