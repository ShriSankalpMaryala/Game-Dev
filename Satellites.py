import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 600 

satellites = []
lines = []
next_satellite = 0 
start_time = 0
total_time = 0
end_time = 0
number_of_satellites = 10

def create_satellites():
    global start_time
    for i in range(number_of_satellites):
        satellite = Actor("Satellite.png")
        satellite.pos = random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        satellites.append(satellite)
    start_time = time.time()

def draw():
    global total_time