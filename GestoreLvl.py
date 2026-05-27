import os
from Livello import *
LVL_DIR = "./levels"

class GestoreLvl():
    def __init__(self,maxy):
        self.livelli = {}
        self.maxy = maxy
        self.caricaLivelli()
        #self.display()
    
    def display(self):
        for i in self.livelli:
            print(i)
            self.livelli[i].display()
            print()

    def caricaLivelli(self):
        livelli = sorted(os.listdir(LVL_DIR))
        for i in livelli:
            if ".txt" in i:
                continue
            el = self.caricaLivello(f"{LVL_DIR}/{i}")
            
    def caricaLivello(self,dire):
        files = os.listdir(dire)
        if len(files) != 2:
            return
        lvl = Livello(dire,self.maxy)
        self.livelli.update({lvl.data.get("name"):lvl})

