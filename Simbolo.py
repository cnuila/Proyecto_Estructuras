class Simbolo:
    
    def __init__(self):
        self.symbol = ''
    
    def __init__(self, symbol):
        self.symbol = symbol

    def setSymbol(self, symbol):
        self.setSymbol = symbol
    def getSymbol(self):
        return self.symbol

    def __str__(self):
        return self.symbol
    
    def equals(self,simbol):
        symbolTemp = Simbolo()
        symbolTemp = simbol
        return self.symbol == symbolTemp.getSymbol()
