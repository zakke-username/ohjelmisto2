def main():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    bensa_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(123)
    bensa_auto.kiihdyta(150)

    sahkoauto.kulje(3)
    bensa_auto.kulje(3)

    print("\n")
    sahkoauto.tulosta_tiedot()
    print("\n")
    bensa_auto.tulosta_tiedot()


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        self.nopeus = max(0, min(self.nopeus, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.nopeus

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus {self.rekisteritunnus}\nHuippunopeus: {self.huippunopeus}\nNykyinen nopeus: {self.nopeus}\nKuljettu matka: {self.kuljettu_matka}")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


main()