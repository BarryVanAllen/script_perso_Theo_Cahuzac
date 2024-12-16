from typing import List, Dict
import operator

class SearchEngine:
    def __init__(self, data):
        self.data = data

    def search(self, field, value):
        return [row for row in self.data if row.get(field, '').lower() == value.lower()]

    def advanced_search(self, field, operator_symbol, value):
        """Recherche avancée avec des opérateurs (>, <, ==, etc.)."""
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
