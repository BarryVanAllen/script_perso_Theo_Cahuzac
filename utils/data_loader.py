class DataLoader:
    def __init__(self, directory: str):
        self.directory = directory
        self.data = []

    def load_csv_files(self) -> None:
        """Charge et consolide les fichiers CSV dans un seul tableau."""
        for filename in os.listdir(self.directory):
            if filename.endswith('.csv'):
                filepath = os.path.join(self.directory, filename)
                for encoding in ['utf-8', 'iso-8859-1', 'windows-1252']:
                    try:
                        with open(filepath, 'r', encoding=encoding) as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                self.data.append(row)
                        print(f"Fichier {filename} chargé avec succès.")
                        break  # Sortir de la boucle si le fichier est ouvert avec succès
                    except UnicodeDecodeError:
                        print(
                            f"Erreur d'encodage pour le fichier {filename} avec l'encodage {encoding}. Tentative avec un autre encodage.")
                        continue  # Essayer le prochain encodage
                    except Exception as e:
                        print(f"Erreur lors de l'ouverture du fichier {filename}: {e}")

    def get_data(self) -> List[Dict]:
        """Renvoie les données consolidées."""
        return self.data
