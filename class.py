class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já esta filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = False

cam1 = Camera('Cannon')
cam2 = Camera('Sony')
cam1.filmar()
cam1.filmar()
cam1.fotografar()
cam2.filmar()
print(cam1.filmando)
print(cam2.filmando)
