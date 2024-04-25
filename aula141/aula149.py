# Context Manager com classes
# Voce pode implementar seus proprios protocolos
# apneas implementando os dunder methods que o 
# Python vai usar. Isso é chamado de Duck typing > Quando 
# vejo um Passaro que caminha como pato, nada como um pato 
# e grasna como um pato, eu chamo aquele passaro de pato.
# Para criar um context manager, os metodos __enter__ e __exit__
# # devem ser implementados.
# O metodo __exit__ receberá a classe de exceção, a exceção e o 
# traceback. Se ele retornar True, exceção no with será suprimida


class MyContextManager:
    def __init__(self, caminho_arquivo, modulo):
        self.caminho_arquivo = caminho_arquivo
        self.modulo = modulo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo =  open (self.caminho_arquivo, self.modulo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando o arquivo')
        self._arquivo.close()
        
with MyContextManager('aula149.txt', 'w') as arqiuvo:
    print('With',arqiuvo)