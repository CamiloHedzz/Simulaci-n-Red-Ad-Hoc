class Nodo:
    
    def __init__(self, corX, corY, id, destino):
        self.id = id
        self.corX = corX
        self.corY = corY
        self.paquetes = []
        self.conexiones = []
        self.distancias = {}
        self.destino = destino
    
