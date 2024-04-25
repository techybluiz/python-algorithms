# __new__ e __init__ em classes Python
# new -> cria um novo obeto e retorna ele (não recebe self)
#new recebe "cls"
# __init__ é o metodo responsavel por inicializar
# a instancia. Por isso, recebe -> self
class A:
    def __new__(cls):
        return super.__new__(cls)
    
    def __init__(self) -> None:
        print('Sou o init')
        
    def __repr__(self) -> str:
        return 'A()'