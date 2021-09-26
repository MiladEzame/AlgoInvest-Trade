import csv
import itertools
import time


def permutations():
    with open("actions.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        actions_finales = []
        for row in csvReader:
            # O(n) search
            actions.append(row)
            # O(n) insert
        global_list = []
        for i in range(1, len(actions) + 1):
            # O(n^3) search
            combi = itertools.combinations(actions, i)
            # O(n!)
            for iter in combi:
                # O(n^2)
                actions_selectionnes = []
                valo = 0
                cout = 0
                for act in iter:
                    # O(n) search
                    actions_selectionnes.append(act[0])
                    # O(n) insert
                    cout += int(act[1])
                    valo += int(act[1]) * float(act[2])
                global_list.append((actions_selectionnes, cout, cout + valo))
                # O(n) insert
        for actions in global_list:
            # O(n)
            if(actions[1] <= 500):
                actions_finales.append(actions)
                # O(n) insert
        benef_max = sorted(actions_finales, key=lambda x: x[2], reverse=True)
        # O(nlog(n))
        return benef_max[0]
        # faire une diapo pour l'analyse du code et expliquer les modifs
        # ameliorations / limite / vérifications des points limites
        # comparaison bruteforce et optimisée (complexité et temps d'execution)


if __name__ == "__main__":
    start_time = time.time()
    meilleure_action = permutations()
    print(meilleure_action)
    print("--- executed in {} seconds ---".format(time.time() - start_time))
