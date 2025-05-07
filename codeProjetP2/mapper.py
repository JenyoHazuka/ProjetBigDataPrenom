#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter=';')

    header = None
    for line in reader:
	header = line
	break # read only header

    if header is None:
	print >> sys.stderr, "Erreur : le fichier est vide ou mal forme"
	sys.exit(1)

    try:
        # Index des colonnes, detectes dynamiquement
        idx_annee = header.index('annais')
        idx_sexe = header.index('sexe')
        idx_prenom = header.index('preusuel')
        idx_nombre = header.index('nombre')
    except ValueError:
        print >> sys.stderr, "Erreur : en-tetes attendus non trouves (annais, sexe, preusuel, nombre)"
        sys.exit(1)

    for row in reader:
        try:
            annee = row[idx_annee].strip()
            sexe = row[idx_sexe].strip()
            prenom = row[idx_prenom].strip()
            nombre = int(row[idx_nombre].strip())

            if annee != 'XXXX' and annee and sexe and prenom:
                print "{}_{}_{}\t{}".format(annee, sexe, prenom, nombre)
        except (IndexError, ValueError):
            continue  # ignore les lignes mal formees

if __name__ == "__main__":
    mapper()