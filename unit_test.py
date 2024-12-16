import unittest
from data_loader import DataLoader
from search import SearchEngine
from report_generator import ReportGenerator
import os
import csv

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        """Création d'un dossier temporaire avec des fichiers CSV pour les tests."""
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)
        self.create_test_csv("test1.csv", [
            {"nom": "Produit A", "catégorie": "Catégorie 1", "prix_unitaire": "10"},
            {"nom": "Produit B", "catégorie": "Catégorie 2", "prix_unitaire": "20"},
        ])

    def tearDown(self):
        """Supprime le dossier temporaire après les tests."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def create_test_csv(self, filename, data):
        """Crée un fichier CSV de test."""
        with open(os.path.join(self.test_dir, filename), 'w', newline='') as f:
            header = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    def test_load_csv_files(self):
        """Test du chargement des fichiers CSV."""
        loader = DataLoader(self.test_dir)
        loader.load_csv_files()
        data = loader.get_data()
        self.assertEqual(len(data), 2)  # Vérifie que 2 lignes ont été chargées
        self.assertEqual(data[0]["nom"], "Produit A")  # Vérifie le contenu du premier produit

class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        """Données de test pour les tests de recherche."""
        self.data = [
            {"nom": "Produit A", "catégorie": "Catégorie 1", "prix_unitaire": "10"},
            {"nom": "Produit B", "catégorie": "Catégorie 2", "prix_unitaire": "20"},
            {"nom": "Produit C", "catégorie": "Catégorie 1", "prix_unitaire": "30"},
        ]
        self.search_engine = SearchEngine(self.data)

    def test_search(self):
        """Test de la méthode de recherche simple."""
        results = self.search_engine.search("nom", "Produit A")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["nom"], "Produit A")

    def test_advanced_search(self):
        """Test de la méthode de recherche avancée."""
        results = self.search_engine.advanced_search("prix_unitaire", ">", "15")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["nom"], "Produit B")

class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        """Données de test pour les tests de génération de rapport."""
        self.data = [
            {"nom": "Produit A", "catégorie": "Catégorie 1", "prix_unitaire": "10"},
            {"nom": "Produit B", "catégorie": "Catégorie 2", "prix_unitaire": "20"},
        ]
        self.output_file = "test_report.csv"

    def tearDown(self):
        """Supprime le fichier de rapport généré après les tests."""
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_summary(self):
        """Test de la génération du rapport."""
        report_generator = ReportGenerator(self.data)
        report_generator.generate_summary(self.output_file)

        # Vérifie que le fichier a été créé
        self.assertTrue(os.path.exists(self.output_file))

        # Vérifie le contenu du fichier
        with open(self.output_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 2)  # Vérifie que 2 lignes ont été écrites
            self.assertEqual(rows[0]["nom"], "Produit A")  # Vérifie le contenu

if __name__ == "__main__":
    unittest.main()
