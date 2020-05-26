# -*- coding: utf-8 -*-
# Practicando Python con Números Aleatorios

import random # La librería random nos proporciona métodos o funciones para gestionar números aleatoriamente

def run():
    num_found = False # inicializo una variable
    random_num = random.randint(0, 20) # Selecciona un numero aleatorio del 0 al 20
    print("***********ADIVINA EL NÚMERO*************")

    while not num_found: # mientras el usuario no adivine el numero, repite esto.
        print("Ingresa un número del 0 al 20:")
        num = int(raw_input()) # ingresa un valor por teclado, y cambia su tipo de valor a entero/int
        if num == random_num:
            print("Que suerte tienes, lo Adivinaste!")
            print("Quieres seguir jugando(s/n)?")
            resp = str(raw_input()) # ingresa un valor por teclado, y cambia su tipo de valor a cadena/string
            if resp=='s':
                run() # RECURSIVIDAD, la función run() se llama dentro de si misma.
            elif resp=='n':
                print("Espero que te hallas divertido, vuelve pronto! Adiós")
                exit() # cierro mi aplicación
        elif num > random_num:
            print("Lo siento, fallaste =(, pero no te desanimes, te daré una pista: El número es más pequeño")
        elif num < random_num:
            print("Lo siento, fallaste =(, pero no te desanimes, te daré una pista: El número es más grande")

if __name__ == "__main__": # aquí arranca/inicia mi aplicación
    run()