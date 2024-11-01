def main():
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti = Kirja("Hytti nro 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    hytti.tulosta_tiedot()


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivut}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


main()