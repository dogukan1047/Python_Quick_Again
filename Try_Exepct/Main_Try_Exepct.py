try:
    # hatanın yakalandığı yerdir
    a = 15
    b = 2
    c = a / b
    x = 7
    d = x
    isim = "Ali"
    karakter = isim[2]
    #Kendi hatamızı fırlattık
    t=0
    if t==0:
        raise ZeroDivisionError

#Hata yakalandı ise bu kısım calısır
except ZeroDivisionError:
    print("payda sifir olamaz")
except NameError:
    print("Bu degisken yok")
except IndexError:
    print("Boyle bir index bulunmuyor")
except Exception:
    print("Bilinmeyen Hata olustu")

else:
#Hata yoksa bu kısım çalışır
    print("Else blogu calıstı")

finally:
#Her turlu durumda burası calısır
    print("finally blogu çalisti")