primeiro_valor = input('Digite o primeiro número: ')
segundo_valor = input('Digite o segundo número: ')

if primeiro_valor > segundo_valor:
        print(f'O primeiro valor {primeiro_valor} é maior ')
elif segundo_valor > primeiro_valor:
    print (f' O segundo valor {segundo_valor} é maior')

elif primeiro_valor == segundo_valor:
      print (f'Os valores {primeiro_valor} e {segundo_valor} são iguais.')
else:
      print ('Valores não correspondem ao sistema')