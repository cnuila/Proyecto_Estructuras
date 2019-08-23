#------------------------------------------Node--------------------------------------------------
class Object:
    def __init__(self):
        self.wenas = "drogas"
class Node:
    def __init__(self):
        #self.pdata = Object()
        self.pdata = None
        self.anterior = None
        self.siguiente = None
        #self.data=data
        #self.next=None
    def setData(self,data):
        self.pdata=data
    def getData():
        return self.data
#----------------------------------LinkedQueue---------------------------------------------
class LinkedQueue:
    def __init__(self):
        self.final = Node()
        self.frente = Node()
        frente=None
        final=None

    def isEmpty(self):
        return self.frente == None
        
    def queue (self, data):
        newNode=Node()
        newNode.setData(pdata)
        if final==None and self.frente==None:
            final=newNode
            frente=newNode
        else:
            newNode=setSiguiente(final)
            final=setAnterior(newNode)
            final=newNode
    def front(self):
        if frente:
            return frente.getData()
        else:
            return None
    def deQueue(self):
        tmp = Node()
        if frente==None:
            return None
        elif frente==final:
            tmp=frente
            tmpData=0
            tmpData= tmp.getData()
            tmp.setData(None)
            del tmp
            frente=None
            final=None
            return tmpData
        else:
            tmp=frente
            frente=tmp.getAnterior()
            tmpData=Object()
            tmpData=tmp.getData()
            tmp.setData(None)
            del tmp
            frente.setSiguiente(None)
            return tmpData
    def clear(self):
        if final:
            del final
        frente=None
        final=None
#--------------------------ArrayQueue------------------------

class ArrayQueue:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.array = []
        final = Node()
        frente = Node()

    def isEmpty(self):
        return self.size==0

    def queue(self,data):
        for i in range(size+1,0,i-1): 
		        array[i]=array[i-1]

        array[0]=data
        size=size+1
        print(data)

    def front(self):
        if size!=0:
            return array[size-1]
        else:
            return None
    
    def deQueue (self):
        if size>0:
            tmp=array[size-1]
            del array[size-1]
            size=size-1
            return tmp
    def clear(self):
        for i in range(size,0,i+1): 
		        if array[i]!=None:
			        del array[i]
        size=0

daniel = ArrayQueue()
print(daniel.isEmpty())

jose=LinkedQueue()
print(jose.isEmpty())