# lista = ['Sonia', 'Maria', 'Jorge']
# lista.append('João')
# lista_numerada = enumerate(lista , start= 10)
# for indice , nome in lista_numerada:
#     print(indice , nome)
# lista_compras = list.append(input('Digite o item da lista: '))
# # lista_ordenada = enumerate(list, start=1)
# # for indice in lista_ordenada:
#    print(indice , list)
# lista = input('Selecione uma opção: '
#               '[i]nserir [A]pagar [L]istar: ')
# print(lista)
# letra = 'i'
# if letra in lista == 'i':
#     print(input('Insira um item: '))
#     list.append(lista)
import os
lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [A]pagar [L]istar: ')

    if opcao == 'i':    
        valor = input('Digite o item: ')
        lista.append(valor)

    elif opcao == 'a':       
        indice_str = input('Digite o indice que deseja apagar: '
        
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar esse item')

    elif opcao == 'l':
           if len(lista) == 0:
              print('nada para listar.')

    for i , valor in enumerate(lista , start=1):
                print( i , valor)
    else: 
        print('Selecione uma opção!')