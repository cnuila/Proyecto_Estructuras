class Alumno:

    #constructor
    def __init__(self,cuenta, nombre):
        self.cuenta = cuenta
        self.nombre = nombre

    #setters y getters
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setCuenta(self,cuenta):
        self.cuenta = cuenta
    def getCuenta(self):
        return self.cuenta

    #toString
    def __str__(self):
        return self.cuenta + " " + self.nombre
    
    #equals
    def equals(self,alumn):
        alumno = Alumno("","")
        alumno = alumn
        return self.cuenta == alumno.getCuenta()