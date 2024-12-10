from humain import Humain

class Brigand(Humain):
    def __init__(self, nom, boisson_favorite="whisky", look="terrifiant", couleur="rouge"):
        super().__init__(nom, boisson_favorite, couleur)
        self.__look = look
        self.__en_prison = False
        self.__dames_enlevees = 2

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Je suis {self.__look}.")
        self.parle(f"J'ai déjà capturé {self.__dames_enlevees} dames.")

    def kidnapper(self, dame):
        if dame.etat == "libre":
            dame.se_faire_enlever()
            self.__dames_enlevees += 1
            self.parle(f"Ah ah ! {dame.quelEstTonNom()}, tu es mienne désormais !")
        else:
            self.parle(f"{dame.quelEstTonNom()} est déjà captive !")

    def se_faire_emprisonner(self, cowboy):
        self.__en_prison = True
        self.parle(f"Damned, je suis fait ! {cowboy.quelEstTonNom()}, tu m'as eu !")

    def manger(self):
        self.parle(f"{self.quelEstTonNom()} mange une grosse miche de pain avec des beans, tout en bavouillant ! Miam !")
