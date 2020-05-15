# -*- coding: utf-8 -*-

def main():
    print("Ingresa un número:")
    num = int(input())
    cont = eval_primo(num)
    if(cont==2):
        print("El número es primo")
    else:
        print("El número no es primo")

def eval_primo(num):
    cont=0
    # Teoria: un numero primo es aquel que solo se divide entre 1 y el mismo y su restante es 0.
    for i in range(1, num+1):
        res=num%i # obtenemos como resultado el restante de la divicion
        if(res==0):
            cont+=1
    return cont

if __name__ == "__main__":
    main()