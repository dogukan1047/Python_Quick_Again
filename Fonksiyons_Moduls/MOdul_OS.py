import os

# 0-)print(os.getcwd())#Hangi klasörde olduğumuzu gösterir
# 1-) os.chdir() --> klasörümüzün yerini değiştirir
# 2-) os.listdir() --> klasör içeriğini döndürür
# 3_) os.mkdir() --> yeni klasör oluşturur
# 4-) os.makedirs("deneme1/deneme2/deneme3")  --> içe içe klasör oluşturulur
# 5-) os.rmdir() --> klasörü siler içi boşsa silmez
# 6-) os.removedirs() --> içe içe klasörleri siler
# 7-) os.rename("ilk ad","ikinci ad") --> dosya ismini değiştirir
# 8-) os.stat() --> Dosya ile ilgili özellikleri liste olarak döner
# 9-) os.walk() --> Sıra sıra tüm klasörlere girer içinde ne var ne yok yazdırır çıkar aynı şekilde devam eder
# 10-) os.path.isfile() --> Dosya mıdır dosya ise True döner
# 11-) os.path.isdir() -->Klasör müdür klasör ise True döner
# 12-) os.path.slittext() --> Dosya ismini ve dosya uznatısını bir tuple dönüştürür
