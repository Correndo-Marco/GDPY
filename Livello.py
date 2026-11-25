import json

OFFSET_LVL = 1000
LVL_DIR = "levels"

class Livello():
    def __init__(self,nomeDir,maxy):
        self.nomeDir = f"{nomeDir}"
        self.corrispondenza = {"x":"Spike.png","c":"Block.png","p":"Portale.png"}
        self.portaliModes = {"c":"Cube","u":"Ufo"}
        self.maxy = maxy
        self.carica()
    
    def display(self):
        print(f"Dir: {self.nomeDir}\nstartMode: {self.data.get("startMode")}")

    def carica(self):
        self.caricaTXT()
        self.caricaJSON()
    
    def caricaTXT(self):
        self.livello = []
        with open(f"{self.nomeDir}/level.txt","r") as f:
            cont = f.readlines()
        for x in range(len(cont)):
            for y in range(len(cont[x])):
                el = cont[x][y]
                if el == "p":
                    mode = self.portaliModes.get(cont[x][y+1])
                    self.livello.append({"img":"Portale.png","x":x*100 + OFFSET_LVL,"y":self.maxy - (y+1)*100-100,"mode":mode})
                else:
                    if y != 0 and cont[x][y-1] == "p":
                        continue
                    tipo = self.corrispondenza.get(el)
                    if tipo in self.corrispondenza.values():
                        self.livello.append({"img":tipo,"x":x*100 + OFFSET_LVL,"y":self.maxy - y*100-100})
    
    def caricaJSON(self):
        with open(f"{self.nomeDir}/data.json") as f:
            self.data = json.load(f)
