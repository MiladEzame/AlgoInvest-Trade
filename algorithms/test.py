import time


def matrice_test():
    matrice = [[0 for x in range(1, 11)] for x in range(1, 2)]

    print(matrice)


if __name__ == "__main__":
    start_time = time.time()
    matrice_test()
    print("--- executed in {} seconds ---".format(time.time() - start_time))
