# namedtuple - tuplas imutaveis com nomes para valores
from collections import namedtuple

carta = namedtuple('Carta', ['valor', 'naipe'])
as_espadas = carta('A', '♠')
print(as_espadas)
print(as_espadas.valor)

for valor in as_espadas:
    print(valor)
    # print(valor._fields)