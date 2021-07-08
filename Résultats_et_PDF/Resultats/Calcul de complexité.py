from matplotlib.pyplot import axis, grid, show, plot, scatter, clf
from numpy import sqrt, linspace, exp
from random import randint
from time import time
from copy import deepcopy


DEPOT = [0, 0]
MOY = []
NB_2OPT_LIST_MOY = []
NB_INTER_LIST_MOY = []


def main(n,max_client,mode="p",nb=10):

    def creer_client_alea(n):
        CLIENTS = []
        for _ in range(n):
            CLIENTS.append([randint(-100, 100), randint(-100, 100)])
        return CLIENTS

    N = []
    T = []
    NB_2OPT_LIST = []
    NB_INTER_LIST = []
    G1 = []
    G2 = []

    for _ in range(nb):

        NB_INTER = 0
        NB_2OPT = 0
        t = time()
        CLIENTS = creer_client_alea(n)

        def copie(liste):
            liste2 = deepcopy(liste)
            return liste2


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


        # Construction de la liste des "savings" pour chaque couple de points
        def savings(DEPOT=DEPOT, CLIENTS=CLIENTS):
            list_savings = []
            client_savings = []
            temp = []
            temp2 = []
            for i in range(0, len(CLIENTS)-1):
                for j in range(i+1, len(CLIENTS)):
                    temp.append((round(distance(CLIENTS[i], DEPOT)+distance(CLIENTS[j], DEPOT)-distance(
                        CLIENTS[i], CLIENTS[j])+0*abs(distance(CLIENTS[i], DEPOT)-distance(CLIENTS[j], DEPOT)), 2)))
                    temp2.append((i+1, j+1))
                list_savings.append(temp)
                client_savings.append(temp2)
                temp = []
                temp2 = []
            return (list_savings, client_savings)


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
        APRES_INTRA_ROUTE = copie(ROUTES)


        # 2_opt pour regler les problemes de croisements intra-routes
        def deux_opt(routes=APRES_INTRA_ROUTE):
            for route in routes:
                if len(route) > 4:
                    for i in range(len(route)-1):
                        for j in range(len(route)-1):
                            if j != i and j != i-1 and j != i+1:
                                if route[i] == 0 and route[j+1] == 0:
                                    if distance(DEPOT, CLIENTS[route[i+1]-1]) + distance(CLIENTS[route[j]-1], DEPOT) > distance(DEPOT, CLIENTS[route[j]-1]) + distance(CLIENTS[route[i+1]-1], DEPOT):
                                        (route[i+1], route[j]) = (route[j], route[i+1])
                                elif route[i+1] == 0 and route[j] == 0:
                                    if distance(CLIENTS[route[i]-1], DEPOT) + distance(DEPOT, CLIENTS[route[j+1]-1]) > distance(CLIENTS[route[i]-1], DEPOT) + distance(DEPOT, CLIENTS[route[j+1]-1]):
                                        (route[i], route[j+1]) = (route[j+1], route[i])
                                elif route[i] == 0:
                                    if distance(DEPOT, CLIENTS[route[i+1]-1]) + distance(CLIENTS[route[j]-1], CLIENTS[route[j+1]-1]) > distance(DEPOT, CLIENTS[route[j]-1]) + distance(CLIENTS[route[i+1]-1], CLIENTS[route[j+1]-1]):
                                        (route[i+1], route[j]) = (route[j], route[i+1])
                                elif route[j] == 0:
                                    if distance(CLIENTS[route[i]-1], CLIENTS[route[i+1]-1]) + distance(DEPOT, CLIENTS[route[j+1]-1]) > distance(CLIENTS[route[i]-1], DEPOT) + distance(CLIENTS[route[i+1]-1], CLIENTS[route[j+1]-1]):
                                        (route[i], route[j+1]) = (route[j+1], route[i])
                                elif route[i+1] == 0:
                                    if distance(CLIENTS[route[i]-1], DEPOT) + distance(CLIENTS[route[j]-1], CLIENTS[route[j+1]-1]) > distance(CLIENTS[route[i]-1], CLIENTS[route[j]-1]) + distance(DEPOT, CLIENTS[route[j+1]-1]):
                                        (route[i], route[j+1]) = (route[j+1], route[i])
                                elif route[j+1] == 0:
                                    if distance(CLIENTS[route[i]-1], CLIENTS[route[i+1]-1]) + distance(CLIENTS[route[j]-1], DEPOT) > distance(CLIENTS[route[i]-1], CLIENTS[route[j]-1]) + distance(CLIENTS[route[i+1]-1], DEPOT):
                                        (route[i+1], route[j]) = (route[j], route[i+1])
                                elif distance(CLIENTS[route[i]-1], CLIENTS[route[i+1]-1]) + distance(CLIENTS[route[j]-1], CLIENTS[route[j+1]-1]) > distance(CLIENTS[route[i]-1], CLIENTS[route[j]-1]) + distance(CLIENTS[route[i+1]-1], CLIENTS[route[j+1]-1]):
                                    (route[i+1], route[j]) = (route[j], route[i+1])


        def distance_comparaison(DEPOT=DEPOT, CLIENTS=CLIENTS, ROUTE_AVANT=ROUTES, ROUTE_APRES=APRES_INTRA_ROUTE):
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
            return (round(d1, 2), round(d2, 2))


        def inter_route(CLIENTS=CLIENTS, routes=APRES_INTRA_ROUTE, distance_matrix=distance_clients, NB_INTER = NB_INTER):
            def plus_proche_par_route(num_client, route, CLIENTS=CLIENTS):
                res = route[1]
                for i in range(2, len(route)-1):
                    if distance(CLIENTS[num_client-1], CLIENTS[res-1]) >= distance(CLIENTS[route[i]-1], CLIENTS[res-1]):
                        res = route[i]
                return res
            while 1:
                res_intermediaire = []
                for route in routes:
                    for point in route[1:-1]:
                        dist_par_routes = []
                        for route2 in routes:
                            dist_par_routes.append((plus_proche_par_route(point, route2), routes.index(route2)))
                        res_intermediaire.append(((point, routes.index(route)), dist_par_routes))
                res_distance = [] # Pour stocker (point, route) qui est le plus proche de (point2, route2) et donne la valeur de distance
                for optim in res_intermediaire:
                    for i in optim[1]:
                        if optim[0] != i:
                            res_distance.append((optim[0], i))
                dist_optimised = []
                for i in res_distance:
                    routes_temp = copie(routes)
                    d1 = distance_comparaison()[1]
                    routes_temp[i[1][1]].insert(routes_temp[i[1][1]].index(i[1][0])+1, i[0][0])
                    routes_temp[i[0][1]].remove(i[0][0])
                    d2 = distance_comparaison(DEPOT, CLIENTS, ROUTES, routes_temp)[1]
                    dist_optimised.append((res_distance.index(i), round(d1-d2, 2)))
                if dist_optimised ==[]:
                    break
                maxi = dist_optimised[0]

                for i in range(1, len(dist_optimised)): # Tri par valeur d'optimisation
                    if dist_optimised[i][1] > maxi[1]:
                        maxi = dist_optimised[i]
                    # valeur = dist_optimised[i]
                    # j = i
                    # while j > 0 and dist_optimised[j-1][1] < valeur[1]:
                    #     dist_optimised[j] = dist_optimised[j-1]
                    #     j -= 1
                    # dist_optimised[j] = valeur
                if len(dist_optimised) > 0 and maxi[1] > 0:
                    NB_INTER += 1
                    routes[res_distance[maxi[0]][1][1]].insert(routes[res_distance[maxi[0]][1][1]].index(res_distance[maxi[0]][1][0])+1, res_distance[maxi[0]][0][0])
                    routes[res_distance[maxi[0]][0][1]].remove(res_distance[maxi[0]][0][0])
                    # dessin(routes)
                else:
                    break
            return NB_INTER


        # Appel de l'opérateur inter-routes
        NB_INTER = inter_route()
        distance1 = distance_comparaison(DEPOT, CLIENTS, ROUTES, APRES_INTRA_ROUTE)

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

        N.append(n)

        if mode != "g":
            temps = time() - t
            T.append(temps)
            NB_INTER_LIST.append(NB_INTER)
            NB_2OPT_LIST.append(NB_2OPT)

        else:
            distance2 = distance_comparaison(DEPOT, CLIENTS, ROUTES, APRES_INTRA_ROUTE)
            gain1 = round(1-distance1[1]/distance1[0],2)*100
            gain2 = round(1-distance2[1]/distance2[0],2)*100
            G1.append(gain1)
            G2.append(gain2)

    if mode == "p":
        x = 0
        for i in T:
            x += i
        MOY.append(x/len(T))
        print(len(MOY))
        y = 0
        for i in NB_INTER_LIST:
            y += i
        NB_INTER_LIST_MOY.append(y/len(NB_INTER_LIST))
        z = 0
        for i in NB_2OPT_LIST:
            z += i
        NB_2OPT_LIST_MOY.append(z/len(NB_2OPT_LIST))

    elif mode == "p" and n == max_client+1:
        print(MOY)
        scatter([x for x in range(len(MOY))], MOY)
        show()
        clf()
        print(NB_INTER_LIST_MOY)
        scatter([x for x in range(len(NB_INTER_LIST_MOY))], NB_INTER_LIST_MOY)
        show()
        clf()
        print(NB_2OPT_LIST_MOY)
        scatter([x for x in range(len(NB_2OPT_LIST_MOY))], NB_2OPT_LIST_MOY)
        show()
        clf()

    elif mode == "w":
        fichier = open("results2.txt","a")
        for i in range(len(T)):
            fichier.write(str(N[i]) + "," + str(T[i]) + "," + str(NB_INTER_LIST[i]) + "," + str(NB_2OPT_LIST[i]) + "\n")
        fichier.close()
        print("n = " + str(n) + " fait")

    elif mode == "g":
        fichier = open("gains.txt","a")
        for i in range(len(G1)):
            fichier.write(str(N[i]) + "," + str(G1[i]) + "," + str(G2[i]) + "\n")
        fichier.close()
        print("n = " + str(n) + " fait")

    if n < max_client:
        main(n+1,max_client,mode,nb)