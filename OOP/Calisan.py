class Calisan():
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"

    def bilgileri_goster(self):
        return f"{self.email} {self.maas}"


class Yazilimci(Calisan):
    zam_orani = 1.2

    def __init__(self, isim, soyisim, maas, bildigiDil):
        super().__init__(isim, soyisim, maas)
        self.bildigiDil = bildigiDil

    def bilgileri_goster(self):
        return f"{self.email} {self.maas} {self.bildigiDil}"


yazilimci1 = Yazilimci("Dogukan", "Polatel", 15000, "Python")
print(yazilimci1.zam_orani)
print(yazilimci1.bilgileri_goster())

