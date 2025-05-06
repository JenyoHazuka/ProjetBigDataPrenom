#!/usr/bin/env python3

import sys
from collections import defaultdict

def reducer():
    aggregated = defaultdict(int)

    for line in sys.stdin:
        try:
            key, value = line.strip().split('\t')
            aggregated[key] += int(value)
        except ValueError:
            # Ignore les lignes mal formées (ex : pas exactement 2 champs)
            continue

    for key, total in aggregated.items():
        print(f"{key}\t{total}")

if __name__ == "__main__":
    reducer()
