print("""--------------------------
      Hesap Makinesi Programına Hoşgeldiniz

      İşlemler;

      1 - Toplama
      2 - Çıkarma
      3 - Çarpma
      4 - Bölme
--------------------------""")

a = int(input("\nbirinci sayıyı giriniz: "))
b = int(input("\nikinici sayıyı giriniz: "))
islem = int(input("\nYapmak istediğiniz işlemi seçiniz: "))

match islem:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("geçersiz işlem")
        
        