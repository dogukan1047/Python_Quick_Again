# filter fonksiyon

liste = [1, 3, 5, 9, 15, 17, 18, 20]

liste2 = list(filter(lambda x: True if x %2==0 else False, liste))
print(liste2)

liste3=list(filter(lambda x: x>=10  and x<100,liste))
print(liste3)


kelimeler=["Ayna","Ahmet","Ana","Kalem","Doktor","Salih","kazak","son"]
a_with_start=list(filter(lambda kelime : kelime.startswith("A"),kelimeler))
print(a_with_start)

a_in_words=list(filter(lambda kelime:"a" in kelime,kelimeler))
print(a_in_words)

newListe=["Dogukan","erik",15,14,{1,4,5}]
newListe=list(filter(lambda x:isinstance(x,str),newListe))
print(newListe)
