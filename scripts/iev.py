import sys

def calculate_ex_offspring(string):
    #genotypes = string.strip().split(' ')
    genotypes = string
    sum = 0
    coeff = [2, 2, 2, 1.5, 1, 0]
    for i in range(len(genotypes)):
        sum += int(genotypes[i])*coeff[i]
    return sum

print(calculate_ex_offspring(sys.argv[1:]))