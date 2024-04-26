"""
Exercicio
Crie funções que duplicam, triplicam
e quadruplicam o numero recebido como parametro
"""
def duplicar(numeros):
    def triplicar(numeros):
        def quadriplicar(numeros):
            return numeros * 4
        print(quadriplicar(4))
        return numeros * 3
    print(triplicar(3))
    return numeros * 2
print(duplicar(2))
