# # Decoradores em python
# decoradores são "Syntax Sugar"


'''
sem a função syntax sugar fariamos o codigo assim:

 pares = []

 for numero in range (0 , 11):
     if numero % 2 == 0:
         pares.append(numero)
 print(pares)

'''
#Agora com a função list comprehension:

pairs = [numbers for numbers in range(0,11) if numbers % 2 ==0]
print(pairs)

#exemplo com '@':


def message(func):
    def wrapper():
        print('Test before function')
        func()
        print('Test after function')
    return wrapper

@message
def my_fuction():
    print('In function')
my_fuction()