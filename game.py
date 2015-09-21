import os, pygame
from player import Player
from cenario import Cenario

main_dir = os.path.split(os.path.abspath(__file__))[0]

class Game(object):

    def __init__(self):
        self.executando = False;
        self.clock = pygame.time.Clock()
        self.startTime = None
        self.lastTime = 0
        self.status = 0
        self.backLocal = 0
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

        self.backgroundMenu = self.load_image('panel.png',0)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)
        self.backgroundMenu = pygame.transform.scale2x(self.backgroundMenu)

        self.backgroundJogo = self.load_image('fase1.png',0)
        #self.backgroundJogo = pygame.transform.scale(self.backgroundJogo, (800, 500))
        self.galinha = Player(self.player, 408, 5)

        self.galinhaAndandoMenu1 = Player(self.player, 120, 1)
        self.galinhaAndandoMenu2 = Player(self.player, 180, 1)
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
        self.galinhaAndandoMenu1.moveDireita()
        self.galinhaAndandoMenu2.moveDireita()


        screen.blit(self.galinhaAndandoMenu1.image, self.galinhaAndandoMenu1.pos)
        screen.blit(self.galinhaAndandoMenu2.image, self.galinhaAndandoMenu2.pos)
        screen.blit(self.textoIniciar, (300,300))
        screen.blit(self.textoSair, (300, 340))
        pygame.draw.circle(screen, (255,255,255), (285, self.posicaoCirculo), 5, 0)
        pygame.display.update()
        return

    def mostraJogo(self, screen):
        #pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.galinha.moveDireita()
                    print("direita",self.galinha.pos.right)
                    self.moveCenario1()
                if evento.key == pygame.K_LEFT:
                    self.galinha.moveEsquerda()
                    print("esquerda",self.galinha.pos.left)
                    #self.moveCenario2()

            if evento.type == pygame.QUIT:
                self.status = 2

        screen.blit(self.backgroundJogo, (self.backLocal,0))
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

    def moveCenario1(self):
        if(self.galinha.pos.right <= 1500):
            self.backLocal -= self.galinha.speed*2
        return
    def moveCenario2(self):
        if((self.galinha.pos.right - self.galinha.pos.right) >= 32):
            self.backLocal += 5
        return
            
        

               

