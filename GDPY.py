import pygame
import sys
import os
import math
from Giocatore import *
from Geometria import *
from Livello import *
import time

os.environ['SDL_VIDEO_CENTERED'] = "1"
FPS = 60
IMG_DIR = "./images/"

class GDPY():
    def __init__(self):
        self.info = {"maxx":1800,"maxy":800}
        self.screen = pygame.display.set_mode((self.info["maxx"],self.info["maxy"]))
        pygame.display.set_caption("GDPY")
        self.bgColor = (255,255,255)
        self.creaPlayer()
        self.creaOstacoli()
        self.running = True
        self.clock = pygame.time.Clock()
        self.loop()
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.gestisciEvento(event)
            print(self.p.vy)
            self.muoviBack()
            self.p.movimenti()
            self.checkCollisioni()
            self.disegna()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def disegna(self):
        self.disegnaBackG()
        self.disegnaPlayer()
        self.disegnaOstacoli()
    
    def disegnaBackG(self):
        self.screen.fill(self.bgColor)
    
    def disegnaPlayer(self):
        self.screen.blit(self.playerImg, (self.p.x,self.p.y))

    def disegnaOstacoli(self):
        for i in self.spikes:
            self.screen.blit(i.img,(i.a.x,i.a.y))
        for i in self.blocks:
            self.screen.blit(i.img,(i.a.x,i.a.y))

    def creaOstacoli(self):
        self.livello = Livello("first",self.info["maxy"])
        self.oggetti = self.livello.carica()
        self.spikes = []
        self.blocks = []
        for i in self.oggetti:
            nom = i.get("img")
            el = pygame.image.load(IMG_DIR+nom)
            if nom == "Spike.png":
                self.spikes.append(Spike(i["x"],i["y"],el))
            elif nom == "Block.png":
                self.blocks.append(Blocco(i["x"],i["y"],el))

    def creaPlayer(self):
        self.p = Giocatore("./images/Cube.png",100,100,300,self.info["maxy"]-100,self.info["maxx"],self.info["maxy"])
        self.playerImg = pygame.image.load(self.p.img)

    def checkCollisioni(self):
        for i in self.spikes:
            if i.collisione(self.p):
                self.perdi()
        maxy = self.info["maxy"]
        for i in self.blocks:
            tip = i.collisione(self.p)
            #print(tip)
            if tip[0]:
                self.perdi()
            else:
                maxy = min(maxy,tip[1])
        self.p.maxy = maxy
        print(f"{self.p.x} {self.p.ry} con maxy {maxy}")

    def muoviBack(self):
        v = self.p.mods[self.p.mod]["vx"]
        for i in self.blocks:
            i.muoviY(v)
        for i in self.spikes:
            i.muoviY(v)
    
    def gestisciEvento(self,event):
        #print(event)
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "\x1b":
                self.running = False
        elif event.type == pygame.TEXTINPUT:
            self.gestisciInput(event)
            
    def gestisciInput(self,event):
        e = event.text
        if e == " " and self.p.aTerra:
            self.p.jump()
        if e == "r":
            self.perdi()
    
    def perdi(self):
        time.sleep(0.5)
        self.creaOstacoli()
        self.p.muori()
        self.disegnaBackG()