# Construction de la liste des "savings" pour chaque couple de points
def savings(DEPOT=DEPOT, CLIENTS=CLIENTS):
    list_savings = []
    client_savings = []
    temp = []
    temp2 = []
    for i in range(0, len(CLIENTS)-1):
        for j in range(i+1, len(CLIENTS)):
            temp.append((round(distance(CLIENTS[i], DEPOT) + 
                distance(CLIENTS[j],DEPOT)-distance(CLIENTS[i],CLIENTS[j]),2)))
            temp2.append((i+1, j+1))
        list_savings.append(temp)
        client_savings.append(temp2)
        temp = []
        temp2 = []
    return (list_savings, client_savings)