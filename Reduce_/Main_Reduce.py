# reduce fonksiyonu
from functools import reduce
from math import gcd

liste = [1, 5, 7, 9]


def toplama(x, y):
    return x + y


def carmpa(x, y):
    return x * y


sonuc1 = reduce(toplama, liste)
print(sonuc1)


# ebob(a,b)*ekok(a,b)=a*b


def ekok(x, y):
    return int((x * y) / gcd(x, y))


ekok_ = reduce(ekok,
               liste)  # birini ile ikincinin ekok alında daha sonra bu sonucla ucuncunun ekok alındı böyle böyle en sona kadar gider
print(ekok_)
