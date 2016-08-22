#! /usr/bin/python2

#imports
from pygame import *
import os
import k
import time
import random

#Constants
WIDTH = 1000
HEIGHT = 750
KEYBOARD = []
KEYBOARD_MODE = "Dvorak"
GAMEWINDOW = display

class Rocket:
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT-200
        self.img = image.load(os.path.join("assets", "flyingrocket.png")).convert_alpha()
    def render(self, surface):
        surface.blit(self.img, (self.x, self.y))
    # all objects must comply with the movement system
    def move(self, x, y, relative=True):
        if relative:
            self.x +=x
            self.y +=y
        else:
            self.x =x
            self.y =y
    # all objects must comply with bounding box system
    def getboundingbox(self):
        return self.x, self.y, self.x+100, self.y+150

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(HEIGHT*-1, 0)
        self.img = image.load(os.path.join("assets", "asteroid.png")).convert_alpha()
    def render(self, surface):
        surface.blit(self.img, (self.x, self.y))
    def move(self, x, y, relative=True):
        if relative:
            self.x +=x
            self.y +=y
        else:
            self.x =x
            self.y =y
    def getboundingbox(self):
        return self.x, self.y, self.x+100, self.y+100

def startup():
    global KEYBOARD, KEYBOARD_MODE, GAMEWINDOW
    #prepare pygame
    init()
    GAMEWINDOW = display.set_mode((WIDTH, HEIGHT))
    display.set_caption('Doge->Moon!Crash')
    #read configs
    f = open("keyboard.config")
    keyboardsettings = f.read()
    f.close()
    keyboardlines = keyboardsettings.split("\n")
    for i in range(0, len(keyboardlines)):
        if "Name" in keyboardlines[i]:
            newconfig = []
            newconfig.append(keyboardlines[i].split("=")[1])
            for j in range(i+2,i+6):
                newconfig.append(keyboardlines[j].split("=")[1])
            KEYBOARD.append(newconfig)
        if "using" in keyboardlines[i]:
            KEYBOARD_MODE = keyboardlines[i].split("=")[1]
    #launch the main loop
    mainLoop()

key_lastpressdelay = 0

def keymovement(object, pressdelay):
    global KEYBOARD, KEYBOARD_MODE, key_lastpressdelay
    if time.time()>key_lastpressdelay:
        key_lastpressdelay = time.time()+pressdelay
        for i in range(0, len(KEYBOARD)):
            if KEYBOARD[i][0] == KEYBOARD_MODE:
                for j in range(0,len(KEYBOARD[i])):
                    keys = key.get_pressed()
                    if k.matchKey(KEYBOARD[i][1],keys):
                        object.move(-1,0)
                    if k.matchKey(KEYBOARD[i][2],keys):
                        object.move(1,0)
                    if k.matchKey(KEYBOARD[i][3],keys):
                        object.move(0,-1)
                    if k.matchKey(KEYBOARD[i][4],keys):
                        object.move(0,1)

def getCollision(bounding1, bounding2):
    if bounding2[0]<bounding1[2]<bounding2[2]:
        if bounding2[1]<bounding1[3]<bounding2[3]:
            return 1
        else:
            return 0
    else:
        return 0

def mainLoop():
    global GAMEWINDOW
    #create objects
    background = image.load(os.path.join("assets", "background.jpg")).convert()
    main_rocket = Rocket()
    asteroid_array = []
    difficulty = 500.0
    on = True
    while on:
        for e in event.get():
            if e.type == QUIT:
                on = False
        GAMEWINDOW.blit(background,(-200,-200))
        main_rocket.render(GAMEWINDOW)
        keymovement(main_rocket,0.0075)
        if random.randint(0,int(difficulty))==1:
            if difficulty - len(asteroid_array)/2 >1:
                difficulty -=len(asteroid_array)/2
            asteroid_array.append([Asteroid(),random.randint(-5, 5), random.randint(0, 5), time.time()])
        asteroids_topop = []
        for i in range(0, len(asteroid_array)):
            if time.time()>asteroid_array[i][3]:
                asteroid_array[i][3] = time.time()+0.01
                asteroid_array[i][0].move(asteroid_array[i][1], asteroid_array[i][2]+1)
            asteroid_array[i][0].render(GAMEWINDOW)
            if asteroid_array[i][0].y > 2*HEIGHT:
                asteroids_topop.append(i)
            if getCollision(asteroid_array[i][0].getboundingbox(),main_rocket.getboundingbox()):
                on = False
        for i in range(0,len(asteroids_topop)):
            asteroid_array.pop(asteroids_topop[i])
        display.flip()


# This is designed so that it can be replaced with a launcher if need be.
startup()