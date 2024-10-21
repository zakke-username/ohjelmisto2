def main():
    uusi_auto = Auto("ABC-123", 142)
    # uusi_auto.kuljettu_matka = 2000
    # uusi_auto.kiihdyta(60)
    # uusi_auto.kulje(1.5)
    # print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")


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


main()
