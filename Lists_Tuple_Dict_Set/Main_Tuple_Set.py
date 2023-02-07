demet = ("Sarı", "Mavi", "Yesil", "Siyah")

print(demet)

for renk in demet:
    print(renk)

# tuple listesine veri eklenmez,güncellenmez,silinmez

kume = {"Mavi", "Sarı", "Yeşil", "Siyah", "Kırmızı", "Cyan"}
kume2 = {"Mavi", "Mavi", "Gri", "Siyah", "Siyah", "Cyan"}

print(kume)  # set veri yapısında veriler sırasız bir şekilde tutulur
print(kume2)  # set veri yapısı tekrarlı elemana izin vermez

kume.add("Pembe")
print("Pembe eklendi:", kume)

kume2.remove("Mavi")
print("Kume2 den Mavi silindi:", kume2)

print(kume.intersection(kume2))  # kümelerin kesişimini aldık
print(kume.union(kume2))  # kümelerin birleşimini aldık
print(kume.difference(kume2))  # kume birde olup kume2 de olmayanlar

bosListe = list()
bosListe1 = []

bosDemet = ()
bosDemet1 = tuple()

bosKume = set()
bosKume1 = {}  # bu dict oluşturur
