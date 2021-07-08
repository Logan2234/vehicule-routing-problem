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