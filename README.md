# Projet Python HIBP

Pour ce projet vous devrez vérifier que vos utilisateurs n'utilisent pas un mot
de passe "corrompu" ("pwned"), pour cela vous avez
[ci-joint](example/users-database.csv) une base de données CSV avec un champ
`login` et un champ `password`, les mots de passe sont haché avec SHA1.

Votre script devra donc :
- parcourir le fichier CSV
- vérifier les empreintes de mots de passe contre l'API du site
  https://haveibeenpwned.com/
- récupérer les paramètres (chemin vers le CSV, URL de l'API, etc.) depuis un
  fichier de configuration
- gérer les erreurs courantes possibles (fichier de BDD non trouvé, etc.)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8
- bonus : utiliser des annotations de type
- bonus+ : ajouter la possibilité de surcharger la configuration via des
  paramètres de ligne de commande
- bonus++: être couvert par des tests unitaires

Si vous utilisez des bibliothèques tierces (non dans la stdlib), il faut les
indiquer dans un fichiers nommé `requirements.txt`, à rendre avec le projet.

En sortie votre script devra afficher le résultat du test pour chaque login.
Exemple :

```
$ python3 script.py
login    pwned      count
-------- ------- --------
toto     False          0
tata     True    23597311
tutu     True       53154
nkarolak False          0
```

Si vous souhaitez ajouter des utilisateurs au fichier CSV, la commande pour
générer un hash sha1 est la suivante :

```
echo -n 'mon mot de passe' | sha1sum
```

À rendre, un fichier ZIP (`NOM1_NOM2_NOM3.zip`) avec le contenu suivant :

```
$ tree NOM1_NOM2_NOM3
├── config.ini          <- votre fichier de configuration
├── README.md           <- une petite documentation d'installation et d'utilisation, c'est toujours utile
├── requirements.txt    <- vos dépendances tierces, s'il y en a
├── script.py           <- votre script
├── test_script.py      <- vos tests unitaires si vous êtes un ou une Pythoniste chevronnée
└── users-database.csv  <- votre base de données
```

Le contenu du fichier `users-database.csv` :

```
login;password
toto;76e4b28b5527652fd7af9a57e17f6adce5bbba78
tata;7c4a8d09ca3762af61e59520943dc26494f8941b
tutu;57b2ad99044d337197c0c39fd3823568ff81e48a
nkarolak;90ecc5a92e2ddf496cbc3d12912ee1bcc8aaf01e
monuser;5f1af74861a055b2afdbd86a5c6acc82786b02ce
```
