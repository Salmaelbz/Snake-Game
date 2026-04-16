import pyglet 

class Score:
    def __init__(self):
        self.score = pyglet.text.Label("0",x=630,y=470,anchor_x="right",anchor_y="top")
        self.une_sec = 0
 
    def update(self, dt):
        self.une_sec += dt
        if  self.une_sec >= 1:
            self.une_sec -= 1
            self.score.text = str(int(self.score.text) + 1)   
        
    def draw(self):       
        self.score.draw() 