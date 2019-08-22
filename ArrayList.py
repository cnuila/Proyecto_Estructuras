from Lista import Lista

class ArrayList(Lista):

    #constructor
    def __init__(self):
        self.size = 0
        self.arreglo = []

    #verifica si la lista está vacía
    def vacia(self):
        return self.size == 0

    #borra los elementos de la lista
    def anula(self):
        for i in range(self.size):
            if self.arreglo[i] != None:
                self.arreglo[i] = None
        self.size = 0
    
    #corre los elementos del arreglo
    def corrimiento(final):
        for i in range(size-1,0,-1):
            arreglo[i+1] = arreglo[i]

    #agrega un elemento a la lista
    def inserta(self, dato, posicion):
        if posicion<= self.size+1 and posicion >= 1:
            if posicion != self.size+1:
                self.corrimiento()
            arreglo[posicion] = dato
            self.size+1
            return True
        else:
            return False

    #devuelve el objeto que está en la posición ingresada
    def elementoPosicion(self, posicion):
        if posicion >= 1 and posicion <= self.size:
            return arreglo[pos]
        else:
            return None
        
    #devuelve el objeto que está en la posición siguiente a la ingresada
    def obtenerSiguiente(self, posicion):
        if posicion >= 1 and posicion <= self.size:
            if posicion == self.size:
                return None
            else:
                return arreglo[pos+1]
        else:
            return None

    #devuelve el objeto que está en la posición anterior a la ingresada
    def obtenerAnterior(self, posicion):
        if posicion >= 1 and posicion <= self.size:
            if posicion == 1:
                return None
            else:
                return arreglo[posicion-1]
        else:
            return None

    #busca un objeto dentro de la lista
    def buscar(self, dato):
        for i in range(self.size):
            if self.arreglo[i] == dato:
                validacion = True
                posicion = i
                break
            else:
                validacion = False
        if validacion:
            return posicion
        else:
            return None

    #borrar un elemento de la lista
    def borrarElemento(self, posicion):
        if posicion >= 1 and posicion <= self.size:
            temp = arreglo[pos-1]
            for i in range(posicion-1,self.size,-1):
                arreglo[i] = arreglo[i+1]
            arreglo[size] = None
            self.size-1
            return temp
        else:
            return None