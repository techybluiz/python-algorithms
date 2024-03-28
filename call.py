class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, name):
        print(name,'calling', self.phone)
        return ' '
    
call1 = CallMe ('26598536')
name = call1('Bianca Luiz')
print(name)
