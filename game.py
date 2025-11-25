#Emma Braddock
#10/23/25
#CSCI 150

"""Imports gamefunctions.py and uses those functions to create a user-engaging game.

Function town_start is the main page loop.The user can either fight, sleep, shop, or quit. If fight is chosen,
user_battle_loop is started and ends when the user flees or dies, return user to the town_start loop.
"""

from gamefunctions import *
from wanderingMonster import *
import json
import math
import pygame
import time
    
    

def user_shopping():
    """Allows user to purchase inventory items"""
    train_inventory = [
        {"move" : "waltz", "type" : "dance", "max_uses" : 1, "damage_inflicted" : 2},
        {"move" : "jazz", "type" : "dance", "max_uses" : 1, "damage_inflicted" : "total"}
        ]
    print_shop_menu(item1Name= "waltz", item1Price=100, item2Name = "jazz", item2Price=300)
    print("Type item name to select, or studio to return back to the studio")
    user_train = input()


    if user_stats["sparkle"] >= 300:
        
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
            print("unregistered command")
            
    elif 299 <= user_stats["sparkle"] >= 100:
        
        if user_train == "waltz":
            user_stats["sparkle"] -= 100
            user_inventory.append(train_inventory[0])
            print("You are now able to use the following in battle:")
            print(user_inventory)
            print(f"Your remaining sparkles: {user_stats["sparkle"]}")

        elif user_train == "jazz":
            print("You do not have enough sparkle. Rest or win dance battles to get more sparkle.")
            
        elif user_train == "studio":
            town_start()

        else:
            print("unregistered command")


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
    """User is taken to map. If user choses green circle, they are returned to the towm,
    or the red circle they fight against pro until one wins.
    Energy is decreased exchangably with the option to use invientory items or flee.
    The returns user to town_start."""
    Wandering_monster = WanderingMonster()
    user_energy = user_stats["energy"]
    user_sparkle = user_stats["sparkle"]
    pro_energy = Wandering_monster.energy
    pro_name = Wandering_monster.name
    pro_color = Wandering_monster.value
    all_damage = 5
    print(f"You have entered into a ballroom dance battle with judge {pro_name} shown in {pro_color}.{pro_name}'s energy: {pro_energy}.")
    print(f"With each perfected samba roll, you decrease {pro_name}'s energy by 5, and they do the same to you.")

    while user_stats["energy"] > 0 and pro_energy > 0:
        user_action = input("You can 1)samba roll  2)use special item 3)chassé away :")

        if user_action == "1":
            user_stats["energy"] -= all_damage
            pro_energy -= all_damage
            print(f"{pro_name}'s energy: {pro_energy} Your energy: {user_stats["energy"]}")

        elif user_action == "2":
            use_special_item()

        elif user_action == "3":
            print("Better luck next time, you chassed away.")
            break #ends battle loop
            town_start(user_stats)
            

        else:
            print("Unrecognized command, You can 3)samba roll 2)use special item 4)chasse away")

    if user_energy <= 0:
        print("You passed out on the dance floor :(")
        town_start(user_stats)
        
    if pro_energy <= 0:
        user_stats["sparkle"] += 3
        print(f"You have bested {pro_name}! Your sparkle: {user_stats["sparkle"]}")
        town_start(user_stats)

def coordinate_to_pixel(coordinates):
    return coordinates[0] * 32, coordinates[1] * 32
        
def battle_map(game_stats):
    print("The green circle returns you to the studio. The other circles are pros and will take you to the dance competition.")
    time.sleep(.5)
    pygame.init()

    SCREEN_WIDTH = 320
    SCREEN_HEIGHT = 320

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = pygame.Rect(32* game_stats["location"][0],32* game_stats["location"][1],32,32)
    mask_surface = pygame.Surface((50,50))
    monsters = []
    town = (300, 300)
    
    running = True
    while running:
        if len(monsters) == 0:
            monsters.append(WanderingMonster())
            monsters.append(WanderingMonster())
        screen.fill((0,0,0))
        player.update(coordinate_to_pixel(game_stats["location"]), (32, 32))
        pygame.draw.rect(screen, (128, 128, 128), player)
        pygame.draw.circle(screen, (0, 255, 0), town, 20)
        for monster in monsters:
            pygame.draw.circle(screen, monster.color, coordinate_to_pixel(monster.location), 20)
  

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if user_stats["location"][1] > 0:
                        user_stats["location"][1] -= 1
                elif event.key == pygame.K_DOWN:
                    if user_stats["location"][1] < 9:
                        user_stats["location"][1] += 1
                elif event.key == pygame.K_LEFT:
                    if user_stats["location"][0] > 0:
                        user_stats["location"][0] -= 1
                elif event.key == pygame.K_RIGHT:
                    if user_stats["location"][0] < 9:
                        user_stats["location"][0] += 1
                
        if user_stats["location"] == monsters[0].location:
            del monsters[0]
            user_battle()
        elif user_stats["location"] == monsters[1].location:
            del monsters[1]
            user_battle()
        elif user_stats["location"] == [9, 9]:
            pygame.quit()
            town_start(user_stats)
        
        pygame.display.update()
        time.sleep(.01)
    pygame.quit()
    

def town_welcome():
    """prints town welcome"""
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
    
def town_choices():
    """prints town options"""
    print()
    print("You are in the studio.")
    print(f"Current energy: {user_stats["energy"]}, Current sparkle: {user_stats["sparkle"]}")
    print("What would you like to do?")
    print(f"1) Leave town (ballroom battle)")
    print(f"2) Sleep (Restore energy for 5 sparkles)")
    print(f"3) Train (new moves for battle)")
    print(f"4) Save and Quit")
    print()
    print("What do you choose?:")

def town_start(user_stats):
    """Prints the home page as the main loop"""
    choice = "r"

    while choice != "q":
        town_choices()
        user_choice_int = int(input())
    
        if user_choice_int == 1:
            battle_map(user_stats)
            
        elif user_choice_int == 2:
            user_stats["energy"] += 5
            print(f"Your energy is: {user_stats["energy"]}")
            town_start(user_stats)

        elif user_choice_int == 3:
            user_shopping()
            
        elif user_choice_int == 4:
            user_stats_json = json.dumps(user_stats)
            user_inventory_json = json.dumps(user_inventory)
            print("Your progress has been saved. See you next time in the studio.")

            with open("progress_stats", "w") as progressfile:
                progressfile.write(user_stats_json)
                
            with open("progress_inventory", "w") as progressfile:
                progressfile.write(user_inventory_json)
                break #breaks town loop and exits user from game
                
            
                    
        else:
            print("That is not an option, please choose 1, 2, 3, or 4.")

#starts user interface

user_name = input("What is your name?:")
print()
print_welcome(name = user_name, width = 40)
print()

user_data = input("Would you like to start a new project(1) or resume(2)?: ")
choice = "r"
if user_data == "1":
    user_stats = {"energy" : 15, "sparkle" : 350, "location":[0,0]}
    user_inventory = []
    town_welcome()
    town_start(user_stats)

elif user_data == "2":
    with open("progress_stats", "r") as progressfile:
        user_stats_convert = json.loads(progressfile.read())
        user_stats = user_stats_convert

    with open("progress_inventory", "r") as progressfile:
        user_inventory_convert = json.loads(progressfile.read())
        user_inventory = user_inventory_convert
        
    town_start(user_stats)

else:
    print("unregistered command")
                    
                    

    




