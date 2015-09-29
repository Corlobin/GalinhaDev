__author__ = 'Ricardo'

import pygame

from ifes.cdp import *

class TelaMenu(object):
    def __init__(self):
        self.opcao = 1

        self.backgroundMenu = Imagem.Imagem.load_image('menu.png', 0)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        #self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)
        #self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)

        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.textoIniciar = self.fonte.render("Iniciar", 1, (0, 0, 0))
        self.textoRanking = self.fonte.render("Ranking", 1, (0, 0, 0))
        self.textoCreditos = self.fonte.render("Creditos", 1, (0, 0, 0))
        self.textoSair = self.fonte.render("Sair", 1, (0, 0, 0))

    def mostrarMenu(self, game):
        #self.som = Som.Som()
        #self.som.tocar(game.music, "tela_menu.wav")
        if game.botoes[0]: #cima
            if (self.opcao <= 4 and self.opcao > 1):
                self.opcao -= 1

        if game.botoes[1]: #baixo
            if(self.opcao >= 1 and self.opcao < 4):
                self.opcao += 1

        if game.botoes[4]:  # KEY ENTER
            #self.som.parar()
            print("CU ")
            print(self.opcao-1)
            if (self.opcao-1) == 3:
                self.opcao = 5



            game.status = (self.opcao-1)

        self.update(game)
        return

    def retornaPosicao(self):
        if(self.opcao == 5):
            return ((4-1) * 30)+5
        return ((self.opcao-1) * 30)+5

    def update(self, game):
        game.screen.blit(self.backgroundMenu, (0, 0))
        game.screen.blit(self.textoIniciar, (300, 300))
        game.screen.blit(self.textoRanking, (300, 330))
        game.screen.blit(self.textoCreditos, (300, 360))
        game.screen.blit(self.textoSair, (300, 390))
        game.screen.blit(self.seta, (275, 300+self.retornaPosicao()))

        #pygame.draw.circle(game.screen, (0, 0, 0), (285, self.posicaoCirculo), 5, 0)
        pygame.display.update()
        game.fps = 10

