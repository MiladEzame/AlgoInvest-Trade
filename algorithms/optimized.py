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
        for p in range(1, LIMIT + 1):
            if int(all_actions[i-1][1]) <= p:
                matrice[i][p] = max((float(all_actions[i-1][2]) * int(all_actions[i-1][1]) +
                                     int(all_actions[i-1][1])), matrice[i-1][p])
            else:
                matrice[i][p] = matrice[i-1][p]


if __name__ == "__main__":
    start_time = time.time()
    read_actions()
    print("--- executed in {} seconds ---".format(time.time() - start_time))
