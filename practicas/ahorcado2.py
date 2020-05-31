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
    max_tries = 7
    tries = 0
    letter_found = False


    print("****************Vamos a Jugar al Doctor Ahorcado****************")
    # print( len(WORDS) )
    random_index = random.randint(0, len(WORDS)-1)
    print(WORDS[random_index])
    random_word = WORDS[random_index]
    hidden_word = len(random_word) * "'_"
    print(hidden_word)
    letter = str( raw_input("Ingresa una letra: ") ).lower()
    # print(letter)
    for i in range( len(random_word) ):
        if (letter==random_word[i]):
            indexs_found = append(i)
        else:
            letter_found = False
    
    if(letter_found):
        print("se encontro la letra: {}".format(i) )
    else:
        print("Ups! no se encontro la letra")

if __name__ == "__main__":
    run()
