# PythonTown : Le projet Western en Python

## Introduction

Bienvenue dans **PythonTown**, un projet en Python où vous pouvez créer des histoires Western avec des personnages comme des brigands, cowboys, dames en détresse, barmen, et shérifs. Ce projet utilise la Programmation Orientée Objet (POO) pour modéliser les personnages et les interactions dans un univers Western.

### Fonctionnalités

- **Humains** : Tous les personnages sont des humains avec des attributs comme leur nom et leur boisson favorite.
- **Héritage** : Les classes de personnages (Brigand, Cowboy, Dame) héritent d'une classe de base `Humain`, permettant de réutiliser les fonctionnalités communes.
- **Surcharge** : Les classes filles redéfinissent certaines méthodes héritées pour ajuster le comportement des personnages (par exemple, la présentation du nom).
- **Interactions** : Les personnages peuvent interagir entre eux (kidnapping, libération, et autres actions).

## Structure du projet

Le projet est divisé en plusieurs classes représentant les différents personnages et leurs interactions :

1. **Classe `Humain`** : Représente un humain avec un nom et une boisson favorite.
2. **Classe `Brigand`** : Hérite de `Humain` et ajoute des comportements spécifiques aux brigands, comme le kidnapping des dames.
3. **Classe `Cowboy`** : Hérite de `Humain` et permet de libérer les dames en détresse.
4. **Classe `Dame`** : Hérite de `Humain` et a des attributs spécifiques comme la couleur de sa robe et son statut (libre ou captive).
5. **Classe `Barman`** : Un barman qui sert des boissons et termine ses phrases par "Coco".
6. **Classe `Sherif`** : Un shérif qui capture les brigands et maintient l'ordre.

## Prérequis

- **Python 3.x** est recommandé.
- Aucune bibliothèque externe n'est nécessaire pour ce projet.

## Comment lancer le projet

1. Clonez ou téléchargez ce projet sur votre machine.
2. Ouvrez votre terminal ou invite de commandes.
3. Allez dans le dossier du projet.
4. Exécutez le fichier principal avec la commande :

```bash
python main.py
```

Cela lancera le programme et vous permettra de voir les personnages interagir entre eux.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou des fonctionnalités à ajouter, n'hésitez pas à ouvrir une _issue_ ou à soumettre une _pull request_.

---

Merci d'avoir choisi de travailler sur **PythonTown** ! Amusez-vous bien avec l'aventure et bon codage !
