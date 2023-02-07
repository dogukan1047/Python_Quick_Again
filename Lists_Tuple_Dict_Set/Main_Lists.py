renkler=["Mavi","Beyaz","Sarı","Mavi","Yesil"]

print("Ilk hali:",renkler)

renkler.append("Gri")

print("Gri eklendi:",renkler)

renkler.insert(0,"Turuncu")

print("Istediğiniz bir yere turuncu eklendi:",renkler)

renkler.remove("Sarı")

print("Sarı silindi :",renkler)

renkler.pop() #en son elemanı siler

print("Liste sonundaki eleman silindi:",renkler)

renkler.reverse()

print("Liste ters cevrildi:",renkler)

renkler.sort()#Listeyi tamamen değiştirir. Bunun yerine sorted kullanılabilirdi .Değişmesini istemiyorsak

print("Kucukten buyuge siralandi:",renkler)

print("Liste key value ilişkisine döndü:",list(enumerate(renkler)))

newList=list(enumerate(renkler))

print(newList[0])

stringRenkler=" ".join(renkler)#listeyi string'e çevirir

print(stringRenkler)

renkler2=stringRenkler.split(" ")#string listeye çevirir

print(renkler2)



