# Funções recursivas e recursividade
# - funções que podem se chamam de volta
# - uteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
#     - Um problema que posso ser dividido em partes menores
#     - Um caso resursivo que resolev o pequeno problema
#     - Um caso base que para a recursão
#     - fatorial - n(5)! = 5* 4* 3* 2* 1* = 120

# def recursiva(start=0, end=10): #RecursionError: maximum recursion depth exceeded
#     start += 1 # quando você tentou colocar mais coisas que o python pode segurar
#     return recursiva(start, end)
# recursiva()

#solução:
def recursiva(start=0, end=10):
    #caso base  
    if start >= end:
     return end

    print(start , end)
    
    start += 1
    return recursiva(start, end)
 
print(recursiva())


