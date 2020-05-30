# Practicando con Strings o Cadena de Caracteres

# -*- coding: utf-8 -*-

def run():
    cad = "Hola German"
    print(dir(cad))
    cad = cad.upper() # MAYUSCULAS
    print(cad)
    cad = cad.lower() # minusculas
    print(cad)
    cad = cad.capitalize() # Mayuscula
    print(cad)
    cad = cad.index("a")
    print(cad)



if __name__ == "__main__":
    run()

# NOTAS:
# Los string no se pueden modificar
# Python 2.7 Utiliza ASCII ( Solo incluye caracteres del lenguaje Ingles )
# Python 3.X Utiliza Unicode (Incluye caracteres especiales de otros lenguajes)