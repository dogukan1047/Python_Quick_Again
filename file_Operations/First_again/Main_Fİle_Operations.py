# myFile=open("file1.txt","r")
# icerik=myFile.read()
# print(icerik)
# myFile.close()

with open("file1.txt", "r") as f:#kendiliğinden kapatır dosyayı
    # icerik=f.read() -->normal sekilde okur
    icerik=f.readlines() #--> satır sonlarında /n bulunur ve satır satır okur bir diziye
    # pozisyon=f.tell() # --> imlecin nerde olduğunu söyler
    # f.seek(0) --> imleci nereye götürmek istiyorsak onu yazarız
    print(icerik)

    for satir in icerik:
        print(satir,end="")
print()
with open("file2.txt", "r") as f1:
    okunacak_miktar=2
    icerik1=f1.read(okunacak_miktar)
    while len(icerik1)>0:
        print(icerik1,end="")
        icerik1=f1.read(okunacak_miktar)


with open("file3.txt", "w") as f2:
   for i in range(5):
       f2.write("Dodo\n")