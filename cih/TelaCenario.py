__author__ = 'Ricardo'

import pygame
from cdp import *
from cdp import *
class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.backgroundJogo = Imagem.Imagem.load_image('fundoteste.png', 0)
        self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (800, 500))
        self.galinha = Jogador.Jogador("playersprites.png", 408, 5)
        self.backLocal = 0
        return

    def mostraFase(self, game):
        self.som = Som.Som()
        self.som.tocar(game.music, "beepbeep.wav")
        x = 0
        y = 0
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    x = self.galinha.getVelocity()
                    print("direita", self.galinha.pos.right)
                    self.moveCenario()

                if evento.key == pygame.K_LEFT:
                    y = self.galinha.getVelocity()
                    self.galinha.moveEsquerda()
                    print("esquerda", self.galinha.pos.left)

            if evento.type == pygame.QUIT:
                game.status = 2

        game.screen.blit(self.backgroundJogo, (self.backLocal, 0))

        self.galinha.mover(x, y)
        self.galinha.update()
        self.galinha.render(game.screen)
        pygame.display.update()
        pygame.display.flip()
        return

    def moveCenario(self):
        if (self.galinha.pos.right <= 1500):
            self.backLocal -= self.galinha.speed * 2
        return
