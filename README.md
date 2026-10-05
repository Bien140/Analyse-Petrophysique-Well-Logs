# Well Log Data Analysis and Petrophysical Interpretation

## Project Description
This project implements a complete data pipeline (ETL) to clean, store, and analyze well log data from the Kansas Geological Survey (KGS). The final objective is to generate a Well Log Plot to visually identify potential reservoir zones based on porosity and permeability indicators.

## Technologies Used
*   Language: Python 3.13
*   Data Processing: Pandas, NumPy
*   Database: PostgreSQL
*   ORM / Driver: SQLAlchemy, pg8000 driver
*   Data Visualization: Matplotlib
*   Security: python-dotenv

## Repository Structure
*   Filtre.ipynb: Jupyter Notebook dedicated to cleaning raw data and calculating porosity.
*   Importation_SQL.ipynb: Jupyter Notebook loading cleaned data into the PostgreSQL database.
*   analyse_visualisation.ipynb: Jupyter Notebook executing SQL queries and generating interpretation plots.
*   db_connection.py: Python module centralizing the database connection function.
*   .env: Configuration file containing database credentials (not versioned).
*   well_logs_clean.csv: CSV file containing the cleaned dataset.
*   well_log_plot.png: Output image of the final generated graph.

## Methodology

1.  Data Cleaning:
    *   Filtering outliers (negative resistivity values, unrealistic bulk density values).
    *   Excluding borehole washout zones using the Differential Caliper (DCAL) curve.
2.  Feature Engineering:
    *   Computing Density Porosity from the bulk density curve (RHOB), assuming a sandstone matrix (2.65 g/cm³) and aqueous fluid (1.0 g/cm³).
3.  Data Storage:
    *   Loading the cleaned dataset into a PostgreSQL relational database to facilitate analytical SQL queries.
4.  Visualization and Interpretation:
    *   Creating a three-track Well Log Plot (Spontaneous Potential, Deep Induction Resistivity, and Porosity) with an inverted depth axis.

## Results and Interpretation
The Well Log Plot analysis highlights a major zone of interest between 2000 and 2200 meters depth. This section exhibits a significant Spontaneous Potential (SP) deflection, indicating permeable rock, along with high porosity (exceeding 30%), confirming excellent storage capacity.

## Configuration and Security
This project uses a .env file to store database authentication details (username, password, database name). The .env file is excluded from Git tracking via a .gitignore file to prevent any sensitive data leakage.












# Analyse de Données de Puits et Interprétation Pétrophysique

## Description du Projet
Ce projet consiste à mettre en place un pipeline de données complet (ETL) pour nettoyer, stocker et analyser des données de diagraphie de puits (well logs) provenant du Kansas Geological Survey (KGS). L'objectif final est de générer un Well Log Plot afin d'identifier visuellement les zones réservoirs potentielles (zones à forte porosité et perméabilité).

## Technologies Utilisées
*   Langage : Python 3.13
*   Traitement de Données : Pandas, NumPy
*   Base de Données : PostgreSQL
*   ORM / Connecteur : SQLAlchemy, pilote pg8000
*   Visualisation : Matplotlib
*   Sécurité : python-dotenv

## Structure du Répertoire
*   Filtre.ipynb : Notebook Jupyter dédié au nettoyage des données brutes et au calcul de la porosité.
*   Importation_SQL.ipynb : Notebook Jupyter chargeant les données nettoyées dans la base de données PostgreSQL.
*   analyse_visualisation.ipynb : Notebook Jupyter exécutant des requêtes SQL et générant les graphiques d'interprétation.
*   db_connection.py : Module Python centralisant la fonction de connexion à la base de données.
*   .env : Fichier de configuration contenant les identifiants de connexion (non versionné).
*   well_logs_clean.csv : Fichier CSV contenant les données nettoyées.
*   well_log_plot.png : Image du graphique final généré.

## Méthodologie

1.  Nettoyage des Données (Data Cleaning) :
    *   Filtrage des valeurs aberrantes (résistivités négatives, densités irréalistes).
    *   Exclusion des zones d'effondrement du trou de forage (washouts) en utilisant la courbe DCAL.
2.  Ingénierie des Caractéristiques (Feature Engineering) :
    *   Calcul de la porosité (Density Porosity) à partir de la courbe de densité (RHOB), en supposant une matrice de grès (2.65 g/cm³) et un fluide aqueux (1.0 g/cm³).
3.  Stockage des Données :
    *   Chargement des données propres dans une base de données relationnelle PostgreSQL pour faciliter les requêtes analytiques.
4.  Visualisation et Interprétation :
    *   Création d'un Well Log Plot à trois pistes (SP, RILD, Porosité) avec inversion de l'axe des profondeurs.

## Résultats et Interprétation
L'analyse du Well Log Plot met en évidence une zone d'intérêt majeure située entre 2000 et 2200 mètres de profondeur. Cette section présente une déflexion significative de la courbe de Potentiel Spontané (SP), indiquant une roche perméable, ainsi qu'une porosité élevée (supérieure à 30%), confirmant une excellente capacité de stockage. 

## Configuration et Sécurité
Ce projet utilise un fichier .env pour stocker les informations d'authentification à la base de données (utilisateur, mot de passe, nom de la base). Le fichier .env est exclu du suivi Git via un fichier .gitignore afin de prévenir toute fuite de données sensibles.