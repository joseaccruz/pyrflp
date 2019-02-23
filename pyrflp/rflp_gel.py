from collections import Counter
import os
import sys

from Bio import Restriction as r
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from pyrflp.utils import get_resources_dir
from pyrflp.utils import load_seqs

def make_gel(fasta, re_name):
    gel = {}

    # 1. get the full list of sequences to analyse
    seqs = load_seqs(fasta)

    # 2. Get the RE
    re = r.__dict__[re_name]

    for seq in seqs:
        gel[seq.id] = []
        for frag in re.catalyze(seq.seq):
            gel[seq.id].append(len(frag))

    return gel

def gel_stats(gel):
    seq_all = sorted(list(set(b for l in gel.values() for b in l)))

    seq_min = seq_all[0]
    seq_max = seq_all[-1]

    return seq_min, seq_max, seq_all


def command(args):
    gel = make_gel(args.fasta, args.re)

    title = "file: {} / rest: {}".format(os.path.basename(args.fasta.name), args.re)

    create_blot(title, gel, args.margin_top, args.margin_bottom, args.margin_left, args.margin_right, args.lane_height, args.lane_width, args.lane_sep, args.band_start, args.band_end, args.band_width)


def exp_ab(x1, y1, x2, y2):
    print(x1, y1, x2, y2)
    b = (y2/y1)**(1/(x2-x1))
    a = y1 * b**(-x1)
    
    return a, b


def create_blot(title, gel, mt, mb, ml, mr, lh, lw, ls, bs, be, bw):
    seq_min, seq_max, seq_all = gel_stats(gel)

    N = len(gel.items())

    HEIGHT = mt + lh + mb
    WIDTH = ml + lw * N + ls * (N - 1) + mr

    a, b = exp_ab(seq_min, mt + be, seq_max, mt + bs)

    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0))

    draw = ImageDraw.Draw(img)

    font_fname = get_resources_dir() + os.sep + "arial.ttf"

    font_title = ImageFont.truetype(font_fname, 15)
    font_seq = ImageFont.truetype(font_fname, 10)

    # draw title
    draw.text((ml, mt / 3), title, fill=(255,255,255), font=font_title)

    # draw lanes
    lx = ml
    for (seq_id, frags) in gel.items():
        draw.rectangle([(lx, mt), (lx + lw, mt + lh)], fill=(80, 80, 80))
        draw.text((lx, mt + lh), seq_id, fill=(255,255,255), font=font_seq)    
        lx += lw + ls

    # draw reference lines
    ry_last = None
    for seq in seq_all:
        ry = a * b**seq

        if ry_last is None or abs(ry_last - ry) > 10:
            draw.text((5, ry-7), str(seq) + "bp", fill=(255,255,255), font=font_seq)
            draw.line([(ml, ry), (WIDTH - mr, ry)], fill=(128, 128, 128), width=1)

            ry_last = ry

    # draw bands
    lx = ml
    for (seq_id, frags) in gel.items():
        bands = sorted(Counter(frags).items(), key=lambda x:x[0])

        for (band, count) in bands:
            by = a * b**band
            draw.rectangle([(lx, by), (lx + lw, by + (bw * count))], fill=(255, 255, 255))
    
        lx += lw + ls

    
    img.save("teste.png")
