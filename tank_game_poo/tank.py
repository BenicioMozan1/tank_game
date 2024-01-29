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
        #spawn_bullet()
        print(f"\n{self.player}'s Tank has tried to shoot {enemy_tank.get_tank_name()}'s tank!")
        shot_possibilities = random.randint(1,3)
        match shot_possibilities:
            case 1:
                print(f"Ops, {self.player} missed the shot!\n")
            case 2:
                print("The shot hit the wall and destroyed it!\n")
                #wall.remove()
            case 3:
                enemy_tank.health_points -= 1 
                print(f"The shot killed {enemy_tank.get_tank_name()}'s tank!!!\n")
                #enemy_tank.kill()
                
             
            

                

    


