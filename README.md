# projetDjango : une petite application pour expérimenter les tests dans Django

## Objectif
Ce programme est un exercice proposé par [OpenClassRooms](https://openclassrooms.com/fr/) dans le cadre de la formation :
Développeur d'applications Python. L'objectif est d'expérimenter les tests comme expliquer dans la formation
[Testez votre projet python](https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python)


## Fonctionnalités
L'application permet de :
* -> 

## Technologie utilisée
* Le projet est développé avec le framework Django. 
* Les données sont sauvegardées dans une base de données sqlite3.
* La librarie pytest est utilisée pour assurer la qualité de l'application.

## Installation
* Téléchargez et dézippez le repository github
* Creer l'environnement virtuel (exemple avec pipenv)
``` bash
mkdir .venv
pipenv install
pipenv shell
```

## Utilisation
* Lancer le serveur : `python manage.py runserver`
* Depuis votre navigateur habituel, l'accès à l'application via l'url : `http:/127.0.0.1:8000`
* Pour creer un compte administrateur, utilisez la commande : `python manage.py createsuperuser`
* Pour accéder à l'administration : `http://127.0.0.1:8000/admin`
