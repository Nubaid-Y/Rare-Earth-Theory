import math

Stages = "Habitable", "Single-Celled", "Multicellular", "Complex", "Intelligent"

def LifeClassification(CurrentStageNum,Temp, Ice, Water, Vapor, RandomNumber):
    StageNumber = CurrentStageNum
    StagesOfLife = [ #make sure to change the %
        ("Habitable",260,360,0,100,0,100,0,100,1.0),
        ("Single-Celled",260,350,0,100,5,100,0,20,0.0005),
        ("Multicellular",260,330,0,50,30,100,0,10,0.00005),
        ("Complex",270,320,0,30,50,100,0,5,0.00001),
        ("Intelligent",270,320,0,30,50,100,0,5,0.000005)
    ]

    if StageNumber >= len(StagesOfLife) - 1:
        return StageNumber

    NextStage = StagesOfLife[StageNumber + 1]
    a,b,c,d,e,f,g,h,i,j = NextStage

    if b <= Temp <= c and d <= Ice <= e and f <= Water <= g and h <= Vapor <= i:
        if RandomNumber <= j:
            StageNumber += 1

    return StageNumber