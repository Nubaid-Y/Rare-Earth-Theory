import pygame
import sys
import math
import time
import random

import TRETButton

from TRETStar import Star
from TRETStar import Radius
from TRETStar import HZ
from TRETStar import massluminosity


from TRETImpactObjects import asteroid
from TRETEquations import Greenhouse
from TRETEquations import PlanetTemp
from TRETEquations import EscapeVelocity
from TRETEquations import Retention
from TRETEquations import YearLengthCalculator

from TRETH2OBehavior import H2OProximity
from TRETH2OBehavior import H2OSimilarity
from TRETH2OBehavior import H2OSimilarityPercentage

from TRETLife import LifeClassification

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
StartingPlanetImage = pygame.image.load('RockyPlanet.png').convert_alpha()

TimeElapsed = pygame.image.load('TimeElapsed.png').convert_alpha()
Myr = pygame.image.load('Myr.png').convert_alpha()
Gyr = pygame.image.load('Gyr.png').convert_alpha()

OrbitalClimate = pygame.image.load('Orbital & Climate.png').convert_alpha()
PlanetTempTextText = pygame.image.load('PlanetTemp.png').convert_alpha()
YearLength = pygame.image.load('YearLength.png').convert_alpha()

Volatiles = pygame.image.load('Volatiles.png').convert_alpha()
H2OImage = pygame.image.load('H2O.png').convert_alpha()
CO2 = pygame.image.load('CO2.png').convert_alpha()
CH4 = pygame.image.load('CH4.png').convert_alpha()
N2 = pygame.image.load('N2.png').convert_alpha()
NH3 = pygame.image.load('NH3.png').convert_alpha()

DerivedGases = pygame.image.load('DerivedGases.png').convert_alpha()
O2 = pygame.image.load('O2.png').convert_alpha()
H2 = pygame.image.load('H2.png').convert_alpha()
He = pygame.image.load('He.png').convert_alpha()

H2ODistribution = pygame.image.load('H2ODistribution.png').convert_alpha()
Ice = pygame.image.load('Ice.png').convert_alpha()
Water = pygame.image.load('Water.png').convert_alpha()
Vapor = pygame.image.load('Vapor.png').convert_alpha()

CelestialImpacts = pygame.image.load('CelestialImpacts.png').convert_alpha()
Asteroids = pygame.image.load('Asteroids.png').convert_alpha()
Planetesimals = pygame.image.load('Planetesimals.png').convert_alpha()

LifeStatus = pygame.image.load('LifeStatus.png').convert_alpha()
LifeStatusBox = pygame.image.load('BOX_imageOLDISH.png').convert_alpha()

supernova = pygame.image.load('supernova.png').convert_alpha()

iceworld = pygame.image.load('iceworld.png').convert_alpha()
rockyworld = pygame.image.load('rockyworld.png').convert_alpha()
gasworld = pygame.image.load('gasworld.png').convert_alpha()

TRET = TRETButton.Button(400,-300, TRET_image, 0.5)
v200 = TRETButton.Button(400,-250, v200_image,0.25)

startbutton = TRETButton.Button(400,-150,start_button,0.45)
exitbutton = TRETButton.Button(400,-50,exit_button,0.45)

STARCHOOSE = TRETButton.Button(400,100, STAR_image, 0.4)
STARTEMPRANGE = TRETButton.Button(400,150, STARtemprange_image, 0.325)
SUNTEMPREF = TRETButton.Button(400,200, SUNtemp_image, 0.275)
BOX = TRETButton.Button(400,300, BOX_image, 0.1)
BOX2 = TRETButton.Button(360, 75, BOX_image, 0.05)

ElapsedTimeImage = TRETButton.Button(400,30, TimeElapsed, 0.25)
MyrImage = TRETButton.Button(435,77.5, Myr, 0.3)
GyrImage = TRETButton.Button(435,77.5, Gyr, 0.3)

OrbitalClimateText = TRETButton.Button(120,30, OrbitalClimate, 0.25)
PlanetTempText = TRETButton.Button(80,75, PlanetTempTextText, 0.20)
BOX4 = TRETButton.Button(180, 75, BOX_image, 0.05)
YearLengthText = TRETButton.Button(80,125, YearLength, 0.20)
BOX13= TRETButton.Button(180, 125, BOX_image, 0.05)

VolatilesText = TRETButton.Button(100,230, Volatiles, 0.25)
H2OText = TRETButton.Button(80,275, H2OImage, 0.25)
BOX5 = TRETButton.Button(180, 275, BOX_image, 0.05)
CO2Text = TRETButton.Button(80,325, CO2, 0.25)
BOX6 = TRETButton.Button(180, 325, BOX_image, 0.05)
CH4Text = TRETButton.Button(80,375, CH4, 0.25)
BOX7 = TRETButton.Button(180, 375, BOX_image, 0.05)
N2Text = TRETButton.Button(80,425, N2, 0.25)
BOX8 = TRETButton.Button(180, 425, BOX_image, 0.05)
NH3Text = TRETButton.Button(80,475, NH3, 0.25)
BOX9 = TRETButton.Button(180, 475, BOX_image, 0.05)

DerivedGasesText = TRETButton.Button(700,30, DerivedGases, 0.25)
O2Text = TRETButton.Button(640,75, O2, 0.25)
BOX10 = TRETButton.Button(740, 75, BOX_image, 0.05)
H2Text = TRETButton.Button(640,125, H2, 0.25)
BOX11 = TRETButton.Button(740, 125, BOX_image, 0.05)

H2ODistributionText = TRETButton.Button(675,180, H2ODistribution, 0.25)
IceText = TRETButton.Button(640,225, Ice, 0.25)
BOX14 = TRETButton.Button(740, 225, BOX_image, 0.05)
WaterText = TRETButton.Button(640,275, Water, 0.25)
BOX15 = TRETButton.Button(740, 275, BOX_image, 0.05)
VaporText = TRETButton.Button(640,325, Vapor, 0.25)
BOX16 = TRETButton.Button(740, 325, BOX_image, 0.05)

CelestialImpactsText = TRETButton.Button(675,380, CelestialImpacts, 0.25)
AsteroidsText = TRETButton.Button(640,425, Asteroids, 0.25)
BOX17 = TRETButton.Button(740, 425, BOX_image, 0.05)
PlanetesimalsText = TRETButton.Button(615,475, Planetesimals, 0.25)
BOX18 = TRETButton.Button(740, 475, BOX_image, 0.05)

LifeStatusText = TRETButton.Button(400,435, LifeStatus, 0.25)
BOX19 = TRETButton.Button(400, 475, LifeStatusBox, 0.125)

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
user_text = ''
active = False
holdertext = "nil"
StageName = "nil"

def MenuDrawingMovement(x,y,w,z):
    x.draw(screen), y.draw(screen), x.movement(w), y.movement(z)

def ButtonImageMovement(x,y,w,z):
    x.movement(w), y.movement(z)

def RegularImage(x):
    x.draw(screen)

def PlanetMovement(x):
    x.draw(screen), x.orbit(400,250,planetorbitalperiod)

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
    #settings
    input_rect = pygame.Rect(340, 275, 130, 48)
    base_font = pygame.font.SysFont('timesnewroman', 35)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)
    text_color = (255,255,255)
    if user_text != "":
        startemptext = float(user_text)
        text_color = StarTempRGB(startemptext)
    text_surface = base_font.render(user_text, True, text_color) # 255,181,8 is yellow ish
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(125, text_surface.get_width()+10)

def DrawDisplayBox():

    input_rect = pygame.Rect(330, 60, 55, 30)
    base_font = pygame.font.SysFont('timesnewroman', 20)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = holdertext

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)

def DrawCoreBox(x,y,z,d):

    input_rect = pygame.Rect(150, z+50*x, 55, 30)
    base_font = pygame.font.SysFont('timesnewroman', d)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = y

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)

def DrawVolatilesBox(x,y,z):

    input_rect = pygame.Rect(150, z+50*x, 55, 30)
    base_font = pygame.font.SysFont('timesnewroman', 20)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = str(y)

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)

def DrawDerivedGasesBox(x,y,z):

    input_rect = pygame.Rect(710, z+50*x, 55, 30)
    base_font = pygame.font.SysFont('timesnewroman', 20)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = y

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)

def DrawH2OBox(x,y,z):

    input_rect = pygame.Rect(710, z+50*x-50, 55, 30)
    base_font = pygame.font.SysFont('timesnewroman', 20)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = y

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)

def DrawCelestialBox(x,y,z):

    input_rect = pygame.Rect(710, z+50*x-100, 55, 30)
    base_font = pygame.font.SysFont('timesnewroman', 20)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = y

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)

def DrawDisplayBox2(x,y):

    input_rect = pygame.Rect(x-90, y-15, 175, 30)
    base_font = pygame.font.SysFont('timesnewroman', 20)
    color = pygame.Color('black')

    pygame.draw.rect(screen, color, input_rect)

    text_color = (255,255,255)
    text = StageName

    text_surface = base_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=input_rect.center)
    screen.blit(text_surface, text_rect)
    #input_rect.w = max(125, text_surface.get_width()+10)


def Luminosity(x,y):
    return (x**2) * ((y/5800)**4)

def SupernovaDrawingMovement(x,y):
    x.draw(screen), x.movement(y)

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
elapsedtime = 0
initialelapsedtime = None
MainGame = False

Yearconstant = 100
asteroiddecay = 15
planetesimaldecay = 5
lastsecond = 0
planetvisible = True
BeginnerPlanetMass = 0
PlanetMass = 0
AsteroidHit = 0
PlanetesimalHit = 0

#PlanetAtmosphere (delivered gases)
H2OTotalSupply = 0
H2OVaporAtmospherePercentage = 0
H2OIceSupply = 0
H2OWaterSupply = 0
H2OVaporSupply = 0
H2OIcePercentage = "nil"
H2OWaterPercentage = "nil"
H2OVaporPercentage = "nil"
CO2 = 0
CO2Percentage = "nil"
CH4 = 0
CH4Percentage = "nil"
N2 = 0.02 * BeginnerPlanetMass
N2Percentage = "nil"
NH3 = 0
NH3Percentage = "nil"

#PlanetDerivedGases
O2 = 0
O2Percentage = "nil"
H2 = 0
H2Percentage = "nil"

#H2O States

IceExist = False
WaterExist = False
VaporExist = False

IceRange = -90,40
IceMidRange = -25
IceProximity = 0

WaterRange = -10,140
WaterMidRange = 75
WaterProximity = 0

VaporRange = 90,220
VaporMidRange = 155
VaporProximity = 0

CurrentStageNumber = 0
Stages = "Habitable", "Single-Celled", "Multicellular", "Complex", "Intelligent"

endelapsedtime = None
SupernovaImage = None

PlanetTypeImage = StartingPlanetImage

Outro = False

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
                distancepx = math.sqrt((TempPlanetX-400)**2 + (TempPlanetY-250)**2)
                AUperpx = ColderLimit/OuterHabitableZone
                DistanceAU = distancepx*AUperpx
                RelativeRadiation = Lrel/(DistanceAU**2)
                BeginnerPlanetMass = random.uniform(0.01,0.03)
                PlanetMass = BeginnerPlanetMass
                PlanetImage = TRETButton.Button(PlanetX,PlanetY,PlanetTypeImage,PlanetMass)
                PlanetClicked = True
                PlanetPlaceChooser = False
                MainGame = True
                if initialelapsedtime is None:
                    initialelapsedtime=pygame.time.get_ticks()
            else:
                print("Planet not placed")
                print(math.sqrt((TempPlanetX-400)**2 + (TempPlanetY-250)**2))
                print(HotterLimit/OuterHabitableZone)
                print(ColderLimit/OuterHabitableZone)

        if not pygame.mouse.get_pressed()[0] == 1:
            PlanetClickLock = False
        pygame.display.flip()

    elif MainGame:

        RegularImage(StarImages[Star(FinalStarTemp)[2]])
        
        planetorbitalperiod =  0.1 + (FinalStarTemp - 2000) * (-0.099/48001)

        if planetvisible:
            PlanetMovement(PlanetImage)
        
        elapsedtime = (pygame.time.get_ticks() - initialelapsedtime)
        supernovacounter = (Star(FinalStarTemp)[3])*100*1000 #the counter is in milliseconds
        
        YrImage = MyrImage
        if elapsedtime >= 100000:
            Yearconstant = 100000
            YrImage = GyrImage
        realtime = (pygame.time.get_ticks() - initialelapsedtime)
        MYA = str(round(realtime/Yearconstant))

        Year_Length = YearLengthCalculator(DistanceAU,Lrel)
        YearLengthDays = Year_Length*365

        GreenhouseAmount = Greenhouse(CO2,CH4,H2OVaporSupply,NH3)
        PlanetTemperature = PlanetTemp(RelativeRadiation,GreenhouseAmount)
        PlanetTemperatureCelsius = PlanetTemperature - 273.15
        EscapeVelocityValue = EscapeVelocity(PlanetMass)

        #WaterLogic
        IceExist, WaterExist, VaporExist, IceProximity, WaterProximity, VaporProximity = H2OProximity(PlanetTemperatureCelsius)

        IceSimilarity = H2OSimilarity(IceExist, IceProximity)
        WaterSimilarity = H2OSimilarity(WaterExist, WaterProximity)
        VaporSimilarity = H2OSimilarity(VaporExist, VaporProximity)

        H2OIcePercentage,H2OWaterPercentage,H2OVaporPercentage = H2OSimilarityPercentage(IceSimilarity,WaterSimilarity,VaporSimilarity)
        
        Atmosphere = H2OVaporSupply+CO2+CH4+N2+NH3+O2+H2

        #make sure H2O is replaced with water vapor.       
        if H2OTotalSupply != 0:
            H2OIceSupply = (H2OIcePercentage/100) * H2OTotalSupply
            H2OWaterSupply = (H2OWaterPercentage/100) * H2OTotalSupply
            H2OVaporSupply = (H2OVaporPercentage/100) * H2OTotalSupply

        def GasPercentage(x):
            return x/float(Atmosphere) * 100

        if H2OTotalSupply != 0:
            if H2OIcePercentage >= 50:
                PlanetTypeImage = iceworld
            elif H2OWaterPercentage > 50:
                PlanetTypeImage = rockyworld
            else:
                PlanetTypeImage = gasworld

        RegularImage(ElapsedTimeImage)
        RegularImage(YrImage)
        
        DrawDisplayBox()
        RegularImage(BOX2)

        RegularImage(OrbitalClimateText)
        RegularImage(PlanetTempText)
        DrawCoreBox(0,f"{PlanetTemperatureCelsius:.3g}°C",60,20)
        RegularImage(BOX4)
        RegularImage(YearLengthText)
        DrawCoreBox(1,f"{YearLengthDays:.3g} D",60,20)
        RegularImage(BOX13)
        RegularImage(VolatilesText)
        RegularImage(H2OText)
        DrawVolatilesBox(0,f"{H2OVaporAtmospherePercentage:.3g}%",260)
        RegularImage(BOX5)
        RegularImage(CO2Text)
        DrawVolatilesBox(1,CO2Percentage,260)        
        RegularImage(BOX6)
        RegularImage(CH4Text)
        DrawVolatilesBox(2,CH4Percentage,260)        
        RegularImage(BOX7)
        RegularImage(N2Text)
        DrawVolatilesBox(3,N2Percentage,260)        
        RegularImage(BOX8)
        RegularImage(NH3Text)
        DrawVolatilesBox(4,NH3Percentage,260)        
        RegularImage(BOX9)

        RegularImage(DerivedGasesText)
        RegularImage(O2Text)
        DrawDerivedGasesBox(0,O2Percentage,60)
        RegularImage(BOX10)
        RegularImage(H2Text)
        DrawDerivedGasesBox(1,H2Percentage,60)
        RegularImage(BOX11)

        RegularImage(H2ODistributionText)
        RegularImage(IceText)
        DrawH2OBox(0,f"{H2OIcePercentage:.3g}%",260)
        RegularImage(BOX14)
        RegularImage(WaterText)
        DrawH2OBox(1,f"{H2OWaterPercentage:.3g}%",260)
        RegularImage(BOX15)
        RegularImage(VaporText)
        DrawH2OBox(2,f"{H2OVaporPercentage:.3g}%",260)
        RegularImage(BOX16)

        RegularImage(CelestialImpactsText)
        RegularImage(AsteroidsText)
        DrawCelestialBox(0,str(AsteroidHit),510)
        RegularImage(BOX17)
        RegularImage(PlanetesimalsText)
        DrawCelestialBox(1,str(PlanetesimalHit),510)
        RegularImage(BOX18)

        RegularImage(LifeStatusText)
        DrawDisplayBox2(400,475)
        RegularImage(BOX19)

        holdertext = str(MYA)

        secondstranslation = int((pygame.time.get_ticks() - initialelapsedtime)/1000)

        if math.exp(-secondstranslation / asteroiddecay) > 0.05:
            asteroidprobability = math.exp(-secondstranslation / asteroiddecay)
        else:
            asteroidprobability = 0.05

        if math.exp(-secondstranslation / planetesimaldecay) > 0.01:
            planetesimalprobability = math.exp(-secondstranslation / planetesimaldecay)
        else:
            planetesimalprobability = 0.01

        if int(secondstranslation) - lastsecond >= random.uniform(0.5,1.5):
            lastsecond = int(secondstranslation)
            rollnumber = random.random()
            if rollnumber < planetesimalprobability:
                PS = random.randint(3,5)
                PStype = random.random()
                PlanetMass += PlanetMass*(0.01*PS)

                planetvisible = False
                PlanetX = PlanetImage.rect.centerx
                PlanetY = PlanetImage.rect.centery

                PlanetImage = TRETButton.Button(PlanetX,PlanetY,PlanetTypeImage,PlanetMass)
                planetvisible = True

                # PlanetAtmosphere (delivered gases)
                H2OTotalSupply += Retention(((asteroid(PStype)[2])*PS), PlanetTemperature, 18, EscapeVelocityValue, Atmosphere)
                CO2 += Retention(((asteroid(PStype)[3])*PS), PlanetTemperature, 44, EscapeVelocityValue, Atmosphere)
                CH4 += Retention(((asteroid(PStype)[4])*PS), PlanetTemperature, 16, EscapeVelocityValue, Atmosphere)
                N2  += Retention(((asteroid(PStype)[5])*PS), PlanetTemperature, 28, EscapeVelocityValue, Atmosphere)
                NH3 += Retention(((asteroid(PStype)[6])*PS), PlanetTemperature, 17, EscapeVelocityValue, Atmosphere)

                # PlanetDerivedGases
                O2 += Retention(((asteroid(PStype)[7])*PS), PlanetTemperature, 32, EscapeVelocityValue, Atmosphere)
                H2 += Retention(((asteroid(PStype)[8])*PS), PlanetTemperature, 2,  EscapeVelocityValue, Atmosphere)

                PlanetesimalHit += 1

                Atmosphere = H2OVaporSupply+CO2+CH4+N2+NH3+O2+H2

                def GasPercentage(x):
                    return x/float(Atmosphere) * 100
                        
                H2OVaporAtmospherePercentage = GasPercentage(H2OVaporSupply)
                CO2Percentage = f"{GasPercentage(CO2):.3g}%"
                CH4Percentage = f"{GasPercentage(CH4):.3g}%"
                N2Percentage = f"{GasPercentage(N2):.3g}%"
                NH3Percentage = f"{GasPercentage(NH3):.3g}%"
                O2Percentage = f"{GasPercentage(O2):.3g}%"
                H2Percentage = f"{GasPercentage(H2):.3g}%"
                
            if rollnumber < asteroidprobability:
                AS = random.randint(1,5)
                AStype = random.random()
                PlanetMass += PlanetMass*(0.0002*AS)

                planetvisible = False
                PlanetX = PlanetImage.rect.centerx
                PlanetY = PlanetImage.rect.centery

                PlanetImage = TRETButton.Button(PlanetX,PlanetY,PlanetTypeImage,PlanetMass)
                planetvisible = True

                # PlanetAtmosphere (delivered gases)
                H2OTotalSupply += Retention(((asteroid(AStype)[2])*AS), PlanetTemperature, 18, EscapeVelocityValue, Atmosphere)
                CO2 += Retention(((asteroid(AStype)[3])*AS), PlanetTemperature, 44, EscapeVelocityValue, Atmosphere)
                CH4 += Retention(((asteroid(AStype)[4])*AS), PlanetTemperature, 16, EscapeVelocityValue, Atmosphere)
                N2  += Retention(((asteroid(AStype)[5])*AS), PlanetTemperature, 28, EscapeVelocityValue, Atmosphere)
                NH3 += Retention(((asteroid(AStype)[6])*AS), PlanetTemperature, 17, EscapeVelocityValue, Atmosphere)

                # PlanetDerivedGases
                O2 += Retention(((asteroid(AStype)[7])*AS), PlanetTemperature, 32, EscapeVelocityValue, Atmosphere)
                H2 += Retention(((asteroid(AStype)[8])*AS), PlanetTemperature, 2,  EscapeVelocityValue, Atmosphere)

                AsteroidHit += 1

                Atmosphere = H2OVaporSupply+CO2+CH4+N2+NH3+O2+H2

                def GasPercentage(x):
                    return x/float(Atmosphere) * 100

                H2OVaporAtmospherePercentage = GasPercentage(H2OVaporSupply)
                CO2Percentage = f"{GasPercentage(CO2):.3g}%"
                CH4Percentage = f"{GasPercentage(CH4):.3g}%"
                N2Percentage = f"{GasPercentage(N2):.3g}%"
                NH3Percentage = f"{GasPercentage(NH3):.3g}%"
                O2Percentage = f"{GasPercentage(O2):.3g}%"
                H2Percentage = f"{GasPercentage(H2):.3g}%"
        
        #ticktranslation = int(pygame.time.get_ticks() - initialelapsedtime) #it is in milliseconds
        CurrentStageNumber = LifeClassification(CurrentStageNumber, PlanetTemperature, H2OIcePercentage, H2OWaterPercentage, H2OVaporPercentage, random.random())
        StageName = Stages[CurrentStageNumber]

        if CurrentStageNumber > 0 and AsteroidHit != 0:
            Atmosphere = H2OVaporSupply+CO2+CH4+N2+NH3+O2+H2
            def GasPercentage(x):
                return x/float(Atmosphere) * 200
            O2 = CurrentStageNumber/100
            O2Percentage = f"{GasPercentage(O2):.3g}%"

        if elapsedtime >= supernovacounter:
            MainGame = False
            SupernovaEvent = True
    elif SupernovaEvent:
        if endelapsedtime is None:
            endelapsedtime = pygame.time.get_ticks()

        endelapsedtimemiliseconds = int(pygame.time.get_ticks() - endelapsedtime)
        endelapsedtimeseconds = endelapsedtimemiliseconds/1000

        exponentialgrowtheffect = 1 - math.exp(-5 * endelapsedtimeseconds)
        SupernovaImageSizeConstant = 0.05 + 0.25 * exponentialgrowtheffect

        if SupernovaImageSizeConstant > 0.3:
            SupernovaImageSizeConstant = 0.3
        SupernovaImage = TRETButton.Button(400,250,supernova,SupernovaImageSizeConstant)
        RegularImage(SupernovaImage)
        
        SupernovaYMovement = 0
        if endelapsedtimemiliseconds > 5000:
            SupernovaEvent = False
            Outro = True
    elif Outro:
        SupernovaDrawingMovement(SupernovaImage,800)
        if SupernovaImage.rect.y > 800:
            TRET = TRETButton.Button(400,-300, TRET_image, 0.5)
            v200 = TRETButton.Button(400,-250, v200_image,0.25)
            startbutton = TRETButton.Button(400,-150,start_button,0.45)
            exitbutton = TRETButton.Button(400,-50,exit_button,0.45)
            user_text = ''
            Outro = False
            menu = True
            StarTempChooser = False
            PlanetChooser = False
            FinalStarTemp = None
            PlanetClicked = False
            PlanetClickLock = False
            PlanetPlaceChooser = False
            initialelapsedtime = None
            MainGame = False

            Yearconstant = 100
            lastsecond = 0
            planetvisible = True
            BeginnerPlanetMass = 0
            PlanetMass = 0
            AsteroidHit = 0
            PlanetesimalHit = 0

            #PlanetAtmosphere (delivered gases)
            H2OTotalSupply = 0
            H2OVaporAtmospherePercentage = 0
            H2OIceSupply = 0
            H2OWaterSupply = 0
            H2OVaporSupply = 0
            H2OIcePercentage = "nil"
            H2OWaterPercentage = "nil"
            H2OVaporPercentage = "nil"
            CO2 = 0
            CO2Percentage = "nil"
            CH4 = 0
            CH4Percentage = "nil"
            N2 = 0.02 * BeginnerPlanetMass
            N2Percentage = "nil"
            NH3 = 0
            NH3Percentage = "nil"

            #PlanetDerivedGases
            O2 = 0
            O2Percentage = "nil"
            H2 = 0
            H2Percentage = "nil"

            #H2O States
            IceExist = False
            WaterExist = False
            VaporExist = False
            
            IceProximity = 0
            WaterProximity = 0
            VaporProximity = 0

            CurrentStageNumber = 0

            endelapsedtime = None
            SupernovaImage = None

            Outro = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()