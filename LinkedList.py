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
            for _ in range(2,posicion-1,1):
                tmp = tmp.getSiguiente()
            tmp.getSiguiente().setAnterior(newNode)
            newNode.setSiguiente(tmp.getSiguiente())
            newNode.setAnterior(tmp)
            tmp.setSiguiente(newNode)
            self.size = self.size + 1
            return True
        elif posicion==self.size:
            for _ in range(posicion):
                tmp = tmp.getSiguiente()
            tmp.setSiguiente(newNode)
            newNode.setAnterior(tmp)
            self.size = self.size + 1
            return True
        else:
            return False

    #Elimina el elemento en la posicion ingresada
    def borrarElemento(self, posicion):
        if posicion==1:
            if self.size>1:
                tmp=self.inicio.getSiguiente()
                tmp.getAnterior().setSiguiente(None)
                tmp.setAnterior(None)
                self.inicio=tmp
            else:
                self.inicio = None
            self.size = self.size -1
        elif posicion>1 and posicion<self.size:
            tmp=self.inicio
            for _ in range(posicion):
                tmp = tmp.getSiguiente()
            tmp.getSiguiente().setAnterior(tmp.getAnterior())
            tmp.getAnterior().setSiguiente(tmp.getSiguiente())
            tmp.setSiguiente(None)
            tmp.setAnterior(None)
            self.size = self.size -1
        elif posicion == self.size:
            for _ in range(self.size):
                tmp = tmp.getSiguiente()
            tmp.getAnterior().setSiguiente(None)
            tmp.setAnterior(None)
            self.size = self.size -1
        else:
            return None
    #Devuelve la posicion del dato a buscar
    def buscar(self, dato):
        tmp = self.inicio
        for i in range(self.size):
            if (tmp.getData() is dato):
                return i
            else:
                tmp = tmp.getSiguiente()
    #Verifica si la lista esta vacia
    def vacia(self):
        if self.inicio == None:
            return True
        else:
            return False
    #Devuelve el dato en la posicion mandada
    def elementoPosicion(self, posicion):
        if posicion>=1 and posicion<=self.size:
            tmp = self.inicio
            for _ in range(2,posicion):
                tmp = tmp.getSiguiente()
            print("El dato del elemento en la posicion ",posicion, "es " ,tmp.getData())
        else:
            print("Ingreso una posicion incorrecta.")
    #Devuelve el dato siguiente a la posicion ingresada
    def obtenerSiguiente(self, posicion):
        if posicion>=1 and posicion<self.size:
            tmp = self.inicio
            for _ in range(2,posicion):
                tmp = tmp.getSiguiente()
            print("El dato del elemento siguiente a la posicion ",posicion, "es " ,tmp.getData())
        else:
            print("Ingreso una posicion incorrecta.")
    #Devuelve el dato anterior a la posicion ingresada
    def obtenerAnterior(self, posicion):
        if posicion>1 and posicion<=self.size:
            tmp = self.inicio
            for _ in range(2,posicion):
                tmp = tmp.getSiguiente()
            print("El dato del elemento anterior a la posicion ",posicion, "es " ,tmp.getData())
        else:
            print("Ingreso una posicion incorrecta.")
    #Vacia la lista
    def anula(self):
        if self.inicio!= None:
            self.inicio=None
            print("La lista se vacio correctamente.")
        else:
            print("La lista esta vacia.")