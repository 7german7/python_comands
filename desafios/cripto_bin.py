# Criptografia con Binarios

# -*- coding: utf-8 -*-
from alfa_bin_mayus import mayus_letter

def cypher(message):
    cypher_word = []

    for letter in message:
        for i in mayus_letter.iterkeys():
            if(letter==i):
                # print('letra {}, es igual a i {}'.format(letter,i))
                cypher_word.append(mayus_letter[i])

    return cypher_word

def descypher(cypher_message):
    descypher_word = ''

    for i in cypher_message:
        #print i
        for key, letter in mayus_letter.iteritems():
            #print letter
            if(i==letter):
                descypher_word+=key
                # print ('{} = {}'.format(letter,i))
    
    return descypher_word

           

if __name__ == "__main__":
    
    message = 'GERMAN'

    cypher_message = cypher(message)
    print cypher_message

    message = descypher(cypher_message)
    print message
