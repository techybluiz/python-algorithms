a , b = 1,2
a, b = b , a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 20, 
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
#print(pessoa_completa)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1 , b2)

def mostra_argumentos_nomeados(*arg, **kwargs):
    print(kwargs)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostra_argumentos_nomeados(nome='aline', qlq=123) 
    
mostra_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}
mostra_argumentos_nomeados(**configuracoes)