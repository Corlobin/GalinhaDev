__author__ = 'Ricardo'

import os, pygame
main_dir = os.path.split(os.path.abspath(__file__))[0]

class Som(object):
    Singleton = None
    def __init__(self):
        return

    def tocar(self, sound, musica):

        try:
            diretorio = main_dir.replace("cdp", "")
            path = os.path.join(diretorio, 'dados/sons/', musica)
            if Som.Singleton is None:
                Som.Singleton = sound.Sound(path)
                Som.Singleton.play()

        except pygame.error:
            print(path)
            raise SystemExit('Nao foi possivel carregar o som %s %s ' % (path, pygame.get_error()))

    def espera_tocar(self, canal):
        while canal.get_busy():
            pass

    def parar(self):
        if (Som.Singleton != None):
            Som.Singleton.stop()
            Som.Singleton = None
