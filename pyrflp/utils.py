import os

from Bio import SeqIO


def load_seqs(fasta):
	seqs = [seq for seq in SeqIO.parse(fasta, "fasta")]

	return seqs


def get_resources_dir():
	return os.path.dirname(__file__)
