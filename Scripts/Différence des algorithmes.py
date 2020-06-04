# TIPE - Algorithme Naïf 1.0 - Méthode Heuristique

from numpy import sqrt
from matplotlib.pyplot import *
from random import randint as rand

# Sachant que départ et arrivée sont des couples, des coordonnées (x0, y0)
list_distance = []
def distance(départ, arrivée):
    return sqrt((arrivée[0]-départ[0])**2+(arrivée[1]-départ[1])**2)

def main(nmb = 10):
    list_départ = []
    list_arrivée = []
    distance_tot = 0

    for i in range(nmb):
        list_départ.append([rand(0,1000),rand(0,1000)])
        list_arrivée.append([rand(0,1000),rand(0,1000)])

    for i in range(len(list_départ)):
        distance_tot += distance(list_départ[i],list_arrivée[i])
    return distance_tot

for i in range(50):
    list_distance.append(int(main(25)))

moyenne = 0
for i in range(len(list_distance)):
    moyenne += list_distance[i]

print("Moyenne de l'algo 1 = " + str(int(moyenne/len(list_distance))) + "km" )

# TIPE - Algorithme semi-naïf 2.0

def minimum(départ, list_arrivée):
    dmin = (list_arrivée[0],distance(départ,list_arrivée[0]),0)
    
    for i in range(1,len(list_arrivée)):

        temp = distance(départ,list_arrivée[i])

        if temp < dmin[1]:
            dmin = (list_arrivée[i],temp,i)
    
    return dmin

def main2(nmb = 10):
    list_départ = []
    list_arrivée = []
    distance_tot = 0

    for i in range(nmb):
        list_départ.append([rand(0,1000),rand(0,1000)]) 
        list_arrivée.append([rand(0,1000),rand(0,1000)])
    
    for i in list_départ:
        minimum_temp = minimum(i,list_arrivée)
        distance_tot += minimum_temp[1]
        list_arrivée.pop(minimum_temp[2])

for i in range(50):
    list_distance.append(int(main2(25)))

moyenne = 0
for i in range(len(list_distance)):
    moyenne += list_distance[i]

print("Moyenne de l'algo 2 = " + str(int(moyenne/len(list_distance))) + "km" )
