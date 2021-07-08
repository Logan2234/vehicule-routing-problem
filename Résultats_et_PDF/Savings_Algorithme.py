from copy import deepcopy
from random import randint
from time import time

from matplotlib.pyplot import show, plot, scatter

t = time()

DEPOT = [0, 0]
NB_INTER = 0
NB_2OPT = 0

# ETUDE POUR RECHERCHE INTER-ROUTES
# CLIENTS = [[10, 82], [87, -42], [36, 86], [58, -82], [83, -71], [28, 29]]

# Belle configuration
# CLIENTS = [[-80, -25], [37, 62], [-100, -41], [0, -53], [-47, -46],
# [-89, 58], [85, 27], [-71, 93], [62, -85], [-45, -27]]

# CAS OU LE 2OPT EST EXECUTE 4 ®FOIS
# CLIENTS = [[12, -72], [0, -48], [82, -79], [-42, 5], [-94, -95], [14, -26], [-3, -78]]

# Demi-plan
# CLIENTS = [[73, -50], [64, 99], [77, 90], [88, 32], [69, -62], [38, -57], [31, 0], [76, 70], [52, -35], [75, -70], [39, 90], [37, -86], [40, -1], [75, 1], [7, -50]]

# CLIENTS = [[86, 22], [29, 17], [4, 50], [25, 13], [67, 37], [13, 7], [62, 15], [84, 38], [34, 3],
# [19, 45], [42, 76], [40, 86], [25, 94], [63, 57], [75, 24], [61, 85], [87, 38], [54, 39], [66, 34],
# [46, 39], [47, 17], [21, 54], [19, 83], [1, 82], [94, 28], [82, 72], [41, 59], [100, 77], [1, 57],
# [96, 7], [57, 82], [47, 38], [68, 89], [16, 36], [51, 38], [83, 74], [84, 2]]

# CLIENTS = [[44, -96], [-49, -57], [56, -48], [14, -55], [-97, -86], [-74, 90], [-54, -25], [36, 64], [-56, 81],
# [-26, 32], [-47, 9], [90, -83], [-58, -82], [78, -12], [-97, -73], [-67, 82], [12, -46], [52, -12], [-36, 35]]

# CLIENTS = [
# [-5, 10],    # location 1
# [10,10],    # location 2
# [-10,7.5],     # location 3
# [-7.5,7.5],   # location 4
# [2.5,5],  # location 5
# [7.5,5],  # location 6
# [-2.5,2.5],  # location 7
# [5,2.5],  # location 8
# [2.5,-2.5],  # location 9
# [10,-2.5],  # location 10
# [-7.5,-5],  # location 11
# [-5,-5],  # location 12
# [-2.5,-7.5],  # location 13
# [5,-7.5],  # location 14
# [-10,-10],    # location 15
# [7.5,-10]]  # location 16


# Cas où un petit zigouigoui reste parce qu'on élimine tous les points trop loins dans l'opérateur inter-route quand on compare aux autres routes
# CLIENTS = [[-5, -2], [-6, 21], [-56, 91], [-99, -19], [78, -12], [-45, -78], [28, -78], [-4, -64], [98, 76], [37, -50], [16, -15], [98, 55], [-5, 97], [24, 44], [-83, -64]]

# Instances A-n32k5
# DEPOT = [82, 76]
# CLIENTS = [[96, 44],
#            [50, 5],
#            [49, 8],
#            [13, 7],
#            [29, 89],
#            [58, 30],
#            [84, 39],
#            [14, 24],
#            [2, 39],
#            [3, 82],
#            [5, 10],
#            [98, 52],
#            [84, 25],
#            [61, 59],
#            [1, 65],
#            [88, 51],
#            [91, 2],
#            [19, 32],
#            [93, 3],
#            [50, 93],
#            [98, 14],
#            [5, 42],
#            [42, 9],
#            [61, 62],
#            [9, 97],
#            [80, 55],
#            [57, 69],
#            [23, 15],
#            [20, 70],
#            [85, 60],
#            [98, 5]]


# CLIENTS = [[35, -98], [90, -70], [10, -69], [60, -65]]
#
# A - n33 - k5
# DEPOT = [42, 68]
# CLIENTS = [77, 97], [28, 64], [77, 39], [32, 33], [32, 8], [42, 92], [8, 3], [7, 14], [82, 17], [48, 13], [53, 82], [39,
#                                                                                                                      27], [
#               7, 24], [67, 98], [54, 52], [72, 43], [73, 3], [59, 77], [58, 97], [23, 43], [68, 98], [47, 62], [52,
#                                                                                                                 72], [
#               32, 88], [39, 7], [17, 8], [38, 7], [58, 74], [82, 67], [42, 7], [68, 82], [7, 48]
#
# A - n80 - k10
# DEPOT = [92, 92]
# CLIENTS = [88, 58], [70, 6], [57, 59], [0, 98], [61, 38], [65, 22], [91, 52], [59, 2], [3, 54], [95, 38], [80, 28], [66,
#                                                                                                                      42], [
#               79, 74], [99, 25], [20, 43], [40, 3], [50, 42], [97, 0], [21, 19], [36, 21], [100, 61], [11, 85], [69,
#                                                                                                                  35], [
#               69, 22], [29, 35], [14, 9], [50, 33], [89, 17], [57, 44], [60, 25], [48, 42], [17, 93], [21, 50], [77,
#                                                                                                                  18], [
#               2, 4], [63, 83], [68, 6], [41, 95], [48, 54], [98, 73], [26, 38], [69, 76], [40, 1], [65, 41], [14, 86], [
#               32, 39], [14, 24], [96, 5], [82, 98], [23, 85], [63, 69], [87, 19], [56, 75], [15, 63], [10, 45], [7,
#                                                                                                                  30], [
#               31, 11], [36, 93], [50, 31], [49, 52], [39, 10], [76, 40], [83, 34], [33, 51], [0, 15], [52, 82], [52,
#                                                                                                                  82], [
#               46, 6], [3, 26], [46, 80], [94, 30], [26, 76], [75, 92], [57, 51], [34, 21], [28, 80], [59, 66], [51,
#                                                                                                                 16], [
#               87, 11]


def creer_client_alea(n=10):
    clients = []
    for _ in range(n):
        clients.append([randint(-100, 100), randint(-100, 100)])
    return clients


CLIENTS = creer_client_alea(20)

print(CLIENTS)


# CLIENTS = [[65, 18], [-7, 53], [25, 31], [35, -87], [-6, -71], [-69, -71], [-57, 100], [-98, 52], [15, 48], [93, 5],
#            [24, -62], [-92, 12], [-31, 84], [-45, -51], [21, 69], [-100, -8], [-18, -16], [-6, 91], [-36, -2], [9, 1],
#            [35, -52], [60, -59], [-50, -24], [70, -37], [81, -100], [9, -12], [-7, 30], [-21, -80], [-77, -64],
#            [-50, 98], [-81, -18], [-23, -1], [57, 79], [32, -77], [-74, -70], [33, -84], [-26, 44], [-33, -60], [49, 4],
#            [20, 82], [-55, -17], [55, 12], [60, 39], [-58, 61], [60, -5], [35, 50], [-23, 99], [-85, 92], [-54, -16],
#            [-98, 51], [-16, 23], [-100, -56], [-2, -45], [4, 41], [-32, -38], [76, -63], [-32, -84], [35, 51],
#            [24, -39], [-19, 28], [-35, -37], [-80, -48], [-80, 34], [-95, 25], [-18, -53], [40, -31], [61, 22],
#            [98, 88], [-57, 31], [-45, 78]]


def copie(liste):
    return deepcopy(liste)


def distance(i, j):
    return ((j[1] - i[1]) ** 2 + (j[0] - i[0]) ** 2) ** (1 / 2)


# Construction de la liste des "savings" pour chaque couple de points
def savings(depot=DEPOT, clients=CLIENTS):
    list_savings = []
    client_savings = []
    tempo = []
    temp2 = []
    for i in range(0, len(clients) - 1):
        for j in range(i + 1, len(clients)):
            tempo.append((round(distance(clients[i], depot) + distance(clients[j], depot) - distance(
                clients[i], clients[j]) + 0 * abs(distance(clients[i], depot) - distance(clients[j], depot)), 2)))
            temp2.append((i + 1, j + 1))
        list_savings.append(tempo)
        client_savings.append(temp2)
        tempo = []
        temp2 = []
    return list_savings, client_savings


# Créer les routes D-i-D
def create_routes(clients=CLIENTS):
    list_route = []
    for i in range(len(clients)):
        list_route.append([0, i + 1, 0])
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
    return new_l_s, new_c_s


# Trier les savings afin d'en retirer les benefices les plus élèves
def order_list(x=joindre_tableaux()):
    list_savings = x[0]
    client_savings = x[1]
    for i in range(len(list_savings)):
        for j in range(i, len(list_savings)):
            if list_savings[j] > list_savings[i]:
                (list_savings[i], list_savings[j]) = (list_savings[j], list_savings[i])
                (client_savings[i], client_savings[j]) = (client_savings[j], client_savings[i])
    return list_savings, client_savings


ROUTES = create_routes()
SAVINGS = order_list()


# Forme les routes en prenant en compte les benefices
def merge_routes(route=ROUTES, list_savings=SAVINGS[0], client_savings=SAVINGS[1]):
    tempo = 0
    for i in range(len(list_savings)):
        for j in range(len(route)):
            if route[j][0] == 0 and route[j][1] == client_savings[i][1]:
                for k in range(len(route)):
                    if route[k][1] == client_savings[i][0] and route[j][2] == 0:
                        _ = route[k].pop()
                        route[k].append(client_savings[i][1])
                        route[k].append(0)
                        route.remove(route[j])
                        tempo = 1
                        break
            if tempo == 1:
                tempo = 0
                break
    return route


ROUTES = merge_routes()
APRES_INTRA_ROUTE = copie(ROUTES)


# 2_opt pour régler les problèmes de croisements intra-routes
def deux_opt(routes=APRES_INTRA_ROUTE, depot=DEPOT):
    for route in routes:
        if len(route) > 4:
            for i in range(len(route) - 1):
                for j in range(len(route) - 1):
                    if j != i and j != i - 1 and j != i + 1:
                        if route[i] == 0 and route[j + 1] == 0:
                            if distance(depot, CLIENTS[route[i + 1] - 1]) + distance(CLIENTS[route[j] - 1], depot) > distance(depot, CLIENTS[route[j] - 1]) + distance(CLIENTS[route[i + 1] - 1], depot):
                                (route[i + 1], route[j]) = (route[j], route[i + 1])
                        elif route[i + 1] == 0 and route[j] == 0:
                            if distance(CLIENTS[route[i] - 1], depot) + distance(depot, CLIENTS[route[j + 1] - 1]) > distance(CLIENTS[route[i] - 1], depot) + distance(depot, CLIENTS[route[j + 1] - 1]):
                                (route[i], route[j + 1]) = (route[j + 1], route[i])
                        elif route[i] == 0:
                            if distance(depot, CLIENTS[route[i + 1] - 1]) + distance(CLIENTS[route[j] - 1], CLIENTS[route[j + 1] - 1]) > distance(depot, CLIENTS[route[j] - 1]) + distance(CLIENTS[route[i + 1] - 1], CLIENTS[route[j + 1] - 1]):
                                (route[i + 1], route[j]) = (route[j], route[i + 1])
                        elif route[j] == 0:
                            if distance(CLIENTS[route[i] - 1], CLIENTS[route[i + 1] - 1]) + distance(depot, CLIENTS[route[j + 1] - 1]) > distance(CLIENTS[route[i] - 1], depot) + distance(CLIENTS[route[i + 1] - 1], CLIENTS[route[j + 1] - 1]):
                                (route[i], route[j + 1]) = (route[j + 1], route[i])
                        elif route[i + 1] == 0:
                            if distance(CLIENTS[route[i] - 1], depot) + distance(CLIENTS[route[j] - 1], CLIENTS[route[j + 1] - 1]) > distance(CLIENTS[route[i] - 1], CLIENTS[route[j] - 1]) + distance(depot, CLIENTS[route[j + 1] - 1]):
                                (route[i], route[j + 1]) = (route[j + 1], route[i])
                        elif route[j + 1] == 0:
                            if distance(CLIENTS[route[i] - 1], CLIENTS[route[i + 1] - 1]) + distance(CLIENTS[route[j] - 1], depot) > distance(CLIENTS[route[i] - 1], CLIENTS[route[j] - 1]) + distance(CLIENTS[route[i + 1] - 1], depot):
                                (route[i + 1], route[j]) = (route[j], route[i + 1])
                        elif distance(CLIENTS[route[i] - 1], CLIENTS[route[i + 1] - 1]) + distance(CLIENTS[route[j] - 1], CLIENTS[route[j + 1] - 1]) > distance(CLIENTS[route[i] - 1], CLIENTS[route[j] - 1]) + distance(CLIENTS[route[i + 1] - 1], CLIENTS[route[j + 1] - 1]):
                            (route[i + 1], route[j]) = (route[j], route[i + 1])


def distance_comparaison(depot=DEPOT, clients=CLIENTS, route_avant=ROUTES, route_apres=APRES_INTRA_ROUTE):
    def distance_constructor(client,  route):
        d = 0
        for j in route:
            for k in range(len(j) - 1):
                if j[k] == 0:
                    d += distance(depot, client[j[k + 1] - 1])
                elif j[k + 1] == 0:
                    d += distance(client[j[k] - 1], depot)
                else:
                    d += distance(client[j[k] - 1], client[j[k + 1] - 1])
        return d
    d1 = distance_constructor(clients, route_avant)
    d2 = distance_constructor(clients, route_apres)
    return round(d1, 2), round(d2, 2)


def inter_route(clients=CLIENTS, routes=APRES_INTRA_ROUTE, nb_inter=NB_INTER):
    def plus_proche_par_route(num_client, road):
        res = road[1]
        for customer in range(2, len(road) - 1):
            if distance(clients[num_client - 1], clients[res - 1]) >= distance(clients[road[customer] - 1], clients[res - 1]):
                res = road[customer]
        return res

    while 1:
        res_intermediaire = []
        for route in routes:
            for point in route[1:-1]:
                dist_par_routes = []
                for route2 in routes:
                    dist_par_routes.append((plus_proche_par_route(point, route2), routes.index(route2)))
                res_intermediaire.append(((point, routes.index(route)), dist_par_routes))
        res_distance = []  # Pour stocker (point, route) qui est le plus proche de (point2, route2) et donne la valeur de distance
        for optim in res_intermediaire:
            for i in optim[1]:
                if optim[0] != i:
                    res_distance.append((optim[0], i))
        dist_optimised = []
        for i in res_distance:
            routes_temp = copie(routes)
            d1 = distance_comparaison()[1]
            routes_temp[i[1][1]].insert(routes_temp[i[1][1]].index(i[1][0]) + 1, i[0][0])
            routes_temp[i[0][1]].remove(i[0][0])
            d2 = distance_comparaison(DEPOT, clients, ROUTES, routes_temp)[1]
            dist_optimised.append((res_distance.index(i), round(d1 - d2, 2)))
        if dist_optimised:
            maxi = dist_optimised[0]
        for i in range(1, len(dist_optimised)):  # Tri par valeur d'optimisation
            if dist_optimised[i][1] > maxi[1]:
                maxi = dist_optimised[i]
        if len(dist_optimised) > 0 and maxi[1] > 0:
            nb_inter += 1
            routes[res_distance[maxi[0]][1][1]].insert(
                routes[res_distance[maxi[0]][1][1]].index(res_distance[maxi[0]][1][0]) + 1, res_distance[maxi[0]][0][0])
            routes[res_distance[maxi[0]][0][1]].remove(res_distance[maxi[0]][0][0])
        else:
            break
    return nb_inter


def dessin(chemin):
    x = [CLIENTS[i][0] for i in range(len(CLIENTS))]
    y = [CLIENTS[i][1] for i in range(len(CLIENTS))]
    scatter(x, y, color=(0.15, 0.15, 0.9))
    scatter(DEPOT[0], DEPOT[1], color=(0.9, 0.15, 0.15))
    for i in chemin:
        x = [DEPOT[0]]
        y = [DEPOT[1]]
        for j in range(1, len(i) - 1):
            x.append(CLIENTS[i[j] - 1][0])
            y.append(CLIENTS[i[j] - 1][1])
        x.append(DEPOT[0])
        y.append(DEPOT[1])
        plot(x, y)
    show()


# Affichage de la disposition après Clarke & Wright
dessin(ROUTES)

# Appel de l'opérateur inter-route
NB_INTER = inter_route()
print("APRES_INTRA_ROUTE = " + str(APRES_INTRA_ROUTE))
dessin(APRES_INTRA_ROUTE)
distance1 = distance_comparaison(DEPOT, CLIENTS, ROUTES, APRES_INTRA_ROUTE)
print("Apres inter-route: " + str(distance1))

# Appel de l'opérateur intra-routes...
FINAL2 = copie(APRES_INTRA_ROUTE)
deux_opt(FINAL2)

# ... autant de fois qu'il est nécessaire
temp = distance_comparaison(DEPOT, CLIENTS, APRES_INTRA_ROUTE, FINAL2)
while temp[0] != temp[1]:
    NB_2OPT += 1
    APRES_INTRA_ROUTE = copie(FINAL2)
    deux_opt(FINAL2)
    temp = distance_comparaison(DEPOT, CLIENTS, APRES_INTRA_ROUTE, FINAL2)
    dessin(APRES_INTRA_ROUTE)

distance2 = distance_comparaison(DEPOT, CLIENTS, ROUTES, APRES_INTRA_ROUTE)
print("Apres tous les 2opt : " + str(distance2))

print("Nombre de 2opt : " + str(NB_2OPT))
print("Nombre de inter-route : " + str(NB_INTER))

gain1 = round(1 - distance1[1] / distance1[0], 2) * 100
gain2 = round(1 - distance2[1] / distance2[0], 2) * 100

print("Gain après l'opérateur inter-route : " + str(gain1) + "%\nGain après l'opérateur 2-opt : " + str(gain2) + "%")
