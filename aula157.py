# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde 
# temos um determinado numero de coisas para escolher
# seus valores são constantes
# grupo -> enum 
import enum

class Directions(enum.Enum):
    LEFT = (enum.auto())
    RIGHT = (enum.auto())

print(Directions(1))
print(Directions(2))

Directions = enum.Enum('Directions', ['LEFT', 'RIGHT'])

def move(direction):
    if not isinstance (direction, Directions):
        raise ValueError('Directions not found')
    print (f'Moving to {direction.name}')

move(Directions.LEFT)
move(Directions.RIGHT)
# mover('acima')
# mover('abaixo')
