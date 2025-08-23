import pygame
import pgzrun
import random
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH/2
CENTRE_Y = HEIGHT/2
CENTRE =  (CENTRE_X,CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag","battery","bottle","crisps"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items,current_level,game_over,game_complete
    screen.clear()
    screen.blit("bg",(0,0))
    if game_over:
        display_message("game over","try again")
    elif game_complete:
        display_message("you won","well done")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items)==0:
        items = make_items(current_level)
        