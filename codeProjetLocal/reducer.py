#!/usr/bin/env python3

import sys
from collections import defaultdict

def reducer():
    aggregated = defaultdict(int)

    for line in sys.stdin:
        try:
            key, value = line.strip().split('\t')
            # Ajoute la valeur (convertie en entier) à la clé correspondante dans le dictionnaire
            aggregated[key] += int(value)
        except ValueError:
            # Ignore les lignes mal formées (par exemple, celles qui n'ont pas exactement 2 champs)
            continue

    # Parcourt les paires clé-valeur agrégées et les imprime dans le format "{key}\t{total}"
    for key, total in aggregated.items():
        print(f"{key}\t{total}")

if __name__ == "__main__":
    reducer()
