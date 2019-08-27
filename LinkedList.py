from Lista import Lista
from Node import Node

class LinkedList(Lista):
    #constructor
    def __init__(self):
        self.inicio = Node()
        self.inicio = None
        self.size = 0
    
    def inserta(self, dato, posicion):
        newNode = Node()
        newNode.setData(dato)
        temp = self.inicio
        if posicion > 1 and posicion < self.size:
            for i in range(2,posicion-1,1):
                temp = temp.getSiguiente()
            temp.getSiguiente().se
    
    def buscar(self, dato):
        pass

    def vacia(self):
        return self.inicio == None

    def elementoPosicion(self, posicion):
        if posicion>=1 and posicion<=self.size:
            tmp = self.inicio
            for i in range(self.size):
                tmp = tmp.getSiguiente()
            return tmp.getData()
        else:
            return None
