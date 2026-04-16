from snake import Snake
from score import Score
from apple import Apple
from vie  import Vie
from boLus import BoLus
from bonus_score import Bonus_Score
from bonus_taille import Bonus_Taille
from malus import Malus
import pyglet

def test_position_initiale():
    serpent = Snake()

    assert len(serpent.snake) == 3
    assert serpent.snake[0].x == 640 // 2
    assert serpent.snake[0].y == 440 // 2 # 440 est al hauteur du plafond
    
def test_bouge_droite(): 
    serpent = Snake()
    serpent.snake[0].x = 10
    serpent.snake[0].y = 20
    direction =[1,0]
    serpent.bouge(direction)
    
    assert serpent.snake[0].x == 30
    assert serpent.snake[0].y == 20
    
def test_bouge_gauche(): 
    serpent = Snake()
    serpent.snake[0].x = 10
    serpent.snake[0].y = 20
    direction =[-1,0]
    serpent.bouge(direction)
    
    assert serpent.snake[0].x == -10
    assert serpent.snake[0].y == 20
    
def test_bouge_haut(): 
    serpent = Snake()
    serpent.snake[0].x = 10
    serpent.snake[0].y = 20
    direction =[0,1]
    serpent.bouge(direction)
    
    assert serpent.snake[0].x == 10
    assert serpent.snake[0].y == 40

def test_bouge_bas():
    serpent = Snake()
    serpent.snake[0].x = 10
    serpent.snake[0].y = 20
    direction =[0,-1]
    serpent.bouge(direction)
    
    assert serpent.snake[0].x == 10
    assert serpent.snake[0].y == 0

def test_tete():
    serpent = Snake()    
    x,y = serpent.tete()
    
    assert x == serpent.snake[0].x 
    assert y == serpent.snake[0].y 
    
def test_se_mord_False():
    serpent = Snake()
    
    assert serpent.se_mord() == False
    
def test_se_mord_True():    
    serpent = Snake()
    serpent.snake[0].x = serpent.snake[1].x
    serpent.snake[0].y = serpent.snake[1].y
    
    assert serpent.se_mord() == True
    
def test_mort_False():
    serpent = Snake()     
    
    assert serpent.mort() == False
    
def test_mort_x_négatif():  
    serpent = Snake()
    serpent.snake[0].x = -20
    
    assert serpent.mort() == True 

def test_mort_x_grand():  
    serpent = Snake()
    serpent.snake[0].x = 640
    
    assert serpent.mort() == True 
    
def test_mort_y_négatif():  
    serpent = Snake()
    serpent.snake[0].y = -20
    
    assert serpent.mort() == True    
    
def test_mort_y_grand():  
    serpent = Snake()
    serpent.snake[0].y = 440
    
    assert serpent.mort() == True
    
def test_mort_mord():  
    serpent = Snake()
    serpent.snake[0].x = serpent.snake[1].x
    serpent.snake[0].y = serpent.snake[1].y
    
    assert serpent.mort() == True              
       
def test_score_incremente():
    score = Score()
    score.une_sec = 0.9
    score.update(0.1)
    
    assert int(score.score.text) == 1
    
def  test_intersection_true():
    pomme = Apple()
    serpent = Snake()
    pomme.apple.x = 300
    pomme.apple.y = 220
    
    assert pomme.intersection(serpent.snake[0]) == True
  
def test_intersection_False():
    pomme = Apple()
    serpent = Snake()
    
    assert pomme.intersection(serpent.snake[0]) == False
    
def test_touche_Pomme_True():
    pomme = Apple()
    serpent = Snake()
    x = pomme.apple.x = 300
    y = pomme.apple.y = 220
    
    assert pomme.touche_pomme(serpent,x,y) == True

def test_touche_Pomme_False():   
    pomme = Apple()
    serpent = Snake()
    x = pomme.apple.x = 300
    y = pomme.apple.y
    
    assert pomme.touche_pomme(serpent,x,y) == False
      
    
def test_placer_intersec():
    pomme = Apple()
    serpent = Snake()
    score = Score()
    pomme.apple.x = 300
    pomme.apple.y = 220
    dt = 0.1
    pomme.placer(dt,serpent,score.score)   
    
    assert serpent.taille_cinq == 5
    assert score.score.text == '5'
    assert pomme.apple.x != 300
    assert pomme.apple.y != 220
    
def test_placer_5sec():
    pomme = Apple()
    serpent = Snake()
    score = Score()
    dt = 0.1
    pomme.cinq_sec = 4.9
    pomme.placer_pomme(serpent)  
    
    assert pomme.apple.x != 320
    assert pomme.apple.y != 80
    
def test_life():
    life = Vie()
    life.life()   
    
    assert life.vie.text == '2'    
    
def test_intersection__BoLus_True():
    serpent = Snake()
    bolus = BoLus((255,0,255))
    bolus.square.x = 320
    bolus.square.y = 210
    
    assert bolus.intersection(serpent) == True
       
def test_intersection__BoLus_False():
    serpent = Snake()
    bolus = BoLus((255,0,255))
    
    assert bolus.intersection(serpent) == False
    
def test_placer_Bolus():
    bolus = BoLus((255,0,255))
    serpent = Snake()
    bolus.apparition = 3.9    
    dt = 0.1
    bolus.placer(dt,4)
    
    assert bolus.square.x != -20
    assert bolus.square.y != -20
    
def test_disparaitre_Bolus_5sec():
    bolus = BoLus((255,0,255))
    serpent = Snake()
    bolus.apparition = 3.9    
    dt = 0.1
    bolus.temps = 4.9
    bolus.placer(dt,4)
        
    assert bolus.square.x == -20
    assert bolus.square.y == -40
    
def test_placer_bonus_score_30sec(): 
    bonus_score = Bonus_Score()
    serpent = Snake()
    score = Score()
    dt = 0.1
    bonus_score.apparition = 29.9
    bonus_score.placer(dt,30,serpent,score.score)
    
    assert bonus_score.square.x != -20
    assert bonus_score.square.y != -20
    
def test_placer_bonus_augmenter_score():
    bonus_score = Bonus_Score()
    serpent = Snake()
    score = Score()
    bonus_score.square.x = 320
    bonus_score.square.y = 220
    dt = 0.1
    bonus_score.placer(dt,30,serpent,score.score)
    
    assert score.score.text == '10'
    assert bonus_score.square.x == -20
    assert bonus_score.square.y == -20
    
def test_placer_bonus_taille_10sec():
    bonus_taille = Bonus_Taille()
    serpent = Snake()
    for i in range(3,10):
       serpent.snake.append(pyglet.shapes.Rectangle(20,20, 20, 20)) 
    score = Score()
    dt = 0.1
    bonus_taille.apparition = 9.9
    bonus_taille.placer(dt,10,serpent)
    
    assert bonus_taille.square.x != -20
    assert bonus_taille.square.y != -20    
    
def test_placer_bonus_diminuer_taille():   
    bonus_taille = Bonus_Taille()
    serpent = Snake()
    for i in range(3,10):
       serpent.snake.append(pyglet.shapes.Rectangle(320,420 - i*20, 20, 20)) 
    bonus_taille.square.x = 320
    bonus_taille.square.y = 220
    dt = 0.1
    bonus_taille.placer(dt,10,serpent)
    
    assert len(serpent.snake) == 5
    assert bonus_taille.square.x == -20
    assert bonus_taille.square.y == -20 
    
def test_placer_malus_45sec():
    malus = Malus()
    serpent = Snake()
    dt = 0.1
    malus.apparition = 44.9
    malus.placer(dt,45,serpent)
    
    assert malus.square.x != -20
    assert malus.square.y != -20      
    
def test_placer_malus_mort():
    malus = Malus()
    serpent = Snake()
    dt = 0.1
    malus.square.x = 320
    malus.square.y = 220
    malus.placer(dt,45,serpent)     
    
    assert malus.mort == 1
    
