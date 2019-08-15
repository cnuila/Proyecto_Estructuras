from Pila import Pila
from Node import Node

class LinkedStack(Pila):

    def __init__(self):
        self.inicio = Node()
        self.inicio = None
    
    def Pila.vacia(self):
        return self.inicio == None

    def tope(self):
        if self.inicio:
            return self.inicio.getData()
        else:
            return None
    
    def saca(self):
        if self.inicio == None:
            return None
        else:
            nodoTemp = self.inicio
            self.inicio = nodoTemp.getSiguiente()
            nodoTemp.setSiguiente(None)
            if (self.inicio):
                self.inicio.setAnterior(None)
            datoTemp = nodoTemp.getData()
            nodoTemp.setData(None)
            return datoTemp
    
    def anula(self):
        if self.inicio:
            self.inicio = None

    def empuja(self, dato):
        nuevoNodo = Node()
        nuevoNodo.setData(dato)
        if self.inicio == None:
            self.inicio = nuevoNodo
        else:
            self.inicio.setAnterior(nuevoNodo)
            nuevoNodo.setSiguiente(self.inicio)
            self.inicio = nuevoNodo