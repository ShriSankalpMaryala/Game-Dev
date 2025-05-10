import pgzrun
from random import randint
TITLE = "Shoot the Alien"
WIDTH = 700
HEIGHT = 800
message = " "

#character
alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill("blue")
    alien.draw()
    screen.draw.text(message,(600,50))

def place():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot"
        place()
    else:
        message = "Bad Shot"

place()
pgzrun.go()
