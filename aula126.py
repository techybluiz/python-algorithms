#__dict__ e vars para atributos de instancia
import json

class Person:
    current_year = 2024
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_year_birthday(self):
        return Person.current_year - self.age

p1 = Person('Bruna', 22)
p1.__dict__['nome'] = 'Teste'

print(p1.get_year_birthday())
print(p1.__dict__)
print(vars(p1)) #vars chama o __dict__

