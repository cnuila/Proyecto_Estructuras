
#------------------------------------------Node--------------------------------------------------
class Node:
    def __init__(self):
        self.anterior = None
        self.siguiente = None
        self.pdata=None
        #self.next=None
    def setData(self,data):
        self.pdata=data
    def getData(self):
        return self.pdata

    def setSiguiente(self,next):
        self.siguiente = next

    def getSiguiente(self):
        return self.siguiente

    def setAnterior(self,prev):
        self.anterior = prev

    def getAnterior(self):
        return self.anterior
#----------------------------------LinkedQueue---------------------------------------------
class LinkedQueue:
    def __init__(self):#constructor de la clase en el cual se inicializan las variables
        self.frente=Node()
        self.final=Node()
        self.frente=None
        self.final=None
    def __del__(self):
        if self.final:
            del self.final
        
    def isEmpty(self):#retorna verdadero si la lista esta vacia
        if self.frente == None:   
            return 'Esta vacia'
        else:
            return 'No esta vacia'
        
        
    def queue (self, data):#metodo utilizado para encolar un elemento
        self.newNode=Node()
        self.newNode.setData(data)
        if self.final==None and self.frente==None:
            self.final=self.newNode
            self.frente=self.newNode
        else:
            self.newNode.setSiguiente(self.final)
            self.final.setAnterior(self.newNode)
            self.final=self.newNode
        print('Ingresado con exito')
    def front(self):#devuelve o retorna el elemento que está al frente de la cola
        if self.frente:
            return self.frente.getData()
        else:
            print('Esta vacia')
            return None
    def deQueue(self):#Quita el elemento que esta enfrente de la cola y hace los corrimientos respectivos
        tmp = Node()
        if self.frente==None:
            return None
        elif self.frente==self.final:
            tmp=self.frente
            tmpData=0
            tmpData=tmp.getData()
            tmp.setData(None)
            del tmp
            self.frente=None
            self.final=None
            print(tmpData)
            return tmpData
        else:
            tmp=self.frente
            self.frente=tmp.getAnterior()
            tmpData=tmp.getData()
            tmp.setData(None)
            del tmp
            self.frente.setSiguiente(None)
            print(tmpData)
            return tmpData
    
    def clear(self):#limpia, es decir elimina todos los elmentos de la cola
        if self.final:
            del self.final
        self.frente=None
        self.final=None
    def mostrar(self,Linked):
        nuevo=Linked
        if(nuevo.front()!=None):
            nuevo.deQueue()
            nuevo.mostrar(nuevo)
#--------------------------ArrayQueue------------------------

class ArrayQueue:
    def __init__(self):#constructor de la clase en el cual se inicializan las variables
        self.size = 0
        self.capacity = 10
        self.array = []
        self.final = Node()
        self.frente = Node()

    def isEmpty(self):#retorna verdadero si la lista esta vacia
        if self.size==0:   
            return 'Esta vacia'
        else:
            return 'No esta vacia'

    def queue(self,data):
        self.array.append(data)
        if self.size==0:
            self.size=self.size+1
        else:
            for i in range(self.size,0,-1): 
		            self.array[i]=self.array[i-1]

            self.array[0]=data
            self.size=self.size+1
        print(data,', registrado con exito')

    def front(self):#retorna el elemento que esta al frente de la cola, sin eliminarlo
        if self.size!=0:
            print(self.size)
            return self.array[self.size-1]
        else:
            return 'Esta vacia'
    
    def deQueue (self):#quita el elemento que esta al frente de la cola y hace sus corrimientos respectivos
        if self.size>0:
            tmp=self.array[self.size-1]
            del self.array[self.size-1]
            self.size=self.size-1
            print(tmp,' retirado con exito')
            return tmp
    def clear(self):#elimina todos los elementos de la lista
        for i in range(self.size,0,+1): 
		        if self.array[i]!=None:
			        del self.array[i]
        self.size=0
    def mostrar(self):#metodo que muestra todos los elementos   
        for i in range(0,self.size,+1): 
            print (self.size-i-1,'-',self.array[i])

#daniel = ArrayQueue()
#jose=LinkedQueue()
#jose.queue(2)
#jose.queue('hey')
#jose.clear()
#jose.mostrar(jose)