import argparse
import re
from data_loader import DataLoader
from search import SearchEngine
from report_generator import ReportGenerator

def parse_search_criteria(search_criteria):
    """
    Analyse une chaîne de recherche au format 'champ < valeur'.
    Renvoie un tuple (champ, opérateur, valeur).
    """
    match = re.match(r"(\w+)\s*(<|>|<=|>=|==|!=)\s*(.+)", search_criteria)
    if not match:
        raise ValueError(f"Critère de recherche invalide : {search_criteria}. Format attendu : 'champ < valeur'.")
    return match.groups()  # Renvoie (champ, opérateur, valeur)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Outil de gestion des stocks.")
    parser.add_argument('--directory', '-d', required=True, help="Dossier contenant les fichiers CSV.")
    parser.add_argument('--search', '-s', metavar='criteria', help="Rechercher un produit (format : 'champ < valeur').")
    parser.add_argument('--report', '-r', metavar='output_file', help="Générer un rapport résumé.")
    parser.add_argument('--sort', metavar='field', help="Trier les résultats par un champ spécifique.")
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Étape 1 : Charger les fichiers CSV
    loader = DataLoader(args.directory)
    loader.load_csv_files()
    data = loader.get_data()
    if not data:
        print("Aucune donnée trouvée dans les fichiers CSV.")
        return

    # Étape 2 : Recherche avec un critère avancé (optionnel)
    if args.search:
        try:
            field, operator, value = parse_search_criteria(args.search)
            print(f"Recherche : {field} {operator} {value}")
            search_engine = SearchEngine(data)
            results = search_engine.advanced_search(field, operator, value)
            if results:
                print(f"Résultats trouvés ({len(results)} lignes) :")
                print(results)
            else:
                print("Aucun résultat trouvé.")
        except ValueError as e:
            print(f"Erreur : {e}")
            return

    # Étape 3 : Génération d'un rapport (optionnel)
    if args.report:
        report_generator = ReportGenerator(data)
        report_generator.generate_summary(args.report)

if __name__ == "__main__":
    main()
