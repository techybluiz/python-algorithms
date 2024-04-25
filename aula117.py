#Salvando um arquivo em JSON

import json

# people = {
#     'name1' : 'Bianca','sobrenome': 'Luiz',
#     'name2': 'Isabella','sobrenome': 'Luiz',
#     'name3': 'Estephane','sobrenome': 'Silva',
#     'name4': 'Beatriz','sobrenome': 'Tre',
#     'name5': 'Thor','sobrenome': 'Luiz',
#     'name6': 'Nathan','sobrenome': 'Muniz',
#     'name7': 'Marcelo','sobrenome': 'Luiz',
#     'name8': 'Bruno', 'sobrenome': 'Luiz',
#     'name9': 'Adriana', 'sobrenome': 'Luiz',
#     'name10': 'Gustavo', 'sobrenome': 'Luiz',
#     'altura' : 1.8,
#     'dev': True,
#     'nada': None
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(people, arquivo,
#               indent=2)

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    people = json.load(arquivo)
