# def toplam(x,y): # Positional arguments
#     return x+y
#
# print(toplam(3,5))
#
# def show_info(name,surname,age="Girilmedi"): # Keywords argument
#     return f"AD: {name} SOYAD: {surname} YAS: {age}"
#
# print(show_info(name="Dogukan",age=19,surname="Polatel"))
# print()


def sums(*args):
    for arg in args:
        print(arg)

def carp(*args):
    carpim=1
    for arg in args:
        carpim*=arg

    return carpim

def fonks(**kwargs):# key value ilişkisine göre saklar dict ={'ad' :"Dogukan"}
    print(kwargs)

fonks(ad="dogukan",yas=15)