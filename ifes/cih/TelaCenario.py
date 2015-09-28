__author__ = 'Ricardo'

import pygame

from ifes.cdp import *


class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.backgroundJogo = Imagem.Imagem.load_image('fundo_editado.png', 0)
        self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (8000, 500))

        self.tank = Jogador.Jogador("oldplayer.gif", 400, 1, 50, 32, 1)
        self.moeda = Moeda.Moeda("coin_gold.png", 400, 400, 32, 20, 8)

        self.backLocal = 0


        self.blocklist = pygame.sprite.Group()
        self.blocklist.add(self.moeda)
        return

    def mostraFase(self, game):
        #self.som = Som.Som()
        #self.som.tocar(game.music, "beepbeep.wav")
        x = 0
        y = 0

        if game.botoes[3]:
            print(x)
            self.tank.moveDireita()
            self.moveCenario()
            print(self.tank.pos.right)
        if game.botoes[2]:
            self.tank.moveEsquerda()

        self.moeda.update()
        game.screen.blit(self.backgroundJogo, (self.backLocal, 0))
        self.tank.render(game.screen)
        self.moeda.render(game.screen)
        pygame.display.update()
        pygame.display.flip()
        return

    def moveCenario(self):
        if (self.tank.pos.right <= 99999):
            self.backLocal -= self.tank.speed*2
            self.moeda.moveEsquerda(self.tank.speed*2)
        return
    def checkCollision(self, sprite1, sprite2):
        print(sprite1)
        print(sprite2)
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        print(col)
