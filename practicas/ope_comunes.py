#********************************************************OPERADORES COMUNES********************************************************

# Longitud de Cadena
cad = "Hola Mundo!"
long = len(cad)
print "longitud de cadena: %s" % (long)

# Longitud de Lista
lis = ["Hola Mundo!", "como estas?", "Mi nombre es German"]
long = len(lis)
print "longitud de lista: %s" % (long)

# Longitud de Tupla
tup = ("Laptop", "17.5", "Asus", 300)
long = len(tup)
print "longitud de tupla: %s" % (long)

# Tipos de datos
numero = 10
decimal = 4.45
cadena = "palabra con espacios"
lista = [1,"dos"]
tupla = ("tres",4)

print type(numero)
print type(decimal)
print type(cadena)
print type(lista)
print type(tupla)

# aplicar conversiones a conjuntos
print lista
print map(str, lista)

# redondeando numeros decimales y definiendo cuantos decimales debe tener
precio = 10.78911534546
print "precio: %f" % (round(precio, 4))

# Generando rangos de una lista
print range(5)

# Sumando los elementos de un conjunto
lista2 = [4,8,2]
print "la suma es: %i" % (sum(lista2))

# organizando un conjunto
print sorted(lista2)

# listando comandos que le podemos aplicar a X dato
print dir(lista2)

# consultar documentacion o informacion de un comando
help(dir)