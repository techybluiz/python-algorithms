# Exercicio - unir lista
# Crie uma função zipper
# O trabalho dessa função será unir duas
# listas na ordem
# Use todos os valores da menor lista.
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# resultado = 
# [('Salvador', 'BA') ,('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest #biblioteca que permite uasr a lista maior

list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
join_list = list(zip_longest(list1 , list2)) #função para usar a lista maior como base
# join_lists = zip(list1 , list2) função para usar a lista menor como base
print(f'The new list was: {join_list}')
print(list(zip_longest(list1, list2, fillvalue = 'Sem cidade'))) #função para none retornar uma str