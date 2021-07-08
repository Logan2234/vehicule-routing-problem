def distance_comparaison(D=DEPOT,C=CLIENTS,R_AV=ROUTES,R_AP=APRES_INTRA_ROUTE):
    d1 = 0
    d2 = 0
    for j in R_AV:
        for k in range(len(j)-1):
            if j[k] == 0:
                d1 += distance(D, C[j[k+1]-1])
            elif j[k+1] == 0:
                d1 += distance(C[j[k]-1], D)
            else:
                d1 += distance(C[j[k]-1], C[j[k+1]-1])
    for j in R_AP:
        for k in range(len(j)-1):
            if j[k] == 0:
                d2 += distance(D, C[j[k+1]-1])
            elif j[k+1] == 0:
                d2 += distance(C[j[k]-1], D)
            else:
                d2 += distance(C[j[k]-1], C[j[k+1]-1])
    return (round(d1, 2), round(d2, 2))