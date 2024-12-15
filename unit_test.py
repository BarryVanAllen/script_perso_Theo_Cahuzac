import unittest
import os
from unittest.mock import patch
from data_loader import DataLoader
from search import SearchEngine
from report_generator import ReportGenerator
import main
import argparse


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        # Création de fichiers CSV temporaires pour les tests
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)

        with open(f"{self.test_dir}/file1.csv", "w") as f:
            f.write("name,category,quantity,price\nPhone,Electronics,50,699\n")

        with open(f"{self.test_dir}/file2.csv", "w") as f:
            f.write("name,category,quantity,price\nLaptop,Electronics,20,999\n")

    def tearDown(self):
        # Suppression des fichiers après les tests
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_load_csv_files(self):
        loader = DataLoader(self.test_dir)
        loader.load_csv_files()
        data = loader.get_data()
        self.assertEqual(len(data), 2)  # 2 lignes chargées
        self.assertEqual(data[0]["name"], "Phone")  # Vérifie# les données


class TestSearchEngine(unittest.TestCase):
    #on met le contenu des fchiers csv pour tester
    def setUp(self):
        self.data = [
            {"name": "Phone", "category": "Electronics", "quantity": "50", "price": "699"},
            {"name": "Laptop", "category": "Electronics", "quantity": "20", "price": "999"},
            {"name": "Laptop", "category": "Electronics", "quantity": "20", "price": "999"},
            {"name": "Laptop", "category": "Electronics", "quantity": "20", "price": "999"},
            {"name": "Chair", "category": "Furniture", "quantity": "200", "price": "49"}
        ]

    def test_search_by_category(self):
        engine = SearchEngine(self.data)
        results = engine.search("category", "Electronics")
        self.assertEqual(len(results), 4)  # Deux résultats trouvés
        self.assertEqual(results[0]["name"], "Phone")

    #vérifie si prend compte des doublons
        results2 = engine.search("name", "Laptop")
        self.assertEqual(len(results2), 3)



    def test_search_no_results(self):
        engine = SearchEngine(self.data)
        results = engine.search("category", "Toys")
        self.assertEqual(len(results), 0)  # Aucun résultat


class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"name": "Phone", "category": "Electronics", "quantity": "50", "price": "699"},
            {"name": "Laptop", "category": "Electronics", "quantity": "20", "price": "999"}
        ]
        self.output_file = "test_report.csv"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_summary(self):
        generator = ReportGenerator(self.data)
        generator.generate_summary(self.output_file)
        self.assertTrue(os.path.exists(self.output_file))  # Vérifie que le fichier est créé

        # Vérifie le contenu du fichier
        with open(self.output_file, "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 3)  # 1 ligne d'en-tête + 2 lignes de données


class TestMainScript(unittest.TestCase):
    def setUp(self):
        # Préparer les fichiers CSV de test
        self.test_dir = os.path.abspath("test_data")
        os.makedirs(self.test_dir, exist_ok=True)

        with open(os.path.join(self.test_dir, "file1.csv"), "w") as f:
            f.write("name,category,quantity,price\nPhone,Electronics,50,699\n")

        with open(os.path.join(self.test_dir, "file2.csv"), "w") as f:
            f.write("name,category,quantity,price\nLaptop,Electronics,20,999\n")

        self.output_file = os.path.abspath("test_summary.csv")

    def tearDown(self):
        # Nettoyer les fichiers après les tests
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    @patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
        directory=os.path.abspath("test_data"), search=None, report=os.path.abspath("test_summary.csv")))
    def test_generate_report(self, mock_args):
        # Vérifie la génération de rapport via le script principal
        main.main()
        self.assertTrue(os.path.exists(self.output_file))