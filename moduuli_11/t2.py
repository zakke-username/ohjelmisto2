def main():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    sahkoauto.kiihdyta(123)

    bensa_auto = Polttomoottoriauto("ACD-123", 165, 32.3)
    bensa_auto.kiihdyta(150)

    sahkoauto.kulje(3)
    bensa_auto.kulje(3)

    print(f"Sähköauto kulkenut {sahkoauto.kuljettu_matka} km, polttomoottoriauto kulkenut {bensa_auto.kuljettu_matka} km")


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


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


main()