# def selamla(isim):
#     print(f"Selamlar, {isim} Bey/Hanım")
#     print("Bugün Nasılsınız?")

# selamla ("Mehmet")
# selamla ("Hülya")
# selamla ("Deniz")

# def topla(a,b,c):
#     print("Toplam =", a+b+c)

# topla(5,12,13)

def faktoriyel(sayi):
    faktoriyel = 1
    if (sayi == 0 or sayi == 1):
        print("Girdiğiniz sayinin faktoriyeli = ", faktoriyel)
    else:
        while   (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Girdiğiniz sayinin faktoriyeli = ", faktoriyel)
            
faktoriyel(5)

