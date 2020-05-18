# -*- coding: utf-8 -*-
# Factorial de un Numero

def fact(num):
    if(num==0):
        return 1

    return num * fact(num-1)

def msg():
    print("Ingresa un Numero")
    num = raw_input()
    return num

def main():
    num = int(msg())
    res = fact(num)
    print "El factorial de %i es: %i" % (num, res)


if __name__ == "__main__":
    main()


# 5! = 5*4*3*2*1*