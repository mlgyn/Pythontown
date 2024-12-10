from humain import Humain

class Dame(Humain):
    def __init__(self, nom, boisson_favorite="thé", couleur="rose", couleur_robe="rouge"):
        super().__init__(nom, boisson_favorite, couleur)
        self.__couleur_robe = couleur_robe
        self.etat = "libre"

    def se_faire_enlever(self):
        self.etat = "captive"
        self.parle("Au secours !")

    def se_faire_liberer(self, cowboy):
        if self.etat == "captive":
            self.etat = "libre"
            self.parle(f"Merci, {cowboy.quelEstTonNom()} ! Vous êtes mon héros !")

    def changer_de_robe(self, nouvelle_couleur):
        self.__couleur_robe = nouvelle_couleur
        self.parle(f"Regardez ma nouvelle robe {self.__couleur_robe} !")

    def manger(self):
        self.parle(f"{self.quelEstTonNom()} mange une salade fraîche, délicatement accompagnée de fruits frais. Très propre !")
