# @property + @setter - getter e setter no modo python
# como getter
#     - p/ enviar quebra codigo cliente 
#     - p / habilitar setter
#     - p/ executar ações ao obter um atraibruto
#Atributos que começam com um ou dois
#() __) underlines não devem ser usados fora da classe

class Caneta:
    def __init__(self, cor):
         self._cor = cor
        #  self._cor = self.cor_tinta #não deve ser usado
         
    @property #obter o valor
    def cor (self):
        print('Property')
        return self._cor
    
    @cor.setter #configurar o valor
    def cor(self, valor):
      self._cor = valor
        
caneta = Caneta('Azul')
caneta.cor = 'Rosa'
#getter -> obter valor
print(caneta.cor)


