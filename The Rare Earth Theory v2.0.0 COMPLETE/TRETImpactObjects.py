# Order: lower %, higher %, H2O, CO2, CH4, N2, NH3, O2, H2
import random

def asteroid(x):
    types = [
        # Rocky asteroids (40%)
        (0.60, 1.01, 0.0003*x, 0.0008*x, 0, 0.0006*x, 0, 0, 0),

        # Icy asteroids (35%)
        (0.25, 0.60, 0.012*x, 0.0012*x, 0.0007*x, 0.0007*x, 0.0006*x, 0, 0.0004*x),

        # Carbon rich asteroids (25%)
        (0.00, 0.25, 0.004*x, 0.002*x, 0.0014*x, 0, 0.0007*x, 0, 0.0003*x)
    ]

    for a,b,c,d,e,f,g,h,i in types:
        if a <= x < b:
            return a,b,c,d,e,f,g,h,i


def Planetesimal(x):
    types = [
        # Rocky asteroids (40%)
        (0.60, 1.01, 0.001*x, 0.003*x, 0, 0.002*x, 0, 0, 0),

        # Icy asteroids (35%)
        (0.25, 0.60, 0.05*x, 0.004*x, 0.0025*x, 0.0025*x, 0.002*x, 0, 0.0008*x),

        # Carbon rich asteroids (25%)
        (0.00, 0.25, 0.012*x, 0.008*x, 0.005*x, 0, 0.0025*x, 0, 0.0006*x)
    ]

    for a,b,c,d,e,f,g,h,i in types:
        if a <= x < b:
            return a,b,c,d,e,f,g,h,i