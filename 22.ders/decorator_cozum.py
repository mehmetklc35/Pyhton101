
def ekstra(fonk):
    # wrapper fonksiyon
    def ekstra_ozellik():
        print("Mükemmel sayıyı bulduran fonksiyon...")
        # 6 : 1+2+3+6=12
        for sayi in range(1,1001):
            toplam = 0
            i = 1
            while i < sayi:
                if sayi % i == 0:
                    toplam += i
                i += 1
            if toplam == sayi:
                print(f"Mükemmel sayi : {sayi}")
        fonk()
    return ekstra_ozellik
        
@ekstra
def asal_bul():
    print("Asal bul fonksiyonu çalıştı......")
    for sayi in range(2,1001):
        i = 2
        say = 0
        while i < sayi:
            if sayi % i == 0:
                say += 1
            i += 1
        if say == 0:
            print(sayi)
            
asal_bul()

    