import pyglet
from random import randint

class BoLus:
    def __init__(self, couleur):
        self.color = couleur
        self.square = pyglet.shapes.Rectangle(-20,-20,20,20,self.color)        
        self.apparition= 0
        self.temps = 0
        self.change = True
        
    def intersection(self,serpent):
        x,y =serpent.tete()
        if (x - self.square.x)**2 + (y - self.square.y) **2 < 20**2:
            return True
        else:
            return False      
            
    def placer(self,dt,temps):
        self.apparition += dt
        if self.apparition >= temps:
            if self.change:
                self.square.x = randint(0,620)
                self.square.y = randint(0,420)
                self.change = False
            self.temps +=dt
            if self.temps >= 5:
               self.temps -= 5
               self.square.x = -20 
               self.square.y = -40 
               self.apparition = 0  
               self.change = True    
                
    def draw(self):
        self.square.draw()
        