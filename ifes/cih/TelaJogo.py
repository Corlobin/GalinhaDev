__author__ = 'Ricardo'

import pygame

from ifes.cih import TelaCenario
from ifes.cih import TelaMenu
from ifes.cih import TelaCreditos
from ifes.cih import TelaRanking

class TelaJogo(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.status = 3
        self.fps = 30
        return

    def inicia(self):
        pygame.init()
        pygame.font.init()
        self.music = pygame.mixer
        self.music.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Guerra em Marte")
        self.screen = pygame.display.set_mode((640, 480))

        self.menu = TelaMenu.TelaMenu()
        self.cenario = TelaCenario.TelaCenario()
        self.ranking = TelaRanking.TelaRanking()
        self.creditos = TelaCreditos.TelaCreditos()

                       #0CIMA  #1BAIX  #2ESQ   #3DIRE  #4ENTER #5ESC
        self.botoes = [False, False, False, False, False, False]

        while self.status != 4: # Loop principal do jogo
            self.capturarEventos()

            if self.status == 0: #prefacio
                self.cenario.mostrarPrefacio(self)
            elif self.status == 1: #ranking
                self.ranking.mostrarRanking(self)
            elif self.status == 2: #creditos
                self.creditos.mostrarCreditos(self)
            elif self.status == 3: #menu
                self.menu.mostrarMenu(self)
            elif self.status == 5: #jogo rodando
                self.cenario.mostraFase(self)

            self.clock.tick(self.fps)
        pygame.quit()
        return

    def capturarEventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.botoes[3] = True
                if evento.key == pygame.K_LEFT:
                    self.botoes[2] = True
                if evento.key == 13:  # KEY ENTER
                    self.botoes[4] = True
                if evento.key == pygame.K_UP:  # PARA CIMA
                    self.botoes[0] = True
                if evento.key == pygame.K_DOWN:  # PARA BAIXO
                    self.botoes[1] = True
                if evento.key == pygame.K_ESCAPE:  # ESC
                    self.botoes[5] = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    self.botoes[3] = False
                if evento.key == pygame.K_LEFT:
                    self.botoes[2] = False
                if evento.key == 13:
                    self.botoes[4] = False
                if evento.key == pygame.K_UP:  # PARA CIMA
                    self.botoes[0] = False
                if evento.key == pygame.K_DOWN:  # PARA BAIXO
                    self.botoes[1] = False
                if evento.key == pygame.K_ESCAPE:  # ESC
                    self.botoes[5] = False
            if evento.type == pygame.QUIT:
                self.status = 4