__author__ = 'Ricardo'

import pygame

from ifes.cih import TelaCenario
from ifes.cih import TelaMenu


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
        self.screen = pygame.display.set_mode((640, 480))

        self.menu = TelaMenu.TelaMenu()
        self.cenario = TelaCenario.TelaCenario()

                       #CIMA  #BAIX  #ESQ   #DIRE  #ENTER #ESC
        self.botoes = [False, False, False, False, False, False]
        while self.status != 2: # Loop principal do jogo
            self.capturarEventos()
            if self.status == 0: #Menu
                self.menu.mostrarMenu(self)
            elif self.status == 1: #Jogo rodando
                self.cenario.mostraFase(self)
        self.clock.tick(30)
        pygame.quit()
        return

    def capturarEventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.botoes[3] = True
                if evento.key == pygame.K_LEFT:
                    self.botoes[2] = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    self.botoes[3] = False
                if evento.key == pygame.K_LEFT:
                    self.botoes[3] = False


#Inicia o jogo
jogo = TelaJogo()
jogo.inicia()

