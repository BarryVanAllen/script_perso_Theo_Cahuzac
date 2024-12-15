from typing import List, Dict

class SearchEngine:
    def __init__(self, data: List[Dict]):
        self.data = data

    def search(self, field: str, value: str) -> List[Dict]:
        """Recherche des lignes dans les données selon un critère."""
        return [row for row in self.data if row.get(field, '').lower() == value.lower()]
