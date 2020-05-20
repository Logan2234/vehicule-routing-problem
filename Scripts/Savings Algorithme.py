from matplotlib.pyplot import axis, grid, show, plot, scatter
from numpy import sqrt
from random import randint

DEPOT = [0,0]
CLIENTS = [[-80, -25], [37, 62], [-100, -41], [33, -53], [-47, -46], [-89, 58], [85, 27], [-71, 93], [62, -85], [-45, -27]]

def creer_client_alea(n=10):
    CLIENTS = []
    for _ in range(n):
        CLIENTS.append([randint(-100,100),randint(-100,100)])
    return CLIENTS

# CLIENTS = creer_client_alea()

def distance(i,j):
    return sqrt((j[1]-i[1])**2+(j[0]-i[0])**2)

    # Savings construit la liste des "savings" pour chaque couple de points

def savings(DEPOT = DEPOT, CLIENTS = CLIENTS):
    list_savings = []
    client_savings = []
    temp = []
    temp2 = []
    for i in range(0, len(CLIENTS)-1):
        for j in range(i+1,len(CLIENTS)):
            temp.append((round(distance(CLIENTS[i],DEPOT)+distance(CLIENTS[j],DEPOT)-distance(CLIENTS[i],CLIENTS[j]),2)))
            temp2.append((i+1,j+1))
        list_savings.append(temp)
        client_savings.append(temp2)
        temp = [] ; temp2 = []
    return (list_savings,client_savings)

def create_routes(DEPOT = DEPOT, CLIENTS = CLIENTS):
    list_route = []
    for i in range(len(CLIENTS)):
        list_route.append([0, i+1, 0])
    return list_route

def joindre_tableaux(list_savings = savings()[0], client_savings = savings()[1]):
    new_l_s = []
    new_c_s = []
    for i in range(len(list_savings)):
        for j in range(len(list_savings[i])):
            new_l_s.append(list_savings[i][j])
            new_c_s.append(client_savings[i][j])
    return (new_l_s, new_c_s)

def order_list(x = joindre_tableaux()):
    list_savings = x[0]
    client_savings = x[1]
    for i in range(len(list_savings)):
        for j in range(i,len(list_savings)):
            if list_savings[j] > list_savings[i]:
                (list_savings[i], list_savings[j]) = (list_savings[j], list_savings[i])
                (client_savings[i], client_savings[j]) = (client_savings[j], client_savings[i])
    return (list_savings, client_savings)

def merge_routes(ROUTE = create_routes(), list_savings = order_list()[0], client_savings = order_list()[1]):
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

def dessin(DEPOT = DEPOT, CLIENTS = CLIENTS, ROUTES = merge_routes()):
    X = [CLIENTS[i][0] for i in range(len(CLIENTS))]
    Y = [CLIENTS[i][1] for i in range(len(CLIENTS))]
    scatter(X,Y,color = (0.15,0.15,0.9))
    scatter(DEPOT[0],DEPOT[1],color = (0.9,0.15,0.15))
    for i in ROUTES:
        X = [0]
        Y = [0]
        for j in range(1,len(i)-1):
            X.append(CLIENTS[i[j]-1][0])
            Y.append(CLIENTS[i[j]-1][1])
        X.append(0) ; Y.append(0)
        plot(X,Y)
    show()

def distance_comparaison(DEPOT = DEPOT, CLIENTS = CLIENTS, ROUTE_AVANT = create_routes() ,ROUTE_APRES = merge_routes()):
    d1 = 0 ; d2 = 0
    for i in range(len(ROUTE_AVANT)):
        d1 += 2 * distance(DEPOT,CLIENTS[ROUTE_AVANT[i][1]-1])
    for j in ROUTE_APRES:
        for k in range(len(j)-1):
            if j[k] == 0:
                d2 += distance(DEPOT,CLIENTS[j[k+1]-1])
            elif j[k+1] == 0:
                d2 += distance(CLIENTS[j[k]-1],DEPOT)
            else:
                d2 += distance(CLIENTS[j[k]-1],CLIENTS[j[k+1]-1])
    return (d1,d2)