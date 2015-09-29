__author__ = 'Ricardo'

import pygame

from ifes.cdp import *

class TelaCreditos(object):
    def __init__(self):

        self.backgroundMenu = Imagem.Imagem.load_image('creditos.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.textoIniciar = self.fonte.render("Voltar", 1, (0, 0, 0))

    def mostrarCreditos(self, game):
        if game.botoes[4]:  # KEY ENTER
            game.status = 3

        game.screen.blit(self.backgroundMenu, (0, 0))
        game.screen.blit(self.textoIniciar, (300, 400))
        game.screen.blit(self.seta, (275, 405))
        pygame.display.update()
        return

