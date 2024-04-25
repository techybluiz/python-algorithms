# abstractmethod para qualquer método já decorado
# É possivel criar @property @property.setter
# @classmethod @staticmethod e método normais como
# abstrato, para isso use @abstractmethod como decorador mais interno
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name) -> None:
        self.name = name
    
    @property
    def name(self): pass
    
    @name.setter
    def name (self, name): pass
    
class Foo(AbstractFoo):
    def __init__(self, name) -> None:
        super().__init__(name)
        print('Teste super')

foo = Foo('Bar')
print(foo.name)