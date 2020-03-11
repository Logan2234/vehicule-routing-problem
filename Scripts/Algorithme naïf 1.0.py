# TIPE - Algorithme Naïf 1.0 - Méthode Heuristique

from numpy import sqrt
from matplotlib.pyplot import *
from random import randint as rand

# Sachant que départ et arrivée sont des couples, des coordonnées (x0, y0)
def distance(départ, arrivée):
    return sqrt((arrivée[0]-départ[0])**2+(arrivée[1]-départ[1])**2)

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

    for i in range(len(list_départ)):
        distance_tot += distance(list_départ[i],list_arrivée[i])
        plot([list_départ[i][0],list_arrivée[i][0]],[list_départ[i][1],list_arrivée[i][1]],color=(0,0,0))
        pause(0.1)
        show(block = False)
    print("Distance totale : " + str(int(distance_tot)) + "km")
