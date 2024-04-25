lista_de_duplicados = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
]

def primeiro_duplicado(lista_de_inteiros):
    numero_checado = set()
    primeiro_duplicado = -1
    nova_lista = []

    for numero in lista_de_inteiros:
        if numero in numero_checado:
            primeiro_duplicado = numero
            break

        numero_checado.add(numero)
    return primeiro_duplicado

  for lista in lista_de_inteiros:
        for numero in lista:
            if numero in nova_lista:
                print('Tem duplicado', numero)
            break
            nova_lista.append(numero)
        print('Não tem duplicado')
  