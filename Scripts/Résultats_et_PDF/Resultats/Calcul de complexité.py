
from matplotlib.pyplot import axis, grid, show, plot, scatter
from numpy import sqrt, linspace, exp
from random import randint
from time import time
from copy import deepcopy


DEPOT = [0, 0]
MOY = []


def main(n):

    if n == 51:
        scatter([x for x in range(len(MOY))], MOY)
        x = linspace(0, n-1, 100)
        plot([y for y in x], [y**4/13500000 for y in x])
        plot([y for y in x], [y**3/100000 for y in x])
        plot([y for y in x], [y**5/500000000 for y in x])
        show()

    def creer_client_alea(n):
        CLIENTS = []
        for _ in range(n):
            CLIENTS.append([randint(-100, 100), randint(-100, 100)])
        return CLIENTS

    CLIENTS = creer_client_alea(n)

    T = []

    for count in range(2):

        t = time()
        temps = 0

        def copie(liste):
            liste2 = deepcopy(liste)
            return liste2

        def distance(i, j):
            return sqrt((j[1]-i[1])**2+(j[0]-i[0])**2)

        # Savings construit la liste des "savings" pour chaque couple de points

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

        # 2_opt pour regler les problemes de croisements

        ROUTES = merge_routes()
        FINAL = copie(ROUTES)

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
                                        (route[i+1], route[j]
                                         ) = (route[j], route[i+1])
                                        continuer = True

            return routes
        FINAL = deux_opt()

        temps = time() - t
        T.append(temps)

    if n <= 50:
        x = 0
        for i in T:
            x += i
        MOY.append(x/len(T))
        print(len(MOY))
        main(n+1)


main(1)
