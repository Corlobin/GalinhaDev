
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
        if self.pos.right <= 642:
            self.pos = self.pos.move(self.speed, self.vertical)
            #self.pos.right = 32
            

    def moveEsquerda(self):
        if self.pos.left >= 0:
            self.pos.left = self.pos.left - self.speed
            #self.pos.right = 662



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
