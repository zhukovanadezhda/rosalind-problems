import sys


def get_seqs_from_fasta(fasta):
    seqs = {}
    name = ''
    seq = ''
    with open(fasta, 'r') as f:
        for line in f.readlines():
            if line[0] == '>':
                seqs[name] = seq
                name = line[1:-1]
                seq = ''
            else:
                seq += line.strip()
    seqs[name] = seq
    del seqs['']
    return seqs

def find_overlaping_graph(seqs, k=3):
    for first_name in seqs:    
        for second_name in seqs:
            if first_name != second_name and seqs[first_name][-k:] == seqs[second_name][:k]:
                print(first_name, second_name)
                
seqs = get_seqs_from_fasta(sys.argv[1])
find_overlaping_graph(seqs)