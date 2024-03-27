
class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name} (x={self.x}, y={self.y},)'
p1 = Ponto(1,2)
p2 = Ponto(781, 829)
print(p1)
print(repr(p2))

print(f'{p2!r}')
