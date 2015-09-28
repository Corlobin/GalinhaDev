__author__ = 'Ricardo'
import pygame

from ifes.cdp.Imagem import Imagem


class Jogador(pygame.sprite.Sprite):
    def __init__(self, img, height, speed, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.width=w
        self.height=h
        self.numImages = 16
        self.cImage = 0


        self.speed = speed
        self.image = Imagem.load_image(img, 1)
        self.pos = self.image.get_rect().move(0, height)
        self.vertical = 0

    def update(self):
        if(self.cImage >= self.numImages-1):
            self.cImage = 0
        else:
            self.cImage += 1

    def render(self, window):
        window.blit(self.image, self.pos, (self.cImage*self.width+15, 0, self.width, self.height))

    def mover(self,x,y):
        if(x > 0):
            self.moveDireita()
        elif(y > 0):
            self.moveEsquerda()


    def moveDireita(self):
        if self.pos.right <= 642:
            self.pos = self.pos.move(self.speed, self.vertical)
        self.update()

    def moveEsquerda(self):
        if self.pos.left >= 0:
            self.pos.left = self.pos.left - self.speed
        self.update()

    ''' Getters '''
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNick(self):
        return self.nick
    def getRecord(self):
        return self.record
    def getVelocity(self):
        return self.speed
    ''' Setters '''
    def setNick(self, nick):
        self.nick = nick
    def setRecord(self, record):
        self.record = record
