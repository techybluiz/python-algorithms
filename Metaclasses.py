# Metaclasses são o tipo das classes
class Pessoa(object, metaclass=type): #object = herança 
    def __new__(cls, *args, **kwargs):
        print('Meu new')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome) -> None:
        print( 'Meu init')
        self.nome = nome
        
p1 = Pessoa('Bia') 
