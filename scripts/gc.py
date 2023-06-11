import sys

def compute_GC_content(fasta):
    nb_C = 0
    nb_G = 0
    nb = 0
    name = None
    seqs = {}
    with open(fasta, 'r') as f:
        for line in f.readlines():
            if line[0] == '>':
                if name != None:
                    seqs[name] = (nb_C + nb_G) / nb
                    nb_C = 0
                    nb_G = 0
                    nb = 0
                name = line.strip()[1:]
            else:
                nb_C += line.count('C')
                nb_G += line.count('G')
                nb += len(line.strip())
    seqs[name] = (nb_C + nb_G) / nb
    return seqs

def find_max_GC_content(seqs):
    for seq in seqs:
        if seqs[seq] == max(seqs.values()):
            return seq, seqs[seq]*100

seqs = compute_GC_content(sys.argv[1])
highest_GC = find_max_GC_content(seqs)
print(f"{highest_GC[0]}\n{highest_GC[1]}")            