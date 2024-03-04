# # pyhtonda fonksiyonlarımıza dinamik olarak ekstra özellik ekler.. 
# # kod tekrarı yapmamızı engeller

# import time

# def kareleri_hesapla(sayilar):    
#     baslama = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i ** 2 )
#     print(f"Bu fonksiyon {str(time.time() - baslama)} saniye sürdü.")
#     return sonuc
    
# def kupleri_hesapla(sayilar):
#     baslama = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i ** 2 )
#     print(f"Bu fonksiyon {str(time.time() - baslama)}  saniye sürdü.")
#     return sonuc


# kareleri_hesapla(range(10000000000))


import time

def zaman_hesapla(fonksiyon):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = fonksiyon(sayilar)
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
        sonuc.append(i ** 2)
    return sonuc


kareleri_hesapla(range(100000))
kupleri_hesapla(range(100000))
    

