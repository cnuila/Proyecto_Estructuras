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
        #return self.arreglo

    #devuelve el objeto que está en la posición ingresada
    def elementoPosicion(self, posicion):
        nombre = self.arreglo[posicion].getNombre()
        cuenta = self.arreglo[posicion].getCuenta()
        return nombre, cuenta
        
    #devuelve el objeto que está en la posición siguiente a la ingresada
    def obtenerSiguiente(self, posicion):
        if posicion == self.size-1:
            nombre = ""
            cuenta = ""
            return nombre, cuenta
        else:
            nombre = self.arreglo[posicion+1].getNombre()
            cuenta = self.arreglo[posicion+1].getCuenta()
            return nombre, cuenta

    #devuelve el objeto que está en la posición anterior a la ingresada
    def obtenerAnterior(self, posicion):
        if posicion == 0:
            nombre = ""
            cuenta = ""
            return nombre, cuenta
        else:
            nombre = self.arreglo[posicion-1].getNombre()
            cuenta = self.arreglo[posicion-1].getCuenta()
            return nombre, cuenta

    #busca un objeto dentro de la lista
    def buscar(self, dato):
        validacion = False
        posicion = -1
        for i in range(self.size):
            if self.arreglo[i].getCuenta() == dato:
                validacion = True
                posicion = i
                break
        if validacion:
            return posicion
        else:
            return posicion

    #borrar un elemento de la lista
    def borrarElemento(self, posicion):
        print("Nombre del alumno: ",self.arreglo[posicion].getNombre()," numero de cuenta: ",self.arreglo[posicion].getCuenta())
        self.arreglo[posicion].setNombre("")
        self.arreglo[posicion].setCuenta("")
        #temp = self.arreglo[posicion]
        for i in range(posicion,self.size-1,1):
            self.arreglo[i] = self.arreglo[i+1]

        self.size = self.size-1
        #return temp

    #imprime los elementos de la lista
    def imprimir(self):
        for i in range(self.size):
            print("Nombre del estudiante:",self.arreglo[i].getNombre(),",numero de cuenta:", self.arreglo[i].getCuenta())