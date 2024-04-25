class Carro:
    def __init__(self , nome):
        self.nome = nome
        
    @property
    def fabricante(self):
        return self.fabricante
    
    @fabricante.setter
    def fabricante(self , fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def acao(self):
        return f'{self.nome} esta funcionando...'
    
carro = Carro('Siena')
motor = Motor('E-Torq')
# fabricante = fabricante_fabrica('Fiat')
# carro.fabricante = fabricante_fabrica

# maquina_de_escrever = fabricante_fabrica('maquina')
# carro.fabricante = fabricante_fabrica

print(motor.acao())
# print(maquina_de_escrever.escrever())
print(carro.fabricante.acao())