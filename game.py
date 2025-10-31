#Emma Braddock
#10/23/25
#CSCI 150

"""Imports gamefunctions.py and uses those functions to create a user-engaging game.

Function town_start_loop is the main page loop.The user can either fight, sleep, or quit. If fight is chosen,
user_battle_loop is started and ends when the user flees or dies, return user to the town_start_loop.
"""

from gamefunctions import *

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
print(f"energy: {my_monster["health"]}")
print(f"sparkle: {my_monster["money"]}")
print(f"signature move: {my_monster["power"]}")
print()

#loops section starts, main loop and fight scene loops

def user_battle():
    user_health = my_monster["health"]
    user_money = my_monster["money"]
    pro_health = 10
    all_damage = 5
    print("You have chosen to enter into a ballroom dance battle with the pros")
    print("With each perfected samba roll, you decrease the pro's energy by 5, and they do the same to you.")

    while user_health > 0 and pro_health > 0:
        user_action = input("You can 1)samba roll  2)use special item 3)chassé away :")

        if user_action == "1":
            user_health -= all_damage
            pro_health -= all_damage
            print(f"Pro's energy: {pro_health} Your energy: {user_health}")

        elif user_action == "2":
            if user_inventory == "waltz":
                pro_health -= 2
                print(f"Pro's energy: {pro_health} Your energy: {user_health}")

            elif user_inventory == "jazz":
                pro_health = 0

            else:
                print("You do not have special items. Go to store to purchase them.")
                user_battle()
                
        

        elif user_action == "3":
            print("Better luck next time, you chassed away.")
            town_start()
            

        else:
            print("Unrecognized command, You can 3)samba roll or 4)chasse away")

    if user_health <= 0:
        print("You passed out on the dance floor :(")
        town_start()
        
    if pro_health <= 0:
        user_money += 3
        print(f"You have bested the Pros! Your sparkle: {user_money}")
        town_start()

    
    
def town_start():
    """Prints the home page as the main loop"""
    user_health = my_monster["health"]
    user_money = my_monster["money"]
    print()
    print("You are in the studio.")
    print(f"Current energy: {user_health}, Current sparkle: {user_money}")
    print("What would you like to do?")
    print(f"1) Leave town (ballroom battle)")
    print(f"2) Sleep (Restore energy for 5 sparkles)")
    print(f"3) Train (new moves for battle)")
    print(f"4) Quit")
    print()
    user_choice = input("What do you choose?:")
    user_choice_int = int(user_choice)

    if 1 < user_choice_int > 4:
        print("That is not an option, please choose 1, 2, or 3.")
        town_start()

    elif user_choice_int == 1:
       user_battle()

    elif user_choice_int == 2:
        user_health = my_monster["health"] +5
        print("Your energy is:", user_health)
        town_start()

    elif user_choice_int == 3:
        user_inventory = []
        train_inventory = [
            {"move" : "waltz", "type" : "dance", "max_uses" : 1, "damage_inflicted" : 2},
            {"move" : "jazz", "type" : "dance", "max_uses" : 1, "note" : "defeats the pros"}
            ]
        print_shop_menu(item1Name= "waltz", item1Price=100, item2Name = "jazz", item2Price=300)
        print("Type item name to select, or studio to return back to the studio")
        user_train = input()
        
        if user_train == "waltz":
            user_money = my_monster["money"] - 100
            user_inventory.append(train_inventory[0])
            print("You are now able to use the following in battle:")
            print(user_inventory)
            print(f"Your remaining sparkles: {my_monster["money"]}")
            
            town_start()

        elif user_train == "jazz":
            user_money = my_monster["money"] - 300
            user_inventory.append(train_inventory[1])
            print("You are now able to use the following in battle:")
            print(user_inventory)
            print(f"Your remaining sparkles: {my_monster["money"]}")
            town_start()
            
        elif user_train == "studio":
            town_start()

        else:
            print("Unregistered command")
            town_start()

    elif user_choice_int == 4:
        return None

    else:
        print("Unrecognized command. Please choose 1, 2, or 3.")
        town_start()

        

town_start()

    




