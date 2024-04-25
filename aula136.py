# Relação entre classes: associação e composição
# Composição é uma especialização da agregação
# Mas nela, quando o objeto "pai" for apagado, todas
# as referencias dos objetos "filhos" tambem são apagadas

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.endereco = []
        
    def inserir_endereco (self, rua, numero):
        self.endereco.append(Endereco(rua, numero))
    
    def listar_endereco (self):
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua ,numero):
        self.rua = rua
        self.numero = numero
        
    def __del__(self):
        print('Apagando', self.rua, self.numero)
        
cliente1 = Cliente('Estephane')
cliente1.inserir_endereco('Av Paulista', 7802)
cliente1.inserir_endereco('Rua Aldeia Zamaicara', 55)
cliente1.listar_endereco()

del cliente1

print('ESSE É O FIM DO CODIGO!')