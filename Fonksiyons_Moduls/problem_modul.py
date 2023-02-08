# zarların gelme olasılığın teorik olasılığa deneme sayısı ile yaklaşımı
import random
from  datetime import *
zarlar={1:0,2:0,3:0,4:0,5:0,6:0}

for i in  range(200):
    zar=random.randint(1,6)
    zarlar[zar]+=1

for zar in zarlar :
    print(f" {zar} gelme olasılığı :{zarlar[zar] /200}")

#  1 ocak 1901 den 31 aralık 2000 kadar kac sefer bir ayın ilk günü pazar olur

pazarSayısı=0
for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime(yil,ay,1).weekday()==6:
            pazarSayısı+=1


print("Kac tane ayın ilk gunu pazardır:",pazarSayısı)


