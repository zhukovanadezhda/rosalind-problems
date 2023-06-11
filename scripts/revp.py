import sys
from Bio.Seq import Seq

def get_seq_from_fasta(fasta):
    seq = ''
    with open(fasta, 'r') as f:
        for line in f.readlines():
            if line[0] != '>':
                seq += line.strip()
    return seq

def find_refp(seq):
    for lim_length in range(4, 13):
        for start_pos in range(len(seq)):
            if Seq(seq[start_pos:start_pos+lim_length]).reverse_complement() == Seq(seq[start_pos:start_pos+lim_length]) and start_pos+lim_length <= len(seq):
                print(start_pos+1, lim_length)
                
seq = get_seq_from_fasta(sys.argv[1])
find_refp(seq)