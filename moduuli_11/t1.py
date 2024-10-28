def main():
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti = Kirja("Hytti nro 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    hytti.tulosta_tiedot()


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)
    
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivut}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, päätoimittaja: {self.paatoimittaja}")


main()