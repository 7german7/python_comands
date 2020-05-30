# Ejercicio del Ahorcado
# ASCII Art => Se implementa para crear imagenes con caracteres

# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'externocleidomastoideo', # 0
    'cefalorraquideo', # 1
    'mesenterio', # 2
    'duramadre', # 3
    'hipofisis', # 4
    'radio', # 5
    'craneo', # 6
    'patela' # 7
]

def run():
    print("****************Vamos a Jugar al Doctor Ahorcado****************")
    # print( len(WORDS) )
    random_index = random.randint(0, len(WORDS)-1)
    print(WORDS[random_index])
    random_word = WORDS[random_index]
    letter = str( raw_input("Ingresa una letra: ") ).lower()
    # print(letter)
    letter_exist = random_word.find(letter)
    if (letter_exist==-1):
        print("Ups! Letra no encontrada")
    else:
        print("Letra encontrada")

if __name__ == "__main__":
    run()
