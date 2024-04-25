# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (isinstance) que 
# podem ter seus proprios atributos e metodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar varias ações.
# Por convenção, usamos PascalCase para nomes de 
# Classes
# string = 'Bianca'
# print(string.upper())
#__init__ -> inicia os atributos da classe
class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
p1 = pessoa('Bianca' , 'Luiz')
# p1.nome = 'Bianca'
# p1.sobrenome = 'Luiz'

print(p1.nome)
print(p1.sobrenome)