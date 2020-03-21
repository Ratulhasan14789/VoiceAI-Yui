import pygame_sdl2 as pygame
import time
pygame.init()

screen = pygame.display.set_mode((900,600))

gif = [pygame.image.load('bat.gif'), pygame.image.load('bat1.gif'), pygame.image.load('bat2.gif'),
       pygame.image.load('bat3.gif'), pygame.image.load('bat4.gif'), pygame.image.load('bat5.gif'),
       pygame.image.load('bat6.gif'), pygame.image.load('bat7.gif')]

gif2 = [pygame.image.load('t1.gif'), pygame.image.load('t2.gif'),
       pygame.image.load('t3.gif'), pygame.image.load('t4.gif'), pygame.image.load('t5.gif'),
       pygame.image.load('t6.gif'), pygame.image.load('t7.gif'), pygame.image.load('t8.gif')]

fig = [pygame.image.load('g.gif'), pygame.image.load('g2.gif'),
       pygame.image.load('g3.gif'), pygame.image.load('g4.gif'), pygame.image.load('g5.gif')]


hulk = [pygame.image.load('u1.gif'), pygame.image.load('u2.gif'),
        pygame.image.load('u3.gif'), pygame.image.load('u4.gif'),
        pygame.image.load('u5.gif'), pygame.image.load('u6.gif')]

hulk2 = [pygame.image.load('q1.gif'), pygame.image.load('q2.gif'),
        pygame.image.load('q3.gif'), pygame.image.load('q4.gif'),
         pygame.image.load('q5.gif'), pygame.image.load('q6.gif')]

smash = [pygame.image.load('h.gif'), pygame.image.load('h2.gif'),
        pygame.image.load('h3.gif'), pygame.image.load('h4.gif'),
         pygame.image.load('h3.gif'), pygame.image.load('h2.gif')]

pow = [pygame.image.load('pu.gif'), pygame.image.load('pu2.gif'),
        pygame.image.load('po.gif'), pygame.image.load('pu4.gif'),
         pygame.image.load('pu5.gif'),pygame.image.load('pu.gif')]

falling = [pygame.image.load('fall.gif'), pygame.image.load('fall2.gif'),
        pygame.image.load('fall3.gif'), pygame.image.load('fall4.gif'),
         pygame.image.load('fall5.gif'),pygame.image.load('fall6.gif'),
        pygame.image.load('fall7.gif'),pygame.image.load('fall8.gif')]

oo = [pygame.image.load('oof.gif'), pygame.image.load('oof.gif'),
        pygame.image.load('oof2.gif'), pygame.image.load('oof2.gif'),
         pygame.image.load('oof3.gif'), pygame.image.load('oof3.gif'), pygame.image.load('oof4.gif'),
        pygame.image.load('oof4.gif'), pygame.image.load('oof5.gif'),
         pygame.image.load('oof5.gif')]

damage = [pygame.image.load('dam.gif'), pygame.image.load('dam.gif'),
          pygame.image.load('dam.gif'), pygame.image.load('dam.gif'),
          pygame.image.load('dam2.gif'), pygame.image.load('dam2.gif'),
          pygame.image.load('dam2.gif'), pygame.image.load('dam3.gif'),
          pygame.image.load('dam3.gif'), pygame.image.load('dam3.gif'),
          pygame.image.load('dam3.gif'), pygame.image.load('dam3.gif'),
          pygame.image.load('dam4.gif'), pygame.image.load('dam4.gif'),
          pygame.image.load('dam4.gif'), pygame.image.load('dam4.gif'),
          pygame.image.load('dam5.gif'), pygame.image.load('dam5.gif'),
          pygame.image.load('dam5.gif'), pygame.image.load('dam5.gif'),
          pygame.image.load('dam6.gif'), pygame.image.load('dam6.gif'),
          pygame.image.load('dam6.gif'), pygame.image.load('dam6.gif')]

out = pygame.image.load('oof5.gif')
hulkhit = pygame.image.load('ouch.gif')

bg = pygame.image.load('city.jpg')
char = pygame.image.load('b1.gif')
charl = pygame.image.load('t.gif')
hul = pygame.image.load('h.gif')

c = 0
dif = 25
oofcount = 0
ouch = False
padam = False

hy = 430

damcount = 0
batdamage = False

xd = 0

hit = False

widthc = 2

axe = False
axecount = 0
sword = 0
change = 18

rect2 = True

powcount = 0

smashcount = 0
runcount = 0

hulkl = False
hulkr = False
smashdown = False

rect = True

xl = 410
yl = 440

ym = 440

g = False
fgcount = 0

stand = False

axe2 = False
axecount2 = 0

x = 375
y = 450

width = 70
height = 7

width2 = 70
height2 = 7

widthc2 = 1
fall = False
c = 0
fallcount = 0
changer = 1

clock = pygame.time.Clock()

def fightl():
    global axecount
    global fgcount
    global x
    global xl
    global yl
    global damcount
    global width
    global height
    global widthc
    global fallcount
    global fall


    screen.blit(bg, (0, 0))

    if rect2:
        pygame.draw.rect(screen, (255, 0, 0), (x, y - 15, width, height))


    if axecount >= 7:
        axecount = 0

    if fgcount >= 4:
        fgcount = 0

    if damcount >= 24:
        damcount = 0

    if fallcount >= 7:
        fallcount = 0
        fall = False

    if axe:
          screen.blit(gif[axecount], (x, y))
          axecount += 1
          time.sleep(0.035)
          if x == xl - 30:
              x -= 2

    elif axe2:
          screen.blit(gif2[axecount], (x, y))
          axecount += 1
          time.sleep(0.035)
          if x == xl - 30:
              x -= 2


    elif batdamage:
        screen.blit(damage[damcount], (x, y))
        damcount += 1

    elif g:
        screen.blit(fig[fgcount], (x, y))
        fgcount += 1

    elif fall:
        screen.blit(falling[fallcount], (x, y))
        fallcount += 1

    else:
        screen.blit(char, (x, y))
        axecount = 0
        fgcount = 0


def hulksm():
    global smashcount
    global runcount
    global c
    global x
    global xl
    global yl
    global ym
    global powcount
    global width2
    global height2
    global widthc2
    global width2
    global rect
    global oofcount
    global ouch
    global changer

    if rect:
        pygame.draw.rect(screen, (255, 0, 0), (xl, yl - 15, width2, height2))

    if smashcount >= 5:
        smashcount = 0

    if width2 < 2:
        width2 = 0
        rect = False
    if xl >= 850:
        xl = 845


    if runcount >= 5:
        runcount = 0

    if powcount == 5:
        time.sleep(0.5)
        powcount = 0

    if oofcount == 8:
        yl += 40
    if oofcount == 9:
        changer = 0
        oofcount = 9
        yl += 40

    if hulkr:
        screen.blit(hulk2[runcount], (xl, yl))
        runcount += 1

    elif hulkl:
        screen.blit(hulk[runcount], (xl, ym))
        runcount += 1


    elif smashdown:
        screen.blit(smash[smashcount], (xl, yl))
        smashcount += 1
        c += 1

    elif padam:
        screen.blit(pow[powcount], (xl, yl))
        powcount += 1

    elif hit:
        yl = 435
        screen.blit(hulkhit, (xl, yl))
        width2 -= widthc

    elif ouch:
        screen.blit(oo[oofcount], (xl, yl))
        oofcount += changer
        yl += 70
        ym += 70

    else:
        yl = 440
        screen.blit(hul, (xl, 440))

    pygame.display.update()


running = True
while running:

    clock.tick(8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fightaction = pygame.key.get_pressed()


    if fightaction[pygame.K_RIGHT] and x > 0 and x < xl:
        if axecount <= 7:
            axe = True
            y = 453
            if axecount > 0:
              x += change
    elif x <= 0:
        x += 15
    elif x >= (xl - 30):
        x -= 1
        xl += 2
    elif x <= -5 and x >= xl - 30:
        x -= 1

    else:
        axe = False

    fightl()

    if fightaction[pygame.K_LEFT] and x > 0 and x < xl:
        if axecount <= 7:
            axe2 = True
            y = 453
            if axecount > 0:
              x -= change
    elif x <= 0:
        x += 15
    elif x >= xl - 30:
        x -= 15
        xl += 2
    elif x <= -5 and x >= xl - 30:
        x -= 1


    else:
        axe2 = False

    fightl()

    if fightaction[pygame.K_2]:
        if fgcount <= 4:
            g = True
            y = 453
        if x >= xl - 40 and fgcount == 1:
            g = True
            y = 453
            hit = True
        else:
            hit = False

        if width2 < 2:
            width2 = 0
            rect = False
            hulkr = False
            hulkl = False
            hit = False
            ouch = True
            yl += 50

        else:
            ouch = False

    elif x >= xl - 30:
        x -= 1


    else:
        g = False
        hit = False


    if fightaction[pygame.K_9] and xl > 30 and xl > x:
        if runcount <= 5:
            hulkl = True
            xl -= 18
            ym = 430
        if xl <= 30:
            xl += 5

    elif x <= -5 and x >= xl - 30:
        x -= 1

    else:
        hulkl = False
        ym = 440

    if fightaction[pygame.K_0] and xl > 20 and xl > x:
        if runcount <= 5:
            hulkr = True
            xl += 18
            yl = 430

    elif xl <= 20:
        xl += 1
        hulkr = False
        yl = 430

    elif x <= -5 and x >= xl - 30:
        x -= 1

    else:
        hulkr = False
        yl = 440

    if fightaction[pygame.K_8]:
        if smashcount <= 4:
            smashdown = True
            xl -= 10
        if xl <= 15:
            xl += 14

        if c == 5:
            smashdown = False
            c = 0


    else:
        smashdown = False


    if fightaction[pygame.K_7]:
        if powcount <= 5:
            padam = True
            yl = 434
            xl -= 12
        if xl <= 20:
            xl += 14
        if powcount == 1:
            yl -= 5


    else:
        padam = False


    hulksm()




    if fightaction[pygame.K_8] and x >= xl - 40:
        if damcount <= 24:
            batdamage = True
            time.sleep(0.05)
            width -= widthc2
        if width < 2:
            width = 0
            rect2 = False

        if width < 2:
            width = 0
            rect2 = False
            batdamage = False
            y = 460
            axe = False
            axe2 = False
            g = False
            fall = True

        else:
            batdamage = True
            fall = False

    elif fightaction[pygame.K_7] and x >= xl - 40:
        if damcount <= 24:
            batdamage = True
            width -= widthc2
        if width < 2:
            width = 0
            rect2 = False

        if width < 2:
            width = 0
            rect2 = False
            batdamage = False
            y = 460
            axe = False
            axe2 = False
            batdamage = False
            g = False
            fall = True

        else:
            batdamage = True
            fall = False


    else:
        batdamage = False

    fightl()


pygame.quit()