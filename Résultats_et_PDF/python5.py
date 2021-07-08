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