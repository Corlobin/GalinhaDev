__author__ = 'Ricardo'

import pygame

from ifes.cdp import *

class TelaMenu(object):
    def __init__(self):
        self.posicaoCirculo = 320

        self.backgroundMenu = Imagem.Imagem.load_image('panel.png', 0)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)

        self.fonte = pygame.font.SysFont("comicsansms", 30)

        self.textoIniciar = self.fonte.render("Iniciar", 1, (255, 255, 225))
        self.textoSair = self.fonte.render("Sair", 1, (255, 255, 225))

    def mostrarMenu(self, game):
        self.som = Som.Som()
        self.som.tocar(game.music, "tela_menu.wav")
        if game.botoes[0]:
            if self.posicaoCirculo == 360:
                self.posicaoCirculo = 320

        if game.botoes[1]:
            if self.posicaoCirculo == 320:
                self.posicaoCirculo = 360

        if game.botoes[4]:  # KEY ENTER
            self.som.parar()
            print("Enter")
            if self.getOpcao() == 1:  # Iniciar
                game.status = 1
            else:  # sair
                game.status = 2
        self.update(game)
        return

    def update(self, game):
        game.screen.blit(self.backgroundMenu, (0, 0))
        game.screen.blit(self.textoIniciar, (300, 300))
        game.screen.blit(self.textoSair, (300, 340))
        pygame.draw.circle(game.screen, (255, 255, 255), (285, self.posicaoCirculo), 5, 0)
        pygame.display.update()


    def getOpcao(self):
        if self.posicaoCirculo == 320:
            return 1
        return 0
