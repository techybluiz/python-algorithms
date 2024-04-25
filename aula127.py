import json
CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Estephane', 20)
p2 = Pessoa('Beatriz', 15)
p3 = Pessoa('Nathan', 35)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open (CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)