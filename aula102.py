#Variaveis livres + nonlocal(locals, globals)
# globals (tudo o que esta definido na função)
print(globals())
def fora(x):
    a = x #variavel livre, pq não esta definida dentro da função (dentro)
    def dentro():
        print(locals()) #locals informa tudo que esta definido a partir dql local
        print(dentro.__code__.co_freevars) #
        return a
    return dentro

dentro1= fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_concatenar):
        return valor_final
    return interna

c = concatenar('a') #sempre retornara o valor inicial, para corrigir usamos a função 'nonlocal = 'variavel'
print(c('b'))
print(c('f'))
print(c('v'))

    