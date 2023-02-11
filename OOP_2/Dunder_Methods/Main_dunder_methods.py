# Dunder methods (magic metods)

# print(3+5)
# print(int.__add__(3,5))
# print("Ali"+"Polatel")
# print(str.__add__("ali","Polatel"))
# print([1,2,3]+[4,5,6])
# print(list.__add__([1,2,3],[4,5,6]))

class Mylist(list):
    def __add__(self, other):# magic metotları kendi isteğimize göre düzenleyebiliriz
        listem_Add=list()
        if len(self)!=len(other):
            print("toplama yapilamaz")
        else:
            for i in range(len(self)):
                listem_Add.append(self[i]+other[i])
        print(listem_Add)
    def __sub__(self, other):
        listem_Sub = list()
        if len(self) != len(other):
            print("Cikarma yapilamaz")
        else:
            for i in range(len(self)):
                listem_Sub.append(self[i] - other[i])
        print(listem_Sub)




liste1=Mylist([1,2,3])
liste2=Mylist([2,5,7])

print(liste1+liste2) #magic metodlar fonksiyon ismi ile çağrıya gerek kalmaz
print(liste1-liste2)
