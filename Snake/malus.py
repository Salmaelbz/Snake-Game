from boLus import BoLus

class Malus(BoLus):
    def __init__(self):
        BoLus.__init__(self,(255,255,0))
        self.mort = 0
            
    def placer(self, dt,temps,serpent):
        BoLus.placer(self,dt,temps) 
        if self.intersection(serpent):  
            self.mort = 1
            self.apparition = 0 
            self.temps = 0 
            self.square.x = -20
            self.square.y = -20
            self.change = True         
        
        