import sys, os
from os.path import dirname
from datetime import datetime
from collections import defaultdict

def argParse(usage="Usage ?"):
    argdict = defaultdict(lambda: False)
    for i, arg in enumerate(sys.argv):
        if arg in ('-w',):
            argdict.update(write = True)
        elif arg in ('-m',):
            _arg = sys.argv.pop(i+1)
            argdict['model'] = _arg
        else:
            if i == 0:
                argdict.setdefault('titles', '') # see defaultdict...
            else:
                argdict.update({'titles':arg})

    return argdict
