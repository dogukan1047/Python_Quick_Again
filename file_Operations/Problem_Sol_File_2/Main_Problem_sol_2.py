with open("School.txt", "r") as myFile:
    with open("gecenler.txt", "w") as gecenler:
        with open("kalanlar.txt", "w") as kalanlar:
            icerik = myFile.readlines()  # satır satır okurken okuduğu her satırı bir listeye atar

            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n", "")  # \n karakteri yerine "" karakterini koyar
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")
                notlar = satir.split(" ")[-1]  # split ile bölündüğü zaman elimizde bir liste olur
                notlar = notlar.split("/")
                birinci_vize = int(notlar[0])
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                ortalama = ((birinci_vize * 0.3) + (ikinci_vize * 0.3) + (final * 0.4))
                bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[-1]]
                if ortalama >= 70 and final>=70:

                    gecenler.write(ad)
                    gecenler.write(" "*(25-len(ad)))
                    gecenler.write(soyad)
                    gecenler.write(" " * (25 - len(soyad)))
                    gecenler.write(bolum)
                    gecenler.write(" " * (25 - len(bolum)))
                    gecenler.write(str(round(ortalama,1)))
                    gecenler.write(" " * 21)
                    gecenler.write("Gecti")
                    gecenler.write("\n")
                else:

                    kalanlar.write(ad)
                    kalanlar.write(" " * (25 - len(ad)))
                    kalanlar.write(soyad)
                    kalanlar.write(" " * (25 - len(soyad)))
                    kalanlar.write(bolum)
                    kalanlar.write(" " * (25 - len(bolum)))
                    kalanlar.write(str(round(ortalama, 1)))
                    kalanlar.write(" " * 21)
                    kalanlar.write("Kaldi")
                    kalanlar.write("\n")

