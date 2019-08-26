class Node:

    #constructor
    def __init__(self):
        self.anterior = None
        self.siguiente = None
        self.data = None

    #setters and getters
    def setSiguiente(self,next):
        self.siguiente = next
    def getSiguiente(self):
        return self.siguiente

    def setAnterior(self,prev):
        self.anterior = prev
    def getAnterior(self):
        return self.anterior

    def setData(self,Data):
        self.data = Data
    def getData(self):
        return self.data