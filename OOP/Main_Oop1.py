from Person import person




print(person.person_count)

personOne = person("Dogukan", "Polatel", 20)
# print(personOne.__dict__)  # calışan birinin özelliklerini dict olarak yazar
print(person.person_count)

personTwo = person("Dogukan", "Polatel", 20)
print(person.person_count)

persoThr = person("Dogukan", "Polatel", 20)
print(person.person_count)

# class metod

# person.name erişemem çünkü bu nesne değişkenidir buna erişmek için sınıf değişkeni olarak tanımlamak gerek

person.show_info1() # ----> class metot çağrısı

person.show_info(personOne) # ----> nesne metot çağrısı


personFour=person.stringe_gore_parcala("Sinem-19")
print(personFour.age)

print(person.yas_hesapla())