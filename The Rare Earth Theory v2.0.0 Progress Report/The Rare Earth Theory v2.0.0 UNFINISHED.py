import pygame
import TRETButton
import sys
import math
from TRETStar import Star
from TRETStar import Radius
from TRETStar import HZ
pygame.init()

pygame.key.set_repeat(250, 30)

screen_height = 500
screen_width = 800
screen = pygame.display.set_mode((screen_width,screen_height)) #add pygame.RESIZABLE if needed
pygame.display.set_caption("The Rare Earth Theory v2.0.0")
background = pygame.image.load("space background.png").convert_alpha()

start_button = pygame.image.load('StartButton.png').convert_alpha()
exit_button = pygame.image.load('EXIT.png').convert_alpha()
TRET_image = pygame.image.load('TRET.png').convert_alpha()
v200_image = pygame.image.load('v200.png').convert_alpha()

STAR_image = pygame.image.load('HowHotIsYourStar.png').convert_alpha()
STARtemprange_image = pygame.image.load('startemprange.png').convert_alpha()
SUNtemp_image = pygame.image.load('suntemp.png').convert_alpha()
BOX_image = pygame.image.load('BOX_image.png').convert_alpha() 

OTS_image = pygame.image.load('O type star.png').convert_alpha()
BTS_image = pygame.image.load('B type star.png').convert_alpha()
ATS_image = pygame.image.load('A type star.png').convert_alpha()
FTS_image = pygame.image.load('F type star.png').convert_alpha()
GTS_image = pygame.image.load('G type star.png').convert_alpha()
KTS_image = pygame.image.load('K type star.png').convert_alpha()
MTS_image = pygame.image.load('M type star.png').convert_alpha()

ClickPlacePlanet = pygame.image.load('Clicktoplace.png').convert_alpha()
TempEarthImage = pygame.image.load('RockyPlanet.png').convert_alpha()

TRET = TRETButton.Button(400,-300, TRET_image, 0.5)
v200 = TRETButton.Button(400,-250, v200_image,0.25)

startbutton = TRETButton.Button(400,-150,start_button,0.45)
exitbutton = TRETButton.Button(400,-50,exit_button,0.45)

STARCHOOSE = TRETButton.Button(400,100, STAR_image, 0.4)
STARTEMPRANGE = TRETButton.Button(400,150, STARtemprange_image, 0.325)
SUNTEMPREF = TRETButton.Button(400,200, SUNtemp_image, 0.275)
BOX = TRETButton.Button(400,300, BOX_image, 0.1)

StarImages = {
    "O": TRETButton.Button(400, 250, OTS_image, 0.06),
    "B": TRETButton.Button(400,250, BTS_image, 0.12),
    "A": TRETButton.Button(400,250, ATS_image, 0.16),
    "F": TRETButton.Button(400,250, FTS_image, 0.17),
    "G": TRETButton.Button(400,250, GTS_image, 0.18),
    "K": TRETButton.Button(400,250, KTS_image, 0.19),
    "M": TRETButton.Button(400,250, MTS_image, 0.20)
    }

CPP = TRETButton.Button(400,40, ClickPlacePlanet, 0.325)

clock = pygame.time.Clock()
base_font = pygame.font.SysFont('timesnewroman', 35)
user_text = ''
input_rect = pygame.Rect(340, 275, 100, 50)
color = pygame.Color('black')
active = False

def MenuDrawingMovement(x,y,w,z):
    x.draw(screen), y.draw(screen), x.movement(w), y.movement(z)

def ButtonImageMovement(x,y,w,z):
    x.movement(w), y.movement(z)

def RegularImage(x):
    x.draw(screen)

def PlanetMovement(x):
    x.draw(screen), x.orbit(400,250,0.025)

def StarTempRGB(t):
    tmin, tmax = 2000,50000
    if t < 2000:
        trelative = 0
    elif t > tmax:
        trelative = 1
    else:
        trelative = (t-2000)/(50000-2000)
    R = 255
    G = 230 * (1 - trelative)
    B = G * 0.75
        
    return(round(R),round(G),round(B))

def DrawTextBox():
    pygame.draw.rect(screen, color, input_rect)
    text_color = (255,255,255)
    if user_text != "":
        startemptext = float(user_text)
        text_color = StarTempRGB(startemptext)
    text_surface = base_font.render(user_text, True, text_color) # 255,181,8 is yellow ish
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(125, text_surface.get_width()+10)

def Luminosity(x,y):
    return (x**2) * ((y/5800)**4)


menu = True
running = True
StarTempChooser = False
PlanetChooser = False
FinalStarTemp = None
OuterHabitableZone = 175
RelativityConstant = 0
Lrel = None
TempPlanetX = 0
TempPlanetY = 0
PlanetX = 0
PlanetY = 0
PlanetClicked = False
PlanetClickLock = False
PlanetPlaceChooser = False

while running:
    clock.tick(60)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.unicode.isdigit():
                user_text += event.unicode
            elif event.key == pygame.K_RETURN:
                if user_text != "":
                    if float(user_text) < 2000:
                        print("too cold!")
                    elif 50000 < float(user_text):
                        print("too hot!")
                    else:
                        print("Confirmed.")
                        FinalStarTemp = float(user_text)

    if menu:
        MenuDrawingMovement(TRET,v200,100,175)
        ButtonImageMovement(startbutton,exitbutton,250,350)
        if startbutton.draw(screen):
            menu = False
            StarTempChooser = True
        if exitbutton.draw(screen):
            running = False
    elif StarTempChooser:
            DrawTextBox()
            RegularImage(STARCHOOSE)
            RegularImage(SUNTEMPREF)
            RegularImage(STARTEMPRANGE)
            RegularImage(BOX)
            if FinalStarTemp != None:
                StarTempChooser = False
                PlanetPlaceChooser = True

    elif PlanetPlaceChooser:
        RegularImage(CPP)
        RegularImage(StarImages[Star(FinalStarTemp)[2]])
        Lrel = Luminosity(Radius(Star(FinalStarTemp)[6],FinalStarTemp,Star(FinalStarTemp)[0],Star(FinalStarTemp)[1]),FinalStarTemp)
        ColderLimit = math.sqrt(Lrel/0.75)
        HotterLimit = math.sqrt(Lrel/1.25)
        RelativityConstant = ColderLimit/OuterHabitableZone
        pygame.draw.circle(
            screen,
            (0,255,100),
            (400,250),
            OuterHabitableZone,
            int(HZ(ColderLimit,HotterLimit,OuterHabitableZone))
        )
        if pygame.mouse.get_pressed()[0] == 1 and not PlanetClickLock and not PlanetClicked:
            PlanetClickLock = True
            TempPlanetX = pygame.mouse.get_pos()[0]
            TempPlanetY = pygame.mouse.get_pos()[1]
            if  HotterLimit/RelativityConstant <= (math.sqrt((TempPlanetX-400)**2 + (TempPlanetY-250)**2)) <= OuterHabitableZone:
                print("Planet placed")
                PlanetX = pygame.mouse.get_pos()[0]
                PlanetY = pygame.mouse.get_pos()[1]
                TempEarthImage = TRETButton.Button(PlanetX,PlanetY,TempEarthImage,0.02)
                PlanetClicked = True
                PlanetPlaceChooser = False
            else:
                print("Planet not placed")
                print(math.sqrt((TempPlanetX-400)**2 + (TempPlanetY-250)**2))
                print(HotterLimit/OuterHabitableZone)
                print(ColderLimit/OuterHabitableZone)

        if not pygame.mouse.get_pressed()[0] == 1:
            PlanetClickLock = False
        
        pygame.display.flip()

    else:
        RegularImage(StarImages[Star(FinalStarTemp)[2]])
        PlanetMovement(TempEarthImage)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()