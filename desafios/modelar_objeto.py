# -*- coding: utf-8 -*-
AUTO_STATUS = ['''
  ______
 /|_||_\`.__
(   _    _ _|
=`-(_)--(_)-'
''','''
            _______
    _-_-  _/\______|___
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'
''','''
   ______
  /|_||_\`.__
 (   _    _ _|
8=`-(_)--(_)-'
''']

MENU = ['''
    1) Encender
    2) Acelerar
    3) Apagar
    4) Salir
''']

class Auto():
    def __init__(self, status):
        self.status = status

    def info(self):
        print('****************Car Information****************')
        print('Estatus: {}'.format(self.status))

    def show_status(self):
        if(self.status=='on'):
            print(AUTO_STATUS[2])
        if(self.status=='off'):
            print(AUTO_STATUS[0])
        if(self.status=='accelerate'):
            print(AUTO_STATUS[1])


def menu():
    print('¿Que deseas hacer con tu auto?')
    print(MENU[0])
    opc = int(raw_input('OPC: '))
    return opc

if __name__ == "__main__":
    
    auto = Auto('off')
    auto.info()
    print(AUTO_STATUS[0])

    while(True):
        opc = menu()
        if(opc==1): # Enciende el auto
            auto.status = 'on'
        if(opc==2): # Acelera el auto
            if(auto.status=='on'):
                auto.status = 'accelerate'
            else:
                print('Debes encender tu auto')
        if(opc==3): # Apaga el auto
            auto.status = 'off'
        if(opc==4): # Salir de la aplicacion
            if(auto.status=='off'):
                print('===>Adios')
                break
            elif(auto.status=='on'):
                print('===>Debes apagar tu auto antes de salir')
            elif(auto.status=='accelerate'):
                print('===>Estaciona y apaga tu auto antes de salir')
        auto.info()
        auto.show_status()
