# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
# resultado = multiplicar(1,2,3,4,5)
# print(resultado)

# def par_impar(numero):
#     multiplo_dois = numero % 2 == 0

#     if multiplo_dois:
#         return f'{numero} é par'
#     return f'O numero {numero} é impar'
# print(par_impar(3))

#Higher Order Functions

def saudacao(msg , nome):
    return f'{msg} ,{nome}'

def executa(funcao , *args):
    return funcao(*args)

print(saudacao('Bom dia!', 'Bianca'))
