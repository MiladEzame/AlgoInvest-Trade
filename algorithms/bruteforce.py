import csv
import itertools
import time


def read_csv():
    with open("actions.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        for row in csvReader:
            actions.append(row)
    permutations(actions)


def permutations(actions):
    actions_finales = []
    for i in range(1, len(actions) + 1):
        combi = itertools.combinations(actions, i)
        for iter in combi:
            valo = 0
            cout = 0
            selected_actions = []
            for act in iter:
                selected_actions.append(act[0])
                cout += int(act[1])
                valo += int(act[1]) * float(act[2])
            if (cout <= 500):
                actions_finales.append((selected_actions, cout, cout + valo))
        benef_max = sorted(actions_finales, key=lambda x: x[2], reverse=True)
    print(benef_max[0])


if __name__ == "__main__":
    start_time = time.time()
    read_csv()
    print("--- executed in {} seconds ---".format(time.time() - start_time))


# création matrice:
# matrice dont le nombre de lignes est égal au nombre d'actions
# matrice dont le nombre de colonnes est égal au cout maximum (ici 500)

# initialisation de la matrice avec des 0

# pour mes actions comprises entre 0 et nombre d'actions (parcours les lignes)
# pour mes couts compris entre 0 et cout maximum (parcours les colonnes)
# si le cout (ou la somme des couts) de mon action est inférieur ou égale à mon cout max:
# l'élément dans ma matrice en case [action actuelle][cout actuel] sera égal au maximum entre
# le calcul de ma valorisation sur 2 ans ET la valorisation pour ce même cout de ma ligne précédente.

# si mon prix est supérieur à mon cout maximum:
# insertion de la valorisation précédente dans le tableau
