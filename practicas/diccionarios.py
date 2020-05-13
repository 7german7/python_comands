#********************************************************DICCIONARIOS********************************************************
# Los diccionarios en python son tipos de datos muy parecidos a los archivos json, los cuales nos permiten crear una lista
# pero con identificadores definidos por nosotros.
# sintaxis dicc = {"id":"valor"}

producto = {"Tipo":"Laptop", "Marca":"Asus", "Precio":350.9, "Modelo":"mod01b148s"}
print producto # imprime todo los datos
print producto["Marca"] # imprime la marca de la laptop

producto["Tipo"] = "PC"
print producto 