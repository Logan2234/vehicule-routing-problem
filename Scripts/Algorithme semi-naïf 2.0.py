# TIPE - Algorithme semi-naïf 2.0

from numpy import sqrt
from matplotlib.pyplot import *
from random import randint as rand

# Sachant que départ et arrivée sont des couples, des coordonnées (x0, y0)

def distance(départ, arrivée):
    return sqrt((arrivée[0]-départ[0])**2+(arrivée[1]-départ[1])**2)

def minimum(départ, list_arrivée):
    dmin = (list_arrivée[0],distance(départ,list_arrivée[0]),0)
    
    for i in range(1,len(list_arrivée)):

        temp = distance(départ,list_arrivée[i])

        if temp < dmin[1]:
            dmin = (list_arrivée[i],temp,i)
    
    return dmin

def main(nmb = 10):
    list_départ = []
    list_arrivée = []
    distance_tot = 0
    clf()

    for i in range(nmb):
        list_départ.append([rand(0,1000),rand(0,1000)]) 
        list_arrivée.append([rand(0,1000),rand(0,1000)])
    
    for i in list_arrivée:
        scatter(i[0],i[1],color=(1,0,0))

    for i in list_départ:
        scatter(i[0],i[1],color=(0,0,1))
        
    for i in list_départ:
        minimum_temp = minimum(i,list_arrivée)
        distance_tot += minimum_temp[1]
        plot([i[0],minimum_temp[0][0]],[i[1],minimum_temp[0][1]],color=(0,0,0))
        list_arrivée.pop(minimum_temp[2])
        pause(0.1)
        show(block = False)
    print("Distance totale : " + str(int(distance_tot)) + "km")