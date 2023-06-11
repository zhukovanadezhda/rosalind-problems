import sys

def return_rabbits(n, m):
    nb_rabbits = ['' for i in range(n+1)]
    return calculate_rabbits(n, m, nb_rabbits)

def calculate_rabbits(n, m, nb_rabbits):
    if n < 3:
        nb_rabbits[n] = 1
    if nb_rabbits[n] != '':
        return nb_rabbits[n]
    if n >= 3 and n < m + 1:
        nb_rabbits[n] = calculate_rabbits(n-1, m, nb_rabbits) + calculate_rabbits(n-2, m, nb_rabbits)
    else:
        nb_rabbits[n] = calculate_rabbits(n-1, m, nb_rabbits) + calculate_rabbits(n-2, m, nb_rabbits) - calculate_rabbits(n-m-1, m, nb_rabbits)
    return nb_rabbits[n]

print(return_rabbits(int(sys.argv[1]), int(sys.argv[2])))