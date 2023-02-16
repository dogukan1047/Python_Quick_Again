# map fonksiyonu bir listedeki değerleri bir fonksiyona atar ve yeni bir liste oalrak geri döndürür

liste = [1, 2, 3, 4, 5]


def kare_al(x):
    return x ** 2


liste2 = list(map(kare_al, liste))

print(liste2)

liste3=list(map(lambda x:x**2,liste))
print(liste3)

liste4=list(map(lambda x,y:x+y,liste2,liste3))
print(liste4)

isimler=["AHmet","aYse","oNur","HuseyIn"]
isimler2=list(map(lambda x:x.lower(),isimler))
print(isimler2)