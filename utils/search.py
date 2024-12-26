
import operator

class SearchEngine:
    def __init__(self, data):
        self.data = data

    def search(self, field, value):
        """Recherche dans la liste de dictionnaire data.

        PRE: self.data est une liste de dictionnaire.
            field est un champ dans les dictionnaires.
            value doit être une chaîne à rechercher dans le champ spécifié.

        POST : renvoie une liste de ligne ou les champs spécifié field correspond exactement à value.

        """
        return [row for row in self.data if row.get(field, '').lower() == value.lower()]

    def advanced_search(self, field, operator_symbol, value):
        """Recherche avancée avec des opérateurs (>, <, ==, etc.).
        PRE: self.data est une liste de dictionnaire.
                field est un champ dans les dictionnaires.
                operator_symbol est opérateur valide.

        POST : Retourne une liste de lignes où le champ field est conforme au triage de l'opérateur.
        RAISE : ValueError : si l'opérateur est invalide ou si la conversion du value en numérique échoue

        """
        OPERATORS = {
            "<": operator.lt,
            ">": operator.gt,
            "<=": operator.le,
            ">=": operator.ge,
            "==": operator.eq,
            "!=": operator.ne,
        }
        if operator_symbol not in OPERATORS:
            raise ValueError(f"Opérateur non pris en charge : {operator_symbol}")

        compare = OPERATORS[operator_symbol]
        try:
            # Comparer en tant que float ou fallback vers une chaîne
            return [row for row in self.data if compare(float(row[field]), float(value))]
        except ValueError:
            return [row for row in self.data if compare(row[field], value)]
#ajout de chatgpt pour les operateur de comparaison
