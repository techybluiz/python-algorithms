#Escopo da classe e de metodos de classe

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
        variavel = 'valor'
        print(variavel)
    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome='leao')
print(leao.nome)
print(leao.executar('Maçã'))


# animal = 'Leao'
# alimento = 'Maçã'
# acao = 'Coemndo'

# print(f'O {animal} esta {acao} {alimento}')