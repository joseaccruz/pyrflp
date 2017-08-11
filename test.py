import math

from Bio import SeqIO
from Bio import Restriction as r


seqs = SeqIO.parse("sample.fasta", "fasta")

#for s in seqs:
#    print s.seq

for rest in r.CommOnly:
    print rest, rest.site, rest.suppl, rest.all_suppliers
