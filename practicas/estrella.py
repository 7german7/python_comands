# Mi primera APP en Python =D

# -*- coding: utf-8 -*-
import turtle

def main():
    ventana = turtle.Screen()
    ventana.title("Dibujando")
    ventana.bgcolor("black")

    dibujo = turtle.Turtle()
    dibujo.setpos(0,-250)
    dibujo.color("yellow")
    dibujo.pensize(10)
    dibujo.penup()
    dibujo.forward(130)
    dibujo.left(110)
    dibujo.pendown()
    dibujo.forward(150)
    dibujo.right(70)
    dibujo.forward(150)
    dibujo.left(130)
    dibujo.forward(150)
    dibujo.right(60)
    dibujo.forward(150)
    dibujo.left(140)
    dibujo.forward(150)
    dibujo.right(60)
    dibujo.forward(150)
    dibujo.left(130)
    dibujo.forward(150)
    dibujo.right(70)
    dibujo.forward(150)
    dibujo.left(135)
    dibujo.forward(150)
    dibujo.right(50)
    dibujo.forward(150)
    
    
    turtle.mainloop()

if __name__ == "__main__":
    main()