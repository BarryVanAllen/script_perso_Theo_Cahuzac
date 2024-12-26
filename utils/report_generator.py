import csv
from typing import List, Dict

class ReportGenerator:
    def __init__(self, data: List[Dict]):
        self.data = data

    def generate_summary(self, output_file):
        """Génère un rapport résumé sous forme de CSV.
        PRE : self.data sont les données consolidé.
                output_file est le chemin vers la ou sera écrit le rapport.
        POST : Génère un fichier csv avec les données CSV trié ou non.
                retourne une string disant que aucune données n'a été trouvé.
        RAISE : Exeption: output_file est un chemin invalide
                IOError : le fichier ne peut pas être écrit.
        """
        if not self.data:
            print("Aucune donnée disponible pour générer un rapport.")
            return

        headers = self.data[0].keys()
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"Rapport généré : {output_file}")
