
class Node:

    #constructor
    def __init__(self):
        self.anterior = Node()
        self.siguiente = Node()
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

    def setData(Data):
        self.data = Data
    def getData():
        return self.data