numbers=[1,2,3,4,5]
letters="abcde"

liste3=[number for number in numbers] # tek tek elemanları başka listeye atar
print(liste3)

liste4=[number**2 for number in numbers] # listedeki sayıların karelerini alır
print(liste4)

liste5=[number for number in numbers if number%2==0] # çift sayıları bastırdı
print(liste5)

liste6=[number**2 for number in numbers if number>4 and number%2==0]
print(liste6)

liste7=[(number,letter) for number in numbers for letter in letters]
print(liste7)

myList=[2,3,4,5]
myList2=[2,6,7,8]

liste8=[number**2 for number in myList if number not in myList2]
print(liste8)

lists=[[1,2,3],[4,5,6,7],[8,9,10,11,12]]
liste9=[number2 for number in lists for number2 in number]
print(liste9)



