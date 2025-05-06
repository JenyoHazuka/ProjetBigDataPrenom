#!/usr/bin/env python3

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter=';')
    header = next(reader)  # lire l'en-tête

    try:
        # Index des colonnes, détectés dynamiquement
        idx_annee = header.index('annais')
        idx_sexe = header.index('sexe')
        idx_prenom = header.index('preusuel')
        idx_nombre = header.index('nombre')
    except ValueError:
        print("Erreur : en-têtes attendus non trouvés (annais, sexe, preusuel, nombre)", file=sys.stderr)
        sys.exit(1)

    for row in reader:
        try:
            annee = row[idx_annee].strip()
            sexe = row[idx_sexe].strip()
            prenom = row[idx_prenom].strip()
            nombre = int(row[idx_nombre].strip())

            if annee != 'XXXX' and annee and sexe and prenom:
                print(f"{annee}_{sexe}_{prenom}\t{nombre}")
        except (IndexError, ValueError):
            continue  # ignore les lignes mal formées

if __name__ == "__main__":
    mapper()
