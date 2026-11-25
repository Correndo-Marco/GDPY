from os import listdir,path
from Livello import *

LVL_DIR = "/levels"
GD_DIR = path.dirname(path.abspath(__file__))

class GestoreLvl():
    def __init__(self,maxy):
        self.livelli = {}
        self.maxy = maxy
        self.caricaLivelli()
        self.display()
    
    def display(self):
        print("Livelli: ")
        for i in self.livelli:
            print(i)
            self.livelli[i].display()
            print()

    def caricaLivelli(self):
        livelli = sorted(listdir(f"{GD_DIR}{LVL_DIR}"))
        for i in livelli:
            if ".txt" in i:
                continue
            el = self.caricaLivello(f"{GD_DIR}{LVL_DIR}/{i}")
            
    def caricaLivello(self,dire):
        files = listdir(dire)
        if len(files) != 2:
            return
        lvl = Livello(dire,self.maxy)
        self.livelli.update({lvl.data.get("name"):lvl})

