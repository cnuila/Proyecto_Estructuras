from Lista import Lista
from Node import Node

class LinkedList(Lista):
    #constructor
    def __init__(self):
        self.inicio = Node()
        self.inicio = None
        self.size = 0
    
    def inserta(self, dato, posicion):
        pass
    
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

    def obtenerSiguiente(self, posicion):
        self.elementoPosicion(posicion+1)
        pass

    def obtenerAnterior(self, posicion):
        self.elementoPosicion(posicion-1)
        pass

    def anula(self):
        pass