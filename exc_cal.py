while True:
   num1 = input('Digite o primeiro numero: ')
   num2 =input('Digite o segundo numero: ')
   operador = input('Informe o operador: ')
   operadores = '+-*/'

   if operador not in operadores:
      print('Digite um operador valido!')
      continue
   
   elif len(operador)> 1:
    print('Digite apenas um operador!') 
    
    if operador == '+':
        print('Resultado:' , num1 + num2)
    elif operador == '-':
        print()
    elif operador == '/':
       print()


    sair = input('Deseja sair: ').lower().startswith('s')
    if sair is True:
      print('Você saiu do sistema.')
      break
    