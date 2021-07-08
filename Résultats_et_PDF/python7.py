# 2_opt pour regler les problemes de croisements intra-routes
def deux_opt(D=DEPOT, C=CLIENTS, routes=APRES_INTRA_ROUTE):
    for route in routes:
        if len(route) > 4:
            for i in range(len(route)-1):
                for j in range(len(route)-1):
                    if j != i and j != i-1 and j != i+1:
                        if route[i] == 0 and route[j+1] == 0:
                            if distance(D, C[route[i+1]-1]) + distance(C[route[j]-1], D) > 
                                distance(D, C[route[j]-1]) + distance(C[route[i+1]-1], D):
                                (route[i+1], route[j]) = (route[j], route[i+1])
                        elif route[i+1] == 0 and route[j] == 0:
                            if distance(C[route[i]-1], D) + distance(D, C[route[j+1]-1]) > 
                                distance(C[route[i]-1], D) + distance(D, C[route[j+1]-1]):
                                (route[i], route[j+1]) = (route[j+1], route[i])
                        elif route[i] == 0:
                            if distance(D, C[route[i+1]-1]) + distance(C[route[j]-1], C[route[j+1]-1]) >  
                                distance(D, C[route[j]-1]) + distance(C[route[i+1]-1], C[route[j+1]-1]):
                                (route[i+1], route[j]) = (route[j], route[i+1])
                        elif route[j] == 0:
                            if distance(C[route[i]-1], C[route[i+1]-1]) + distance(D, C[route[j+1]-1]) > 
                                distance(C[route[i]-1], D) + distance(C[route[i+1]-1], C[route[j+1]-1]):
                                (route[i], route[j+1]) = (route[j+1], route[i])
                        elif route[i+1] == 0:
                            if distance(C[route[i]-1], D) + distance(C[route[j]-1], C[route[j+1]-1]) > 
                                distance(C[route[i]-1], C[route[j]-1]) + distance(D, C[route[j+1]-1]):
                                (route[i], route[j+1]) = (route[j+1], route[i])
                        elif route[j+1] == 0:
                            if distance(C[route[i]-1], C[route[i+1]-1]) + distance(C[route[j]-1], D) > 
                                distance(C[route[i]-1], C[route[j]-1]) + distance(C[route[i+1]-1], D):
                                (route[i+1], route[j]) = (route[j], route[i+1])
                        elif distance(C[route[i]-1], C[route[i+1]-1]) + distance(C[route[j]-1], C[route[j+1]-1]) > 
                            distance(C[route[i]-1], C[route[j]-1]) + distance(C[route[i+1]-1], C[route[j+1]-1]):
                            (route[i+1], route[j]) = (route[j], route[i+1])