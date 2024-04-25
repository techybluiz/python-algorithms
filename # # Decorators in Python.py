# # Decorators in Python
# decorators are "Syntax Sugar"


'''
without the syntax sugar function:

 pairs = []

 for number in range (0 , 11):
     if numero % 2 == 0:
         pares.append(number)
 print(pairs)

'''
#Now with the list comprehension function:

pairs = [numbers for numbers in range(0,11) if numbers % 2 ==0]
print(pairs)

#exemple with '@':

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