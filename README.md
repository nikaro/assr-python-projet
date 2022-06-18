# Projet Python HIBP

Pour ce projet vous devrez vérifier que vos utilisateurs n'utilisent pas un mot
de passe "corrompu" ("pwned"), pour cela vous avez à disposition une base de
données (CSV ou SQLite au choix) avec un champ `login` et un champ `password`,
les mots de passe sont haché avec SHA1.

Votre script devra donc :
- parcourir la base de données
- vérifier les empreintes de mots de passe contre l'API du site
  https://haveibeenpwned.com/
- récupérer les paramètres (chemin vers la BDD, URL de l'API, etc.) depuis un
  fichier de configuration
- gérer les erreurs courantes possibles (fichier de BDD non trouvé, etc.)
- être découpé en fonctions (une pour chaque partie essentielle du script)
- être conforme au guide de style PEP8
- bonus : utiliser des annotations de type
- bonus+ : ajouter la possibilité de surcharger la configuration via des
  paramètres de ligne de commande

Si vous utilisez des bibliothèques tierces (non dans la stdlib), il faut les
indiquer dans un fichiers nommé `requirements.txt`, à rendre avec le projet.

En sortie votre script devra afficher le résultat du test pour chaque login.
Exemple :

```
$ python3 script.py
login    pwned      count
-------- ------- --------
toto     False          *
tata     True    ********
tutu     True       *****
nkarolak False          *
```

Si vous souhaitez ajouter des utilisateurs à la base de données, la commande
pour générer un hash sha1 est la suivante :

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
└── users-database.*    <- votre base de données
```
