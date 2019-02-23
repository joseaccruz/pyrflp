import sys

from Bio import Restriction as r

def command(args):
    """
    Lists the available restriction enzimes
    """
    # selects the REs to list
    if args.sup is not None:
        res = r.RestrictionBatch(first=[], suppliers=args.sup)
    elif args.all:
        res = r.AllEnzymes
    else:
        res = r.CommOnly


    # sorts the RE list
    res = sorted(res, key=str)

    for re in res:
        sys.stdout.write("{:16} {}\n".format(str(re), re.site))

    """
    if re_list is not None:
        res = list(filter(lambda re: str(re) in re_list, res))

    if re_suppliers is not None:
        res = list(filter(lambda re: len(set(re.suppl) & re_suppliers), res))

    return res
    """

    sys.stdout.write("------\n{} restriction enzimes listed\n\n".format(len(res)))

