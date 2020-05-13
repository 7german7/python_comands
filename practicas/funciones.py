#********************************************************FUNCIONES********************************************************
# Python nos permite crear funciones en la cual podemos introducir instrucciones especificas.
# Utilizando la palabra reservada "def" podemos definir una funcion y dentro de los parentesis definimos los parametros.
# Sintaxsis: def function_name(parametros):

#Ejemplo de una funcion que imprime "Hola mundo!"
def saludo(): # creamos la funcion
    print "Hola mundo" # instrucciones dentro de mi funcion

saludo() #llamada de mi funcion

# Ejemplo de una funcion que suma un conjunto de numeros
def sumatoria(numeros):
    return sum(numeros)

numeros = range(3) # crea una lista [0, 1, 2] y la asignamos a la variable "numeros"
resultado = sumatoria(numeros) # llamamos nuestra funcion y guardamos el valor que nos retorna(resultado)
print resultado # imprimimos el resultado