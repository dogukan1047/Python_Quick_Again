person = {"isim": "Dogukan", "yas": 20, "cinsiyet": "m", "hobiler": ["Sinema", "Konser", "Yazılım"]}

print("Dict yazdırıldı:", person)

print("Değerler yazdırıldı", person.values())

print("Anahtar yazdırıldı", person.keys())

person.update({"isim": "Dogukan Polatel", "yas": 19})

print(person)

print(person.items()
      )

for i,j in person.items():
      print(i,"-:",j)