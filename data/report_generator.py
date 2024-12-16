import csv
from typing import List, Dict

class ReportGenerator:
    def __init__(self, data: List[Dict]):
        self.data = data

    def generate_summary(self, output_file):
        """Génère un rapport résumé sous forme de CSV."""
        if not self.data:
            print("Aucune donnée disponible pour générer un rapport.")
            return

        headers = self.data[0].keys()
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"Rapport généré : {output_file}")
