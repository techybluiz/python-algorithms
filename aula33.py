#faça um programa que pergunte a hora ao usuario
#baseando-se no horario descrito exiba a
#saudação apropriada.

horas = input('Digite ás horas: ')

try:
    hora = float(horas)

    if hora > 11:
        print("Boa tarde!")
    elif hora <= 11:
        print('Bom dia!')
except:
    print('Boa noite!')
 