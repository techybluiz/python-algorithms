#Introdução ao try/except
#numero_str = input('Insira um numero para ser dobrado: ')
#try:
#    print('STR:' , numero_str)
#    numero_float = float(numero_str)
#    print('Floar:' , numero_float)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
#except:
#    print('Isso não é um número')

velocidade = 61
local_carro = 90

radar_1 = 60
local = 100
radar_range = 1
if velocidade > radar_1:
    print('Seu carro ultrapassou o radar 1 ')
if local_carro >= (local - radar_range) and \
    local_carro <= (local + radar_range):
    print('Carro multado em radar 1')




