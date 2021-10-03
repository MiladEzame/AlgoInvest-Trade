import time
import csv


LIMIT = 500


def read_actions():
    with open("actions.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        for row in csvReader:
            actions.append((row[0], row[1], row[2]))
        creation_matrice(LIMIT, actions)


def creation_matrice(LIMIT, all_actions):

    matrice = [[0 for x in range(LIMIT+1)] for x in range(len(all_actions) + 1)]
    for i in range(1, len(all_actions) + 1):
        for c in range(1, LIMIT + 1):
            if int(all_actions[i-1][1]) <= c:
                matrice[i][c] = max(float(all_actions[i-1][2]) * int(all_actions[i-1][1]) +
                                    matrice[i-1][c-(int(all_actions[i-1][1]))], matrice[i-1][c])
            else:
                matrice[i][c] = matrice[i-1][c]
    c = LIMIT
    n = len(all_actions)
    actions_selectionnees = []

    while c >= 0 and n >= 0:
        a = all_actions[n-1]
        if matrice[n][c] == int(matrice[n-1][c-(int(a[1]))]) + (float(a[2])):
            actions_selectionnees.append(a)
            c -= a[1]

        n -= 1

    print(round(matrice[-1][-1], 2))
    print("ACTIONS SELECTED")
    print(actions_selectionnees)


if __name__ == "__main__":
    start_time = time.time()
    read_actions()
    print("--- executed in {} seconds ---".format(time.time() - start_time))
