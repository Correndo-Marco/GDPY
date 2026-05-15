class Giocatore():
    def __init__(self,immagine,dimx,dimy,x,y,maxx,maxy):
        self.img = immagine
        self.dimx = dimx
        self.dimy = dimy
        self.maxx = maxx
        self.maxy = maxy
        self.x = x
        self.y = y
        self.rx = self.x + self.dimx    #vertice vero sotto destra
        self.ry = self.y + self.dimy    #vertice vero sotto destra
        self.mod = "Cube1"
        self.mods = {
            "Cube1" : {"vx":10,"vy":-30,"g":2},
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
        if self.aTerra:
            self.azzeraVelocita()
    
    def avanti(self):
        self.x += self.mods[self.mod].get("vx")
        self.rx = self.x + self.dimx
    
    def indietro(self):
        self.x = 0
        self.rx = self.x + self.dimx

    def jump(self):
        self.y += self.mods[self.mod].get("vy")
        self.aggiornaVelocita()
        self.ry = self.y + self.dimy
        self.changeATerra()
    
    def cadi(self):
        self.y += self.vy
        if self.y > self.maxy-self.dimy:
            self.y = self.maxy - self.dimy
        self.aggiornaVelocita()
        self.ry = self.y + self.dimy
        self.changeATerra()
    
    def movimenti(self):
        self.movx()
        self.movy()

    def movx(self):
        if self.rx < self.maxx:
            self.avanti()
        else:
            self.indietro()

    def movy(self):
        if self.ry < self.maxy:
            self.cadi()
        