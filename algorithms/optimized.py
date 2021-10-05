import time
import csv


LIMIT = 500


def read_actions():
    with open("actions.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        for row in csvReader:
            if(float(row[1]) >= 0):
                actions.append((row[0], float(row[1]), float(row[2])))
        creation_matrice(LIMIT, actions)


def read_actions_entiers():
    with open("dataset1.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        for row in csvReader:
            if(float(row[1]) > 0):
                actions.append((row[0], round(float(row[1])*100), float(row[2])/100))
        creation_matrice_datasets(LIMIT, actions)


def creation_matrice(LIMIT, all_actions):

    matrice = [[0 for x in range(LIMIT + 1)] for x in range(len(all_actions) + 1)]
    for i in range(1, len(all_actions) + 1):
        for c in range(1, LIMIT + 1):
            if int(all_actions[i-1][1]) <= c:
                matrice[i][c] = max(all_actions[i-1][2] * all_actions[i-1][1] +
                                    matrice[i-1][c-(int(all_actions[i-1][1]))], matrice[i-1][c])
            else:
                matrice[i][c] = matrice[i-1][c]
    c = LIMIT
    n = len(all_actions)
    actions_selectionnees = []

    while c >= 0 and n > 0:
        a = all_actions[n-1]
        try:
            if matrice[n][c] == matrice[n-1][c-(int(a[1]))] + a[2] * a[1]:
                actions_selectionnees.append(a)
                c -= int(a[1])
        except IndexError:
            print(len(matrice))
            print(a, c, n)
            raise
        n -= 1
    print("ACTIONS SELECTIONNEES :")
    cout = 0
    for action in actions_selectionnees:
        print(action[0])
        cout += action[1]
    print("COUT TOTAL : {}".format(cout))
    print("PROFIT TOTAL : {:.2f}".format(matrice[-1][-1]))


def creation_matrice_datasets(LIMIT, all_actions):
    LIMIT *= 100
    matrice = [[0 for x in range(LIMIT + 1)] for x in range(len(all_actions) + 1)]
    for i in range(1, len(all_actions) + 1):
        for c in range(1, LIMIT + 1):
            if int(all_actions[i-1][1]) <= c:
                matrice[i][c] = max(all_actions[i-1][2] * all_actions[i-1][1] +
                                    matrice[i-1][c-(int(all_actions[i-1][1]))], matrice[i-1][c])
            else:
                matrice[i][c] = matrice[i-1][c]
    c = LIMIT
    n = len(all_actions)
    actions_selectionnees = []

    while c >= 0 and n > 0:
        a = all_actions[n-1]
        try:
            if matrice[n][c] == matrice[n-1][c-(int(a[1]))] + a[2] * a[1]:
                actions_selectionnees.append((a[0], a[1]/100, a[2]))
                c -= int(a[1])
        except IndexError:
            print(len(matrice))
            print(a, c, n)
            raise
        n -= 1
    print("ACTIONS SELECTIONNEES : ")
    cout = 0
    for action in actions_selectionnees:
        print("- {}".format(action[0]))
        cout += action[1]*100
    print("COUT TOTAL : {}".format(cout/100))
    print("PROFIT TOTAL : {}".format(round(matrice[-1][-1])/100))


if __name__ == "__main__":
    start_time = time.time()
    read_actions()
    # read_actions_entiers()
    print("--- executed in {} seconds ---".format(time.time() - start_time))
