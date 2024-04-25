"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print (f'Seu nome é {nome}')
    break
"""
"""
contador = 0

while contador <= 100:
    contador +=1

    if contador == 5:
        print('Numero 5')
        continue
    print('Numero: ', contador)
    if contador==50:
        break
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_colunas:
    coluna = 1
    
    while coluna <= qtd_linhas:
        print(f'{linha=}, {coluna=}')

        coluna += 1
    
    linha +=1
print('Acabou')
  