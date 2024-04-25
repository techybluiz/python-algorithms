#os.shutil - Mover, copiar e apagar arquivos
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os .rename
# copiar -> os.unlink
# Apagar ->shutil.rmtree

import os
import shutil

home = os.path.expanduser('~')
desktop = os.path.join(home, 'Desktop')
print(desktop)
