# Terá 2 usuário o A e o B, ambos tem senhas diferentes.
# Ele pergunta primeria qual usuário, e depois qual a senha
# Obiviamente se eu digitar usuário A, com a senha do usuário B, vai dar inválido.
# Tenho que digitar o usuário e digitar a senha correta desse usuário

usuario = input("Informe seu usuario: ")
senhaA= int(123)
senhaB = int(456)
senha_digitada = int(input("Digite sua senha: "))

if  usuario.lower () =='a':
    if senhaA == senha_digitada:
     print("Você entrou no sistema!")
    else:
        print("Senha incorreta")
        print('Acesso negado')
elif usuario.lower () =='b':
    if senhaB == senha_digitada:
     print("Você entrou no sistema!")
    else:
       print("Senha incorreta")
       print('Acesso negado')
else:
    print("Usuario não cadastrado")