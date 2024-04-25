# filter -> é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
produtos = [
    {'produtcs 1' : 'milk','price': 10.00},
    {'produtcs 2' : 'sugar','price': 5.00},
    {'produtcs 3' : 'butter','price': 13.00},
    {'produtcs 4' : 'rice','price': 20.00},
    {'produtcs 5' : 'beans','price': 9.00},
]

# novos_produtos = [
#     p for p in produtos
#     if p['price'] > 10 #Maneira de filtar usando if 
# ]

novos_produtos = filter(
    lambda produto:produto['price'] > 10, produtos  # função filter para filtrar produtos apenas acima de 10
)

print_iter(produtos)
print()
print_iter(novos_produtos)