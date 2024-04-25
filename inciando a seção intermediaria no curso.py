#inciando a seção intermediaria no curso python
# def soma(x,y,z=0):
#     if z is not None:
#         print(f'{x=} y={y} z={z}', '/' 'x + y + z =' , x + y + z)
#     else: 
#         print(f'{x=} y={y}' ,'/' 'x + y + =' , x + y )
# soma(1,2,3)

# def escopo():
#     x = 1 
#     def outro_escopo():
#         y = 2
#         x = 2
#         print(x,y)
#     outro_escopo()
#     print(x)
# escopo()
'''
retorno das funções
*args = empacotamento e desempacotamento
'''
# x , y , *resto = 1, 2, 3, 4, 5
def soma(*args): #desempacota
    total = 0
    for numero in args:
        total+= numero
    return total
soma( 1,2,3,4,5)
print(sum((1,2,3,4,5,))) #soma dos valores (empacota)

numero = 1,2,3,4,5,6,7,8,9,
# print(*numero)




#  soma1 = soma(2 , 2)
# soma2 = soma(3 , 3)
# print(soma1 + soma2)
