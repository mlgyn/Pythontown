from abc import ABC, abstractmethod

class Humain(ABC):
    def __init__(self, nom, boisson_favorite="eau",  couleur="pas de couleur"):
        self.__nom = nom
        self.__boisson_favorite = boisson_favorite
        self.__couleur = couleur

    def parle(self, texte):
        couleur_code = self.get_color_code()  
        print(f"{couleur_code}{self.quelEstTonNom()} dit : {texte}\033[0m")

    def se_presenter(self):
        self.parle(f"Bonjour, je suis {self.__nom} et ma boisson favorite est {self.__boisson_favorite}.")

    def boire(self):
        self.parle(f"Ah ! un bon verre de {self.__boisson_favorite} ! GLOUPS !")

    def quelEstTonNom(self):
        return self.__nom

    def quelleEstTaBoisson(self):
        return self.__boisson_favorite
    
    def quelEstTaCouleur(self):
        return self.__couleur  # Retourne la couleur du personnage
    
    def get_color_code(self):
        # Dictionnaire pour les couleurs de base. Vous pouvez l'étendre.
        couleurs = {
            "rouge": "\033[31m",
            "bleu": "\033[34m",
            "vert": "\033[32m",
            "jaune": "\033[33m",
            "cyan": "\033[36m",
            "magenta": "\033[35m",
            "gris": "\033[37m",
            "noir": "\033[30m",
            "brun": "\033[38;5;94m", 
            "rose": "\033[38;5;213m",  # Ajout de la couleur rose
            "pas de couleur": "\033[0m"  # Si aucune couleur n'est définie, pas de changement
        }
        return couleurs.get(self.__couleur, "\033[0m")

    @abstractmethod
    def manger(self):
        pass  # Cette méthode doit être implémentée dans chaque sous-classe
