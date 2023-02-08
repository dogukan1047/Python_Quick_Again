####################################################################################################
import math
from Faiz_hesaplama import faiz

sonuc=math.factorial(6)
print(sonuc)

sonuc=faiz(1000,20)
print(sonuc)

print("------------------------------------------------------------------------------------------")
print()
#######################################################################################################

import random

print("0 ile 1 aralıgında random sayı üretildi :",random.random())

print("istenilen aralıkta random sayı uretildi  :",random.uniform(10,30))

print("istenilen aralıkta int sayı üretildi üst sınırda dahil oldu :",random.randint(1,5))

liste=["Siyah","Beyaz","Mavi","Gri","Yesil","Turuncu"]

print("Verilen listeden random bir eleman secildi :",random.choice(liste))

print("Verilen listeden random istenilen sayıda eleman seçimi :",random.sample(liste,3))

print("---------------------------------------------------------------------------------------------------------")
print()

##############################################################################################################

import time

zaman=time.time()
print("Gecerli zamanın saniye cinsinden degeri 1 ocak 1970 ten beri :",zaman)

baslangıc=time.time()
liste=[]

for i in range(10000):
    liste.append(i)

bitis=time.time()
print("time comp o(n):",bitis-baslangıc)


zaman1=time.asctime()
print("Suanki tarih:",zaman1)
zaman1=time.strftime("%d:%m:%Y")
print("(Gun) (ay) (yıl) olarak zaman yazdırıldı:",zaman1)
time.sleep(3)
print()
print("Program sonlandı")

######################################################################################################