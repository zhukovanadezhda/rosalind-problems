import sys


def return_rabbits(n, k):
    nb_rabbits = ['' for i in range(n+1)]
    return calculate_rabbits(n, k, nb_rabbits)

def calculate_rabbits(n, k, nb_rabbits):
    if n < 3:
        nb_rabbits[n] = 1
    else:
        nb_rabbits[n] = calculate_rabbits(n-1, k, nb_rabbits) + k * calculate_rabbits(n-2, k, nb_rabbits)
    return nb_rabbits[n]

print(return_rabbits(int(sys.argv[1]), int(sys.argv[2])))