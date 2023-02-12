# Decorator
import time

def decorator(fonk):
    def wrapper():
        print("fonksiyon çalışmadan önceki islem")
        fonk()
        print("fonksiyon çalıştıka sonraki işlem")
    return wrapper

@decorator
def fonksiyon():
    print("fonksiyon")



def zaman_hesapla_decorater(fonk):
    def wrapper(*args,**kwargs):
        baslangic=time.time()
        fonk(*args,**kwargs)
        bitis=time.time()
        print(f"islem {bitis-baslangic} saniye sürdü")
    return wrapper


def kareleri_al(liste):
    for i in liste:
        print(i**2)


@zaman_hesapla_decorater
def kupleri_al(liste):
    for i in liste:
        print(i**3)


@zaman_hesapla_decorater
def topla(a,b):
    time.sleep(1)
    return a+b



kupleri_al(range(15))

kareleri_Al1=zaman_hesapla_decorater(kareleri_al)
kareleri_Al1(range(15))

