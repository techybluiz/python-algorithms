#Operadores de comparação (relacionais)
#maior............ 2 > 1
#maior ou igual... 2 >= 2
#menor............ 1 < 2
#menor ou igual....1 <= 2
#diferente.........'a' !='b'
#igual.............'a'== 'a'

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
condicao = primeiro_valor >= segundo_valor

if condicao:
    print('O Primeiro valor é maior que o segundo')

else:
    print ('O segundo valor é maior que o primeiro')
