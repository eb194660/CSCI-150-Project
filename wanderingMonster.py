import time
import random

class WanderingMonster:

    def __init__(self):
        value = random.randint(1,4)
        if value == 1:
            self.name = "Bruno"
            self.energy = 5
            self.value = "yellow"
            self.color = (255, 255, 0)
            self.location = [random.randint(0, 9), random.randint(0, 9)]
            
        elif value == 2:
            self.name = "Carrie"
            self.energy = 8
            self.value = "pink"
            self.color = (255, 192, 203)
            self.location = [random.randint(0, 9), random.randint(0, 9)]
            
        elif value == 3:
            self.name = "Glen"
            self.energy = 7
            self.value = "purple"
            self.color = (160, 32, 240)
            self.location = [random.randint(0, 9), random.randint(0, 9)]

        elif value == 4:
            self.name = "Derek"
            self.energy = 6
            self.value = "blue"
            self.color = (0, 0, 255)
            self.location = [random.randint(0, 9), random.randint(0, 9)]
        
