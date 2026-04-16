import pyglet
from random import randint

class Apple:
    def __init__(self):
        self.apple = pyglet.shapes.Circle(320,80,radius=40,color=(254,27,0))
        self.cinq_sec = 0
        
    def intersection(self, tete):
        x = tete.x
        y = tete.y
        if (x-self.apple.x)**2 + (y - self.apple.y)**2 <= 40**2:  
            return True
        else:
            return False
        
    def touche_pomme(self, serpent, x,y):
        for i in range(1, len(serpent.snake)):
            if (x-serpent.snake[i].x)**2 + (y - serpent.snake[i].y)**2 <= 45**2:
                return True
        return False    
                   
    def placer_pomme(self,serpent):
        x = randint(40,600)
        y = randint(40,400)
        while self.touche_pomme(serpent, x,y):
            x = randint(40,600)
            y = randint(40,400)
        self.apple = pyglet.shapes.Circle(x,y,radius=40,color=(254,27,0))    
                               
    def placer(self,dt,serpent,score):
        self.cinq_sec += dt
        if  self.intersection(serpent.snake[0]):   
            serpent.taille_cinq +=5
            score.text = str(int(score.text) + 5) 
            self.cinq_sec = 0  
            self.placer_pomme(serpent)
        elif self.cinq_sec >= 5:
            self.cinq_sec -= 5    
            self.placer_pomme(serpent)
        
    def draw(self):       
        self.apple.draw()    
    
