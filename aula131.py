# @property - um getter no moddo Pythonico
# getter - um metodo para obter um atributo
# @property é uma propriedade do objeto, ela
# é um meodo que se comporta como um
# atributo
#forma segura e confiável de obter informações 
# importantes de seus objetos em Python!
# Geralmente é usada nas seguintes situações:
#     - como getter
#     - p/ enviar quebra codigo cliente 
#     - p / habilitar setter
#     - p/ executar ações ao obter um atraibruto
#codigo cliente é o codigo que usa seu codigo
#####################################################
# class Caneta:
#     def __init__(self, cor):
#         #private, protected public(proteger o atributo)
#         self.cor_tinta = cor
#     def get_cor(self):
#         return self.cor_tinta
        
# caneta = Caneta('Azul')
# print(caneta.get_cor())

#decorator para alterar atributos
class Caneta:
    def __init__(self, cor):
         self.cor_tinta = cor
         
    @property
    def cor (self):
        print('Cor vermelho')
        return self.cor_tinta
        
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
