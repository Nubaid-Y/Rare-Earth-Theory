import math

IceRange = (-150, 30)
IceMidRange = -70

WaterRange = (-10, 40)
WaterMidRange = 15

VaporRange = (25, 350)
VaporMidRange = 135

def H2OProximity(x):
    IceExist = False
    WaterExist = False
    VaporExist = False

    IceProximity = 0
    WaterProximity = 0
    VaporProximity = 0

    if IceRange[0] < x < IceRange[1]:
        IceExist = True
        IceProximity = abs(x - IceMidRange)

    if WaterRange[0] < x < WaterRange[1]:
        WaterExist = True
        WaterProximity = abs(x - WaterMidRange)

    if VaporRange[0] < x < VaporRange[1]:
        VaporExist = True
        VaporProximity = abs(x - VaporMidRange)

    return IceExist, WaterExist, VaporExist, IceProximity, WaterProximity, VaporProximity


def H2OSimilarity(exists, proximity):
    if exists:
        return 1 / (1 + proximity)
    else:
        return 0


def H2OSimilarityPercentage(x, y, z):
    SimilarityTotal = x + y + z

    if SimilarityTotal == 0:
        return 0, 0, 0

    return (((x/SimilarityTotal) * 100),((y/SimilarityTotal) * 100),((z/SimilarityTotal) * 100))