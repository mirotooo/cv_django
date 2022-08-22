# cv_django
Mon CV avec Django

Pour utiliser le code il faut cloner le repository. Il y aura un dossier nommé `cv_django-main`.

Ensuite il faut créer l'environnement, ouvrir un terminal dans le dossier qui <strong>contient</strong> le dossier nommé `cv_django-main`

```
py -m venv virtual_env
```

Il faut également activer l'environnement:

```
.\virtual_env\Scripts\activate
```

Ensuite installer les dépendances:

```
pip install -r ./cv_django-main/requirements.txt
```

Dans le meme terminal, lancer le serveur:

```
py .\cv_django-main\manage.py runserver
```
