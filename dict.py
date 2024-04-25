perguntas = [
    {
        'Pergunta': 'Qual é a função que exibe uma mensagem em python? ',
        'Opções': ['print', 'len', 'list', 'def'],
        'Resposta': 'print',
    },

     {
        'Pergunta': 'Qual função usada para importar uma biblioteca? ',
        'Opções': ['array', 'import', 'import()', 'include'],
        'Resposta': 'import',
     },
     {
        'Pergunta': 'Qual é a função que cria uma estrutura de repetição',
        'Opções': ['for', 'while', 'except', 'return'],
        'Resposta': 'print',
     },

     {
        'Pergunta': 'O que a função pop faz? ',
        'Opções': ['exibe uma lista', 'deleta uma lista', 'importa uma lista', 'deleta o ultimo item da lista'],
        'Resposta': 'deleta o ultimo item da lista',
     },
]

acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    option = pergunta['Opções']
    for i, opcao in enumerate(option):
        print(f'{i}', opcao)
    print()

escolha = input('Escolha uma opção: ')
print(escolha)

acertou = False
escolha_int = None
qtd_opcoes = len(option)

if escolha.isdigit():
    escolha_int = int(escolha)

if escolha_int is not None:
    if escolha_int>= 0 and escolha_int < qtd_opcoes:
        if option[escolha_int]==pergunta['Resposta']:
            acertou = True

print()

if acertou:
    acertos += 1
    print('Acertou 👍')
else:
    print('Errou ❌')
print()

print('Você acetou', acertos)
print('de', len(perguntas), 'perguntas')