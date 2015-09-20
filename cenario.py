import pygame
'''
Created on 07/09/2015

@author: Ricardo
'''

class Cenario(object):

    def __init__(self, img_Location, size):
        print(img_Location)
        self.scenario = pygame.image.load(img_Location)
        self.scenarioRect = self.scenario.get_rect()
        self.rect = pygame.Rect((0,0),size)
        self.image = self.scenario.subsurface(self.rect)
        self.collideWall1 = pygame.Rect((2335,43),(14,244))
        self.collideWall2 = pygame.Rect((4168,43),(14,244))
        self.collideWall3 = pygame.Rect((7015,43),(14,244))

