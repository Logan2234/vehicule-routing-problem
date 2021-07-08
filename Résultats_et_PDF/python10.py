def dessin(chemin):
    X = [CLIENTS[i][0] for i in range(len(CLIENTS))]
    Y = [CLIENTS[i][1] for i in range(len(CLIENTS))]
    scatter(X, Y, color=(0.15, 0.15, 0.9))
    scatter(DEPOT[0], DEPOT[1], color=(0.9, 0.15, 0.15))
    for i in chemin:
        X = [DEPOT[0]]
        Y = [DEPOT[1]]
        for j in range(1, len(i)-1):
            X.append(CLIENTS[i[j]-1][0])
            Y.append(CLIENTS[i[j]-1][1])
        X.append(DEPOT[0])
        Y.append(DEPOT[1])
        plot(X, Y)
    show()