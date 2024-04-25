#Atributos de classe

class Person:
    current_year = 2024
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_year_birthday(self):
        return Person.current_year - self.age

p1 = Person('Isabella', 22)
p2 = Person('Marcelo', 49)
p3 = Person('Adriana', 44)

print(p1.get_year_birthday())
print(p2.get_year_birthday())
print(p3.get_year_birthday())