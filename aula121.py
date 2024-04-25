# #metodo de instancias de classes em python
# Classe é um molde que gera novas instancias (objetos)

class Carro:
    def __init__(self, nome = 'Sei lá'):
        self.nome =  nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerrando...')

fusca = Carro('Fusca ')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='celta')
celta.acelerar()
