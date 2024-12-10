from humain import Humain

class Barman(Humain):
    def __init__(self, nom, bar_name=None, couleur="brun"):
        super().__init__(nom, "vin",couleur)
        self.__bar_name = bar_name if bar_name else f"Chez {nom}"

    def servir(self, humain):
        print(f"{self.quelEstTonNom()} sert un verre de {humain.quelleEstTaBoisson()} à {humain.quelEstTonNom()}.")

    def se_presenter(self):
        self.parle(f"Bienvenue {self.__bar_name}. Je suis {self.quelEstTonNom()}, le barman.")

    def manger(self):
        self.parle(f"{self.quelEstTonNom()} mange un bon morceau de fromage accompagné de pain, et termine avec un verre de vin.")
