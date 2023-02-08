# Dosya uzantılarına göre her dosyayı farklı klasöre koyma

import os


def duzenle():
    klasor = input("Duzenlenecek Klasor:")
    dosyalar = []
    uzantılar = []

    def list_dir():
        for dosya in os.listdir(klasor):# verilen yoldaki dosyaları listeler
            if os.path.isdir(os.path.join(klasor, dosya)):# klasör olursa devam eder
                continue
            if dosya.startswith("."):#gizli dosyaları es gecer
                continue
            else:
                dosyalar.append(dosya)
                print("Dosyalar:",dosyalar)

    list_dir()
    # uzantıları alma
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]# dosyaları uzantılara göre parcalar
        if uzanti in uzantılar:
            continue
        else:
            uzantılar.append(uzanti)
            print("Uzantilar:",uzantılar)
    for uzanti in uzantılar:
        if os.path.isdir(os.path.join(klasor, uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor, uzanti))

    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor, dosya), os.path.join(klasor, uzanti, dosya))


if __name__ == '__main__':
    duzenle()
