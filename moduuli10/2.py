def main():
    t = Talo(1, 7, 3)
    for i in range(len(t.hissit)):
        print(f"Hissin {i} kerros: {t.hissit[i].nykyinen_kerros}")
    t.aja_hissia(0, 200)
    t.aja_hissia(1, 4)
    t.aja_hissia(2, -15)
    for i in range(len(t.hissit)):
        print(f"Hissin {i} kerros: {t.hissit[i].nykyinen_kerros}")


class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
    
    def kerros_alas(self):
        self.nykyinen_kerros = max(self.alin_kerros, min(self.nykyinen_kerros-1, self.ylin_kerros))
        print(f"Kerros: {self.nykyinen_kerros}")

    def kerros_ylos(self):
        self.nykyinen_kerros = max(self.alin_kerros, min(self.nykyinen_kerros+1, self.ylin_kerros))
        print(f"Kerros: {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kerros):
        if kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros != kerros and self.nykyinen_kerros < self.ylin_kerros:
                self.kerros_ylos()
        elif kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros != kerros and self.nykyinen_kerros > self.alin_kerros:
                self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara
        self.hissit = []
        for i in range(hissien_maara):
            uusi_hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(uusi_hissi)
    
    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)


main()
