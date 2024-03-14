#Função para exemplificar (args)

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multilicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
duplica = executa(cria_multilicador(2), 10)

print(duplica)
