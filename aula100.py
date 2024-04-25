# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
from dados import produtos

novos_dados = [
   {**p, 'preco' : round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
# ordene os produtos por nome decrescente (do maior para menor)
# gere produtos_ordenados_por_nome por deep copy( copia profunda)
# ordene os produtos por preco crescente (do menor para maior)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse= True)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
    )
    
ordem_crescente_de_produtos = sorted(produtos,
        key=lambda p:p['preco'])
ordenados_produtos = copy.deepcopy(produtos_ordenados_por_nome)
print('Produtos reias:')
print(*produtos, sep='\n')
print()
print('Produtos ordenado por nome: ')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('Produtos ordenados por preço: ')
print(*produtos_ordenados_por_preco, sep='\n')

# for produto, info in produtos_ordenados_por_nome.items():
#     print(produtos_ordenados_por_nome)