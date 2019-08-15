#from Lista import Lista

class ArrayList:

    #constructor
    def __init__(self):
        self.capacidad = 0
        self.size = 0
        self.arreglo = []

    #verifica si la lista está vacía
    def vacia(self):
        if self.size==0:
            return True
        else
            return False

    #borra los elementos de la lista
    def anula(self):
        for i in range(self.size):
            if self.arreglo[i] != None:
                self.arreglo[i] = None
        self.size = 0
    
    #amplia el arreglo
    def ampliar(self):
        if self.size == self.capacidad:
            newArray = [] #new capacity
            for i in range(self.size):
                newArray[i] = arreglo[i]
            arreglo = newArray
            newCapacity = self.capacidad*2
            self.capacidad = newCapacity

    #corre los elementos del arreglo
    def corrimiento(final):
        i = self.size
        for i to range

    
    #devuelve el objeto que está en la posición ingresada
    def elementoPosicion(self, posicion):
        if posicion >= 1 and posicion <= self.size:
            return arreglo[pos]
        else:
            return None
        




    