# Suma Recursiva
# -*- coding: utf-8 -*-

def suma(num, acum):
    if(num<=0):
        return acum
    else:
        acum = acum + num
        num = num-1
        #print('acum: {}, num: {}'.format(acum,num))
    
    return suma(num, acum)
        


if __name__ == "__main__":
    resultado = 0
    print('=======SUMA RECURSIVA========')
    num = int(raw_input('Ingresa un numero: '))
    resultado = suma(num, resultado)
    print("El resultado es: {}".format(resultado))