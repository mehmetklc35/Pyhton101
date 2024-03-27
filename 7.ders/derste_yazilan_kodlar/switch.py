def switch(deger, a, b):
    case={}
    while True:
        try:
 
            case = {

                 1:a+b,
                 2:a-b,
                 3:a*b,
                 4:a/b,
 
            }
            print(case[deger])  # parametreden gelen değeri basıyoruz
            break #programın döngüden çıkmasını sağlıyoruz
 
 
 
        except KeyError:
            print(case['default']) #hatalı giriş olduğu anda default değeri basıyoruz .
            break #programın döngüden çıkmasını sağlıyoruz

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

switch(islem,a,b)


