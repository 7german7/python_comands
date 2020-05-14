#********************************************************CLASES********************************************************
import sys 
usuario = raw_input()
clave = int(raw_input())

if (usuario=="junior" and clave==123456):
    print "bienvenido: %s" %(usuario)
else:
    print "usuario o clave incorrecta"