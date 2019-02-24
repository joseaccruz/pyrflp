import argparse
import sys

from pyrflp import rflp_lre
from pyrflp import rflp_lsup
from pyrflp import rflp_analyse
from pyrflp import rflp_gel


__VERSION__ = "0.0.2"


#
# main
#
parser = argparse.ArgumentParser(description="RFLP Experiment Design.")
parser.set_defaults(func=None)

subparsers = parser.add_subparsers(title="actions")

parser_lre = subparsers.add_parser ("lre", help="Lists restriction enzymes.")
parser_lre.add_argument("--all", "-a", action="store_true", help="Show all REs (by default shows only the common REs).")
parser_lre.add_argument("--sup", "-s", type=str, default=None, nargs="*", help="Shows REs only for the specified suppliers (see 'lsup' commmand).")
parser_lre.set_defaults(func=rflp_lre.command)

parser_lsup = subparsers.add_parser ("lsup", help="Lists suppliers.")
parser_lsup.set_defaults(func=rflp_lsup.command)

parser_analyse = subparsers.add_parser ("analyse", help="Analyse the best RE combination for a given set of sequences.")
parser_analyse.add_argument("fasta", type=argparse.FileType("r"))
parser_analyse.add_argument("--all", "-a", action="store_true", help="Uses all REs (by default uses only the common REs).")
parser_analyse.add_argument("--ncomb", "-nc", type=int, default=2, help="How many REs should be combined in the search for the best match.")
parser_analyse.add_argument("--ntop",  "-nt", type=int, default=5, help="How many top results should be displayed.")
parser_analyse.set_defaults(func=rflp_analyse.command)

parser_gel = subparsers.add_parser ("gel", help="Generate a gel corresponding to the digestion of the sequences on FASTA by the restriction enzyme on re...")
parser_gel.add_argument("fasta", type=argparse.FileType("r"))
parser_gel.add_argument("image", type=str, help="Name of the output image file in (PNG) format.")
parser_gel.add_argument("re", type=str, help="Restriction enzyme to apply.")
parser_gel.add_argument("--margin_top",    "-mt", type=int, default=50, help="Top margin of gel.")
parser_gel.add_argument("--margin_bottom", "-mb", type=int, default=20, help="Bottom margin of gel.")
parser_gel.add_argument("--margin_left",   "-ml", type=int, default=50, help="Left margin of gel.")
parser_gel.add_argument("--margin_right",  "-mr", type=int, default=20, help="Right margin of gel.")
parser_gel.add_argument("--lane_height",   "-lh", type=int, default=500, help="Lane height.")
parser_gel.add_argument("--lane_width",    "-lw", type=int, default=50, help="Lane width.")
parser_gel.add_argument("--lane_sep",      "-ls", type=int, default=25, help="Space between lanes.")
parser_gel.add_argument("--band_start",    "-bs", type=int, default=10, help="Position of the first band in respect to the lane.")
parser_gel.add_argument("--band_end",      "-be", type=int, default=490, help="Position of the last band.")
parser_gel.add_argument("--band_width",    "-bw", type=int, default=1,  help="Width of the thinest band.")
parser_gel.set_defaults(func=rflp_gel.command)


args = parser.parse_args()

if args.func is not None:
	args.func(args)
else:
	parser.print_usage()

	

