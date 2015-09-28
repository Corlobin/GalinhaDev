__author__ = 'Ricardo'


from cih import TelaCenario, TelaMenu
import pygame


class TelaJogo(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.status = 0
        return

    def inicia(self):
        pygame.init()
        pygame.font.init()
        self.music = pygame.mixer
        self.music.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Papaleguas - Beep beep!")
        pygame.key.set_repeat(1)
        self.screen = pygame.display.set_mode((640, 480))

        self.menu = TelaMenu.TelaMenu()
        self.cenario = TelaCenario.TelaCenario()

        while self.status != 2: # Loop principal do jogo
            for evento in pygame.event.get():
                if self.status == 0: #Menu
                    self.menu.mostrarMenu(self, evento)
                elif self.status == 1: #Jogo rodando
                    self.cenario.mostraFase(self, evento)


        self.clock.tick(30)
        pygame.quit()
        return


#Inicia o jogo
jogo = TelaJogo()
jogo.inicia()

