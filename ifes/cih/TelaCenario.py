__author__ = 'Ricardo'

import pygame

from ifes.cdp import *


class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.backgroundJogo = Imagem.Imagem.load_image('fundoteste.png', 0)
        self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (800, 500))

        self.galinha = Jogador.Jogador("andando.png", 402, 0.5, 28, 32)
        self.backLocal = 0

        return

    def mostraFase(self, game, evento):
        self.som = Som.Som()
        self.som.tocar(game.music, "beepbeep.wav")
        x = 0
        y = 0
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                print("Movimentou")
                self.galinha.moveDireita()
                self.moveCenario()
            if evento.key == pygame.K_LEFT:
                print("esquerda", self.galinha.pos.left)

        if evento.type == pygame.QUIT:
            game.status = 2

        game.screen.blit(self.backgroundJogo, (self.backLocal, 0))
        self.galinha.render(game.screen)
        pygame.display.update()
        pygame.display.flip()
        return

    def moveCenario(self):
        if (self.galinha.pos.right <= 1500):
            self.backLocal -= self.galinha.speed
        return
