# Forme les routes en prenant en compte les benefices
def merge_routes(ROUTE=ROUTES,l_savings=SAVINGS[0],c_savings=SAVINGS[1]):
    temp = 0
    for i in range(len(l_savings)):
        for j in range(len(ROUTE)):
            if ROUTE[j][0] == 0 and ROUTE[j][1] == c_savings[i][1]:
                for k in range(len(ROUTE)):
                    if ROUTE[k][1]==c_savings[i][0] and ROUTE[j][2]==0:
                        _ = ROUTE[k].pop()
                        ROUTE[k].append(c_savings[i][1])
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