from matplotlib.pyplot import axis, grid, show, plot, scatter
from numpy import sqrt
from random import randint
from copy import deepcopy


DEPOT = [0, 0]

# CLIENTS - Belle configuration

# CLIENTS = [[-80, -25], [37, 62], [-100, -41], [0, -53], [-47, -46],
     #      [-89, 58], [85, 27], [-71, 93], [62, -85], [-45, -27]]

# CLIENTS - CAS A ETUDIER

# CLIENTS = [[20, 0], [-16, -12], [16, -12]]

# CLIENTS demi-plan

# CLIENTS = [[73, -50], [64, 99], [77, 90], [88, 32], [69, -62], [38, -57], [31, 0],
# [76, 70], [52, -35], [75, -70], [39, 90], [37, -86], [40, -1], [75, 1], [7, -50]]


def creer_client_alea(n=10):
    CLIENTS = []
    for _ in range(n):
        CLIENTS.append([randint(-100, 100), randint(-100, 100)])
    return CLIENTS


CLIENTS = creer_client_alea()


def copie(liste):
    liste2 = deepcopy(liste)
    return liste2


def distance(i, j):
    return sqrt((j[1]-i[1])**2+(j[0]-i[0])**2)


# Construction de la liste des "savings" pour chaque couple de points
def savings(DEPOT=DEPOT, CLIENTS=CLIENTS):
    list_savings = []
    client_savings = []
    temp = []
    temp2 = []
    for i in range(0, len(CLIENTS)-1):
        for j in range(i+1, len(CLIENTS)):
            temp.append((round(distance(
                CLIENTS[i], DEPOT)+distance(CLIENTS[j], DEPOT)-distance(CLIENTS[i], CLIENTS[j]), 2)))
            temp2.append((i+1, j+1))
        list_savings.append(temp)
        client_savings.append(temp2)
        temp = []
        temp2 = []
    return (list_savings, client_savings)
print(savings()[0])

# Creer les routes D-i-D
def create_routes(DEPOT=DEPOT, CLIENTS=CLIENTS):
    list_route = []
    for i in range(len(CLIENTS)):
        list_route.append([0, i+1, 0])
    return list_route


def joindre_tableaux(res=savings()):
    list_savings = res[0]
    client_savings = res[1]
    new_l_s = []
    new_c_s = []
    for i in range(len(list_savings)):
        for j in range(len(list_savings[i])):
            new_l_s.append(list_savings[i][j])
            new_c_s.append(client_savings[i][j])
    return (new_l_s, new_c_s)


# Trier les savings afin d'en retirer les benefices les plus eleves
def order_list(x=joindre_tableaux()):
    list_savings = x[0]
    client_savings = x[1]
    for i in range(len(list_savings)):
        for j in range(i, len(list_savings)):
            if list_savings[j] > list_savings[i]:
                (list_savings[i], list_savings[j]) = (
                    list_savings[j], list_savings[i])
                (client_savings[i], client_savings[j]) = (
                    client_savings[j], client_savings[i])
    return (list_savings, client_savings)


ROUTES = create_routes()
SAVINGS = order_list()


# Forme les routes en prenant en compte les benefices
def merge_routes(ROUTE=ROUTES, list_savings=SAVINGS[0], client_savings=SAVINGS[1]):
    temp = 0
    for i in range(len(list_savings)):
        for j in range(len(ROUTE)):
            if ROUTE[j][0] == 0 and ROUTE[j][1] == client_savings[i][1]:
                for k in range(len(ROUTE)):
                    if ROUTE[k][1] == client_savings[i][0] and ROUTE[j][2] == 0:
                        _ = ROUTE[k].pop()
                        ROUTE[k].append(client_savings[i][1])
                        ROUTE[k].append(0)
                        ROUTE.remove(ROUTE[j])
                        temp = 1
                        break
            if temp == 1:
                temp = 0
                break
    return ROUTE


ROUTES = merge_routes()
FINAL = copie(ROUTES)


# 2_opt pour regler les problemes de croisements
def deux_opt(routes=FINAL):
    continuer = True
    while continuer:
        continuer = False
        for route in routes:
            if len(route) > 4:
                for i in range(len(route)-1):
                    for j in range(len(route)-1):
                        if j != i and j != i-1 and j != i+1:
                            if route[i] == 0:
                                if distance(DEPOT, CLIENTS[route[i+1]-1]) + distance(CLIENTS[route[j]-1], CLIENTS[route[j+1]-1]) > distance(DEPOT, CLIENTS[route[j]-1]) + distance(CLIENTS[route[i+1]-1], CLIENTS[route[j+1]-1]):
                                    (route[i+1], route[j]
                                     ) = (route[j], route[i+1])
                                    continuer = True
                            elif route[j] == 0:
                                if distance(CLIENTS[route[i]-1], CLIENTS[route[i+1]-1]) + distance(DEPOT, CLIENTS[route[j+1]-1]) > distance(CLIENTS[route[i]-1], DEPOT) + distance(CLIENTS[route[i+1]-1], CLIENTS[route[j+1]-1]):
                                    (route[i], route[j+1]
                                     ) = (route[j+1], route[i])
                                    continuer = True
                            elif distance(CLIENTS[route[i]-1], CLIENTS[route[i+1]-1]) + distance(CLIENTS[route[j]-1], CLIENTS[route[j+1]-1]) > distance(CLIENTS[route[i]-1], CLIENTS[route[j]-1]) + distance(CLIENTS[route[i+1]-1], CLIENTS[route[j+1]-1]):
                                (route[i+1], route[j]) = (route[j], route[i+1])
                                continuer = True

    return routes


def dessin(chemin=FINAL):
    X = [CLIENTS[i][0] for i in range(len(CLIENTS))]
    Y = [CLIENTS[i][1] for i in range(len(CLIENTS))]
    scatter(X, Y, color=(0.15, 0.15, 0.9))
    scatter(DEPOT[0], DEPOT[1], color=(0.9, 0.15, 0.15))
    for i in chemin:
        X = [0]
        Y = [0]
        for j in range(1, len(i)-1):
            X.append(CLIENTS[i[j]-1][0])
            Y.append(CLIENTS[i[j]-1][1])
        X.append(0)
        Y.append(0)
        plot(X, Y)
    show()


deux_opt()


def distance_comparaison(DEPOT=DEPOT, CLIENTS=CLIENTS, ROUTE_AVANT=ROUTES, ROUTE_APRES=FINAL):
    d1 = 0
    d2 = 0
    for j in ROUTE_AVANT:
        for k in range(len(j)-1):
            if j[k] == 0:
                d1 += distance(DEPOT, CLIENTS[j[k+1]-1])
            elif j[k+1] == 0:
                d1 += distance(CLIENTS[j[k]-1], DEPOT)
            else:
                d1 += distance(CLIENTS[j[k]-1], CLIENTS[j[k+1]-1])
    for j in ROUTE_APRES:
        for k in range(len(j)-1):
            if j[k] == 0:
                d2 += distance(DEPOT, CLIENTS[j[k+1]-1])
            elif j[k+1] == 0:
                d2 += distance(CLIENTS[j[k]-1], DEPOT)
            else:
                d2 += distance(CLIENTS[j[k]-1], CLIENTS[j[k+1]-1])
    return (d1, d2)


dessin(ROUTES)
dessin()
print(distance_comparaison())