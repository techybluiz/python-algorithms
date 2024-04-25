# Herança simples - Relações entre classe
#Associação - Usa outro objeto
#Agregação - Usa e Tem outro objeto
#Composição - é dono de
#Herança - Objeto é outro objeto

#Herança vs composição

#Classe principal (pessoa)
#     -> super class, base class, parent class
# Classes filhas (cliente)
#     -> sub class, child class, derived class
class Pessoa:
    def __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...
    
class Aluno(Pessoa):
    ...
    
c1 = Cliente('Bianca', 'Luiz')
c1.falar_nome()
a1 = Aluno('Beatriz', 'Matsuzaki')
a1.falar_nome()