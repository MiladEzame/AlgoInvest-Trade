import csv
import itertools
import time


def read_csv():
    with open("actions.csv", "r") as action:
        csvReader = csv.reader(action, delimiter=";")
        actions = []
        for row in csvReader:
            # O(n) search
            actions.append(row)
    permutations(actions)


def permutations(actions):
    actions_finales = []
    for i in range(1, len(actions) + 1):
        # O(n^3) search
        combi = itertools.combinations(actions, i)
        # O(n!)
        for iter in combi:
            # O(n^2)
            valo = 0
            cout = 0
            selected_actions = []
            for act in iter:
                # O(n) insert
                selected_actions.append(act[0])
                cout += int(act[1])
                valo += int(act[1]) * float(act[2])
            if (cout <= 500):
                actions_finales.append((selected_actions, cout, cout + valo))
            # O(n) insert
        # O(n) insert
        benef_max = sorted(actions_finales, key=lambda x: x[2], reverse=True)
        # O(nlog(n))
    print(benef_max[0])


if __name__ == "__main__":
    start_time = time.time()
    read_csv()
    print("--- executed in {} seconds ---".format(time.time() - start_time))
