IMG_DIR = "./images"

class Giocatore():
    def __init__(self,maxx,maxy,mod):
        self.dimx = 100
        self.dimy = 100
        self.maxx = maxx
        self.maxy = maxy
        self.originalMaxy = maxy
        self.x = 300
        self.y = self.maxy - self.dimy
        self.rx = self.x + self.dimx    #vertice vero sotto destra
        self.ry = self.y + self.dimy    #vertice vero sotto destra
        self.mod = mod
        self.modes = {
            "Cube" : {"vx":10,"vy":-30,"g":1.7,"img":f"{IMG_DIR}/Cube.png"},
            "Ufo" : {"vx":10,"vy":-25,"g":1.5,"img":f"{IMG_DIR}/Ufo.png"}
            }
        self.resetImg()
        self.resettaVelocita()
        self.aTerra = True
    
    def changeATerra(self):
        self.aTerra = True if self.ry == self.maxy else False

    def resettaVelocita(self):
        self.vy = self.modes[self.mod].get("vy")

    def azzeraVelocita(self):
        self.vy = 0

    def aggiornaVertici(self):
        self.ry = self.y + self.dimy

    def aggiornaY(self):
        self.y += self.vy

    def subisciG(self):
        maxvy = abs(self.modes[self.mod].get("vy"))      #conto della massima velocità
        if self.vy < maxvy:
            self.vy += self.modes[self.mod].get("g")
        else:
            self.vy = maxvy
    
    def agisci(self,mode):
        self.changeATerra()
        if self.mod == "Cube" and self.aTerra:
            self.jump()
        elif self.mod == "Ufo":
            if mode == "C":
                self.jump()

    def jump(self):
        self.resettaVelocita()
        self.aggiornaY()
        self.subisciG()
        self.aggiornaVertici()
        self.changeATerra()
    
    def cadi(self):
        self.aggiornaY()
        if self.y > self.maxy - self.dimy:
            self.y = self.maxy - self.dimy
            self.azzeraVelocita()
        else:
            self.subisciG()
        self.aggiornaVertici()
        self.changeATerra()
            
    def movimenti(self):
        self.movy()

    def movy(self):
        if self.ry < self.maxy:
            self.cadi()
        else:
            self.azzeraVelocita()
        
        if self.y < 0:
            self.y = 0
            self.azzeraVelocita()
    
    def resetPos(self):
        self.y = self.maxy - self.dimy

    def muori(self):
        self.maxy = self.originalMaxy
        self.resetPos()
        self.azzeraVelocita()
    
    def resetImg(self):
        self.img = self.modes[self.mod].get("img")

    def toggleMod(self,mod):
        if mod == self.mod:
            return
        if mod in self.modes.keys():
            self.mod = mod
            self.resetImg()
        