# e-library

Une interface Web à la base de données SQLite `library.db` utilisée dans le cours

## Installation du dépôt
 
Pour installer l'application Web, il faut entrer les commandes suivantes qui ont
été testées sur un environnement de type "Custom" dans Cloud9 (https://c9.io)

```{bash}

$ git clone https://github.com/oci1315/oci-webapp-elibrary.git
$ python3 -m venv venv
$ source activate venv/bin/activate
$ cd oci-webapp-elibrary
$ pip install -r requirements.txt

```

# Démarrer le serveur 

```{bash}

$ python app.py

```