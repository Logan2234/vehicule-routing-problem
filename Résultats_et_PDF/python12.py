distance2 = distance_comparaison(DEPOT, CLIENTS, ROUTES, APRES_INTRA_ROUTE)
print("Apres tous les 2opt: " + str(distance2))


print("Nombre de 2opt: " + str(NB_2OPT))
print("Nombre de inter-route: " + str(NB_INTER))

gain1 = round(1-distance1[1]/distance1[0],2)*100
gain2 = round(1-distance2[1]/distance2[0],2)*100

print("Gain apres l operateur inter-route: " + str(gain1) + "%\nGain apres l operateur 2-opt: " + str(gain2) + "%")