# Decorator Fonksiyonların Oluşturulması ve Kullanılması
# Bu konuda decorator konseptini anlamaya çalışacağız.

# Decorator fonksiyonlar, Pythonda fonksiyonlarımıza dinamik 
# olarak ekstra özellik eklediğimiz fonksiyonlardır ve decorator 
# fonksiyonların kullanımı kod tekrarı yapmamızı engeller. Pythonda 
# decorator fonksiyonlar Flask gibi frameworklerde oldukça fazla kullanılır.

# import time

# def kareleri_hesapla(sayilar):
#     baslama = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i ** 2)
#     print(f"Bu fonksiyon {str(time.time() - baslama)} saniye sürdü.")
#     return sonuc

# def kupleri_hesapla(sayilar):
#     baslama = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i ** 3)
#     print(f"Bu fonksiyon {str(time.time() - baslama)} saniye sürdü")
#     return sonuc

# kareleri_hesapla(range(1000000))

# kupleri_hesapla(range(1000000))


# Bu iki fonksiyonda fonksiyonların çalışma sürelerini ölçmek için 
# time modülünü kullandık. Ancak dikkat ederseniz, hem bu fonksiyonlara 
# ekstradan iş yaptırdık , hem de 2 fonksiyonda da aynı satırları yazdık. 
# Yani, aslında kod tekrarına düştük. Ancak eğer bu fonksiyonlara ekstra 
# özellik ekleyen decorator bir fonksiyonumuz olsaydı, burada ne kod tekrarına 
# düşecektik ne de fonksiyonlara ekstradan satır ekleyecektik. İşte decoratorların 
# tam olarak önemi budur. İsterseniz zaman_hesapla isimli decorator'ımızı ilk önce yazalım. 
# Daha sonra decoratorları açıklamaya çalışalım.

import time

def zaman_hesapla(fonksiyon):
    def wrapper(sayilar):
        baslama = time.time()
        print("FONKSİYONLARIMIZ ÇALIŞMAYA BAŞLADI..")
        # güvenlik sorguları yaz çalıştır
        sonuc = fonksiyon(sayilar)
        # yine aynı güvenlik sorgularını çalıştır.
        print("FONKSİYONLARIMIZ ÇALIŞMASINI BİTİRDİ..")
        bitis = time.time()
        print(fonksiyon.__name__ + " " + str(bitis-baslama) + " saniye sürdü.")
        return sonuc
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc 

@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 3)
    return sonuc

kareleri_hesapla(range(1000000))
kupleri_hesapla(range(1000000))

# Burada zaman_hesapla() isimli decorator bir fonksiyon yazdık. 
# Örneğin kareleri_hesapla(range(100000)) fonksiyonu çağrılırken 
# aslında senaryomuz şu şekilde çalışıyor;

#         1. kareleri_hesapla fonksiyonu zaman_hesapla fonksiyonuna argüman olarak gidiyor.
#         2. wrapper fonksiyonu kareleri_hesapla fonksiyonuna argüman olarak gönderilen 
#         "sayılar" argümanını argüman olarak alıyor.
#         3. wrapper fonksiyonu hem zaman hesaplama işlemini gerçekleştiriyor,hem de gönderilen
#         fonksiyonu çalıştırıyor. Böylelikle bu fonksiyona ekstra özellik ekliyor.
#         4.zaman_hesaplama fonksiyonu en son işlem olarak wrapper fonksiyonumuzu dönüyor.
        
        
# İşte decorator fonksiyonlarımızın aslında işlevi tamamıyla bu şekilde. 
# Burada gördüğümüz gibi decoratorlar sayesinde, hem kod tekrarından kurtulduk, 
# hem de zaman hesaplama işlemimizi decorator fonksiyonumuzda gerçekleştirdik.