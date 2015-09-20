import os, pygame
from player import Player

main_dir = os.path.split(os.path.abspath(__file__))[0]

class Game(object):

    def __init__(self):
        self.executando = False;
        self.clock = pygame.time.Clock()
        self.startTime = None
        self.lastTime = 0
        self.status = 0
        return

    def inicia(self, altura, largura):
        self.altura = altura
        self.largura = largura

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Bem vindo")
        screen = pygame.display.set_mode((640, 480))

        #Coisas do MENU
        self.posicaoCirculo = 320
        self.player = self.load_image('galinhaAndando.gif',1)

        self.backgroundMenu = self.load_image('menu3.png',0)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)

        self.backgroundJogo = self.load_image('fundoteste.png',0)
        self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (800, 500))
        self.galinha = Player(self.player, 408, 5)

        self.galinhaAndandoMenu = Player(self.player, 40, 1)
        self.fonte = pygame.font.SysFont("comicsansms",30)
        self.textoIniciar = self.fonte.render("Iniciar",1, (255,255,225))
        self.textoSair = self.fonte.render("Sair",1, (255,255,225))


        while self.status != 2:
            if self.status == 0: #Menu
                self.mostraMenu(screen)
            elif self.status == 1: #Jogo rodando
                self.mostraJogo(screen)
            self.clock.tick(60)


        pygame.quit()
        return


    def mostraMenu(self, screen):
        for evento in pygame.event.get():
            #print(evento)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP: #PARA CIMA
                    if self.posicaoCirculo == 360:
                        self.posicaoCirculo = 320

                if evento.key == pygame.K_DOWN: #PARA BAIXO
                    if self.posicaoCirculo == 320:
                        self.posicaoCirculo = 360

                if evento.key == 13: #KEY ENTER
                    print("Enter")
                    if self.getOpcao() == 1: #Iniciar
                        self.status = 1
                        print("iniciar")
                    else: #sair
                        self.status = 2

            if evento.type == pygame.QUIT:
                self.status = 2


        screen.blit(self.backgroundMenu, (0,0))
        self.galinhaAndandoMenu.moveDireita()
        screen.blit(self.galinhaAndandoMenu.image, self.galinhaAndandoMenu.pos)
        screen.blit(self.textoIniciar, (300,300))
        screen.blit(self.textoSair, (300, 340))
        pygame.draw.circle(screen, (0,0,0), (285, self.posicaoCirculo), 5, 0)
        pygame.display.update()
        return

    def mostraJogo(self, screen):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.galinha.moveDireita()
                    print("galinha andando :p")
                    print(self.galinha.pos)
                if evento.key == pygame.K_LEFT:
                    self.galinha.moveEsquerda()
                    print("galinha andando :p")
                    print(self.galinha.pos)

            if evento.type == pygame.QUIT:
                self.status = 2

        screen.blit(self.backgroundJogo, (0,0))
        screen.blit(self.galinha.image, self.galinha.pos)

        pygame.display.update()
        return





    def load_image(self, name, transparent):
        path = os.path.join(main_dir, 'dados/imagens/', name)
        try:
            surface = pygame.image.load(path)
        except pygame.error:
            raise SystemExit('Nao foi possivel carregar a imagem %s %s ' %(path, pygame.get_error()))
        if transparent:
            corner = surface.get_at((0, 0))
            surface.set_colorkey(corner, pygame.RLEACCEL)
        return surface.convert()

    def getOpcao(self):
        if self.posicaoCirculo == 320:
            return 1
        return 0

               

