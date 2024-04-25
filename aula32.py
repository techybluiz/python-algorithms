entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    entrada_par = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if entrada_par:
        par_impar_texto = 'par'

    print(f'O numero {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
