from random import randint, random
from pygame import mixer
import pygame, os

pygame.init()
mixer.init()

mixer.music.load(os.path.join('Assets', 'jan.mp3'))

pygame.display.set_caption("flepi")

FPS = 30
EKRAN = pygame.display.set_mode((1000, 500))
BELA = (230, 230, 230)
CRNA = (0, 0, 0)
CRNA2 = (20, 20, 30)
CRVENA = (250, 5, 5)
ACC = 0.5
V_PT = 36
POZADINA = pygame.image.load(os.path.join('Assets', 'nebo.png'))
POD = pygame.image.load(os.path.join('Assets', 'pod.png'))
POD2 = POD
BRZINA = 5

SETTINGS = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'setings.png')), (32, 32))
BIRAJ = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'biraj.png')), (250, 250))

NEBO = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'nebo_pozadina.png')), (2000, 64))
NEBO2 = NEBO

OVO = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ovo.png')), (256, 120))
OVO2 = OVO

ILI = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ili.png')), (128, 128))

MEJN = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'bektumejn.png')), (264, 40))

GOTOVO = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'gotovo.png')), (500, 500))

STUBG = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'stub_g.png')), (64, 500))
STUBD = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'stub_d.png')), (64, 500))

PODESINEPODESENO = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'podesinepodeseno.png')),
    (580, 50))

NATRAG = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'natrag.png')), (123, 30))

SLAJDER = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'slajder.png')), (200, 50))

BRZ = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'brzina.png')), (200, 50))

UBRZANJE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ubrzanje.png')), (280, 50))

LOPTA = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'slajderd.png')), (50, 50))
LOPTA2 = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'slajder dp.png')), (50, 50))
JEDAN = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '1.png')), (20, 50))
DVA = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '2.png')), (20, 50))
TRI = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '3.png')), (20, 50))
CETIRI = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '4.png')), (20, 50))
PET = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '5.png')), (20, 50))
SEST = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '6.png')), (20, 50))
SEDAM = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '7.png')), (20, 50))
OSAM = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '8.png')), (20, 50))
DEVET = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '9.png')), (20, 50))
NULA = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', '0.png')), (20, 50))
SKOR = [NULA, JEDAN, DVA, TRI, CETIRI, PET, SEST, SEDAM, OSAM, DEVET]

sett = pygame.Rect(10, 10, 32, 32)

skor = 0


def pocetak_crtaj():
    EKRAN.blit(POZADINA, (0, 0))
    EKRAN.blit(NEBO, (0, 404))

    EKRAN.blit(STUBG, (100, -400))
    EKRAN.blit(STUBD, (100, 200))
    EKRAN.blit(STUBG, (900, -350))
    EKRAN.blit(STUBD, (900, 250))
    EKRAN.blit(STUBG, (500, -250))
    EKRAN.blit(STUBD, (500, 350))

    EKRAN.blit(POD, (0, 468))

    EKRAN.blit(SETTINGS, (10, 10))

    EKRAN.blit(BIRAJ, (375, 0))

    EKRAN.blit(OVO, (150, 220))
    EKRAN.blit(OVO2, (594, 220))
    EKRAN.blit(ILI, (436, 220))
    pygame.display.update()


def pocetak():
    pocetak_crtaj()
    dugme1 = pygame.Rect(150, 220, 256, 120)
    dugme2 = pygame.Rect(594, 220, 256, 120)
    dugmebool1 = False
    dugmebool2 = False

    vozi = True
    while vozi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if dugme1.collidepoint(pos):
                    ptica = pygame.transform.scale(
                        pygame.image.load(os.path.join('Assets', 'flepi.png')),
                        (V_PT + 12, V_PT))
                    main(ptica)
                    exit()
                if dugme2.collidepoint(pos):
                    ptica = pygame.transform.scale(
                        pygame.image.load(os.path.join('Assets',
                                                       'flepi_2.png')),
                        (V_PT + 12, V_PT))
                    main(ptica)
                    exit()
                if sett.collidepoint(pos):
                    podesavanja()
                    pocetak_crtaj()


def crtaj_podesavanja():
    EKRAN.blit(POZADINA, (0, 0))
    EKRAN.blit(NEBO, (0, 404))

    EKRAN.blit(STUBG, (500 - 32, -400))
    EKRAN.blit(STUBD, (500 - 32, 200))
    EKRAN.blit(STUBG, (100 - 32, -350))
    EKRAN.blit(STUBD, (100 - 32, 250))
    EKRAN.blit(STUBG, (900 - 32, -250))
    EKRAN.blit(STUBD, (900 - 32, 350))

    EKRAN.blit(POD, (0, 468))

    EKRAN.blit(PODESINEPODESENO, (210, 20))
    EKRAN.blit(MEJN, (368, 390))
    EKRAN.blit(NATRAG, (439, 440))
    EKRAN.blit(SLAJDER, (100, 225))
    EKRAN.blit(SLAJDER, (700, 225))
    EKRAN.blit(BRZ, (100, 225 - 55))
    EKRAN.blit(UBRZANJE, (660, 225 - 55))
    EKRAN.blit(LOPTA, (90 + BRZINA * 6.7, 225))
    EKRAN.blit(LOPTA2, (690 + ACC * 170, 225))

    pygame.display.update()


def podesavanja():
    crtaj_podesavanja()
    global BRZINA
    global ACC
    lopta = pygame.Rect(115, 225, 170, 50)
    lopta2 = pygame.Rect(715, 225, 170, 50)

    vozi = True
    while vozi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if lopta.collidepoint(pos):
                    BRZINA = (pos[0] - 25 - 90) / 6.7 + 0.01
                    crtaj_podesavanja()
                if lopta2.collidepoint(pos):
                    ACC = (pos[0] - 25 - 690) / 170 + 0.01
                    crtaj_podesavanja()
                if pygame.Rect(439, 440, 123, 30).collidepoint(pos):
                    vozi = False
                if pygame.Rect(368, 390, 264, 40).collidepoint(pos):
                    pocetak()
                    exit()


def crtaj(joj, VEL, pod1, pod2, nebo1, nebo2, ptica, stubg, stubd):
    global skor

    #nebo
    EKRAN.blit(POZADINA, (0, 0))
    #pod2
    nebo1.x -= BRZINA // 2
    nebo2.x -= BRZINA // 2
    EKRAN.blit(NEBO, (nebo1.x, nebo1.y))  #pod1vu promx
    EKRAN.blit(NEBO2, (nebo2.x, nebo2.y))

    #stubovi
    for stub in stubg:
        if stub.x - 32 < 250 and stub.x - 32 > 250 - BRZINA:
            skor += 1
        if stub.x < -64 + BRZINA:
            stubg.remove(stub)
        else:
            stub.x -= BRZINA
            EKRAN.blit(STUBG, (stub.x, stub.y))

    for stub in stubd:
        if stub.x < -64 + BRZINA:
            stubd.remove(stub)
        else:
            stub.x -= BRZINA
            EKRAN.blit(STUBD, (stub.x, stub.y))

    #pod
    pod1.x -= BRZINA
    pod2.x -= BRZINA
    EKRAN.blit(POD, (pod1.x, pod1.y))  #pod1vu promx
    EKRAN.blit(POD2, (pod2.x, pod2.y))
    #ptica
    ptica = pygame.transform.rotate(ptica, -VEL * 6)
    EKRAN.blit(ptica, (joj.x, joj.y))

    EKRAN.blit(SETTINGS, (10, 10))

    n = skor

    EKRAN.blit(SKOR[n % 10], (490, 20))
    n = n // 10
    EKRAN.blit(SKOR[n % 10], (460, 20))

    pygame.display.update()


def izgubio_crtaj(ptica, x, y, stubg, stubd):
    EKRAN.blit(POZADINA, (0, 0))
    EKRAN.blit(NEBO, (0, 404))

    for stub in stubg:
        EKRAN.blit(STUBG, (stub.x, stub.y))

    for stub in stubd:
        EKRAN.blit(STUBD, (stub.x, stub.y))

    EKRAN.blit(POD, (0, 468))
    EKRAN.blit(SETTINGS, (10, 10))
    EKRAN.blit(ptica, (x, y))
    EKRAN.blit(GOTOVO, (250, 0))
    pygame.display.update()


def izgubio(ptica, x, y, stubg, stubd):
    EKRAN.blit(GOTOVO, (250, 0))
    pygame.display.update()

    vozi = True
    while vozi:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if sett.collidepoint(pos):
                    podesavanja()
                    izgubio_crtaj(ptica, x, y, stubg, stubd)
                else:
                    main(ptica)
                    exit()


def main(ptica):
    global skor
    skor = 0

    clock = pygame.time.Clock()

    joj = pygame.Rect(250, 250, V_PT + 12, V_PT)
    pod1 = pygame.Rect(0, 468, 1000, 32)
    pod2 = pygame.Rect(1000, 468, 1000, 32)
    nebo1 = pygame.Rect(0, 404, 2000, 64)
    nebo2 = pygame.Rect(2000, 404, 2000, 64)

    stubg = []
    stubd = []

    VEL = 0
    i = 0

    stubg.append(pygame.Rect(1000, -400, 64, 500))
    stubd.append(pygame.Rect(1000, 230, 64, 500))

    vozi = True
    while vozi:
        clock.tick(FPS)

        i += 1
        if i == 250 // BRZINA:
            r = randint(-450, -200)
            stubg.append(pygame.Rect(1000, r, 64, 500))
            stubd.append(pygame.Rect(1000, r + 630, 64, 500))
            i = 0

        for stub in stubg:
            if joj.colliderect(stub):
                vozi = False
        for stub in stubd:
            if joj.colliderect(stub):
                vozi = False

        if pod1.x < -1000 + BRZINA:
            pod1.x = 0
            pod2.x = 1000
        if nebo1.x < -2000 + BRZINA // 2:
            nebo1.x = 0
            nebo2.x = 2000
        if joj.y < 468 - VEL - V_PT and joj.y > 0:
            joj.y += VEL
            VEL += ACC
        else:
            vozi = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if sett.collidepoint(pos):
                    podesavanja()
                else:
                    VEL = -7

        crtaj(joj, VEL, pod1, pod2, nebo1, nebo2, ptica, stubg, stubd)

    x = joj.x
    y = joj.y
    izgubio(ptica, x, y, stubg, stubd)
    exit()


mixer.music.play()
pocetak()
mixer.music.stop()
pygame.quit()
#nap prog koji odredjuje
#koliko u intervalu
#postoji brojeva
#deljiva k