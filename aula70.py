frase = 'bianca'

i = 0 
qtd_atual = 0
letra_mais_vezes = '    '

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_atual < letra_mais_vezes:
        qtd_atual = letra_atual
        letra_mais_vezes = letra_atual

    i += 1
    
    print('A letra que apareceu mais vezes foi'
          f'{letra_mais_vezes}')
 