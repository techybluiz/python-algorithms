# Metodos de classe
# São metodos onde 'Self' será 'cls', ou seja
# ao inves de receber a instancia no primeiro
# parametro, receberemos a propria classe

class Pessoa:
    ano = 2024 #atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod  #decorator
    def metodo_de_classe(cls):
        print('Hey')
        
p1 = Pessoa('João', 34)
print(Pessoa.ano)
Pessoa.metodo_de_classe()