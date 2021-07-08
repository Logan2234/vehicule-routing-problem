# Analyse des données de gains

from matplotlib.pyplot import show, axis, clf, scatter, plot, grid, legend, hist
from numpy import linspace, log

fichier = open("gains.txt","r")

_ = fichier.readline() # Débarassé de la première ligne

lignes = fichier.readlines() # On récupère les lignes

for ligne in range(len(lignes)):
    lignes[ligne] = lignes[ligne][:-1].split(",") # Pour chaque ligne on supprime le "\n" et on sépare les données

x = range(1,101)
N = [0]*100
gain1 = [0]*100
gain2 = [0]*100

maximum = 0
maximum2 = 0
for i in range(len(lignes)):
    n = int(lignes[i][0])-1
    N[n] += 1
    gain1[n] += float(lignes[i][1])
    gain2[n] += float(lignes[i][2])
    if float(lignes[i][2]) > maximum2:
        maximum2 = float(lignes[i][2])
    if float(lignes[i][1]) > maximum:
        maximum = float(lignes[i][1])


for i in range(len(N)):
    nbr = N[i]
    if nbr != 0:
        gain1[i] /= nbr
        gain2[i] /= nbr

print(maximum)
print(maximum2)

scatter(0,40,c="w")
plot(x, gain1, label = "Gain après l'opérateur inter-route (en %)", marker = "+")
plot(x, gain2, label = "Gain après l'opérateur 2-opt (en %)", marker = "+")
legend()
show()