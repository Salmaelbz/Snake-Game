import pyglet
from pyglet.window import key 

from snake import Snake
from score import Score
from apple import Apple
from vie import Vie
from bonus_score import Bonus_Score
from bonus_taille import Bonus_Taille
from malus import Malus


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "Snake")
        
        self.score = Score()
        
        self.vie = Vie()
        
        self.plafond = pyglet.shapes.Line(0, 440, 640, 440, color=(0xFF, 0xFF, 0xFF))
        
        self.snake = Snake()
        
        self.direction_actuelle = [0,0] # stop
        
        self.direction_ancienne = [0,1] # haut 
        
        self.pomme = Apple()
        
        self.bonus_score = Bonus_Score()
        
        self.bonus_taille = Bonus_Taille()
        
        self.malus = Malus()
        
        self.G_O = pyglet.text.Label("",x=320,y=420,font_size = 28,anchor_x="center",anchor_y="center") 
        
        pyglet.clock.schedule_interval(self.update, 1/10)
        
    def update(self, dt):
        if self.direction_actuelle ==[0,0]:
           return 
        self.snake.bouge(self.direction_actuelle)   
        if self.snake.mort() or self.malus.mort == 1:
            self.malus.mort = 0
            self.vie.life()
            if self.vie.vie.text != '0':
                self.snake.replacer()
                self.direction_actuelle = [0,0]
                self.pomme.placer_pomme(self.snake)
            else:
                self.G_O = pyglet.text.Label("Game over !",x=320,y=220,font_size = 28,anchor_x="center",anchor_y="center")    
            return  
        self.score.update(dt)
        self.pomme.placer(dt,self.snake,self.score.score) 
        self.bonus_score.placer(dt,30,self.snake,self.score.score)
        self.bonus_taille.placer(dt,10,self.snake)
        self.malus.placer(dt,45,self.snake)
        
    def on_key_press(self, symbol, modifiers):
        if self.direction_actuelle == [0,0]: 
            if symbol == key.SPACE:
                self.direction_actuelle = self.direction_ancienne
            else:
                return
        else: 
            if symbol == key.SPACE:    
                self.direction_ancienne =  self.direction_actuelle
                self.direction_actuelle = [0,0]   
            if symbol == key.UP and self.direction_actuelle != [0,-1]:
                self.direction_actuelle =[0,1] # haut    
            elif symbol == key.DOWN and self.direction_actuelle != [0,1]:
                self.direction_actuelle =[0,-1] # bas    
            elif symbol == key.RIGHT and self.direction_actuelle != [-1,0]:
                self.direction_actuelle =[1,0] # droite
            elif symbol == key.LEFT and self.direction_actuelle != [1,0]:
                self.direction_actuelle =[-1,0] # gauche             
        
    def on_key_release(self, symbol, modifiers):
        pass   
         
    def on_draw(self):
        self.clear()
        self.score.draw()
        self.vie.draw()
        self.plafond.draw()
        if self.G_O.text == '':
            self.snake.draw()    
            self.pomme.draw()
            self.bonus_score.draw()
            self.bonus_taille.draw()
            self.malus.draw()
        self.G_O.draw()
        
        
       
        

      
       