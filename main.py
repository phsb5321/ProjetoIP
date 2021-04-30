import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
clock = pygame.time.Clock()


class tela_branca1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/tela branca.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 45
        self.rect[1] = SCREEN_HEIGTH - 595


class tela_branca2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/tela branca.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 82
        self.rect[1] = SCREEN_HEIGTH - 595


class nave_fim(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/parabens.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 9
        self.rect[1] = SCREEN_HEIGTH /7


class tela_fim(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/fim.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 0


#class tela_perdeu(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('./assets/').convert_alpha()
        #self.rect = self.image.get_rect()
        #self.rect[0] = 0
        #self.rect[1] = 0


class vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/vida.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 8
        self.rect[1] = SCREEN_HEIGTH - 595


class vida1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/vida.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 45
        self.rect[1] = SCREEN_HEIGTH - 595


class vida2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/vida.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 82
        self.rect[1] = SCREEN_HEIGTH - 595


class caderno(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/caderno.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = SCREEN_HEIGTH - 600


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('./assets/NaveCima1.png').convert_alpha(),
                       pygame.image.load('./assets/NaveCima2.png').convert_alpha(),
                       pygame.image.load('./assets/NaveCima3.png').convert_alpha(),
                       pygame.image.load('./assets/NaveCima4.png').convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load('./assets/NaveCima1.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGTH / 2
        self.speed_x = 0
        self.speed_y = 0
        self.vida = 3
        self.score = 0

    def update(self):
        self.current_image = (self.current_image + 1) % 2
        self.image = self.images[self.current_image]

        self.speed_x = 0
        self.speed_y = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -3
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 3
        if keystate[pygame.K_UP]:
            self.speed_y = -3
        if keystate[pygame.K_DOWN]:
            self.speed_y = 3

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.vida == 3:
            vida_group.draw(screen)
            vida1_group.draw(screen)
            vida2_group.draw(screen)
        if self.vida == 2:
            vida_group.draw(screen)
            vida1_group.draw(screen)
            tela_branca2_group.draw(screen)
        if self.vida == 1:
            vida_group.draw(screen)
            tela_branca1_group.draw(screen)
        if self.vida == 0:
            pygame.quit()
        if self.score == 5:
            tela_fim_group.draw(screen)
            nave_fim_group.draw(screen)

        if pygame.sprite.groupcollide(nave_group, aster_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela1_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela2_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela3_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y

        palavra = ()
        if pygame.sprite.groupcollide(nave_group, letra_m_group, False, True):
            self.score += 1
            palavra += 'M',
            print(palavra)
        if pygame.sprite.groupcollide(nave_group, letra_a_group, False, True):
            self.score += 1
            palavra += 'A',
            print(palavra)

        if pygame.sprite.groupcollide(nave_group, letra_r_group, False, True):
            self.score += 1
            palavra += 'R',
            print(palavra)

        if pygame.sprite.groupcollide(nave_group, letra_t_group, False, True):
            self.score += 1
            palavra += 'T',
            print(palavra)

        if pygame.sprite.groupcollide(nave_group, letra_e_group, False, True):
            self.score += 1
            palavra += 'E',
            print(palavra)


            print(palavra)

        if pygame.sprite.groupcollide(nave_group, letra_g_group, False, True):
            self.vida -= 1

        if pygame.sprite.groupcollide(nave_group, letra_i_group, False, True):
            self.vida -= 1

        if pygame.sprite.groupcollide(nave_group, letra_n_group, False, True):
            self.vida -= 1


        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGTH:
            self.rect.bottom = SCREEN_HEIGTH
        if self.rect.top < 0:
            self.rect.top = 0


class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Asteroides.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 110
        self.rect[1] = SCREEN_HEIGTH - 300


class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = SCREEN_HEIGTH - 250


class Estrela1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 650
        self.rect[1] = SCREEN_HEIGTH - 550


class Estrela2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 500
        self.rect[1] = SCREEN_HEIGTH - 400


class Estrela3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 750
        self.rect[1] = SCREEN_HEIGTH - 150


class LetraM(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/M.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = SCREEN_HEIGTH - 200


class LetraA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/A.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 740
        self.rect[1] = SCREEN_HEIGTH - 580


class LetraR(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/R.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 130
        self.rect[1] = SCREEN_HEIGTH - 380


class LetraT(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/T.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 690
        self.rect[1] = SCREEN_HEIGTH - 80


class LetraE(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/E.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 590
        self.rect[1] = SCREEN_HEIGTH - 200


class LetraG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/G.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 510
        self.rect[1] = SCREEN_HEIGTH - 490


class LetraI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/I.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 295
        self.rect[1] = SCREEN_HEIGTH - 185


class LetraN(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/N.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 690
        self.rect[1] = SCREEN_HEIGTH - 380


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

BACKGROUND = pygame.image.load('./assets/background.png')

pygame.display.set_caption("Freirinho")
icon = pygame.image.load('./assets/icone.png')
pygame.display.set_icon(icon)

nave_group = pygame.sprite.Group()
nave = Nave()
nave_group.add(nave)

aster_group = pygame.sprite.Group()
aster = Asteroide()
aster_group.add(aster)

estrela_group = pygame.sprite.Group()
estrela = Estrela()
estrela_group.add(estrela)

estrela1_group = pygame.sprite.Group()
estrela1 = Estrela1()
estrela1_group.add(estrela1)

estrela2_group = pygame.sprite.Group()
estrela2 = Estrela2()
estrela2_group.add(estrela2)

estrela3_group = pygame.sprite.Group()
estrela3 = Estrela3()
estrela3_group.add(estrela3)

letra_m_group = pygame.sprite.Group()
letra_m = LetraM()
letra_m_group.add(letra_m)

letra_a_group = pygame.sprite.Group()
letra_a = LetraA()
letra_a_group.add(letra_a)

letra_r_group = pygame.sprite.Group()
letra_r = LetraR()
letra_r_group.add(letra_r)

letra_t_group = pygame.sprite.Group()
letra_t = LetraT()
letra_t_group.add(letra_t)

letra_e_group = pygame.sprite.Group()
letra_e = LetraE()
letra_e_group.add(letra_e)

letra_g_group = pygame.sprite.Group()
letra_g = LetraG()
letra_g_group.add(letra_g)

letra_i_group = pygame.sprite.Group()
letra_i = LetraI()
letra_i_group.add(letra_i)

letra_n_group = pygame.sprite.Group()
letra_n = LetraN()
letra_n_group.add(letra_n)

vida_group = pygame.sprite.Group()
vida = vida()
vida_group.add(vida)

vida1_group = pygame.sprite.Group()
vida1 = vida1()
vida1_group.add(vida1)

vida2_group = pygame.sprite.Group()
vida2 = vida2()
vida2_group.add(vida2)

caderno_group = pygame.sprite.Group()
caderno = caderno()
caderno_group.add(caderno)

tela_fim_group = pygame.sprite.Group()
tela_fim = tela_fim()
tela_fim_group.add(tela_fim)

nave_fim_group = pygame.sprite.Group()
nave_fim = nave_fim()
nave_fim_group.add(nave_fim)

tela_branca1_group = pygame.sprite.Group()
tela_branca1 = tela_branca1()
tela_branca1_group.add(tela_branca1)

tela_branca2_group = pygame.sprite.Group()
tela_branca2 = tela_branca2()
tela_branca2_group.add(tela_branca2)


def draw():
    nave_group.draw(screen)
    aster_group.draw(screen)
    estrela_group.draw(screen)
    estrela1_group.draw(screen)
    estrela2_group.draw(screen)
    estrela3_group.draw(screen)
    letra_m_group.draw(screen)
    letra_a_group.draw(screen)
    letra_r_group.draw(screen)
    letra_t_group.draw(screen)
    letra_e_group.draw(screen)
    letra_g_group.draw(screen)
    letra_i_group.draw(screen)
    letra_n_group.draw(screen)
    caderno_group.draw(screen)


def update():
    nave_group.update()
    aster_group.update()
    estrela_group.update()
    estrela1_group.update()
    estrela2_group.update()
    estrela3_group.update()
    letra_m_group.update()
    letra_a_group.update()
    letra_r_group.update()
    letra_t_group.update()
    letra_e_group.update()
    letra_g_group.update()
    letra_i_group.update()
    letra_n_group.update()
    caderno_group.update()
    vida_group.update()
    vida1_group.update()
    vida2_group.update()
    nave_fim_group.update()
    tela_fim_group.update()
    tela_branca1_group.update()
    tela_branca2_group.update()


while True:
    screen.blit(BACKGROUND, (0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw()
    update()
    pygame.display.update()






