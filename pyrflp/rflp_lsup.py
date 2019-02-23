import sys

from Bio import Restriction as r

def command(args):
    """
    Lists all suppliers
    """
    r.RestrictionBatch().show_codes()

