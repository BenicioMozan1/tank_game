#import random
#import time
from tank import Tank
#from bullet import Bullet
#from map import Map


t1 = Tank("Benicio", 3)
t2 = Tank("JUCIMAR", 3)

game_loop = True


while game_loop:
    t1.shoot(t2)
    if t2.get_hp() == 0:
        game_loop = False
    

       