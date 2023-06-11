import sys

def fill_dna_matrix(fasta):
    dna_matrix = []
    seq = ''
    with open(fasta, 'r') as f:
        for line in f.readlines():
            if line[0] != '>':
                seq += line.strip()
            else:
                dna_matrix.append(seq)
                seq = ''
    dna_matrix.append(seq)
    dna_matrix.remove('')
    return dna_matrix

def fill_profile_matrix(dna_matrix):
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for j in range(len(dna_matrix[0])):
        temp = ''
        for seq in dna_matrix:
            temp += seq[j]
        for key in profile_matrix:
            profile_matrix[key].append(temp.count(key))
    return profile_matrix

def find_consensus(profile_matrix):
    consensus = ''
    for j in range(len(profile_matrix['A'])):
        max = 0
        for key in profile_matrix:
            if profile_matrix[key][j] > max:
                max = profile_matrix[key][j]
                cons = key
        consensus += cons
    return consensus
    
    
dna_matrix = fill_dna_matrix(sys.argv[1])
profile_matrix = fill_profile_matrix(dna_matrix)
print(find_consensus(profile_matrix))
for key in profile_matrix:
    print(f"{key}: ", end='')
    for j in profile_matrix[key]:
        print(f"{j} ", end='')
    print()