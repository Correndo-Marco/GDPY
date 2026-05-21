class Giocatore():
    def __init__(self,immagine,dimx,dimy,x,y,maxx,maxy):
        self.img = immagine
        self.dimx = dimx
        self.dimy = dimy
        self.maxx = maxx
        self.maxy = maxy
        self.originalMaxy = maxy
        self.x = x
        self.y = y
        self.rx = self.x + self.dimx    #vertice vero sotto destra
        self.ry = self.y + self.dimy    #vertice vero sotto destra
        self.mod = "Cube1"
        self.mods = {
            "Cube1" : {"vx":10,"vy":-30,"g":1.7},
            "Cube2" : {"vx":10,"vy":-50,"g":1}
            }
        self.azzeraVelocita()
        self.aTerra = True
    
    def changeATerra(self):
        self.aTerra = True if self.ry == self.maxy else False

    def azzeraVelocita(self):
        self.vy = self.mods[self.mod].get("vy")

    def aggiornaVelocita(self):
        self.vy += self.mods[self.mod].get("g")
    
    def jump(self):
        self.azzeraVelocita()
        self.y += self.vy
        self.aggiornaVelocita()
        self.ry = self.y + self.dimy
        self.changeATerra()
    
    def cadi(self):
        self.y += self.vy
        if self.y > self.maxy - self.dimy:
            self.y = self.maxy - self.dimy
        else:
            self.aggiornaVelocita()
        self.ry = self.y + self.dimy
        self.changeATerra()
            
    def movimenti(self):
        self.movy()

    def movy(self):
        if self.ry < self.maxy:
            self.cadi()
        else:
            self.vy = 0
    
    def resetPos(self):
        self.y = self.maxy - self.dimy

    def muori(self):
        self.maxy = self.originalMaxy
        self.resetPos()
        self.vy = 0
    