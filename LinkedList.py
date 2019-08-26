from Lista import Lista
from Node import Node

class LinkedList(Lista):
    #constructor
    def __init__(self):
        self.inicio = Node()
        self.inicio = None
        self.size = 0
    #Agrega elemento a la lista en la posicion ingresada
    def inserta(self, dato, posicion):
        newNode = Node()
        newNode.setData(dato)
        tmp = self.inicio
        if self.inicio == None:
            self.inicio = newNode
            self.size = self.size + 1
            return True
        elif posicion == 1:
            tmp.setAnterior(newNode)
            newNode.setSiguiente(tmp)
            self.size = self.size + 1
            return True
        elif posicion>1 and posicion<self.size:
            for i in range(posicion-1):
                tmp = tmp.getSiguiente()
            tmp.getSiguiente().setAnterior(newNode)
            newNode.setSiguiente(tmp.getSiguiente())
            newNode.setAnterior(tmp)
            tmp.setSiguiente(newNode)
            self.size = self.size + 1
            return True
        elif posicion==self.size:
            for i in range(posicion):
                tmp = tmp.getSiguiente()
            tmp.setSiguiente(newNode)
            newNode.setAnterior(tmp)
            self.size = self.size + 1
            return True
        else:
            return False
    #Elimina el elemento en la posicion ingresada
    def borrarElemento(self, posicion):
        tmp = self.inicio
        if posicion == 1:
            self.inicio = tmp.getSiguiente()
            tmp.getSiguiente().setAnterior(None)
            tmp.setSiguiente(None)
        elif posicion>1 and posicion<self.size:
            for i in range(posicion):
                tmp = tmp.getSiguiente()
            tmp.getSiguiente().setAnterior(tmp.getAnterior())
            tmp.getAnterior().setSiguiente(tmp.getSiguiente())
            tmp.setSiguiente(None)
            tmp.setAnterior(None)
        elif posicion == self.size:
            tmp.getAnterior().setSiguiente(None)
            tmp.setAnterior(None)
        else:
            return None
    #Devuelve la posicion del dato a buscar
    def buscar(self, dato):
        tmp = self.inicio
        for i in range(self.size):
            if (tmp.getData is dato):
                return i
            else:
                tmp = tmp.getSiguiente()
        pass
    #Verifica si la lista esta vacia
    def vacia(self):
        return self.inicio == None
    #Devuelve el dato en la posicion mandada
    def elementoPosicion(self, posicion):
        if posicion>=1 and posicion<=self.size:
            tmp = self.inicio
            for i in range(2,posicion):
                tmp = tmp.getSiguiente()
            return tmp.getData()
        else:
            return None
    #Devuelve el dato siguiente a la posicion ingresada
    def obtenerSiguiente(self, posicion):
        if posicion>=1 and posicion<self.size:
            tmp = self.inicio
            for i in range(2,posicion):
                tmp = tmp.getSiguiente()
            return tmp.getData()
        else:
            return None
    #Devuelve el dato anterior a la posicion ingresada
    def obtenerAnterior(self, posicion):
        if posicion>1 and posicion<=self.size:
            tmp = self.inicio
            for i in range(2,posicion):
                tmp = tmp.getSiguiente()
            return tmp.getData()
        else:
            return None
    #Vacia la lista
    def anula(self):
        if self.inicio!= None:
            self.inicio.setSiguiente(None)
        else:
            print("La lista esta vacia")
            return None
