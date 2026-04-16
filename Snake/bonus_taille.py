import pyglet
from boLus import BoLus

class Bonus_Taille(BoLus):
    def __init__(self):
        BoLus.__init__(self,(0,0,255))
    
    def placer(self,dt,temps,serpent):
        if(len(serpent.snake))>=10:
            BoLus.placer(self,dt,temps)  
            if self.intersection(serpent):  
                print('+')
                for i in range(0,5):
                    serpent.snake.pop()
                print('+')    
                self.apparition = 0 
                self.temps = 0 
                self.square.x = -20
                self.square.y = -20
                self.change = True 
                