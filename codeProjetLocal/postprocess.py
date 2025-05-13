import sys
from collections import defaultdict
from operator import itemgetter

# Définir la fonction principale pour le post-traitement des données
def postprocess():
    grouped = defaultdict(list)

    for line in sys.stdin:
        key, total = line.strip().split('\t')
        annee, sexe, prenom = key.split('_')
        # Regrouper les données par année et sexe, en stockant le prénom et le total
        grouped[(annee, sexe)].append((prenom, int(total)))

    # Parcourir les données regroupées, triées par année et sexe
    for (annee, sexe), prenoms in sorted(grouped.items()):
        # Trier les prénoms par total décroissant et prendre les 5 premiers
        top_5 = sorted(prenoms, key=itemgetter(1), reverse=True)[:5]
        # Afficher l'année et le sexe (convertir le code sexe en 'M' ou 'F')
        print(f"Année: {annee}, Sexe: {'F' if sexe == '2' else 'M'}")
        # Afficher les 5 prénoms les plus fréquents et leurs totaux
        for prenom, total in top_5:
            print(f"{prenom}: {total}")
        # Affichage d'une ligne vide pour séparer les groupes
        print()

if __name__ == "__main__":
    postprocess()
