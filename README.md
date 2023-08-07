# Atelier sur l'utilisation d'une base de données partagée

## Introduction

Le but de cet atelier est de vous familiariser avec les bonnes pratiques de travail en équipe sur une même base de données - que celle-ci soit hébergée localement sur l'ordinateur de chacun, ou qu'elle soit hébergée dans le cloud.

L'atelier aborde deux sujets:

- La configuration de votre environnement de travail
- La migration de schéma d'une base de données partagée

## Déroulement et correction

Ce document vous indique étape par étape les tâches à réaliser. À tout moment, vous pouvez rouler le script *grading.py* se situant dans le dossier *grading/* afin d'avoir un apperçu du nombre de tests qui réussissent ou qui échouent. Afin de rouler le fichier, il suffit de taper la commande:
```
python grading/grading.py
```

La correction finale se fera de manière automatique en utilisant les mêmes tests que ceux du script *grading.py*. Vous pouvez donc vous fier à ce script pour savoir si votre code fonctionne ou non.

## Prérequis

Vous devez avoir MySQL8 et Python installés sur votre machine.

Plusieurs packages Python sont requis pour ce projet. Afin de tous les installer facilement, roulez la commande:
```
pip install -r requirements.txt
```

## Mise en situation et présentation du code

Ce projet représente une application web simple représentant un domaine musical. L'application comprend un serveur Flask, une interface HTML ainsi qu'une base de données. Cependant, cette base de données n'est pas encore configurée ni connectée au projet. Ceci sera votre première tâche. 