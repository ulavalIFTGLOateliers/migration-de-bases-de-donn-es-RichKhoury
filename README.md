# Atelier sur l'utilisation d'une base de données partagée

## Introduction

Le but de cet atelier est de vous familiariser avec les bonnes pratiques de travail en équipe sur une même base de données - que celle-ci soit hébergée localement sur l'ordinateur de chacun, ou qu'elle soit hébergée dans le cloud.

L'atelier aborde deux sujets:

- La configuration de votre environnement de travail
- La migration de schéma d'une base de données partagée

## Déroulement et correction

Ce document vous indique étape par étape les tâches à réaliser. À tout moment, vous pouvez rouler le script *grading.py* se situant dans le dossier *grading/* afin d'avoir un apperçu du nombre de tests qui réussissent ou qui échouent. Afin de rouler le fichier, il suffit de taper la commande:
```shell
python grading/grading.py
```

La correction finale se fera de manière automatique en utilisant les mêmes tests que ceux du script *grading.py*. Vous pouvez donc vous fier à ce script pour savoir si votre code fonctionne ou non.

## Prérequis

Vous devez avoir MySQL8 / Oracle et Python installés sur votre machine.

Plusieurs packages Python sont requis pour ce projet. Afin de tous les installer facilement, roulez la commande:
```shell
pip install -r requirements.txt
```

## Mise en situation et structure du code

Ce projet représente une application web simple représentant un domaine musical. L'application comprend un serveur Flask, une interface HTML ainsi qu'une base de données. Cependant, cette base de données n'est pas encore configurée ni connectée au projet. Ceci sera votre première tâche. Au cours de l'atelier, vous aurez à modifier le fichier *database.py* ainsi que les fichiers migrate_*.sql et rollback_*.sql situés dans le dossier *scripts*. Vous n'aurez pas à toucher aux autres fichiers, cependant vous pouvez vous référer à [DOCUMENTATION.md](https://github.com/ulaval-atelier-bd/ulaval-atelier-starter-code/blob/master/DOCUMENTATION.md) pour en connaître leur utilité. Le schéma initial de la base de données ainsi que les schémas cibles vers lesquels vous aurez à migrer sont illustrés dans le fichier [SCHEMA.md](https://github.com/ulaval-atelier-bd/ulaval-atelier-starter-code/blob/master/SCHEMA.md).

Afin de rouler l'application web, il suffit de rouler le script *server.py*:
```shell
python server.py
```
**Attention: cette commande ne fonctionnera pas tant que vous n'aurez pas complété l'étape 1.**

Une fois le serveur lancé, ouvrez votre navigateur et dirigez vous vers l'URL 127.0.0.1:5000 afin d'afficher l'interface graphique.

## Étape 1 - Configurer votre environnement de travail

Le but de cette étape est de comprendre comment travailler sur une même base de données en équipe. Cet atelier s'effectue sur une base de données hébergée en local sur votre machine, cependant les principes restes les mêmes pour une base de données hébergée sur un cloud.

Lorsque vous travaillez en équipe sur une base de code partagée, vous utilisez un système de gestion du versionnage tel que *git*. Dans un tel projet, le code servant d'interface vers la BD est commun à tous. Dans le cas de cet atelier, ce code se trouve dans la classe **Database** dans le dossier *database.py*. Cependant, puisque chaque membre de l'équipe héberge sa propre version de la base de données en local sur sa machine, il est impossible d'écrire les informations de connexion directement dans le code, puisque celles-ci diffèrent pour chaque machine. De plus, ceci constituerait une faille de sécurité car n'importe qui ayant accès au repo Github pourrait lire les identifiants de connexion. Comment procéder?

### Utiliser des variables d'environnement

La solution à ce problème est d'utiliser des variables d'environnement. Celles-ci sont des variables externes au programme, dont les valeurs peuvent être récupérer au moment de l'exécution du programme. Chaque membre de l'équipe aura donc ses propres variables d'environnement contenant les informations de connexion à leur BD locale.

Pour commencer, vous devez créer une nouvelle base de données nommée *atelier_bd* sur votre serveur SQL local:
```sql
CREATE DATABASE atelier_bd;
USE atelier_bd;
```

Maintenant, vous devez créer les variables d'environnement propices à la bonne connexion de l'application à cette base de données. Pour ce faire, une bonne pratique est de mettre ces variables dans un fichier **.env** qui se trouve à la racine de votre projet. Par la suite, il sera possible d'indiquer à l'application d'aller récupérer les valeurs souhaitées directement dans ce fichier.

**Créez un fichier .env à la racine de votre projet.**

**À l'intérieur de ce fichier, vous devez ajouter les variables d'environnement**. Le format d'un fichier **.env** est une paire clé-valeur (nom de la variable ainsi que sa valeur) par ligne:
```
VAR1=VALEUR1
VAR2=VALEUR2
```

Vous devez ajouter les 5 variables d'environnement suivantes, nommées exactement comme ceci:

- HOST: l'adresse de votre serveur SQL. En local, ceci est 127.0.0.1
- PORT: le numéro de port de votre serveur SQL. Par défaut, MySQL roule sur le port 3306, et Oracle sur le port 1521
- DATABASE: le nom de votre BD. Dans notre cas, **atelier_bd**
- USER: votre nom d'utilisateur pour votre serveur
- PASSWORD: votre mot de passe


### Récupérer des variables d'environnement

Maintenant que vos variables sont bien créées, il faut indiquer à notre programme 