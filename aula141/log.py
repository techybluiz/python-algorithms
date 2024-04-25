#Abstração
#Herança -> é um...
from pathlib import Path

LOF_FILE = Path(__file__).parent / 'log.txt'

class Log: #classe mãe
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    
    
class LogFileMixin(Log): #herança
    def _log(self, msg):
        msg_new = f'{msg} ({self.__class__.__name__})'
        print('Salcando no log:', msg_new)
        with open(LOF_FILE, 'a') as arquivo:
            arquivo.write(msg_new)
            arquivo.write('\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})') 
           
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Teste log')
    lp.log_sucess('Sucesso!')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_sucess('Sucesso')
    print(LOF_FILE)