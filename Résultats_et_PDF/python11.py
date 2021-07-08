# Appel de l operateur inter-routes
NB_INTER = inter_route()
dessin(APRES_INTRA_ROUTE)
distance1 = distance_comparaison(DEPOT, CLIENTS, ROUTES, APRES_INTRA_ROUTE)
print("Apres inter-route: " + str(distance1))

# Appel de l'operateur intra-routes...
FINAL2 = copie(APRES_INTRA_ROUTE)
deux_opt(FINAL2)

# ... autant de fois qu il est necessaire
temp = distance_comparaison(DEPOT, CLIENTS, APRES_INTRA_ROUTE, FINAL2)
while temp[0] != temp[1]:
    NB_2OPT += 1
    APRES_INTRA_ROUTE = copie(FINAL2)
    deux_opt(FINAL2)
    temp = distance_comparaison(DEPOT, CLIENTS, APRES_INTRA_ROUTE, FINAL2)
    dessin(APRES_INTRA_ROUTE)