#map - para mapear dados

from functools import partial

produtcs = [
    {'produtcs 1' : 'milk','price': 10.00},
    {'produtcs 2' : 'sugar','price': 5.00},
    {'produtcs 3' : 'butter','price': 13.00},
    {'produtcs 4' : 'rice','price': 20.00},
    {'produtcs 5' : 'beans','price': 9.00},
]

def increase_price(vallue, percentage):
    return round(vallue * percentage, 2)

increase_ten_percentage = 'teste'

new_produtcs = [
    {**p, 'preco': increase_price(p['price'], 1.1)}
]