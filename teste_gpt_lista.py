# Função para adicionar um item à lista de compras
def adicionar_item(lista, item):
    lista.append(item)
    print(f"{item} foi adicionado à lista de compras.")

# Função para remover um item da lista de compras
def remover_item(lista, indice):
    try:
        item_removido = lista.pop(indice)
        print(f"{item_removido} foi removido da lista de compras.")
    except IndexError:
        print("O índice fornecido não existe na lista.")

# Função para exibir todos os itens da lista de compras
def listar_itens(lista):
    print("Lista de Compras:")
    for i, item in enumerate(lista):
        print(f"{i+1}. {item}")

# Função principal
def main():
    lista_compras = []

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar item à lista")
        print("2. Remover item da lista")
        print("3. Listar itens da lista")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            item = input("Digite o item que deseja adicionar à lista: ")
            adicionar_item(lista_compras, item)
        elif opcao == "2":
            if len(lista_compras) == 0:
                print("A lista de compras está vazia.")
            else:
                indice = int(input("Digite o índice do item que deseja remover: ")) - 1
                remover_item(lista_compras, indice)
        elif opcao == "3":
            if len(lista_compras) == 0:
                print("A lista de compras está vazia.")
            else:
                listar_itens(lista_compras)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()