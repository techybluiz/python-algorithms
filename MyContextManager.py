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
