# Relações entre classes: associação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá seu ciclo de 
# vida idependente . Geralmete é uma relação de um para 
# muitos , onde um objeto tem um ou muitos objetos.
# se trata de uma relação onde objetos precisa de
# outro para fazer determinada tarefa.
# (existem controversas sobre as definições de agregação)

class PurchaseCart:
    def __init__(self):
     self.products = []
     
    def total(self):
        return sum ([p.price for p in self.products])

    def insert_products(self, *product):
        print()
        for product in product:
            self.products.append(product)

    def list_products(self):
        print()
        for product in self.products:
            print(product.name, product.price)
        print()
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        return

cart = PurchaseCart()
p1, p2 = Product('Telephone', 50.0), Product('Controle', 15.0)
cart.insert_products(p1,p2)
cart.list_products()
print(f'Total purchases: R$ {cart.total()}')