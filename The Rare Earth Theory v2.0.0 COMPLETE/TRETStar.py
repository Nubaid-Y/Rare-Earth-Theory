import pygame
import math

def Star(K):
    classification = [
        (30000, 50001, "O", 0.005, 2.0,False,10,3),
        (10000, 30000, "B", 0.05, 1.8,False,8,3),
        (7500, 10000, "A", 1.0, 1.4,False,2,2),
        (6000, 7500, "F", 4, 1.2,False,1.3,2),
        (5000, 6000, "G", 10, 1.0,False,1,2),
        (3500, 5000, "K", 25, 1.3,False,0.8,2),
        (2000, 3500, "M", 500, 8.0,True,0.3,1)
    ]
    for a,b,c,d,e,f,g,h in classification:
        if a <= K < b:
            return a,b,c,d,e,f,g,h

def Radius(baseR,Ts,lower,upper):
    R = baseR * (Ts/((upper + lower)*(1/2)))
    return R

def HZ(x,y,z):
    xrel = x/z
    return x/xrel - y/xrel

def massluminosity(x,y):
    if x == 1:
        return ((y/0.23)**(1/2.3))
    elif x ==2:
        return (y**(1/4))
    else:
        return ((y/1.4)**(1/3.5))