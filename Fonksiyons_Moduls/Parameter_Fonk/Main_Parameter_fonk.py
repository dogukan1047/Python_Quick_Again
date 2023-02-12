def topla(a,b):
    return a+b

def carp(a,b):
    return a*b

def islem_yap(fonk,a,b):
    return fonk(a,b)

print(islem_yap(topla,5,9))# sadece fonksiyon ismini parametre olarak göndermemiz gerek

liste1=[1,2,3,4,5]
liste2=[2,5,7,4]

def kare_al(x):
    return x*x
def kup_al(x):
    return x**3

def map_fonk(fonk,liste):
    sonuc=list()
    for i in liste:
        sonuc.append(fonk(i))
    return sonuc

print(map_fonk(kare_al,liste2))