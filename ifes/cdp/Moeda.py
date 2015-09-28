__author__ = 'Ricardo'


__author__ = 'Ricardo'
import pygame

from ifes.cdp.Imagem import Imagem


class Moeda(pygame.sprite.Sprite):
    def __init__(self, img, width, height, w, h, qtd):
        pygame.sprite.Sprite.__init__(self)
        self.width=w
        self.height=h
        self.numImages = qtd
        self.cImage = 0
        self.image = Imagem.load_image(img, 1)
        self.rect = self.image.get_rect()
        self.pos = self.image.get_rect().move(width, height)
        self.vertical = 0

    def update(self):
        if(self.cImage >= self.numImages-1):
            self.cImage = 0
        else:
            self.cImage += 1

    def render(self, window):
        window.blit(self.image, self.pos, (self.cImage*self.width, 0, self.width, self.height))

    def moveEsquerda(self, velocidade):
        self.pos.left -= velocidade

