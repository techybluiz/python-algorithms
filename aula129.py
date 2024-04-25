# @staticmethod (metodos estaticos) são inuteis em python
# metodos estaticos são metodos que estao dentro da 
# classe, mas nao tem acesso ao self nem ao cls
# Em resumo, são funções que existem dentro da sua classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)
c1 = Classe()
c1.funcao_que_esta_na_classe(1,2,3)
    