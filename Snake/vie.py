import pyglet
 
class Vie:
    def __init__(self):
        self.vie = pyglet.text.Label("3",x=10,y=470,anchor_x="left",anchor_y="top")
        
    def life(self):
        if self.vie.text != '0':
            self.vie.text = str(int(self.vie.text) - 1)  
        
    def draw(self):       
        self.vie.draw()     
            
         