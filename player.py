
import pygame

class Player(pygame.sprite.Sprite):
    image = None
    def __init__(self, image, height, speed):
        pygame.sprite.Sprite.__init__(self)

        if Player.image is None:
            # This is the first time this class has been
            # instantiated. So, load the image for this and
            # all subsequence instances.
            Player.image = image

        self.speed = speed
        self.image = Player.image
        self.pos = image.get_rect().move(0, height)
        self.vertical = 0


    def moveDireita(self):
        self.pos = self.pos.move(self.speed, self.vertical)
        if self.pos.right > 600:
            self.pos.right = 0

    def moveEsquerda(self):
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