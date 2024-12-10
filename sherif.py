from cowboy import Cowboy

class Sherif(Cowboy):
    def __init__(self, nom, boisson_favorite="eau", couleur="vert"):
        # Le shérif est un cowboy, donc on utilise le constructeur de Cowboy
        super().__init__(nom, boisson_favorite, couleur)
        self.__nombre_brigands_arretes = 5

    def se_presenter(self):
        # Le shérif se présente en mentionnant combien de brigands il a coffrés
        super().se_presenter()
        self.parle(f"J'ai arrêté {self.__nombre_brigands_arretes} brigand(s).")

    def coffrer(self, brigand):
        # Le shérif arrête un brigand et l'emmène en prison
        self.__nombre_brigands_arretes += 1
        brigand.se_faire_emprisonner(self)
        self.parle("Au nom de la loi, je vous arrête !")

    def rechercher_brigand(self, brigand):
        # Le shérif met une affiche pour rechercher le brigand
        self.parle(f"Je suis à la recherche de {brigand.quelEstTonNom()}, le plus dangereux des brigands.")
        print(f"OYEZ OYEZ BRAVE GENS !! 200 $ à qui arrêtera {brigand.quelEstTonNom()} mort ou vif !")
       
 