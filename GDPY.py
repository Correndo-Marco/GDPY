import pygame
import sys
import os
import math
from Giocatore import *
from Geometria import *
from GestoreLvl import *
import time

os.environ['SDL_VIDEO_CENTERED'] = "1"

FPS = 60
IMG_DIR = "./images/"

class GDPY():
    def __init__(self):
        self.info = {"maxx":1800,"maxy":800}
        self.screen = pygame.display.set_mode((self.info["maxx"],self.info["maxy"]))
        pygame.display.set_caption("GDPY")
        self.gestore = GestoreLvl(self.info["maxy"])
        self.bgColor = (255,255,255)
        self.nomeLivello = "first"
        self.attemptCount = 1
        self.creaOstacoli()
        self.creaPlayer()
        self.running = True
        self.clock = pygame.time.Clock()
        self.loop()
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.gestisciEvento(event)
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
        for i in self.portali:
            self.screen.blit(i.img,(i.a.x,i.a.y))

    def creaOstacoli(self):
        self.livello = self.gestore.livelli.get(self.nomeLivello)
        self.oggetti = self.livello.livello
        self.winCount = len(self.oggetti)
        print(self.oggetti)
        self.spikes = []
        self.blocks = []
        self.portali = []
        for i in self.oggetti:
            nom = i.get("img")
            el = pygame.image.load(IMG_DIR+nom)
            if nom == "Spike.png":
                self.spikes.append(Spike(i["x"],i["y"],el))
            elif nom == "Block.png":
                self.blocks.append(Blocco(i["x"],i["y"],el))
            elif nom == "Portale.png":
                self.portali.append(Portale(i["x"],i["y"],el,i["mode"]))

    def creaPlayer(self):
        self.p = Giocatore(self.info["maxx"],self.info["maxy"],self.livello.data.get("startMode"))
        self.playerImg = pygame.image.load(self.p.img)

    def checkCollisioni(self):
        conto = 0
        for i in self.spikes:
            if i.a.x > self.p.x + 150:      #se troppo avanti
                continue
            elif self.p.x > i.b.x + 150:    #se troppo indietro
                conto += 1
                continue
            if i.collisione(self.p):
                self.perdi()
        maxy = self.info["maxy"]

        for i in self.blocks:
            if i.a.x > self.p.x + 150:
                continue
            elif self.p.x > i.b.x + 150:
                conto += 1
                continue
            tip = i.collisione(self.p)
            if tip[0]:
                self.perdi()
            else:
                maxy = min(maxy,tip[1])
        self.p.maxy = maxy

        for i in self.portali:
            if i.a.x > self.p.x + 150:
                continue
            elif self.p.x > i.b.x + 150:
                conto += 1
                continue
            if i.collisione(self.p) and self.p.mod != i.mode:
                self.togglePMod(i.mode)
            
        if self.checkWin(conto):
            print(f"Hai vinto in {self.attemptCount} attempts")
        #print(f"{self.p.x} {self.p.ry} con maxy {maxy} e salta:{self.p.aTerra} e mod:{self.p.mod}")
    
    def muoviBack(self):
        v = self.p.modes[self.p.mod]["vx"]
        for i in self.blocks:
            i.muoviY(v)
        for i in self.spikes:
            i.muoviY(v)
        for i in self.portali:
            i.muoviY(v)
    
    def checkWin(self,conto):
        return conto == self.winCount

    def gestisciEvento(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "\x1b":
                self.running = False
            elif event.unicode == " ":
                self.gestisciInput(event,"C")
        elif event.type == pygame.TEXTINPUT:    
            self.gestisciInput(event,"P")
            
    def gestisciInput(self,event,tipo):
        e = event.text if tipo == "P" else event.unicode
        if e == "r":
            self.perdi()
        if e == " ":
            self.p.agisci(tipo)
    
    def togglePMod(self,mode):
        self.p.toggleMod(mode)
        self.playerImg = pygame.image.load(self.p.img)

    def perdi(self):
        self.attemptCount += 1
        time.sleep(0.4)
        self.creaOstacoli()
        self.p.muori()
        self.togglePMod(self.livello.data.get("startMode"))
        time.sleep(0.1)
        self.disegnaBackG()
        self.disegnaPlayer()
