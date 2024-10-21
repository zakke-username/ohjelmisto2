def main():
    uusi_auto = Auto("ABC-123", 142)
    uusi_auto.kiihdyta(30)
    uusi_auto.kiihdyta(70)
    uusi_auto.kiihdyta(50)
    print(f"Nopeus: {uusi_auto.nopeus} km/h")
    print("Hätäjarrutus!")
    uusi_auto.kiihdyta(-200)
    print(f"Nopeus: {uusi_auto.nopeus} km/h")


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        self.nopeus = max(0, min(self.nopeus, self.huippunopeus))


main()
