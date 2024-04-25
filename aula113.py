#Função reduce -> faz a redução de um iterável em um valor

from functools import reduce
 
produtos = [
    {'produtcs 1' : 'milk','price': 10.00},
    {'produtcs 2' : 'sugar','price': 5.00},
    {'produtcs 3' : 'butter','price': 13.00},
    {'produtcs 4' : 'rice','price': 20.00},
    {'produtcs 5' : 'beans','price': 9.00},
]

def funcao_do_reduce(acumulador, produto):
    print('Acumulador',acumulador)
    print('produto', produto)
    return acumulador + produto['price']

total = reduce(
    funcao_do_reduce, #valor inicial
    produtos, # valor do iteravel
    0
    )

print(f'O total é : {total}')