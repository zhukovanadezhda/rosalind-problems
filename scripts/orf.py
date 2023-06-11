import sys
from Bio.Seq import Seq

def get_seq_from_fasta(fasta):
    seq = ''
    with open(fasta, 'r') as f:
        for line in f.readlines():
            if line[0] != '>':
                seq += line.strip()
    return seq

def find_orf(seq):
    start_pos = seq.find('ATG')
    protein = []
    for i in range(seq.count('ATG')):
        orf = str((Seq(seq[start_pos:]).translate()))
        stop = orf.find('*')
        if stop != -1:
            protein.append(orf[:stop])
        start_pos = seq.find('ATG', start_pos + 1, -1)
    return protein
        
seq = Seq(get_seq_from_fasta(sys.argv[1]))
proteins = set([i for i in (find_orf(seq) + find_orf(seq.reverse_complement()))])

for prot in proteins:
    print(prot)