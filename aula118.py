def add_cliente(nome, lista=[]):
    lista.append(nome)
    return lista

lista1 = []
cliente1 = add_cliente('luiz', lista1)
add_cliente('Joana', cliente1)
print(cliente1)


cliente2 = add_cliente('Helena')
add_cliente('Maria', cliente1)
print(cliente2)
