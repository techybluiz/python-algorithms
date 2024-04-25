def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_planet(method_):
    def internal(self, *args,**kwargs):
        result = method_(self, *args, **kwargs)
        
        if 'Earth' in result:
            return 'Você esta em casa'
        return result
    return internal

# @add_repr
# class Team:
#     def __init__(self, name):
#         self.name = name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def falar_nome(self):
        return f'O Planeta é {self.name}'

# corinthians = Team('corinthians')
# atalanta = Team('Atalanta')

Earth = Planet('Earth')
mars = Planet('Mars')

# print(corinthians)
# print(atalanta)
print(Earth)
print(mars)
print(Earth.falar_nome())
print(mars.falar_nome())