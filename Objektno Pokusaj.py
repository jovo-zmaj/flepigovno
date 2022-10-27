from random import randint, random
from pygame import mixer
import pygame, os

pygame.init()
mixer.init()

mixer.music.load(os.path.join('Assets', 'jan.mp3'))

pygame.display.set_caption("flepi_objektni")


class Ptica:
    #Ekran
    EKRAN = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
    velE = []

    #Slike
    ptica_sl = []  # 'flepi.png' 16x12
    pozadina_sl = pygame.image.load(os.path.join('Assets','nebo.png'))  #1000 500
    pod_sl = pygame.image.load(os.path.join('Assets', 'pod.png'))  #1000 32
    settings_sl = pygame.image.load(os.path.join('Assets','setings.png'))  #32 32
    biraj_sl = pygame.image.load(os.path.join('Assets', 'biraj.png'))
    nebo_sl = pygame.image.load(os.path.join('Assets', 'nebo_pozadina.png'))
    ovo_sl = pygame.image.load(os.path.join('Assets', 'ovo.png'))  # 32x15
    ili_sl = pygame.image.load(os.path.join('Assets', 'ili.png'))  # 32
    mejn_sl = pygame.image.load(os.path.join('Assets','bektumejn.png'))  # 66 10
    gotovo_sl = pygame.image.load(os.path.join('Assets', 'gotovo.png'))  # 128
    stub_sl = []  # 'stub_g.png' , 'stub_d.png'
    podesinepodeseno_sl = pygame.image.load(os.path.join('Assets', 'podesinepodeseno.png'))  #116 10
    natrag_sl = pygame.image.load(os.path.join('Assets', 'natrag.png'))  #41 10
    slajder_sl = pygame.image.load(os.path.join('Assets','slajder.png'))  #40 10
    brzina_sl = pygame.image.load(os.path.join('Assets', 'brzina.png'))
    ubrzanje_sl = pygame.image.load(os.path.join('Assets', 'ubrzanje.png'))
    lopta_sl = []  #'slajderd.png' , 'slajder dp.png' 10x10
    broj_sl = []  # 'n.png' 4x10

    #hitboksovi
    ptica_rect = pygame.Rect(10, 10, 32, 32)
    pod_rect = []
    settings_rect = pygame.Rect(10, 10, 32, 32)
    ovo_rect = []
    mejn_rect = pygame.Rect(10, 10, 32, 32)
    stub_rect = []
    natrag_rect = pygame.Rect(10, 10, 32, 32)
    lopta_rect = []

    #Logika
    br = 5
    acc = 0.5
    skor = 0

    ptica12 = 0

    stubg = []
    stubd = []

    def razmisljaj(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.VIDEORESIZE:
                self.promeniVelE(event.size)

    def promeniVelE(self,velET):  #tapl a inace ne
        xE = velET[0]
        yE = velET[1]

        self.EKRAN = pygame.display.set_mode((xE, yE), pygame.RESIZABLE)
        self.velE = [xE, yE]

        #slike
        ptx = (0.003 * xE) * 16  #3/1000
        pty = (0.003 * xE) * 12
        self.ptica_sl = [ pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'flepi.png')),(ptx, pty)), pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'flepi.png')),(ptx, pty)) ]

        self.pozadina_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'nebo.png')), (xE, yE))

        pty = (0.001 * xE) * 32  #1/1000
        self.pod_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pod.png')), (xE, pty))

        self.settings_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'setings.png')),(pty, pty))

        pty = (0.0078 * xE) * 32  #7.8/1000
        self.biraj_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'biraj.png')), (pty, pty))

        pty = (0.002 * xE) * 32  #2/1000
        self.nebo_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'nebo_pozadina.png')),(2 * xE, pty))

        pty = (0.008 * xE)  #8/1000
        self.ovo_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ovo.png')),(pty * 32, pty * 15))

        pty = (0.004 * xE)  #4/1000
        self.ili_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ili.png')),(pty * 32, pty * 32))

        self.mejn_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bektumejn.png')),(pty * 66, pty * 10))

        self.gotovo_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'gotovo.png')),(pty * 128, pty * 128))

        pty = (0.002 * xE)  #2/1000
        self.stub_sl = [ pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'stub_g.png')),(pty * 32, pty * 250)),pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'stub_d.png')),(pty * 32, pty * 250))]

        pty = (0.005 * xE)  #5/1000
        self.podesinepodeseno_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'podesinepodeseno.png')),(pty * 116, pty * 10))

        pty = (0.003 * xE)  #3/1000
        self.natrag_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'natrag.png')),(pty * 41, pty * 10))

        pty = (0.005 * xE)  #5/1000
        self.slajder_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'slajder.png')),(pty * 40, pty * 10))

        self.brzina_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'brzina.png')),(pty * 40, pty * 10))

        self.ubrzanje_sl = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ubrzanje.png')),(pty * 56, pty * 10))

        self.lopta_sl = [ pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'slajderd.png')),(pty * 10, pty * 10)),pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'slajderd dp.png')),(pty * 10, pty * 10))]

        for i in range(10):
            self.broj_sl.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets',str(i) + '.png')),(pty * 4, pty * 10)))

        #hitboks
        pty = (0.003 * xE)
        self.ptica_rect = pygame.Rect(xE / 4, yE / 4, pty * 16, pty * 12)

        pty = (0.001 * xE) * 32
        self.pod_rect = [pygame.Rect(0, yE - pty, xE, pty),pygame.Rect(xE, yE - pty, xE, pty)]

        self.settings_rect = pygame.Rect(xE / 100, xE / 200, pty, pty)

        pty = (0.008 * xE)################################################
        self.ovo_rect = [ pygame.Rect(0.15*xE, 0.44*yE, pty * 32, pty * 15) , pygame.Rect(0.6*xE, 0.44*yE, pty * 32, pty * 15) ]


        self.mejn_rect = pygame.Rect(0.368*xE, 0.78*yE, 32, 32)

        
        pty = (0.002 * xE)
        self.stub_rect = [pygame.Rect(xE, -0.8*yE, pty*32, pty*250),pygame.Rect(xE, 0.46*yE, pty*32, pty*250)]


        pty = (0.003 * xE)
        self.natrag_rect = pygame.Rect(0.44*xE, 0.88*yE, pty*41, pty*10)

        self.lopta_rect = [pygame.Rect(0.44*xE, 0.125*yE, pty*41, pty*10),pygame.Rect(0.44*xE, 0.44*yE, pty*41, pty*10)]
        

    def crtaj(self):
        pass

    def razmisljaj(self):
        pass

    def pocetak(self):
        pass

    def podesavanja(self):
        pass

    def izgubio(self):
        pass

    def __innit__(self,xE, yE):
        self.promeniVelE((xE, yE))

        self.br = 5
        self.acc = 0.5
        self.skor = 0

        self.pocetak()


def main():
    FPS = 30
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        pass


mixer.music.play()
main()
mixer.music.stop()
pygame.quit()
exit()
