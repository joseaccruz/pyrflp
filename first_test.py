import math

from Bio import SeqIO
from Bio import Restriction as r
import numpy as np

REF_LEN = 2
REF_DIST = 20


# the distance is inversely proportional to the log10 of the length of the fragment.
def distance(x, prec=2):
    return np.round((math.log(REF_LEN, 10) * REF_DIST) / math.log(x, 10), prec)


seqs = [seq for seq in SeqIO.parse("sample.fasta", "fasta")]

for rest in r.CommOnly:
    print rest, rest.site

    for sr in seqs:
        rest_sites = rest.search(sr.seq)

        if len(rest_sites) > 0:
            print "\t", sr.id
            print "\t", map(lambda x: distance(x), sorted(filter(lambda x: x > 1, list(set([len(x) for x in rest.catalyse(sr.seq)])))))


#for x in range(2, 1001):
#    print x, distance(x)

