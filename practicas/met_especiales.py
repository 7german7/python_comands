#********************************************************METODOS ESPECIALES********************************************************

class Persona():
    def __init__(self, nombre_p, edad_p):
        self.nombre = nombre_p
        self.edad = edad_p

    def detalles(self):
        print "nombre: %s, edad: %i" % (self.nombre, self.edad)


class Auto():
    def __init__(self, marca_a, modelo_a):
        self.marca = marca_a
        self.modelo = modelo_a
    
    def detalles(self):
        print "marca: %s, modelo: %s" % (self.marca, self.modelo)


nueva = Persona("German", 27)
nueva.detalles()

nuevo = Auto("Mustang", "GT")
nuevo.detalles()
