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
    matrice = [[0 for x in range((LIMIT))] for x in range(len(all_actions))]

    for action in range(1, len(all_actions)):
        print(action)


# n actions (lignes) et 0 à coût max(colonnes)
# Remplissage de la matrice :
# Pour chaque lignes de la matrice entre 0 et n il y a l'action (nom, cout, benef)
# Chaque colonnes de ma matrice contiendra une valeur entre 0 et mon coût maximum
# Remplir chaque cellule de ma matrice avec les coûts correspondants
# Comparer chaque cellule avec la précédente pour voir si elle est plus profitable que la précédente
# Récupérer la meilleure valeur et la renvoyer


if __name__ == "__main__":
    start_time = time.time()
    read_actions()
    print("--- executed in {} seconds ---".format(time.time() - start_time))
