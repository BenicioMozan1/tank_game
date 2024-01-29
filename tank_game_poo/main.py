#import random
import time
from tank import Tank
#from bullet import Bullet
from map import Map

#map_walls = []
#map_walls.append(Map.walls)

t1 = Tank("BENICIO", 1)
t2 = Tank("JUCIMAR", 1)

game_loop = True


while game_loop:
    player2_turn = 0
    player1_turn = 0
    
    print(f"\nPLAYER 1 TURN. \n")
    player1_turn = input("PRESS (S) TO SHOOT A BULLET:\n").upper()
    if player1_turn == "S":
        t1.shoot(t2)
        time.sleep(1)
    if t2.get_hp() == 0:
        print(f"{t1.get_tank_name()} WIN!")
        game_loop = False
        break
    
    print(f"\nPLAYER 2 TURN. \n")
    player2_turn = input("PRESS (S) TO SHOOT A BULLET:\n").upper()
    if player2_turn == "S":
        t2.shoot(t1)
        time.sleep(1)
    if t1.get_hp() == 0:
        print(f"{t2.get_tank_name()} WIN!")
        game_loop = False
        break
    
    

       