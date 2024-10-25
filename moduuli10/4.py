import random


def main():
    autot = []
    for i in range(10):
        uusi_auto = Auto(f"ABC-{i+1}", random.randint(100,200))
        autot.append(uusi_auto)
    #
    # for i in range(100000):
    #     kisa = Kilpailu("testi", 8000, autot)
    #     for a in autot:
    #         a.huippunopeus = random.randint(100,200)
    #         a.nopeus = 0
    #         a.kuljettu_matka = 0
    #     tunti = 0
    #     while True:
    #         kisa.tunti_kuluu()
    #         if kisa.kilpailu_ohi():
    #             break
    #         tunti += 1
    #
    # for a in autot:
    #     print(a.rekisteritunnus, a.voitot)

    kisa = Kilpailu("Suuri romuralli", 8000, autot)
    i = 0
    while True:
        kisa.tunti_kuluu()
        if i % 10 == 0 and i > 0:
            print(f"\n\nTilanne tunnilla {i}:\n")
            kisa.tulosta_tilanne()
        if kisa.kilpailu_ohi():
            break
        i += 1
    print("\n\nKisa ohi! Lopputilanne:\n")
    kisa.tulosta_tilanne()


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    
    def tunti_kuluu(self):
        for a in self.autot:
            a.kiihdyta(random.randint(-10,15))
            a.kulje(1)
    
    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':16} {'Kuljettu matka':16} {'Huippunopeus':16} {'Nykyinen nopeus':16}")
        for a in self.autot:
            print(f"{a.rekisteritunnus:16} {a.kuljettu_matka:<16} {a.huippunopeus:<16} {a.nopeus:<16}")
    
    def kilpailu_ohi(self):
        maalissa = False
        for a in self.autot:
            if a.kuljettu_matka >= self.pituus:
                a.voitot += 1
                maalissa = True
        if maalissa:
            return True
        else:
            return False


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
        self.voitot = 0
    
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        self.nopeus = max(0, min(self.nopeus, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.nopeus


main()
