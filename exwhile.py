"""
nome = 'Bianca Luiz'
tamanho_nome = len(nome)

indice = 0
novo_nome = ''

while indice <len(nome):
    letra =  nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
print (novo_nome)
"""
""" calculadora com while"""


 
while True:
    sair = input('Deseja sair? ')
    sair = sair.lower()
    sair = sair.startswith('s')
    print(f' Você saiu do programa {sair}')

...
numero1 = input('Digite o primeiro numero: ')
numero2 = input('Digite o segundo numero: ')
operador = input('Insira o operador: ')