from Object import Object
from Pila import Pila

class Node:

    #constructor
    def __init__(self):
        self.anterior = None
        self.siguiente = None
        self.data = None

    #setters and getters
    def setSiguiente(next):
        self.siguiente = next
    def getSiguiente():
        return self.siguiente

    def setAnterior(prev):
        self.anterior = prev
    def getAnterior():
        return self.anterior

    def setData(pData):
        self.data = pData
    def getData():
        return self.pData