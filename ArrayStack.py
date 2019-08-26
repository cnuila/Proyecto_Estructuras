from Pila import Pila

class ArrayStack(Pila):

    #constructor
    def __init__(self):
        self.size = 0
        self.arreglo = []
    
    #elimina todos los elementos de la pila
    def anula(self):
        for i in range(self.size):
            if self.arreglo[i] != None:
                self.arreglo[i] = None    
        self.size = 0 #reinicia el size
    
    #agrega un elemento a la pila 
    def empuja(self,data):
        self.arreglo.append(data) #agrega el dato enviado al final del arreglo
        self.size = self.size+1
    
    #saca el elemento en el tope de la pila
    def saca(self):
        if self.size == 0:
            return None
        else:
            datoTemp = self.arreglo[self.size-1] #se guarda temporalmente para mostrarlo
            self.arreglo[self.size-1] = None
            self.size-1
            return datoTemp
    
    #Devuelve el elemento en el tope de la pila
    def tope(self):
        if self.size == 0:
            return None
        else:
            return self.arreglo[self.size-1]

    #devuelve si la pila esta vacia
    def vacia(self):
        return self.size == 0

        
            
        
            