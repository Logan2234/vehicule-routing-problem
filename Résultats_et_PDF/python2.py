def copie(liste):
    return deepcopy(liste)

def distance(i, j):
    return ((j[1]-i[1])**2+(j[0]-i[0])**2)**(1/2)

# Utile pour l'implementation d'un operateur inter-routes
def distance_matrix(CLIENTS=CLIENTS):
    res = [[0 for i in range(len(CLIENTS))] for j in range(len(CLIENTS))]
    for i in range(len(CLIENTS)-1):
        for j in range(i+1, len(CLIENTS)):
            res[i][j] = round(distance(CLIENTS[i], CLIENTS[j]), 2)
    return res

distance_clients = distance_matrix()