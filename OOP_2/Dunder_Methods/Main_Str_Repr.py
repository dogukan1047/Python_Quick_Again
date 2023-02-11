from datetime import date


# __str__ ve __repr__

class Futbolcu():
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def __str__(self):
        return f"AD: {self.isim} SOYAD: {self.soyisim} YAS: {self.yas}"

    def __repr__(self):
        return f'Futbolcu("{self.isim}","{self.soyisim}",{self.yas})'


futbolcu1 = Futbolcu("Dogukan", "Polatel", 15)

print(futbolcu1)
print()

a = "dogukan"
number = 15.022
bugun = date.today()

print(str(a))  # dogukan
print(repr(a))  # 'dogukan'
print()

print(str(number))  # 15.022
print(repr(number))  # 15.022
print()

print(bugun)  # 2023-02-11
print(str(bugun))  # 2023-02-11
print(repr(bugun))  # datetime.date(2023,2,11)
