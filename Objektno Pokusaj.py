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
    pozadina_sl = pygame.image.load(os.path.join('Assets',
                                                 'nebo.png'))  #1000 500
    pod_sl = pygame.image.load(os.path.join('Assets', 'pod.png'))  #1000 32
    settings_sl = pygame.image.load(os.path.join('Assets',
                                                 'setings.png'))  #32 32
    biraj_sl = pygame.image.load(os.path.join('Assets', 'biraj.png'))
    nebo_sl = pygame.image.load(os.path.join('Assets', 'nebo_pozadina.png'))
    ovo_sl = pygame.image.load(os.path.join('Assets', 'ovo.png'))  # 32x15
    ili_sl = pygame.image.load(os.path.join('Assets', 'ili.png'))  # 32
    mejn_sl = pygame.image.load(os.path.join('Assets',
                                             'bektumejn.png'))  # 66 10
    gotovo_sl = pygame.image.load(os.path.join('Assets', 'gotovo.png'))  # 128
    stub_sl = []  # 'stub_g.png' , 'stub_d.png'
    podesinepodeseno_sl = pygame.image.load(
        os.path.join('Assets', 'podesinepodeseno.png'))  #116 10
    natrag_sl = pygame.image.load(os.path.join('Assets', 'natrag.png'))  #41 10
    slajder_sl = pygame.image.load(os.path.join('Assets',
                                                'slajder.png'))  #40 10
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

    def razmisljaj():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.VIDEORESIZE:
                promeniVelE(event.size)

    def promeniVelE(velET):  #tapl a inace ne
        xE = velET[0]
        yE = velET[1]

        self.EKRAN = pygame.display.set_mode((xE, yE), pygame.RESIZABLE)
        self.velE = [xE, yE]

        #slike
        ptx = (0.003 * xE) * 16  #3/1000
        pty = (0.003 * xE) * 12
        ptica_sl = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('Assets', 'flepi.png')),
                (ptx, pty)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('Assets', 'flepi.png')),
                (ptx, pty))
        ]

        pozadina_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'nebo.png')), (xE, yE))

        pty = (0.001 * xE) * 32  #1/1000
        pod_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'pod.png')), (xE, pty))

        settings_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'setings.png')),
            (pty, pty))

        pty = (0.0078 * xE) * 32  #7.8/1000
        biraj_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'biraj.png')), (pty, pty))

        pty = (0.002 * xE) * 32  #2/1000
        nebo_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'nebo_pozadina.png')),
            (2 * xE, pty))

        pty = (0.008 * xE)  #8/1000
        ovo_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'ovo.png')),
            (pty * 32, pty * 15))

        pty = (0.004 * xE)  #4/1000
        ili_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'ili.png')),
            (pty * 32, pty * 32))

        mejn_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'bektumejn.png')),
            (pty * 66, pty * 10))

        gotovo_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'gotovo.png')),
            (pty * 128, pty * 128))

        pty = (0.002 * xE)  #2/1000
        stub_sl = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('Assets', 'stub_g.png')),
                (pty * 32, pty * 250)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('Assets', 'stub_d.png')),
                (pty * 32, pty * 250))
        ]

        pty = (0.005 * xE)  #5/1000
        podesinepodeseno_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'podesinepodeseno.png')),
            (pty * 116, pty * 10))

        pty = (0.003 * xE)  #3/1000
        natrag_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'natrag.png')),
            (pty * 41, pty * 10))

        pty = (0.005 * xE)  #5/1000
        slajder_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'slajder.png')),
            (pty * 40, pty * 10))

        brzina_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'brzina.png')),
            (pty * 40, pty * 10))

        ubrzanje_sl = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'ubrzanje.png')),
            (pty * 56, pty * 10))

        lopta_sl = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('Assets', 'slajderd.png')),
                (pty * 10, pty * 10)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('Assets', 'slajderd dp.png')),
                (pty * 10, pty * 10))
        ]

        for i in range(10):
            broj_sl.append(
                pygame.transform.scale(
                    pygame.image.load(os.path.join('Assets',
                                                   str(i) + '.png')),
                    (pty * 4, pty * 10)))

        #hitboks
        pty = (0.003 * xE)
        ptica_rect = pygame.Rect(xE / 4, yE / 2, pty * 16, pty * 12)

        pty = (0.001 * xE) * 32
        pod_rect = [
            pygame.Rect(0, yE - pty, xE, pty),
            pygame.Rect(xE, yE - pty, xE, pty)
        ]

        settings_rect = pygame.Rect(xE / 100, xE / 100, pty, pty)

        pty = (0.008 * xE)################################################
        ovo_rect = [ pygame.Rect(0.15*xE, 0.11*yE, pty * 32, pty * 15) , pygame.Rect(0.6*xE, 0.11*yE, pty * 32, pty * 15) ]


         mejn_rect = pygame.Rect(0.368*xE, 0.195*yE, 32, 32)

        
         pty = (0.002 * xE)
         stub_rect = [pygame.Rect(xE, -0.2*yE, pty*32, pty*250),pygame.Rect(xE, 0.115*yE, pty*32, pty*250)]


         pty = (0.003 * xE)
         natrag_rect = pygame.Rect(0.44*xE, 0.22*yE, pty*41, pty*10)

        lopta_rect = [pygame.Rect(0.44*xE, 0.125*yE, pty*41, pty*10),pygame.Rect(0.44*xE, 0.44*yE, pty*41, pty*10)]
        

    def crtaj():
        pass

    def razmisljaj():
        pass

    def pocetak():
        pass

    def podesavanja():
        pass

    def izgubio():
        pass

    def __innit__(xE, yE):
        promeniVelE((xE, yE))

        br = 5
        acc = 0.5
        skor = 0

        pocetak()


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
