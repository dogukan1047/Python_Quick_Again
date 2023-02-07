# Ekrandan alınan sayının asal olup olmadığını kontrol eden program

number = int(input("Sayinizi giriniz:"))
i = 2
while i < 10:
    if number % i == 0:
        print("asal sayı değil:")
        break
    i += 1
    if i == 10:
        print("asal sayıdır:")

# ekrandan girilen sayının pozitif bölen sayısını bulan program
bolen_sayısı = 0
for i in range(1, number + 1):
    if number % i == 0:
        bolen_sayısı += 1

print(bolen_sayısı)

# Ekrandan girilen sayının rakamları toplamını hesaplayan bir program yazınız


toplam = 0
str_sayi = str(number)

for rakam in str_sayi:
    toplam += int(rakam)

print(toplam)

# ekrandan alınan bir metinde hangi harfin kaç kere geçtigini bulan program


metin = input("Metininizi giriniz:")

sozluk = dict()

for harf in metin:
    if harf in sozluk:
        sozluk[harf] += 1
    else:
        sozluk[harf] = 1
for harf, adet in sozluk.items():
    print(harf, adet)

# Ekrandan okunan bir metinde a harflerini büyük yapan bir program yazınız
metin2=""

for harf in metin :
    if harf =="a":
        metin2+="A"
    else:
        metin2+=harf

print(metin2)