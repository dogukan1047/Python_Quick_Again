# Lambda
a=[15,20,25]
kare_al = lambda x: x * x
print(kare_al(5))

kup_al = lambda x: x ** 3
print(kup_al(5))

toplam = lambda x, y: x + y
print(toplam(10 , 12))

genel_toplam=lambda *args : sum(args)
print(genel_toplam(1,2,3,4,5,6,7,8,9))

print((lambda x,y,z : z+y*x)(3,5,7))

liste=[("Dogukan",19),("Cemre",23),("Emel",24),("Hakan",28)]
liste.sort()
print(liste)
liste.sort(key=lambda x :x[1])
print(liste)



