#********************************************************CLASES********************************************************
# Las clases son la representacion de un objeto en programacion

class Persona():
    def __init__(self, nombre_p, edad_p):
        self.nombre = nombre_p
        self.edad = edad_p

    def detalles(self):
        print "nombre: %s, edad: %i" % (self.nombre, self.edad)


nueva = Persona("German", 27)
nueva.detalles()