class Giocatore():
    def __init__(self,dimx,dimy,x,y,maxx,maxy):
        self.dimx = dimx
        self.dimy = dimy
        self.maxx = maxx
        self.maxy = maxy
        self.originalMaxy = maxy
        self.x = x
        self.y = y
        self.rx = self.x + self.dimx    #vertice vero sotto destra
        self.ry = self.y + self.dimy    #vertice vero sotto destra
        self.mod = "Ufo"
        self.mods = {
            "Cube" : {"vx":10,"vy":-30,"g":1.7,"img":"./images/Cube.png"},
            "Ufo" : {"vx":10,"vy":-25,"g":1.5,"img":"./images/Ufo.png"}
            }
        self.resetImg()
        self.azzeraVelocita()
        self.aTerra = True
    
    def changeATerra(self):
        self.aTerra = True if self.ry == self.maxy else False

    def azzeraVelocita(self):
        self.vy = self.mods[self.mod].get("vy")

    def subisciG(self):
        self.vy += self.mods[self.mod].get("g")
    
    def agisci(self):
        if self.mod == "Cube" and self.aTerra:
            self.jump()
        elif self.mod == "Ufo":
            self.jump()

    def jump(self):
        self.azzeraVelocita()
        self.y += self.vy
        self.subisciG()
        self.ry = self.y + self.dimy
        self.changeATerra()
    
    def cadi(self):
        self.y += self.vy
        if self.y > self.maxy - self.dimy:
            self.y = self.maxy - self.dimy
        else:
            self.subisciG()
        self.ry = self.y + self.dimy
        self.changeATerra()
            
    def movimenti(self):
        self.movy()

    def movy(self):
        if self.ry < self.maxy:
            self.cadi()
        else:
            self.vy = 0
        if self.y < 0:
            self.y = 0
            self.vy = 0
    
    def resetPos(self):
        self.y = self.maxy - self.dimy

    def muori(self):
        self.maxy = self.originalMaxy
        self.resetPos()
        self.vy = 0
    
    def resetImg(self):
        self.img = self.mods[self.mod].get("img")

    def toggleMod(self):
        if self.mod == "Cube":
            self.mod = "Ufo"
        else:
            self.mod = "Cube"
        self.resetImg()
        