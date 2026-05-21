OFFSET_LVL = 800

class Livello():
    def __init__(self,nomeF,maxy):
        self.nomeF = f"./levels/{nomeF}.txt"
        self.corrispondenza = {"x":"Spike.png","c":"Block.png"}
        self.maxy = maxy

    def carica(self):
        livello = []
        with open(self.nomeF,"r") as f:
            cont = f.readlines()
        for x in range(len(cont)):
            for y in range(len(cont[x])):
                tipo = self.corrispondenza.get(cont[x][y])
                if tipo in self.corrispondenza.values():
                    livello.append({"img":tipo,"x":x*100 + OFFSET_LVL,"y":self.maxy - y*100-100})
        return livello
