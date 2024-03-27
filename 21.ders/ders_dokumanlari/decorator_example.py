
def ekstra(fonk):
    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0

        for sayi in sayilar:
            if sayi % 2 == 0:
                ciftler_toplami += sayi
                cift_sayilar += 1
            else:
                tekler_toplami += sayi
                tek_sayilar += 1
        print("Tek sayıların ortalaması: ", tekler_toplami/tek_sayilar)
        print("Çift sayıların ortalaması: ",ciftler_toplami/cift_sayilar)

        fonk(sayilar)
    return wrapper

@ekstra
def ortalamaBul(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    print("Genel ortalama: ",toplam/len(sayilar))

ortalamaBul([1,2,3,4,5,6,7,11,33,22])