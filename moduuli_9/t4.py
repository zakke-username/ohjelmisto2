import random


def main():
    autot = []
    for i in range(10):
        uusi_auto = Auto(f"ABC-{i+1}", random.randint(100,200))
        autot.append(uusi_auto)

    while True:
        maalissa = False
        for auto in autot:
            auto.kiihdyta(random.randint(-10,15))
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                maalissa = True
        if maalissa:
            break

    print("\n")
    print(f"{'Rekisteritunnus':16} {'Kuljettu matka':16} {'Huippunopeus':16} {'Nykyinen nopeus':16}")
    for auto in autot:
        print(f"{auto.rekisteritunnus:16} {auto.kuljettu_matka:<16} {auto.huippunopeus:<16} {auto.nopeus:<16}")


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
