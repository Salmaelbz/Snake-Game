import pyglet
from boLus import BoLus

class Bonus_Score(BoLus):
    def __init__(self):
        BoLus.__init__(self,(238,130,238))
    
    def placer(self, dt,temps,serpent,score):
        BoLus.placer(self,dt,temps) 
        if self.intersection(serpent):  
            score.text = str(int(score.text) + 10) 
            self.apparition = 0 
            self.temps = 0 
            self.square.x = -20
            self.square.y = -20
            self.change = True 
            