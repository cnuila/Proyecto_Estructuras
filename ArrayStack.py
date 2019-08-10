from Pila import Pila

class ArrayStack(Pila):

    def __init__(self):
        self.size = 0
        self.capacity = 1024
        self.arreglo = []
    
    def anula(self):
        for i in range(self.size):
            if self.arreglo[i] != None:
                self.arreglo[i] = None       
        size = 0
    
    def resize(self):
        newCapacity = self.capacity*2
        
            
        
            