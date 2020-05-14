#********************************************************FUNCIONES - DIBUJANDO UN CUADRADO INGRESANDO PARAMETROS********************************************************

import turtle

# Cuerpo principal de mi APP
def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    num = make_square(dave)

    turtle.mainloop()


# Funciones
def make_square(dave):
    print("Vamos a dibujar un cuadrado")
    print("Ingresa un Numero")
    lenght = int(raw_input())

    i = 0
    for i in range(4):
        make_line_and_left(dave, lenght)

def make_line_and_left(dave, lenght):
    dave.forward(lenght)
    dave.left(90)
    
if __name__ == "__main__":
    main()