class Alumno:

    #constructores
    def __init__(self):
        self.cuenta = ""
        self.nombre = ""
    
    def __init__(cuenta, nombre):
        self.cuenta = cuenta
        self.nombre = nombre

    #setters y getters
    def setNombre(nombre):
        self.nombre = nombre
    def getNombre():
        return nombre

    def setCuenta(cuenta):
        self.cuenta = cuenta
    def getCuenta():
        return self.cuenta

    #toString
    def __str__():
        return self.cuenta + " " + self.nombre
    
    #equals
    def equals(self,alumn):
        alumno = Alumno()
        alumno = alumn
        return self.cuenta == alumno.getCuenta()