# Grand-debat
Récolte et ouverture des données du grand débat

# Utilisation
Le script stocke les informations uniquement des réunions pour l'instant dans une base de données MongoDB.
Pour l'utiliser, renommez `config.json.example` en `config.json` et remplacez les champs comme nécessaire.
Vous pouvez ensuite lancer la récupération d'informations avec la commande suivante:
`python main.py`
Si vous préférez utiliser un fichier `csv`, le script `build_csv.py` vous permettera de le faire avec la commande suivante:
`python build_csv.py`

# Vie privée
Pour des raisons de respect de la vie privée, le script ne stocke pas les `username`, `displayname` et `id` des citoyens. Cela est fait dans la fonction `clean_event` du fichier `granddebat/db.py`

# Remarques
L'utilisation de l'API graphQl en utilisant la requete en dur n'est peut-être pas la meilleure façon de faire, mais je n'ai pas trouvé de libs graphQL en python permettant de passer des arguments de la même manière que l'API graphql du site du gran débat
