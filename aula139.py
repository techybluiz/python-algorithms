# super() é a super classe na sub classe
# Classe principal (pessoa)
#     -> super class, base class, parent class
# Classes filhas(Cliente)
#     -> sub class, child class, derived class

class MinhaString(str):
    def upper(self) -> None:
        print('Teste upper')
        retorno = super().upper()
        print('Depois do upper')
        return retorno

string = MinhaString('Luiz')
print(string.upper())