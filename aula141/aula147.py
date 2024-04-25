# Dunder Methods __repr__ and __str__ 

class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name} (x={self.x}, y={self.y},)'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return  resultado_self > resultado_other
    
    
if __name__ == '__main__':
    p1 = Ponto(5,2)
    p2 = Ponto(3, 8)
    p3 = p1 + p2 #self + other
    print(p3)
    print('P1 é maior que p2?',p1 > p2)
    print('P2 é maior que p1?',p2 > p1)