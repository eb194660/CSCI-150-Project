#Emma Braddock
#10/23/25
#CSCI 150

"""Imports gamefunctions.py and uses those functions to create a user-engaging game.

Function town_start is the main page loop.The user can either fight, sleep, shop, or quit. If fight is chosen,
user_battle_loop is started and ends when the user flees or dies, return user to the town_start loop.
"""

from gamefunctions import *
user_stats = {"energy" : 15, "sparkle" : 350}
user_inventory = []

#first, welcoming the user with print_welcome funtion
user_name = input("What is your name?:")
print()
print_welcome(name = user_name, width = 40)
print()

#second, assigning user a random monster using new_random_monster_function
my_monster = new_random_monster()
print("You have been chosen to compete on this season's Dancing with the Stars!")
print(my_monster["description"])
print()
print("Your partner is the . . .")
print(my_monster["name"])
print()
print("Here is a little more information . . .")
print(f"energy: {user_stats["energy"]}")
print(f"sparkle: {user_stats["sparkle"]}")
print(f"signature move: {my_monster["power"]}")
print()

def user_shopping():
    """Allows user to purchase inventory items"""
    train_inventory = [
        {"move" : "waltz", "type" : "dance", "max_uses" : 1, "damage_inflicted" : 2},
        {"move" : "jazz", "type" : "dance", "max_uses" : 1, "damage_inflicted" : "total"}
        ]
    print_shop_menu(item1Name= "waltz", item1Price=100, item2Name = "jazz", item2Price=300)
    print("Type item name to select, or studio to return back to the studio")
    user_train = input()
                
    if user_train == "waltz":
        user_stats["sparkle"] -= 100
        user_inventory.append(train_inventory[0])
        print("You are now able to use the following in battle:")
        print(user_inventory)
        print(f"Your remaining sparkles: {user_stats["sparkle"]}")
            
                
    elif user_train == "jazz":
        user_stats["sparkle"] -= 300
        user_inventory.append(train_inventory[1])                
        print("You are now able to use the following in battle:")
        print(user_inventory)
        print(f"Your remaining sparkles: {user_stats["sparkle"]}")

    elif user_train == "studio":
        town_start()

    else:
        print("Unregistered command")
        town_start()

def use_special_item():
    """user selects special item to be used in battle"""
    print(user_inventory)
    user_in_use = input("What item would you like to use? 1) waltz 2) jazz:")
    if user_in_use == "1":
        for item in user_inventory:
             if item["move"] == "waltz":
                    pro_energy -= 2
                    del user_inventory[0]
                    print(f"Pro's energy: {pro_energy} Your energy: {user_stats["energy"]}")

    elif user_in_use == "2":
        for item in user_inventory:
            if item["move"] == "jazz":
                    pro_energy = 0
                    del user_inventory[0]
                    user_stats["sparkle"] += 3
                    print(f"You have bested the Pros! Your sparkle: {user_stats["sparkle"]}")
                    town_start()

    else:
        print("You do not have special items. Go to store to purchase them.")

def user_battle():
    """User fights against pro until one wins.
    Energy is decreased exchangablym witht he option to use invientory items or flee.
    The returns user to town_start."""
    
    user_energy = user_stats["energy"]
    user_sparkle = user_stats["sparkle"]
    pro_energy = 10
    all_damage = 5
    print("You have chosen to enter into a ballroom dance battle with the pros")
    print("With each perfected samba roll, you decrease the pro's energy by 5, and they do the same to you.")

    while user_stats["energy"] > 0 and pro_energy > 0:
        user_action = input("You can 1)samba roll  2)use special item 3)chassé away :")

        if user_action == "1":
            user_stats["energy"] -= all_damage
            pro_energy -= all_damage
            print(f"Pro's energy: {pro_energy} Your energy: {user_stats["energy"]}")

        elif user_action == "2":
            use_special_item()

        elif user_action == "3":
            print("Better luck next time, you chassed away.")
            town_start()
            

        else:
            print("Unrecognized command, You can 3)samba roll 2)use special item 4)chasse away")

    if user_energy <= 0:
        print("You passed out on the dance floor :(")
        town_start()
        
    if pro_energy <= 0:
        user_stats["sparkle"] += 3
        print(f"You have bested the Pros! Your sparkle: {user_stats["sparkle"]}")
        town_start()


def town_choices():
    """prints town welcome and options"""
    print()
    print("You are in the studio.")
    print(f"Current energy: {user_stats["energy"]}, Current sparkle: {user_stats["sparkle"]}")
    print("What would you like to do?")
    print(f"1) Leave town (ballroom battle)")
    print(f"2) Sleep (Restore energy for 5 sparkles)")
    print(f"3) Train (new moves for battle)")
    print(f"4) Quit")
    print()
    print("What do you choose?:")

def town_start():
    """Prints the home page as the main loop"""
    choice = "r"

    while choice != "q":
        town_choices()
        user_choice_int = int(input())
    
        if user_choice_int == 1:
            user_battle()
            
        elif user_choice_int == 2:
            user_stats["energy"] += 5
            print(f"Your energy is: {user_stats["energy"]}")
            town_start()

        elif user_choice_int == 3:
            user_shopping()
            
        elif user_choice_int == 4:
            break
                    
        else:
            print("That is not an option, please choose 1, 2, 3, or 4.")
            

town_start()

    




