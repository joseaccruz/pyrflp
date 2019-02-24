import itertools
import math

from Bio import Restriction as r
import numpy as np
from scipy.misc import comb
from tqdm import tqdm

from pyrflp.utils import load_seqs

BLOT_MIN_DIST = 0.1

# the distance is inversely proportional to the log10 of the length of the fragment.

class DiscriminantMatrix:
	def __init__(self, res, M):
		self._res = res
		self._M = M

		s = np.sum(M)
		l = len(M)

		# only the upper half
		t = (s - l) / 2	
		n = (l**2 - l) /2

		# percentage of sequences discriminated by this matrix
		self._perc = t / n

	def __str__(self):
		return ", ".join(list(map(str, self._res)))



def load_res(re_all=False, re_list=None, re_suppliers=None):
	if re_all:
		res = r.AllEnzymes
	else:
		res = r.CommOnly

	if re_list is not None:
		res = list(filter(lambda re: str(re) in re_list, res))

	if re_suppliers is not None:
		res = list(filter(lambda re: len(set(re.suppl) & re_suppliers), res))

	return res


def select_res_seqs(seqs, res):
	res_new = []

	for re in res:
	    for seq in seqs:
	        if re.search(seq.seq):
	        	res_new.append(re)
	        	break

	return res_new


def compare(blot):
	N = len(blot)

	M = np.identity(N)

	for i in range(N):
		for j in range(i+1, N):
			(ii, jj) = np.meshgrid(np.array(blot[i]), np.array(blot[j]))

			z = np.abs(ii - jj) < BLOT_MIN_DIST

			ki = z.sum(axis=0)
			kj = z.sum(axis=1)

			if len(np.argwhere(ki == 0)) > 0 or len(np.argwhere(kj == 0)) > 0:
				M[i][j] = 1
				M[j][i] = 1

	return M

def run_gel(seqs, res):
	blot = {}

	for seq in seqs:
		blot[seq.id] = {}
		for re in sorted(res, key=str):
			blot[seq.id][str(re)] = re.catalyze(seq.seq)

	return blot

def combine(dms, count, top):
	iter_count = int(comb(len(dms), count))
	#conf = input("Will verify {} combinations, are you sure [y/n]?".format(iter_count))
	conf = "y"

	if conf.strip().lower() != "y":
		return

	dms_top = []
	l = len(dms[0]._M)

	for batch in tqdm(iterable=itertools.combinations(dms, count), total=iter_count):
		res = []
		M = np.zeros((l, l))

		for dm in batch:
			M += dm._M
			res += dm._res

		M = (M > 0).astype(int)

		batch_dm = DiscriminantMatrix(res, M)

		if (len(dms_top) < top) or (dms_top[-1]._perc < batch_dm._perc):
			dms_top.append(batch_dm)
			dms_top.sort(key=lambda dm: dm._perc, reverse=True)
			dms_top = dms_top[:top]

			#print(dms_top[0]._perc, dms_top[-1]._perc)

	return dms_top

def optimize(seqs, res, ncomb, ntop):
	# list of DiscrimantMatrices
	dms = []

	for re in sorted(res, key=str):
		blot = []
		for seq in seqs:
			frags = re.catalyze(seq.seq)
			frags = filter(lambda frag: len(frag) > 0, frags)
			dists = list(map(lambda frag: math.log(len(frag), 10), frags))

			blot.append(dists)

		M = compare(blot)

		#print(re, np.sum(M), np.sum(M) / (len(seqs)**2))
		dms.append(DiscriminantMatrix([str(re)], M))

	dms_top = combine(dms, ncomb, ntop)

	for dm in dms_top:
		print(dm, "(%d%%)" % int(dm._perc * 100))
		for (r, c) in np.argwhere(dm._M == 0):
			if r < c:
				print("\t", seqs[r].id, seqs[c].id)


def analyse(fasta, ncomb=2, ntop=5, re_all=False, re_list=None, re_suppliers=None):
	# 1. get the full list of sequences to analyse
	seqs = load_seqs(fasta)

	# 2. get the list of REs to use
	res = load_res(re_all, re_list, re_suppliers)

	# 3. select cutting sequences
	res = select_res_seqs(seqs, res)

	# 4. select cutting sequences
	optimize(seqs, res, ncomb, ntop)


def command(args):
	analyse(args.fasta, args.ncomb, args.ntop)

#make_blot("sample.fasta", ["TaqI"])
