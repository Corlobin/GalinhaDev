__author__ = 'Ricardo'
import pygame
from TelaMenu import TelaMenu
from TelaCenario import TelaCenario
class Jogo(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.status = 0
        return

    def inicia(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Bem vindo")
        self.screen = pygame.display.set_mode((640, 480))
        self.menu = TelaMenu()
        self.cenario = TelaCenario()
        while self.status != 2: # Loop principal do jogo
            if self.status == 0: #Menu
                self.menu.capturarEventos(self)
            elif self.status == 1: #Jogo rodando
                self.cenario.mostraFase1(self)
            self.clock.tick(60)
        pygame.quit()
        return



