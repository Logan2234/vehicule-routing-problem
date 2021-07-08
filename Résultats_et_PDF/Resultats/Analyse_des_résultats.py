# Analyse des données

from matplotlib.pyplot import show, axis, clf, scatter, plot, grid, legend
from numpy import linspace

fichier = open("results2.txt","r")

_ = fichier.readline() # Débarassé de la première ligne

lignes = fichier.readlines() # On récupère les lignes

for ligne in range(len(lignes)):
    lignes[ligne] = lignes[ligne][:-1].split(",") # Pour chaque ligne on supprime le "\n" et on sépare les données

x = range(1,101)
N = [0]*100
time = [0]*100
nb_2opt = [0]*100
nb_inter = [0]*100

for i in range(len(lignes)):
    n = int(lignes[i][0])-1
    N[n] += 1
    time[n] += float(lignes[i][1])
    nb_inter[n] += int(lignes[i][2])
    nb_2opt[n] += int(lignes[i][3])

for i in range(len(N)):
    nbr = N[i]
    if nbr != 0:
        time[i] /= nbr
        nb_inter[i] /= nbr
        nb_2opt[i] /= nbr

from numpy import log

abscisse = linspace(1,100,1000)
plot(abscisse, [y**4*1.3e-06 for y in abscisse], color = "red", label = "y = 1.3*10^(-6)*x^4")
scatter(x, (time), marker = ".", label = "Temps moyen",c="blue")
fichier = open("test.txt","a")
for i in time:
    print(str(i))
    fichier.write(str(i) + "\n")
legend()
show()
clf()

scatter(x, nb_inter, marker = ".", label = "Nombre moyen d'exécution de l'opérateur inter-route")
# print(nb_inter)
scatter(x, nb_2opt, label = "Nombre moyen d'exécution du 2-opt", marker = ".")
legend()
show()
clf()
#
# NB_INTER_ROUTE = []
# TEMPS = []
# NB_2OPT = []
# for ligne in lignes:
#     TEMPS.append(ligne[1])
#     NB_INTER_ROUTE.append(ligne[2])
#     NB_2OPT.append(ligne[3])
#
# res= [0]*45
# res2= []
#
# from numpy import average
#
# for i in range(45):
#     liste = []
#     for j in range(len(NB_INTER_ROUTE)):
#         if int(NB_INTER_ROUTE[j]) == i:
#             liste.append(float(TEMPS[j]))
#     res[i] = average(liste)
#
# for i in range(11):
#     liste = []
#     for j in range(len(NB_2OPT)):
#         if int(NB_2OPT[j]) == i:
#             liste.append(float(TEMPS[j]))
#     if liste != []:
#         res2.append(average(liste))

# scatter(range(45),res, label="Temps d'exécution en fonction du nombre\nd'exécutions de la fonction inter_route")
# scatter([0,1,2,3,4,5,6,10],res2, label = "Temps d'exécution en fonction du nombre\nd'exécutions de la fonction 2_opt")
# legend()
# show()