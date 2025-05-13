#!/usr/bin/env python3

import sys
import csv

def mapper():
    # Lecture des données d'entrée depuis stdin en utilisant un lecteur CSV avec un délimiteur ';'
    reader = csv.reader(sys.stdin, delimiter=';')
    # Lecture de la première ligne pour obtenir les en-têtes
    header = next(reader)  # lire l'en-tête

    try:
        # Détection dynamique des index des colonnes nécessaires à partir des en-têtes
        idx_annee = header.index('annais')  # Index de la colonne 'annais' (année)
        idx_sexe = header.index('sexe')    # Index de la colonne 'sexe' (genre)
        idx_prenom = header.index('preusuel')  # Index de la colonne 'preusuel' (prénom)
        idx_nombre = header.index('nombre')    # Index de la colonne 'nombre' (nombre d'occurrences)
    except ValueError:
        # Gestion des erreurs si les en-têtes attendus ne sont pas trouvés
        print("Erreur : en-têtes attendus non trouvés (annais, sexe, preusuel, nombre)", file=sys.stderr)
        sys.exit(1)  # Arrêt du programme avec un code d'erreur

    # Parcours les lignes du fichier CSV
    for row in reader:
        try:
            # Extraction et nettoyage des valeurs des colonnes
            annee = row[idx_annee].strip()
            sexe = row[idx_sexe].strip()
            prenom = row[idx_prenom].strip()
            nombre = int(row[idx_nombre].strip())

            # Vérification des conditions : l'année ne doit pas être 'XXXX' ou vide,
            # et les autres champs doivent être valides
            if annee != 'XXXX' and annee and sexe and prenom:
                # Émission d'une clé-valeur sous la forme "année_sexe_prénom    valeur"
                print(f"{annee}_{sexe}_{prenom}\t{nombre}")
        except (IndexError, ValueError):
            # Ignorer les lignes mal formées ou contenant des erreurs de conversion
            continue

if __name__ == "__main__":
    mapper()
