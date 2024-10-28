def main():
    h = Hissi(1,7)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(-10)
    h.siirry_kerrokseen(999)
    h.siirry_kerrokseen(h.alin_kerros)


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


main()
