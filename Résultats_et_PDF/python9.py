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
        res_distance = [] # Pour stocker (point, route) le plus proche de (point2, route2) et donne la valeur de distance
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
        if dist_optimised != []:
            maxi = dist_optimised[0]
        for i in range(1, len(dist_optimised)): # Tri par valeur d'optimisation
            if dist_optimised[i][1] > maxi[1]:
                maxi = dist_optimised[i]
        if len(dist_optimised) > 0 and maxi[1] > 0:
            NB_INTER += 1
            routes[res_distance[maxi[0]][1][1]].insert(
                routes[res_distance[maxi[0]][1][1]].index(res_distance[maxi[0]][1][0])+1, res_distance[maxi[0]][0][0])
            routes[res_distance[maxi[0]][0][1]].remove(res_distance[maxi[0]][0][0])
            # dessin(routes)
        else:
            break
    return NB_INTER