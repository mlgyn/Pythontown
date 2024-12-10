from humain import Humain

class Cowboy(Humain):
    def __init__(self, nom, boisson_favorite="lait", couleur="bleu"):
        super().__init__(nom, boisson_favorite, couleur)
        self.__popularite = 150

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Ma popularité est de {self.__popularite}.")


    def tirer_sur(self, brigand):
        print(f"Le  {self.quelEstTonNom()} tire sur {brigand.quelEstTonNom()}. PAN !")
        self.parle("Prend ça, rascal !")

    def liberer(self, dame):
        if dame.etat == "captive":
            dame.se_faire_liberer(self)
            self.__popularite += 1
        else:
            self.parle(f"{dame.quelEstTonNom()} est déjà libre.")

    def manger(self):
        self.parle(f"{self.quelEstTonNom()} mange un steak bien saignant, sans cérémonie, accompagné de quelques haricots. Pas de manières !")
