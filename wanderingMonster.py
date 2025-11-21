class WanderingMonster:

    def __init__(self):
        self.location = (0,0)
        self.color = (0,0,0)
        self.name = ""
        
    def new_random_judge(self):
        """Creates a random judge. Parameters: None. Returns: name, energy, color."""

        value = random.randint(1,4)
        
        if value == 1:
            self.name = "Bruno"
            self.energy = 5
            color = "yellow"
            self.color = (255, 255, 0)
            
        elif value == 2:
            self.name = "Carrie"
            self.energy = 8
            color = "pink"
            self.color = (255, 192, 203)
            
        elif value == 3:
            self.name = "Glen"
            self.energy = 7
            color = "purple"
            self.color = (160, 32, 240)

        elif value == 4:
            self.name = "Derek"
            self.energy = 6
            color = blue
            self.color = (0, 0, 255)

        return {"name": self.name, "energy": self.energy, "color": color}

    def monster_map_moves(self):
        
        monster1 = pygame.Rect(80,80,32,32)
        monsterspeed = 3
        pygame.draw.rect(screen, self.color, monster1)
        key = pygame.key.get_pressed()
        key_press_count = 0
        if key[pygame.K_UP]:
            key_press_count += 1
            if key_press_count % 2 ==0:
                for self.location in range(768, 568):
                    self.location = random.randint(-mosterspeed, monsterspeed)
                    monster1.move_ip(self.location)
        elif key[pygame.K_DOWN]:
            key_press_count += 1
            if key_press_count % 2 ==0:
                for self.location in range(768, 568):
                    self.location = random.randint(-mosterspeed, monsterspeed)
                    monster1.move_ip(self.location)
        elif key[pygame.K_LEFT]:
            key_press_count += 1
            if key_press_count % 2 ==0:
                for self.location in range(768, 568):
                    self.location = random.randint(-mosterspeed, monsterspeed)
                    monster1.move_ip(self.location)
        elif key[pygame.K_RIGHT]:
            key_press_count += 1
            if key_press_count % 2 ==0:
                for self.location in range(768, 568):
                    self.location = random.randint(-mosterspeed, monsterspeed)
                    monster1.move_ip(self.location)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                    
        if player.colliderect(monster1):
            running = False
            user_battle()
