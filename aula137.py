# Exercicio com classes
#     1 - Crie uma classe Carro (nome)
#     2 - Crie uma classe Motor (nome)
#     3 - Crie uma classe Fabricante (nome)
#     4 - Faça a ligação entre carro tem motor
#OBS: Um motor pode ser de varios carros
# 5 - Faça a ligação entre Carro e Fabricante
# obs. Um fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._producer = None
 #MOTOR
    @property
    def motor (self):
        return self._motor
    
    @motor.setter
    def _producer(self, value):
        self._producer = value
 
#FABRICANTE         
    @property
    def _producer (self):
        return self._producer
    
    @_producer.setter
    def _producer(self , value):
        self._producer = value

class Motor:
    def __init__(self, name):
        self.name = name
        

class Producer:
    def __init__(self, name):
        self.name = name


siena = Car('Siena')
fiat = Producer('Fiat')
motor = Motor ('vetor')
siena.producer = fiat
siena.motor = motor

print(siena.name, siena.producer.name, siena.motor.name)

gol = Car('Gol')
fiat = Producer('Volkswagen')
motor = Motor ('TotalFlex ')
gol.producer = fiat
gol.motor = motor

print(gol.name, gol.producer.name, gol.motor.name)

