#!/usr/bin/env python2
import csv

# Entree/sortie
input_file = './csv/ParDepartementDepuis2000.csv'           # Le fichier d'origine
output_file = './csv/nat2022_valid.csv'    # Le fichier de sortie

def is_valid_row(row):
    # Verifie qu'il y a exactement 5 champs
    if len(row) != 5:
        return False

    # Extraire les champs dans le bon ordre
    sexe, preusuel, annais, dept, nombre = row

    # Supprimer les espaces blancs avant de verifier les valeurs
    annais = annais.strip()
    sexe = sexe.strip()
    preusuel = preusuel.strip()
    nombre = nombre.strip()
    dept = dept.strip()

    # Verification que tous les champs requis ne sont pas vides
    if not (annais and sexe and nombre and dept and preusuel):
        return False

    # Verifie annais soit un chiffre de 4 chiffres et refuse les XXXX
    if not (annais.isdigit() and len(annais) == 4) or annais == 'XXXX':
        return False

    # Verifie les prenoms soient valides
    if not (preusuel.isalpha() and 0 < len(preusuel) < 30 and preusuel not in ['_PRENOMS_RARES', 'XXXX']):
        return False

    # Verifie le departement soit un chiffre d'alphanumerique de 1 a 3 chiffres (exemple : 2A, 2B pour la Corse)
    if dept in ['XX', 'XXXX'] or not (1 <= len(dept) <= 3 and dept.replace('A', '').replace('B', '').isdigit()):
        return False

    # Verifie le nombre soit un chiffre
    if not (nombre.isdigit() and int(nombre) >= 0):
        return False

    # Verifie le sexe soit 1 ou 2
    if not (sexe in ['1', '2']):
        return False

    # La ligne est valide
    return True

def main():
    with open(input_file, mode='r') as infile, \
         open(output_file, mode='w') as outfile:
        
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Ignore l'en-tete du fichier d'entree
        next(reader, None)

        # Ecrire l'entete dans le fichier de sortie
        writer.writerow(['sexe', 'preusuel', 'annais', 'dept', 'nombre'])

        # Parcourir les lignes et ecrire uniquement les lignes valides
        for row in reader:
            if is_valid_row(row):
                writer.writerow(row)

if __name__ == '__main__':
    main()