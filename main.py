from data_loader import DataLoader
from search import SearchEngine
from report_generator import ReportGenerator
import os


def prompt_user(prompt_text):
    """Affiche un prompt et récupère la réponse de l'utilisateur."""
    return input(f"{prompt_text} : ").strip()


def print_table(data):
    """
    Affiche une liste de dictionnaires sous forme de tableau.
    """
    if not data:
        print("Aucun résultat à afficher.")
        return

    # Obtenir les clés pour l'en-tête
    headers = data[0].keys()

    # Calculer la largeur de chaque colonne
    col_widths = {key: len(key) for key in headers}
    for row in data:
        for key, value in row.items():
            col_widths[key] = max(col_widths[key], len(str(value)))

    # Construire l'en-tête
    header_line = " | ".join(f"{key.ljust(col_widths[key])}" for key in headers)
    separator_line = "-+-".join("-" * col_widths[key] for key in headers)

    # Construire les lignes de données
    rows = []
    for row in data:
        rows.append(" | ".join(f"{str(row[key]).ljust(col_widths[key])}" for key in headers))

    # Afficher le tableau
    print(header_line)
    print(separator_line)
    print("\n".join(rows))


def interactive_mode(data):
    """
    Démarre le mode interactif pour que l'utilisateur puisse utiliser le programme.
    """

    filtered_data = []
    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Rechercher")
        print("2. Quitter")
        choice = prompt_user("Entrez votre choix (1 ou 2)")

        if choice == "1":
            print("\nRecherche :")
            field = prompt_user("Sur quel champ voulez-vous chercher (ex: nom, catégorie, prix_unitaire)")
            while field not in ["nom", "catégorie", "prix_unitaire"]:
                field = prompt_user("Sur quel champ voulez-vous chercher (ex: nom, catégorie, prix_unitaire)")

            if field in ["catégorie", "prix_unitaire"]:  # Champs où les opérateurs sont pertinents
                operator_symbol = prompt_user("Quel opérateur voulez-vous utiliser (ex: <, >, <=, >=, ==, !=)")
                while operator_symbol not in ["<", ">", "<=", ">=", "==", "!="]:
                    operator_symbol = prompt_user("Quel opérateur voulez-vous utiliser (ex: <, >, <=, >=, ==, !=)")
                value = prompt_user(f"Quelle valeur cherchez-vous pour le champ '{field}'")
                search_engine = SearchEngine(data)
                try:
                    filtered_data = search_engine.advanced_search(field, operator_symbol, value)
                    if filtered_data:
                        print(f"\nRésultats trouvés ({len(filtered_data)} lignes) :")
                        print_table(filtered_data)
                    else:
                        print("\nAucun résultat trouvé.")
                except ValueError as e:
                    print(f"Erreur : {e}")
            else:
                value = prompt_user(f"Quelle valeur cherchez-vous pour le champ '{field}'")
                search_engine = SearchEngine(data)
                filtered_data = search_engine.search(field, value)
                if filtered_data:
                    print(f"\nRésultats trouvés ({len(filtered_data)} lignes) :")
                    print_table(filtered_data)
                else:
                    print("\nAucun résultat trouvé.")

            inputUser = prompt_user("voulez-vous générer un rapport ? (oui ou non)")
            while inputUser not in ["oui", "non"]:
                inputUser = prompt_user("voulez-vous générer un rapport ? (oui ou non)")

            if inputUser == "oui":
                output_file = prompt_user("Entrez le nom du fichier de rapport (ex: rapport.csv)")
                report_generator = ReportGenerator(filtered_data)
                report_generator.generate_summary(output_file)

        elif choice == "2":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


def main():
    while True:
        directory = prompt_user("Entrez le dossier contenant les fichiers CSV")

        if not os.path.exists(directory):
            print("Le fichier ou dossier n'existe pas. Veuillez réessayer.")
        elif not os.path.isdir(directory):
            print("Le chemin spécifié n'est pas un dossier. Veuillez réessayer.")
        else:
            break

    loader = DataLoader(directory)
    loader.load_csv_files()
    data = loader.get_data()

    if not data:
        print("Aucune donnée trouvée dans les fichiers CSV.")
        return

    print(f"\n{len(data)} lignes de données chargées avec succès.")
    interactive_mode(data)

if __name__ == "__main__":
    main()


