import pyglet

class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            self.snake.append(pyglet.shapes.Rectangle(640//20//2*20,440//20//2*20 - i * 20, 20, 20, color = (154, 205, 50)))
        self.taille_cinq = 0    
        
    def bouge(self, direction):
        x = self.snake[0].x + 20 * direction[0]
        y = self.snake[0].y + 20 * direction[1]
        dernier_x = self.snake[len(self.snake) - 1].x
        dernier_y = self.snake[len(self.snake) - 1].y
        i = len(self.snake) - 1
        while i > 0:
            self.snake[i].x = self.snake[i-1].x
            self.snake[i].y = self.snake[i-1].y
            i -=1
        self.snake[0].x = x 
        self.snake[0].y = y   
        if self.taille_cinq > 0:
            self.taille_cinq -= 1
            self.snake.append(pyglet.shapes.Rectangle(dernier_x,dernier_y, 20, 20, color = (154, 205, 50)))
        
    def tete(self):
        return self.snake[0].x, self.snake[0].y      
         
    def se_mord(self):
        x,y = self.tete()
        for i in range(1, len(self.snake)):
            if (x == self.snake[i].x) and (y == self.snake[i].y):
                return True
        return False 
        
    def mort(self):
        x,y = self.tete()
        if x < 0:
            return True
        elif x + 20 > 640:
            return True
        elif y < 0:   
            return True
        elif y + 20 > 440:
            return True
        elif self.se_mord():
            return True
        else:
            return False 
        
    def replacer(self):
        self.snake[0].x = 640//20//2*20
        self.snake[0].y = 0
        for i in range(1,len(self.snake)):
            self.snake[i].x = 640//20//2*20
            self.snake[i].y = - i * 20
          
    def draw(self):
        for cell in self.snake:
            cell.draw()        