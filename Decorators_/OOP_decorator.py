# property ,@setter ,@deleter

class Person:
    def __init__(self, name, surnname):
        self.name = name
        self.surname = surnname
        # self.nameSurname=name +" "+surnname

    @property  # özellik gibi davranmsına olanak sağlar
    def adsoyad(self):
        return f"{self.name}.{self.surname}"

    @property
    def email(self):
        return f" {self.name}.{self.surname}@sirket.com "

    @adsoyad.setter
    def adsoyad(self, name):
        ad, soyad = name.split(" ")
        self.name = ad
        self.surname = soyad
    @adsoyad.deleter
    def adsoyad(self):
        print("silindi")



personel = Person("Dogukan", "Polatel")
print(personel.adsoyad)
personel.name = "Cem"

print(personel.adsoyad)

del personel.adsoyad
