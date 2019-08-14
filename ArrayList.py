from Lista import Lista

class ArrayList(Lista):

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
            if(self.arreglo[i] != None):
                self.arreglo[i] = None
        self.size = 0
    
    


    