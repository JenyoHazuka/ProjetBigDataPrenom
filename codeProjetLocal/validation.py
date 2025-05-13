#!/usr/bin/env python3
import csv

# Entrée/sortie
input_file = './csv/dpt2022.csv'           # Le fichier d'origine
output_file = './csv/natDpt2022_valid.csv'    # Le fichier de sortie

def is_valid_row(row):
    # Vérifie qu'il y a exactement 5 champs
    if len(row) != 5:
        return False

    # Extraire les champs dans le bon ordre
    sexe, preusuel, annais, dept, nombre = row

    # Supprimer les espaces blancs avant de vérifier les valeurs
    annais = annais.strip()
    sexe = sexe.strip()
    preusuel = preusuel.strip()
    nombre = nombre.strip()
    dept = dept.strip()

    # Vérification que tous les champs requis ne sont pas vides
    if not (annais and sexe and nombre and dept and preusuel):
        return False

    # Vérifie annais soit un chiffre de 4 chiffres et refuse les XXXX
    if not (annais.isdigit() and len(annais) == 4) or annais == 'XXXX':
        return False

    # Vérifie les prénoms soient valides
    if not (preusuel.isalpha() and 0 < len(preusuel) < 30 and preusuel not in ['_PRENOMS_RARES', 'XXXX']):
        return False

    # Vérifie le département soit un chiffre d'alphanumérique de 1 à 3 chiffres (exemple : 2A, 2B pour la Corse)
    if dept in ['XX', 'XXXX'] or not (1 <= len(dept) <= 3 and dept.replace('A', '').replace('B', '').isdigit()):
        return False

    # Vérifie le nombre soit un chiffre
    if not (nombre.isdigit() and int(nombre) >= 0):
        return False

    # Vérifie le sexe soit 1 ou 2
    if not (sexe in ['1', '2']):
        return False

    # La ligne est valide
    return True

def main():
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Ignore l'en-tête du fichier d'entrée
        next(reader, None)

        # Écrire l'entête dans le fichier de sortie
        writer.writerow(['sexe', 'preusuel', 'annais', 'dept', 'nombre'])

        # Parcourir les lignes et écrire uniquement les lignes valides
        for row in reader:
            if is_valid_row(row):
                writer.writerow(row)

if __name__ == '__main__':
    main()