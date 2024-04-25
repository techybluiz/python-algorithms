"""
split - divide uma string
join - une uma string
"""
# frase = 'olha só que coisa interessante'
# lista_palavras = frase.split(' ')

# for i , frase in enumerate(lista_palavras):
#     print(lista_palavras[i])

# print(lista_palavras)


#Lista de listas

salas = [
    ['Maria', 'Helena'],
    ['Elaine',],
    ['Luiz' , 'João', 'Eduarda',],
]

for sala in salas:
    print(f'A sala é: {sala}')
    for aluno in sala:
        print(aluno)
print(*salas, sep='\n')