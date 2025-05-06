import sys
from collections import defaultdict
from operator import itemgetter

def postprocess():
    grouped = defaultdict(list)

    for line in sys.stdin:
        key, total = line.strip().split('\t')
        annee, sexe, prenom = key.split('_')
        grouped[(annee, sexe)].append((prenom, int(total)))

    for (annee, sexe), prenoms in sorted(grouped.items()):
        top_5 = sorted(prenoms, key=itemgetter(1), reverse=True)[:5]
        print(f"Année: {annee}, Sexe: {'F' if sexe == '2' else 'M'}")
        for prenom, total in top_5:
            print(f"{prenom}: {total}")
        print()

if __name__ == "__main__":
    postprocess()
