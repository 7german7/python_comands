#********************************************************TIPOS DE DATOS********************************************************
# Python maneja diferentes tipos de datos y por ser un lenguaje de programacion con tipado dimamico no es obligatorio declarar
# el tipo de dato como los lenguajes de programacion con tipado  estatico (C, C++, entre otros), entre los cuales se encuentran:

# int (numeros enteros)
print "********************************************************************************"
a = 5;
print "a=%i" % (a)
print type(a)

# bool (boleanos)
print "********************************************************************************"
boleano = True # True o False
print "booleano=%i" % (boleano) # imprime 0 o 1
print type(boleano)

# str (cadenas de texto)
print "********************************************************************************"
cadena = "Hola Mundo!"
print "mensaje=%s" % (cadena)
print type(cadena)

# [] Listas o arreglos
print "********************************************************************************"
lista = ["German", 10, "Trinidad y Tobago"]
print lista # imprime todos los datos de la lista
print lista[0] # imprime un valor especifico de la lista, este caso puede ser: lista[0], lista[1] o lista[2]
print type(lista)

# {} Diccionarios (Datos tipos Json)
print "********************************************************************************"
persona = {"nombre":"German", "apellido":"Ceballos", "edad": 27, "pais": "Trinidad y Tobago"}
print persona # imprime todo el contenido
print persona["pais"] # imprime un valor especifico
print type(persona)

# () Tuplas (Igual que las listas o arreglos, pero a diferencia que los datos no se pueden modificar)
print "********************************************************************************"
laptop = ("Asus", 17.5, "gris", "ligera")
print laptop # imprime todo los valores
print laptop[2] # imprime un color especifico
print type(laptop)