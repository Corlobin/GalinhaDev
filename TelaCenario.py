__author__ = 'Ricardo'

import pygame

from player import Player
from Imagem import Imagem


class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.backgroundJogo = Imagem.load_image('fundoteste.png', 0)
        self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (800, 500))
        self.galinha = Player("galinhaAndando.gif", 408, 5)
        self.backLocal = 0
        return

    def mostraFase1(self, game):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.galinha.moveDireita()
                    print("direita", self.galinha.pos.right)
                    self.moveCenario1()
                if evento.key == pygame.K_LEFT:
                    self.galinha.moveEsquerda()
                    print("esquerda", self.galinha.pos.left)

            if evento.type == pygame.QUIT:
                game.status = 2

        game.screen.blit(self.backgroundJogo, (self.backLocal, 0))
        game.screen.blit(self.galinha.image, self.galinha.pos)
        pygame.display.update()
        return

    def moveCenario1(self):
        if (self.galinha.pos.right <= 1500):
            self.backLocal -= self.galinha.speed * 2
        return

    def moveCenario2(self):
        if ((self.galinha.pos.right - self.galinha.pos.right) >= 32):
            self.backLocal += 5
        return
