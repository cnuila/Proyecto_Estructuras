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
        self.arreglo.clear()
        self.size = 0
    
    #corre los elementos del arreglo
    def corrimiento(self,posicion):
        self.arreglo.append(self.arreglo[self.size])
        for i in range(self.size-1,posicion-1,-1):
            self.arreglo[i+1] = self.arreglo[i]

    #agrega un elemento a la lista
    def inserta(self, dato, posicion):
        if posicion != self.size:
            self.corrimiento(posicion)
        self.arreglo.insert(posicion,dato)
        self.size = self.size+1
        return True

    #devuelve el objeto que está en la posición ingresada
    def elementoPosicion(self, posicion):
        print(posicion)
        temp = self.arreglo[posicion-1]
        return temp
        
    #devuelve el objeto que está en la posición siguiente a la ingresada
    def obtenerSiguiente(self, posicion):
        if posicion == self.size:
            return None
        else:
            return self.arreglo[posicion]

    #devuelve el objeto que está en la posición anterior a la ingresada
    def obtenerAnterior(self, posicion):
            if posicion == 1:
                return None
            else:
                temp = self.arreglo[posicion-2]
                return temp

    #busca un objeto dentro de la lista
    def buscar(self, dato):
        validacion = False
        posicion = -1
        for i in range(self.size):
            if self.arreglo[i] == dato:
                validacion = True
                posicion = i
                break
        if validacion:
            return posicion
        else:
            return posicion

    #borrar un elemento de la lista
    def borrarElemento(self, posicion):
            temp = self.arreglo[posicion-1]
            for i in range(posicion-1,self.size-1,1):
                self.arreglo[i] = self.arreglo[i+1]
            self.arreglo.pop()
            self.size = self.size-1
            return temp