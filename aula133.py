# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso esta protegido'
    
    def _metodo_publico(self):
        self.__metodo_private()
        return 'metodo_publico'

    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
f = Foo()   
print(f.public)
print(f._protected)
# print(f.__metodo_private) #erro de atributo-> esta fora da classe
print(f._Foo__metodo_private())