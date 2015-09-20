import pygame
from pygame import *
from time import clock


class Cenario():

	def __init__(self, img_Location, size):
		
		self.scenario = pygame.image.load(img_Location)
		self.scenarioRect = self.scenario.get_rect()

		self.rect = pygame.Rect((0,0),size)
		self.image = self.scenario.subsurface(self.rect)

		self.collideWall1 = pygame.Rect((2335,43),(14,244))
		self.collideWall2 = pygame.Rect((4168,43),(14,244))
		self.collideWall3 = pygame.Rect((7015,43),(14,244))

	def update(self, option, personagem, movRate):

		self.tempScenario = pygame.Surface.copy(self.scenario)

		if self.rect.right != self.scenarioRect.right and option == 1:

			if not personagem.firstTimeMid:
				self.leftFree = False
				self.rightFree = False

				if (not personagem.rightCollided or personagem.firstTimeCollided) and not personagem.firstTimeNotCollided:
					self.rect = self.rect.move((movRate,0))
					personagem.firstTimeCollided = False

				if personagem.firstTimeNotCollided:
					personagem.firstTimeNotCollided = False

				if self.rect.right == self.scenarioRect.right:
					self.rightFree = True
			else:
				self.leftFree = True
				self.rightFree = False

			self.image = self.tempScenario.subsurface(self.rect)

		elif self.rect.left != self.scenarioRect.left and option == 2:

			if not personagem.firstTimeMid:
				self.leftFree = False
				self.rightFree = False

				if (not personagem.leftCollided or personagem.firstTimeCollided) and not personagem.firstTimeNotCollided:
					self.rect = self.rect.move((-movRate,0))
					personagem.firstTimeCollided = False

				if personagem.firstTimeNotCollided:
					personagem.firstTimeNotCollided = False
									
				if self.rect.left == self.scenarioRect.left:
					self.leftFree = True
			else:
				self.leftFree = False
				self.rightFree = True

			self.image = self.tempScenario.subsurface(self.rect)

		elif option == 3:

			self.image = self.tempScenario.subsurface(self.rect)




