class A:
    ...
    def quem_sou(self):
        print('A')
class B(A):
    ...
    def quem_sou(self):
        print('B')
class C(A):
    ...
    def quem_sou(self):
        print('C')
class D(B,C):
    ...
    def quem_sou(self):
        print('D')
        
d = D()
resultado = d.quem_sou()
print(f'O valor agora é: {resultado}')