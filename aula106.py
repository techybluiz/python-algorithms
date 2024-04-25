#Decoradores com parâmetros

# def decorator(func):
#     print('decorator 1')

#     def internal(*args, **kwargs):
#         print('internal')
#         result = func(*args, **kwargs)
#         return result
#     return internal
# @decorator
# def sum (x,y):
#     print(f'{sum.__name__}')
#     return x + y

# ten_plus_five = sum (10, 5)
# print(ten_plus_five)

#Ordem dos decoradores

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:' , nome)
        
        def sua_nova_funcao(*args , **kwargs):
            res = func(*args , **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return(decorador)
    
@parametros_decorador(nome = 'segundo' )  
@parametros_decorador(nome = 'primeiro')      
def soma( x, y):
    return x + y

dez_mais_cinco = soma( 10, 5)
print(dez_mais_cinco)#exibe 15, primeiro,segundo-> pq o decorador,decora o resultado(res) da função