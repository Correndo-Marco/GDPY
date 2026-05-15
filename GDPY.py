import pygame
import sys
import os
import math
from Giocatore import *
import time

os.environ['SDL_VIDEO_CENTERED'] = "1"
FPS = 60
DEBUG = False

spikes = [
    {"x":400},{"x",800}
]

class GDPY():
    def __init__(self):
        self.info = {"maxx":1800,"maxy":800}
        self.screen = pygame.display.set_mode((self.info["maxx"],self.info["maxy"]))
        pygame.display.set_caption("GDPY")
        self.creaPlayer()
        self.creaOstacoli()
        self.running = True
        self.clock = pygame.time.Clock()
        self.loop()
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.gestisciEvento(event)
            print(self.p.rx,self.p.ry)
            self.disegna()
            self.p.movimenti()
            self.checkCollisioni()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def disegna(self):
        self.disegnaBackG(not DEBUG)
        self.disegnaPlayer()
        self.disegnaOstacoli()
    
    def disegnaBackG(self,cond):
        if cond:
            self.screen.fill((255,255,255))
        
    
    def disegnaPlayer(self):
        self.screen.blit(self.playerImg, (self.p.x,self.p.y))

    def disegnaOstacoli(self):
        for i in self.ostacoli:
            self.screen.blit(i.get("img"),(i.get("x"),i.get("y")))
        for i in self.blocks:
            self.screen.blit(i.get("img"),(i.get("x"),i.get("y")))


    def creaOstacoli(self):
        self.infoSpikes = [
            {"img":"./images/Spike.png","x":600,"y":self.info["maxy"]-100},
            {"img":"./images/Spike.png","x":1100,"y":self.info["maxy"]-100}
        ]
        self.ostacoli = []
        for i in self.infoSpikes:
            nom = i.get("img")
            el = pygame.image.load(nom)
            self.ostacoli.append({"img":el,"x":i.get("x"),"y":i.get("y")})
        
        self.infoBlocks = [
            {"img":"./images/Block.png","x":700,"y":self.info["maxy"]-100},
            {"img":"./images/Block.png","x":800,"y":self.info["maxy"]-100},
        ]
        self.blocks = []
        for i in self.infoBlocks:
            nom = i.get("img")
            el = pygame.image.load(nom)
            self.blocks.append({"img":el,"x":i.get("x"),"y":i.get("y")})
    
    def creaPlayer(self):
        self.p = Giocatore("./images/Cube.png",100,100,0,self.info["maxy"]-100,self.info["maxx"],self.info["maxy"])
        self.playerImg = pygame.image.load(self.p.img)

    def checkCollisioni(self):
        for i in self.infoSpikes:
            ostx , osty = i.get("x") , i.get("y")
            if self.p.rx > ostx and self.p.x < ostx+100 and self.p.ry > osty:   #collisione con lo spike
                self.perdi()
        c = 0
        for i in self.infoBlocks:
            ostx , osty = i.get("x") , i.get("y")
            if self.p.ry > osty and self.p.rx > ostx and self.p.x < ostx+100:       #collisione col blocco
                self.perdi()
            elif self.p.ry < osty and self.p.rx > ostx:         #va sopra il blocco
                self.p.maxy = osty     
            

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
    
    def perdi(self):
        time.sleep(2)
        self.p.indietro()
        self.disegnaBackG(True)