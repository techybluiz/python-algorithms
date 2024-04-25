#Operadores lógicos
entrada = input('Selecione [E] para Entrar Ou [S] para sair: ')
senha_digitada = 'Insira a Senha: '
senha_permitida = '12345'
senha = input('Senha: ') or 'Sem senha cadastrada'


if (entrada == 'E' or entrada== 'e') and senha_digitada == senha_permitida:
    print('Você entrou no sistema')

else:
    print ('Sem senha cadastrada')
