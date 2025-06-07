import pygame
import pgzrun
from random import randint
TITLE = "Ash and Pikachu"
WIDTH = 600
LENGTH = 500
SCORE  = 0
game_over = False
ash = Actor("ash",(100,100))
pikachu = Actor("pikachu")
pikachu.pos = 200,200

def draw():
    screen.blit("background",(0,0))
    ash.draw()
    pikachu.draw()
    screen.draw.text("SCORE: "+ str(score),color = "blue",topleft = (50,50))

    if game_over:
        screen.fill("red")
        screen.draw.text("Your score is: "+ str(score),color = "red",topleft = (50,50),fontsize = 50)


def place():
    flower.x = randint(50,WIDTH-50)
    flower.y = randint(50,HEIGHT-50)
def time_up():
    global game_over
    game_over = True    

def update():
    global score
    if keyboard.left:
        ash.x -= 4
    if keyboard.right:
        ash.x += 4
    if keyboard.up:
        ash.y -= 4
    if keyboard.down:
        ash.y += 4

    pikachu = ash.colliderect(pikachu)
    if pikachu:
        score+=10
        place()

clock.schedule(time_up,60)

    
pgzrun.go()


