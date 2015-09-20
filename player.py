'''
Created on 06/09/2015

@author: Ricardo
'''

class Player(object):
    
    
    '''
        Modelo do player
    '''


    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
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