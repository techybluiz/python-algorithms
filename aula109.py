# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations , permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

people = [
    'Isabella', 'Estephane', 'Beatriz' , 'Bruna',
]

tshirt = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g', 'gg'],
    ['feminino', 'masculino', 'unisex'],
    ['algodão', 'poliéster']
]

# print(*list(combinations(people, 2)), sep= '\n')
# print()
# print(*list(permutations(people, 2)), sep= '\n') # repete cada nome com outro nome

print_iter(product(*tshirt))