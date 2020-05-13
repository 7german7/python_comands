#********************************************************TUPLAS********************************************************
# Con este tipo de variable podemos crear una lista o un arreglo, a diferencia que su contenido no se puede modificar.

lista_modificable = ["PC de Escritorio", "Mac", 15]
print lista_modificable
lista_modificable[0] = "PC"
print lista_modificable

lista_no_modificable = ("Laptop", "Asus", 17)
print lista_no_modificable
lista_no_modificable[1] = "Acer" # muestra error
print lista_no_modificable