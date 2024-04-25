"""
texto = 'Bianca'
i = 0
tamanho_str = len(texto)

while i < tamanho_str:
    print (texto[i])
    i+=1


Repetição com 'for'

texto = 'python'

novo_texto = ''
for letra in texto:
    novo_texto += F'*{letra}'
    print (letra)
print(novo_texto)
"""
"""
numeros = range(0, 26 , 2)
print(numeros)

for numeros in numeros:
    print(numeros)
"""
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8')
        continue
    for j in range (1,3):
        print(i,j)
else:
    print('For completo com sucesso!')