
def verificar_horas(horario):
    partes = horario.split(':')
    if len(partes) !=2:
        return False
    try:
        horas = int(partes[0])
        minutos = int (partes[1])
        if horas<0 or horas >23 or minutos < 0 or minutos > 59:
            return False
    except ValueError:
        return False
    return True   
while True:
    horario = input("Digite ás horas: ")
    if verificar_horas(horario):
        horas = int(horario.split(':')[0])
        print( f'Ás horas são {horario}')
        if horas <= 12:
                print (" Bom dia! ")
        elif horas <= 18:
                print('Boa tarde! ')
        elif horas >18 and horario <=12:
            print ('Boa noite!')  
        else:
                print ('Horario invalido')
        break
    else:
         print('Hoario invaliddo.')