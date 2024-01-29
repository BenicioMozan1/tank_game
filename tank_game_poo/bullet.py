import random
from tank import Tank

class Bullet:
    def __init__(self, damage):
        self.damage = damage
        

    def spawning_bullet(self):
       bullet_chance = random.randint(1,3)
       match bullet_chance:
            case 1:
               self.damage = 1
            case 2:
               self.damage = 2
            case 3:
               self.damage = 3
    
   
        
        
               
               
            
    
   

        
