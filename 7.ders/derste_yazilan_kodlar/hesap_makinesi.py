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

if (islem == 1):
    print(a+b)
elif (islem == 2):
    print(a-b)
elif (islem == 3):
    print(a*b)
elif (islem == 4):
    print(a/b)
else:
    print("böyle bir işlem tanımlı değil.")
