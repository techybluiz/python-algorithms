
entrada = input('Digite [E] para entrar ou [S] para sair: ')
senha_correta = int (12345)

if entrada.lower() == 'e':
    senha_digitada = int(input('Digite sua senha: '))
    if senha_digitada == senha_correta:
        print("Bem-vindo ao sistema!")
    else:
     print('Senha incoreta')
elif entrada.lower() == 's':
   print('Você saiu do sistema')
else:
   print('Opção inválida')