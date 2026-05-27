class Coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Oggetto():
    def __init__(self,ax,ay,bx,by,ahx,ahy,bhx,bhy,img):
        self.a = Coordinate(ax,ay)      #vertice alto sinistro oggetto
        self.b = Coordinate(bx,by)      #vertice  basso destro oggetto
        self.ah = Coordinate(ahx,ahy)   #vertice alto sinistro hitbox
        self.bh = Coordinate(bhx,bhy)   #vertice basso destro hitbox
        self.img = img
    
    def muoviY(self,v):
        for i in [self.a,self.b,self.ah,self.bh]:
            i.x -= v

class Spike(Oggetto):
    def __init__(self,x,y,img):
        super().__init__(x,y,x+100,y+100,x+20,y+20,x+80,y+100,img)

    def collisione(self,p):
        return p.rx > self.ah.x and p.x < self.bh.x and p.ry > self.ah.y and p.y < self.bh.y

class Blocco(Oggetto):
    def __init__(self,x,y,img):
        super().__init__(x,y,x+100,y+100,x,y,x+100,y+100,img)
    
    def collisione(self,p):
        if p.rx > self.a.x and p.x < self.b.x:
            if p.ry <= self.a.y and p.x < self.b.x:
                return [False,self.a.y]
            elif p.ry > self.a.y and p.y < self.b.y:
                return [True,p.originalMaxy]
        return [False,p.originalMaxy]

class Portale(Oggetto):
    def __init__(self,x,y,img,mode):
        super().__init__(x,y,x+100,y+200,x,y,x+100,y+200,img)
        self.mode = mode
    
    def collisione(self,p):
        if p.rx > self.a.x and p.rx < self.b.x:
            return True
    