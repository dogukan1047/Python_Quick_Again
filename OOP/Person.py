from datetime import date

class person():
    # sınıf değişkenleri
    person_count = 0

    def __init__(self, name, surname='polatel', age=17):
        # nesne değişkenleri
        self.name = name
        self.surnanme = surname
        self.age = age
        person.person_count += 1

    # nesne metodu
    def show_info(self):
        print(f"{self.name}")

    # class metodu
    @classmethod
    def show_info1(cls):
        print(f"{cls.person_count}")

    @classmethod
    def stringe_gore_parcala(cls, str_):
        name, age = str_.split("-")
        return cls(name, age)

    @staticmethod
    def yas_hesapla():
        return date.today()
