import random

class Tank:
    game_over = False
    def __init__(self, player, health_points):
        self.player = player
        self.health_points = health_points
    
    def get_tank_name(self):
        return self.player
    
    def get_hp(self):
        return self.health_points
    
    def kill_enemy_tank(enemy_tank):
        enemy_tank = 0
    
    def shoot(self, enemy_tank):
        print(f"\n{self.player}'s Tank has tried to shoot {enemy_tank.get_tank_name()}'s tank!\n")
        die_chance = random.randint(1,3)
        match die_chance:
            case 1:
                print("Ops, you missed the shot!\n")
            case 2:
                print("The shot hit the wall an destroyed it!\n")
                #wall.remove()
            case 3:
                print(f"The shot killed {enemy_tank.get_tank_name()}'s tank, you win!!!\n")
                #enemy_tank.kill()
                enemy_tank.health_points -= 1
             
            

                

    


