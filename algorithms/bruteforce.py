import csv
import itertools


def permutations():
    with open("actions.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        actions_finales = []
        for row in csvReader:
            actions.append(row)
        global_list = []
        for i in range(1, len(actions) + 1):
            combi = itertools.combinations(actions, i)
            for iter in combi:
                actions_selectionnes = []
                valo = 0
                cout = 0
                for act in iter:
                    actions_selectionnes.append(act[0])
                    cout += int(act[1])
                    valo += int(act[1]) * float(act[2])
                global_list.append((actions_selectionnes, cout, cout + valo))
        for actions in global_list:
            if(actions[1] <= 500):
                actions_finales.append(actions)
        benef_max = sorted(actions_finales, key=lambda x: x[2], reverse=True)
        return benef_max[0]
        # faire une diapo pour l'analyse du code et expliquer les modifs
        # ameliorations / limite / vérifications des points limites
        # comparaison bruteforce et optimisée (complexité et temps d'execution)


if __name__ == "__main__":
    meilleure_action = permutations()
    print(meilleure_action)
