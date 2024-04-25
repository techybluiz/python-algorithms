'''
Closure e funções 
que retornam outras funções
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} , {nome}'
    return saudar
bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao('Bom noite')

# print(bom_dia('Bianca'))
# print(boa_noite('Nathan'))

for nome in ['Adriana', 'Bianca', 'Marcelo']:
    print(bom_dia(nome))
    print(boa_noite(nome))