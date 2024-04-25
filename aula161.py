# implementando o protocolo do iterator em python
class MinhaLista():
    def __init__(self) -> None:
        self._data = {}
        self._index= 0
        
    def append(self, valor):
        self._data[self._index] = valor
        self._index += 1
    
if __name__ == '__main__':
    lista = MinhaLista()
    lista.append('Bianca')
    lista.append('Luiz')
    print(lista._data)