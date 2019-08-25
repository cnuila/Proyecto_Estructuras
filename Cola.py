
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
    def __init__(self):
        self.frente=Node()
        self.final=Node()
        self.frente=None
        self.final=None
    def __del__(self):
        if self.final:
            del self.final
        
    def isEmpty(self):
        return self.frente == None
        
    def queue (self, data):
        self.newNode=Node()
        self.newNode.setData(data)
        if self.final==None and self.frente==None:
            self.final=self.newNode
            self.frente=self.newNode
        else:
            self.newNode.setSiguiente(self.final)
            self.final.setAnterior(self.newNode)
            self.final=self.newNode
    def front(self):
        if self.frente:
            return self.frente.getData()
        else:
            return None
    def deQueue(self):
        tmp = Node()
        if self.frente==None:
            return None
        elif self.frente==self.final:
            self.tmp=frente
            self.tmpData=0
            self.tmpData= tmp.getData()
            self.tmp.setData(None)
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
    def clear(self):
        if self.final:
            del self.final
        self.frente=None
        self.final=None
#--------------------------ArrayQueue------------------------

class ArrayQueue:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.array = []
        self.final = Node()
        self.frente = Node()

    def isEmpty(self):
        return self.size==0

    def queue(self,data):
        self.array.append(data)
        if self.size==0:
            self.size=self.size+1
        else:
            for i in range(self.size,0,-1): 
		            self.array[i]=self.array[i-1]

            self.array[0]=data
            self.size=self.size+1
        print(data)

    def front(self):
        if self.size!=0:
            print(self.size)
            return self.array[self.size-1]
        else:
            return None
    
    def deQueue (self):
        if self.size>0:
            self.tmp=self.array[self.size-1]
            del self.array[self.size-1]
            self.size=self.size-1
            return self.tmp
    def clear(self):
        for i in range(self.size,0,+1): 
		        if self.array[i]!=None:
			        del self.array[i]
        self.size=0

daniel = ArrayQueue()
jose=LinkedQueue()

jose.queue(2)
jose.queue('hey')
print(jose.front())
jose.deQueue()
print(jose.front())
jose.clear()
