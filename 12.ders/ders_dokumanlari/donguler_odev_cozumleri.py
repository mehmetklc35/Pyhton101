# Problem 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

# Bir sayının kendi hariç bölenlerinin toplamı kendine 
# eşitse bu sayıya "mükemmel sayı" denir. 
# Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
# while True:
#     sayi = int(input("Lütfen sayıyı giriniz (Çıkmak için 0'a bas): "))
#     if sayi == 0:
#         print("Programdan çıkılıyor...")
#         break

#     toplam = 0
#     i = 1
#     while(i<sayi):
#         if (sayi%i == 0):
#             toplam += i
#         i += 1

#     if (toplam == sayi):
#         print("Bu sayi mükemmel sayıdır : ",sayi)
#     else:
#         print("Bu sayi mükemmel sayı değildir : ",sayi)


# Problem 2
# Kullanıcıdan aldığınız bir sayının "Armstrong" 
# sayısı olup olmadığını bulmaya çalışın.

# Örnek olarak, Bir sayı eğer 4 basamaklı ise 
# ve oluşturan rakamlardan herbirinin 4. kuvvetinin 
# toplamı( 3 basamaklı sayılar için 3.kuvveti ) o 
# sayıya eşitse bu sayıya "Armstrong" sayısı denir.

# Örnek olarak : 1634 = 1^4 + (1296)6^4 + (81)3^4 + (256)4^4
        
# while True:
#     sayi = input("Lütfen sayınızı giriniz (Çıkmak için q'ya basın.): ")
#     if sayi == "q":
#         print("Programdan çıkılıyor...")
#         break
#     if sayi == "":
#         continue
#     basamak_sayisi = len(sayi)
#     sayi = int(sayi)
#     basamak = 0
#     toplam = 0

#     gecici_sayi = sayi

#     # while(gecici_sayi>0):
#     #     basamak = gecici_sayi % 10
#     #     toplam += basamak ** basamak_sayisi
#     #     gecici_sayi =  gecici_sayi // 10

#     for i in range(0,basamak_sayisi):
#         basamak = gecici_sayi % 10
#         toplam += basamak ** basamak_sayisi
#         gecici_sayi =  gecici_sayi // 10

#     if (sayi == toplam):
#         print(f"Girilen sayı {sayi}'dir. Ve bu bir armstrong sayısıdır.")
#     else:
#         print(f"Girilen sayı {sayi}'dir. Ve bu bir armstrong sayısı değildir.")


# Problem 3
# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

# İpucu: İç içe 2 tane for döngüsü kullanın. 
# Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
        
# for i in range(0,11):
#     for j in range(0,11):
#         print(f"{i} x {j} = {i*j}")
#     print("***********")

# Problem 4
# Her bir while döngüsünde kullanıcıdan bir 
# sayı alın ve kullanıcının girdiği sayıları 
# "toplam" isimli bir değişkene ekleyin. Kullanıcı
# "q" tuşuna bastığı zaman döngüyü sonlandırın ve 
# ekrana "toplam değişkenini" bastırın.

# İpucu : while döngüsünü sonsuz koşulla başlatın 
# ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

# toplam = 0
# while True:
#     sayi = input("Sayıyı giriniz (Çıkmak ve toplamı görebilmek için q'ya basabilirsiniz.) : )")
#     if (sayi == "q"):
#         print(f"Girdiğiniz sayıların toplamı {toplam}'dir.")
#         break
#     toplam += int(sayi)

# Problem 5
# 1'den 100'e kadar olan sayılardan sadece 3'e 
# bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

# for i in range(1,101):
#     if i % 3 != 0:
#         continue
#     print(f"Sayımız: {i} ve bu sayı 3'e tam bölünür.")
    
# Problem 6
# Buradaki problemin çözümünü derslerimizde
# özellikle öğrenmedik. Burada mantık yürüterek 
# ve list comprehension kullanarak 1'den 100'e kadar 
# olan sayılardan sadece çift sayıları bir listeye 
# atmayı yapmayı çalışın.

# liste = list()
# for i in range(1,101):
#     if i % 2 == 0:
#         liste.append(i)
# print(liste)

liste = [i for i in range(1,101) if i % 2 == 0 ]
print(liste)