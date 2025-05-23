
# Nettoyeur de fichiers RDF et RIS bib_nettoyage_RIS_RDF.py

## Description
Ce projet est un script Python conçu pour nettoyer automatiquement des fichiers `.rdf` et `.ris` en supprimant certaines balises ou lignes spécifiques. Il est conçu pour être simple à utiliser, même si vous n'avez pas de connaissances techniques.

## Fonctionnalités
- Supprime les balises `<DC:subject>` et `<dcterms:abstract>` dans les fichiers `.rdf`
- Supprime les lignes commençant par `KW  -` (mots-clés) et `AB  -` (résumés) dans les fichiers `.ris`
- Crée des copies corrigées dans un dossier nommé `fichier corrigé`
- Affiche un résumé des éléments supprimés

## Prérequis
- Windows 10 ou 11
- Python 3 installé (téléchargeable ici : https://www.python.org/downloads/)

## Installation
1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous que Python 3 est installé sur votre machine.

## Utilisation
1. Placez tous vos fichiers `.rdf` et `.ris` dans le même dossier que ce script.
2. Double-cliquez sur le fichier `bib_nettoyage_RIS_RDF.py` (ou faites un clic droit > Ouvrir avec > Python).
3. Une fenêtre s'ouvrira et vous demandera si les fichiers sont bien placés. Cliquez sur "Oui" pour lancer le nettoyage.

## Résultats attendus
- Un dossier nommé `fichiers nettoyes` sera créé automatiquement.
- Les fichiers nettoyés y seront enregistrés avec la date du jour ajoutée à leur nom.
- Une fenêtre vous indiquera combien de balises ou lignes ont été supprimées.

## Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une *issue* ou une *pull request* pour toute amélioration ou correction.

