__author__ = 'Ricardo'


from TelaMenu import TelaMenu
from TelaCenario import TelaCenario
import pygame


class TelaJogo(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.status = 0
        return

    def inicia(self):
        pygame.init()
        pygame.font.init()
        self.music = pygame.mixer
        self.music.init()

        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Papaleguas - Beep beep!")
        pygame.key.set_repeat(1)
        self.screen = pygame.display.set_mode((640, 480))
        self.menu = TelaMenu()
        self.cenario = TelaCenario()
        while self.status != 2: # Loop principal do jogo
            if self.status == 0: #Menu
                self.menu.capturarEventos(self)
            elif self.status == 1: #Jogo rodando
                self.cenario.mostraFase(self)
            self.clock.tick(60)
        pygame.quit()
        return

#Inicia o jogo
jogo = TelaJogo()
jogo.inicia()

