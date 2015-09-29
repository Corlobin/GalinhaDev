__author__ = 'Ricardo'

import pygame

from ifes.cdp import *


class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.backgroundJogo = Imagem.Imagem.load_image('fundo_editado.png', 0)
        self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (8000, 500))

        # Prefacio
        self.backgroundPrefacio = Imagem.Imagem.load_image('tela_tutorial.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 18)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.textoIniciar = self.fonte.render("Continuar", 1, (0, 0, 0))
        self.pontos = self.fonte.render("Pontos: ", 1, (0, 0, 0))

        self.tank = Jogador.Jogador("oldplayer.gif", 390, 3, 60, 60, 1)

        self.moeda1 = Moeda.Moeda("coin_gold.png", 400, 400, 32, 20, 8)
        self.moeda2 = Moeda.Moeda("coin_copper.png", 600, 400, 32, 20, 8)
        self.moeda3 = Moeda.Moeda("coin_silver.png", 800, 400, 32, 20, 8)
        self.moeda1.setPontos(3)
        self.moeda2.setPontos(2)
        self.moeda3.setPontos(1)

        self.backLocal = 0

        self.blocklist = pygame.sprite.Group()
        self.blocklist.add(self.moeda1)
        self.blocklist.add(self.moeda2)
        self.blocklist.add(self.moeda3)

        return
    def mostrarPrefacio(self, game):
        self.som = Som.Som()
        self.som.tocar(game.music, "texto_prefacio.wav")
        if game.botoes[4]:  # KEY ENTER
            game.status = 5

        game.screen.blit(self.backgroundPrefacio, (0, 0))
        game.screen.blit(self.textoIniciar, (410, 370))
        game.screen.blit(self.seta, (385, 370))

        pygame.display.update()
        game.fps = 30

    def mostraFase(self, game):
        self.som = Som.Som()
        self.som.tocar(game.music, "fase1.wav")
        x = 0
        y = 0

        if game.botoes[3]:
            self.moveCenarioDireita()
        if game.botoes[2]:
            self.moveCenarioEsquerda()

        self.checkCollision(self.tank)

        game.screen.blit(self.backgroundJogo, (self.backLocal, 0))
        game.screen.blit(self.pontos, (500, 0))

        self.tank.render(game.screen)
        self.desenhaMoedas(game.screen)
        pygame.display.update()
        pygame.display.flip()
        game.fps = 30


    def moveCenarioDireita(self):
        if (self.backLocal <= 9999):
            self.backLocal -= self.tank.speed*2
            for moeda in self.blocklist:
                moeda.moveEsquerda(self.tank.speed*2)
        return
    def moveCenarioEsquerda(self):
        if (self.backLocal < 0):
            self.backLocal += self.tank.speed*2
            for moeda in self.blocklist:
                moeda.moveDireita(self.tank.speed*2)
        return

    def desenhaMoedas(self, game):
        for moedas in self.blocklist:
            moedas.update()
            moedas.render(game)

    def checkCollision(self, sprite1):
        for moedas in self.blocklist:
            if sprite1.getRect().colliderect(moedas.getRect()):
                print("Colidiram")
                self.blocklist.remove(moedas)
                self.tank.atualizaPontuacao(moedas.getPontos())
                self.atualizaPontuacao()

    def atualizaPontuacao(self):
        pontuacao = format("Pontos: %d" %(self.tank.getPontuacao()))
        self.pontos = self.fonte.render(pontuacao, 1, (255, 255, 225))

