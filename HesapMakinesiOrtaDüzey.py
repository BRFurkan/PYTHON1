print("""

[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üs Alma
[6] Mod Alma

""")
giris = input("Hangisini Yapmak İstiyorsunuz: ")

if giris == "1" :
    x = float(input("x sayısını giriniz: "))
    y = float(input("y sayısını giriniz: "))
    print("Sonucunuz: " , x + y)
elif giris == "2":
    x = float(input("x sayısını giriniz: "))
    y = float(input("y sayısını giriniz: "))
    print("Sonucunuz: ", x - y)
elif giris == "3":
    x = float(input("x sayısını giriniz: "))
    y = float(input("y sayısını giriniz: "))
    print("Sonucunuz: ", x * y)
elif giris == "4":
    x = float(input("x sayısını giriniz: "))
    y = float(input("y sayısını giriniz: "))
    print("Sonucunuz:",x / y)
    if y != 0:
      print("İşlem Sonucu: ", x / y)
    else:
      print("y sayısı 0 olamaz ")
elif giris == "5":
    x = float(input("x sayısını giriniz: "))
    y = float(input("y sayısını giriniz: "))
    print("Sonucunuz: ",x ** y)
elif giris == "6":
    x = float(input("x sayısını giriniz: "))
    y = float(input("y sayısını giriniz: "))
    print("Sonucunuz: ",x % y)
else:
    print("Yanlış sayı girdin.1,2,3,4,5 veya 6 gir")
