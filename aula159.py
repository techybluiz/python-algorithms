# dataclasses - o módulo dataclasses fornece
# um decorador e funções para criar metodos
# como __init__(), __repr__(), (entre outros)

from dataclasses import dataclass

@dataclass(frozen=False)
class Pessoa:
    nome: str
    sobrenome: str
    
    def __post_init__(self):
        self.nome_completo = f'{self.nome}, {self.sobrenome}'
        

if __name__ == '__main__':
    p1 = Pessoa('Bianca', 'Luiz')
    p1.nome_completo = 'Nathan Gabriel'
    print(p1)
    print(p1.nome_completo)