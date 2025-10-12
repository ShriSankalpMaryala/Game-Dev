import pgzrun
import random
#screen dimensions
WIDTH = 1000
HEIGHT = 600
#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)
#create a ship
ship = Actor('ship')
bug = Actor('bug')
ship.pos = (WIDTH//2, HEIGHT-60)
speed = 1
#define a list for bullets
bullets = []
#defining a list of enemies
enemies = []
score = 0 
direction = 1
ship.dead = False
ship.countdown = 90

for x in range(8):
    for y in range(4):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50*x 
        enemies[-1].y = 100 + 50*y 

def display_score():
    screen.draw.text(str(score), (50,50))

def game_over():
    screen.draw.text("Game Over", (0,0))

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets [-1].x = ship.x
            bullets [-1].y = ship.y - 50

def update():
    global score
    global direction
    move_down = False
    
    #ship_movement
    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed

            if ship.x <= 0:
                ship.x = 0
                
        elif keyboard.right:
            ship.x += speed

            if ship.x >= WIDTH:
                ship.x = WIDTH
    
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    
    if len(enemies) == 0:
        game_over()
    
    #movement_of_enemies

    if len(enemies)>0 and (enemies[-1].x >WIDTH - 50 or enemies[0].x <50):
        move_down = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x += 5*direction
        if move_down == True:
            enemy.y += 100
        if enemy.y >HEIGHT:
            enemies.remove(enemy)
        
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
                if len(enemies)== 0:
                    game_over()

        if enemy.colliderect(ship):
            ship.dead = True

    if ship.dead:
        ship.countdown -= 1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90


                

def draw():
    screen.clear()
    screen.blit("nightsky", (0,0))
    for bullet in bullets:
        bullet.draw()
    
    for enemy in enemies:
        enemy.draw()
    
    if ship.dead == False:
        ship.draw()
    
    display_score()
    if len(enemies) == 0:
        game_over()

pgzrun.go()

    



            