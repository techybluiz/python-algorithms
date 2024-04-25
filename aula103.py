# Funções decoradoras e decoradores
# Decorar = adicionar/ remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções

def create_function(function):
    def internal(*args, **kwargs):
        print('I will decorate')
        for arg in args:
            is_string(arg)
        result = function(*args , **kwargs)
        print(f'Its result was {result}')
        print('Now yes, it has been decorated! Following result: ')
        return result
    return(internal)

def inverte_string(string):
    return string [::-1]

def is_string(parameters):
    if not isinstance(parameters, str):
        raise TypeError('Parameters must be a string')

invert_string_parameter = create_function(inverte_string)
inverted = invert_string_parameter('123')

print(inverted)