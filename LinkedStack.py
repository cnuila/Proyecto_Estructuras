from Pila import Pila
from Node import Node

class LinkedStack(Pila):
    #constructor
    def __init__(self):
        self.inicio = Node()
        self.inicio = None
    
    #verifica si la pila esta vacia
    def vacia(self):
        return self.inicio == None

    #devuelve el elemento en el tope de la pila
    def tope(self):
        if self.inicio:
            return self.inicio.getData()
        else:
            return None

    #saca el elemento en el tope de la pila
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
    
    #elimina el nodo del inicio desvinculando a todos los demas
    def anula(self):
        if self.inicio:
            self.inicio = None

    #agrega un elemento a la pila
    def empuja(self, dato):
        nuevoNodo = Node()
        nuevoNodo.setData(dato)
        if self.inicio == None:
            self.inicio = nuevoNodo
        else:
            self.inicio.setAnterior(nuevoNodo)
            nuevoNodo.setSiguiente(self.inicio)
            self.inicio = nuevoNodo