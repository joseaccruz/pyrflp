import os

import argparse

parser = argparse.ArgumentParser(description='Sugests the best ER for our research.')
parser.add_argument('infile', type=str, help='FASTA file to process')
parser.add_argument('--output', type=str, help='Outfile')

args = parser.parse_args()

if os.path.isfile(args.infile):
    print "Ficheiro!!"
    print open(args.infile).read()
else:
    print "Not Ficheiro!!"

print args.output
