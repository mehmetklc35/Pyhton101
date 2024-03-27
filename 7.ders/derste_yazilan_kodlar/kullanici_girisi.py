print("***********\n Kullanici Girişi \n***********\n")
kullanici_adi = "nova"
sifre = "123"

kullanici_adi1 = input("Kullanici adinizi giriniz: ")
sifre1 = input("Sifrenizi giriniz: ")
if (kullanici_adi == kullanici_adi1 and sifre == sifre1):
    print("sisteme hoşgeldiniz.")
elif(kullanici_adi != kullanici_adi1):
    print("Böyle bir kullanıcı sistemde tanımlı değil")
elif(sifre != sifre1):
    print("şifreniz yanlıştır.")
