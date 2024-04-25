# #Exercicio:
# #some os valores nas listas retornando uma nova
# #com os valores somados
# #Se uma lista for maior que a outra, a soma só vai 
# # considerar o tamanho da menor

# list_A = [1 , 2, 3, 4, 5, 6, 7]
# list_B = [1 ,2 , 3, 4]
# list_new = []
# for i in range(len(list_B)):
#     list_new.append(list_A[i] + list_B[i])
# print(list_new)
   
   
# Count é um iterador sem fim
#Diferente da função range que tem fim
from itertools import count
#count é um contador infinito 
counter = count(0,1)
for i in counter:
    if i > 100:
        break
    print((counter))
