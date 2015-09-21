import pygame

from Imagem import Imagem


class Player(pygame.sprite.Sprite):
    def __init__(self, img, height, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = Imagem.load_image(img, 1)
        self.pos = self.image.get_rect().move(0, height)
        self.vertical = 0


    def moveDireita(self):
        if self.pos.right <= 642:
            self.pos = self.pos.move(self.speed, self.vertical)

    def moveEsquerda(self):
        if self.pos.left >= 0:
            self.pos.left = self.pos.left - self.speed

    ''' Getters '''
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNick(self):
        return self.nick
    def getRecord(self):
        return self.record
    
    ''' Setters '''
    def setNick(self, nick):
        self.nick = nick
    def setRecord(self, record):
        self.record = record
