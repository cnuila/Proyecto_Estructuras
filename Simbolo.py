class Simbolo:
    
    #constructores
    def __init__(self):
        self.symbol = ''
    
    def __init__(self, symbol):
        self.symbol = symbol

    #setters y getters
    def setSymbol(self, symbol):
        self.setSymbol = symbol
    def getSymbol(self):
        return self.symbol

    #toString
    def __str__(self):
        return self.symbol
    
    #equals
    def equals(self,simbol):
        symbolTemp = Simbolo()
        symbolTemp = simbol
        return self.symbol == symbolTemp.getSymbol()
