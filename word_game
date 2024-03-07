import os
import random

palavras = ['perfume', 'python', 'aleatorio', 'clima', 'trabalho']
letras_acertadas = ''
palavra_secretanumero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavras:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavras:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavras:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavras)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

