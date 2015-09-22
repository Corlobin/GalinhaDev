__author__ = 'Ricardo'

import pygame

from Imagem import Imagem
from Som import Som

class TelaMenu(object):
    def __init__(self):

        self.posicaoCirculo = 320

        self.backgroundMenu = Imagem.load_image('panel.png', 0)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)

        self.fonte = pygame.font.SysFont("comicsansms", 30)
        self.textoIniciar = self.fonte.render("Iniciar", 1, (255, 255, 225))
        self.textoSair = self.fonte.render("Sair", 1, (255, 255, 225))

        return

    def capturarEventos(self, game):

        som = Som()
        som.tocar(game.music, "tela_menu.wav")

        for evento in pygame.event.get():
            pygame.key.set_repeat(1)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:  # PARA CIMA
                    if self.posicaoCirculo == 360:
                        self.posicaoCirculo = 320

                if evento.key == pygame.K_DOWN:  # PARA BAIXO
                    if self.posicaoCirculo == 320:
                        self.posicaoCirculo = 360

                if evento.key == 13:  # KEY ENTER
                    som.parar()
                    print("Enter")
                    if self.getOpcao() == 1:  # Iniciar
                        game.status = 1
                    else:  # sair
                        game.status = 2

            if evento.type == pygame.QUIT:
                game.status = 2

        game.screen.blit(self.backgroundMenu, (0, 0))

        game.screen.blit(self.textoIniciar, (300, 300))
        game.screen.blit(self.textoSair, (300, 340))
        pygame.draw.circle(game.screen, (255, 255, 255), (285, self.posicaoCirculo), 5, 0)
        pygame.display.update()
        return

    def getOpcao(self):
        if self.posicaoCirculo == 320:
            return 1
        return 0
