import time
import math

class WanderingMonster:

    def __init__(self):
        self.location = (0,0)
        self.color = (0,0,0)
        self.name = ""
        
    def new_random_judge(self):
        """Creates a random judge. Parameters: None. Returns: name, energy, color."""

        value = random.randint(1,4)
        monsterspeed = 3
        if value == 1:
            self.name = "Bruno"
            self.energy = 5
            value = "yellow"
            self.color = (255, 255, 0)
            self.location = (([random.randint(-monsterspeed, monsterspeed) in range (700, 500)]), 50, 50)
            
        elif value == 2:
            self.name = "Carrie"
            self.energy = 8
            value = "pink"
            self.color = (255, 192, 203)
            self.location = (([random.randint(-monsterspeed, monsterspeed) in range (700, 500)]), 50, 50)
            
        elif value == 3:
            self.name = "Glen"
            self.energy = 7
            value = "purple"
            self.color = (160, 32, 240)
            self.location = (([random.randint(-monsterspeed, monsterspeed) in range (700, 500)]), 50, 50)

        elif value == 4:
            self.name = "Derek"
            self.energy = 6
            vale = blue
            self.color = (0, 0, 255)
            self.location = (([random.randint(-monsterspeed, monsterspeed) in range (700, 500)]), 50, 50)

        return {"name": self.name, "energy": self.energy, "color": value, "location": self.location}
        
    
