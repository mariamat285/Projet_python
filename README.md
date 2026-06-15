# Système de Nettoyage de Données Médicales

Projet de Programmation Python 1 — Université Rose Dieng  
Année Académique 2025-2026

## Autrices

- **Mariama Thiam**
- **Khadidiatou Diasse**

---

## Description

Ce programme permet de charger, nettoyer, valider et exporter un fichier de données patients brutes (`patients_bruts.txt`). Il détecte automatiquement les anomalies, rejette les patients invalides, supprime les doublons et produit un dataset propre exploitable par les équipes data science.

---

## Structure du projet

```
projet_python/
├── data/
│   ├── patients_bruts.txt        # Fichier de données brutes
│   ├── patients_propres.csv      # Généré après export
│   └── patients_propres.json     # Généré après export (bonus)
├── rapport/
│   └── rapport.txt               # Généré après export
├── logs/
│   └── logs.txt                  # Généré automatiquement(bonus)
├── src/
│   ├── main.py                   # Menu principal
│   ├── chargement.py             # Lecture du fichier
│   ├── nettoyage.py              # Fonctions de nettoyage
│   ├── validation.py             # Vérification des données
│   ├── statistiques.py           # Calculs et statistiques
│   ├── export.py                 # Écriture des fichiers de sortie
│   ├── recherche.py              # Recherche de patients (bonus)
│   ├── choix.py                  # Logique des options du menu (bonus)
│   └── logs.py                   # Système de logs automatiques (bonus)
└── README.md
```
```

---

## Lancer le programme

Depuis la racine du projet :

```bash
python src/main.py
```
## Menu

```
============================================
 SYSTÈME DE NETTOYAGE DE DONNÉES MÉDICALES
============================================
1. Charger les données brutes
2. Afficher les anomalies détectées
3. Nettoyer les données
4. Afficher les statistiques
5. Exporter les données propres
6. Quitter
```

---

## Description des modules

| Module | Rôle |
|---|---|
| `chargement.py` | Lit le fichier brut et retourne une liste de dictionnaires patients |
| `nettoyage.py` | Corrige les formats — noms, téléphones, villes, doublons |
| `validation.py` | Vérifie chaque champ et détecte les anomalies |
| `statistiques.py` | Calcule les statistiques sur les patients valides |
| `export.py` | Exporte les données propres en CSV, JSON et rapport texte |
| `recherche.py` | Recherche un patient par critère dans les données propres |
| `choix.py` | Gère la logique de chaque option du menu de manière modulaire |
| `logs.py` | Enregistre automatiquement chaque action avec horodatage |
---

## Erreurs gérées

- Noms/prénoms mal formatés (minuscules, majuscules, espaces)
- Âges invalides (manquant, négatif, supérieur à 120)
- Téléphones mal formatés (espaces, tirets, préfixes internationaux)
- Villes mal orthographiées
- Groupes sanguins invalides
- Poids et tailles non numériques ou hors limites
- Doublons exacts et quasi-doublons

---

## Technologies utilisées

- Python 3
- Modules standard : `csv`, `json`, `datetime`
