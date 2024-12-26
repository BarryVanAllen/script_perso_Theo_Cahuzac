# script_perso

## Description

Ce projet est un programme qui permet de charger et de manipuler des fichiers CSV. Il offre une interface interactive pour rechercher des données selon différents critères.

## Prérequis

- Python 3.x
- Bibliothèques Python nécessaires (pandas)

## Installation

1. télécharger les fichiers
     télécharger tout les fichiers et les installer selon l'arborescence suivante :
   structure : 
├── main.py                # Script principal du programme
│
├── data/                  # Dossier contenant les fichiers CSV
│   ├── fichier1.csv
│   ├── fichier2.csv
│   └── ...
|── utils/                 # Dossier pour les fonctions utilitaires (si applicable)
    ├── data_loader.py     # Chargement des données
    ├── report_generator.py # Génération de rapports
    └── ...
      

3. installer pandas dans le powerShell
     pip install pandas

3.lancer le programme dans le powershell et dans le répertoire courant de votre installation
  python main.py
![Capture d'écran 2024-12-16 175826](https://github.com/user-attachments/assets/43efe2e2-093c-4a9a-aea4-5fcd52d0b27f)

##exemple de commande et les résultats :
**data = dir ou se trouve les fichiers csv, --field = sur quoi on va trier, --operator = l'operateur, --value = la valeur que l'on veut.**
python main.py data --field "prix_unitaire" --operator "<" --value "100"
![Capture d'écran 2024-12-26 175431](https://github.com/user-attachments/assets/68d8bc54-fed1-44b4-a8b8-b8102be41fcb)


python main.py data --field "categorie" --operator "==" --value "electronique"
![Capture d'écran 2024-12-26 175452](https://github.com/user-attachments/assets/972b245c-a083-484b-ab1f-89c18303d50c)

