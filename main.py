import argparse
import os
from utils.data_loader import DataLoader
from utils.search import SearchEngine
from utils.report_generator import ReportGenerator


def print_table(data):
    """Affiche une liste de dictionnaires sous forme de tableau.
    PRE : data est une liste de dictionnaires
    POST : Affiche un tableau dans la console avec les données de data.
            Si data vide retourne "Aucun résultat à afficher".
    """
    if not data:
        print("Aucun résultat à afficher.")
        return

    headers = data[0].keys()
    col_widths = {key: max(len(key), max(len(str(row.get(key, ""))) for row in data)) for key in headers}

    header_line = " | ".join(f"{key.ljust(col_widths[key])}" for key in headers)
    separator_line = "-+-".join("-" * col_widths[key] for key in headers)

    print(header_line)
    print(separator_line)
    for row in data:
        print(" | ".join(f"{str(row.get(key, '')).ljust(col_widths[key])}" for key in headers))


def main():
    """ fonction principale ou l'utilisateur choisit le triage à effectuer sur data.
    PRE: les arguments que l'utilisateur fournis via la ligne de commande.
    POST : ne retourne rien
    RAISE : Exception : si le répertoire n'existe pas ou est invalide.
    """
    parser = argparse.ArgumentParser(description="Programme d'analyse de données CSV.")
    parser.add_argument("directory", help="Répertoire contenant les fichiers CSV.")
    parser.add_argument("--field", help="Champ pour la recherche.")
    parser.add_argument("--operator", help="Opérateur de comparaison (>, <, ==, etc.).")
    parser.add_argument("--value", help="Valeur à chercher.")
    parser.add_argument("--output", help="Fichier de rapport de sortie (CSV).")

    args = parser.parse_args()

    if not os.path.exists(args.directory) or not os.path.isdir(args.directory):
        print("Le répertoire spécifié est invalide.")
        return

    loader = DataLoader(args.directory)
    loader.load_csv_files()
    data = loader.get_data()

    if not data:
        print("Aucune donnée chargée.")
        return

    print(f"{len(data)} lignes de données chargées.")

    if args.field and args.value:
        search_engine = SearchEngine(data)
        try:
            if args.operator:
                results = search_engine.advanced_search(args.field, args.operator, args.value)
            else:
                results = search_engine.search(args.field, args.value)
            if results:
                print(f"\nRésultats trouvés ({len(results)} lignes) :")
                print_table(results)
                if args.output:
                    report_generator = ReportGenerator(results)
                    report_generator.generate_summary(args.output)
            else:
                print("\nAucun résultat trouvé.")
        except ValueError as e:
            print(f"Erreur : {e}")
    else:
        print("Mode interactif activé. Fournissez --field et --value pour une recherche directe.")
        # Appel du mode interactif ici si nécessaire


if __name__ == "__main__":
    main()

