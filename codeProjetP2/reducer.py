#!/usr/bin/env python2

import sys
from collections import defaultdict

def reducer():
    aggregated = defaultdict(int)

    for line in sys.stdin:
        try:
            key, value = line.strip().split('\t')
            aggregated[key] += int(value)
        except ValueError:
            # Ignore les lignes mal formees (ex : pas exactement 2 champs)
            continue

    for key, total in aggregated.items():
        print "{}\t{}".format(key,total)

if __name__ == "__main__":
    reducer()
