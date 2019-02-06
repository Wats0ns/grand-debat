# Grand-debat
Récolte et ouverture des données du grand débat

# Utilisation
Le script stocke les informations uniquement des réunions pour l'instant dans une base de données MongoDB.
Pour l'utiliser, renommez `config.json.example` en `config.json` et remplacez les champs comme nécessaire.
Vous pouvez ensuite lancer la récupération d'informations avec la commande suivante:
`python main.py`
Si vous préférez utiliser un fichier `csv`, le script `build_csv.py` vous permettera de le faire avec la commande suivante:
`python build_csv.py`
