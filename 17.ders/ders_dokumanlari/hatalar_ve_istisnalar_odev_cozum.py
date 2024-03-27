# Problem 1
# Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

# liste = ["345","sadas","324a","14","kemal"]

# Bu listenin içindeki stringlerden içinde sadece rakam 
# bulunanları ekrana yazdırın. Bunu yaparken try,except 
# bloklarını kullanmayı unutmayın.

# def checkNumber(x):
#     try:
#         x = int(x)
#         return x
#     except:
#         pass

# liste = ["345","sadas","324a","14","kemal"]

# liste2 = [int(i) for i in liste if checkNumber(i) is not None]
# print(liste2)

# for i in liste:
#     try:
#         eleman = int(i)
#         print(eleman)
#     except:
#         pass


# Problem 2
# Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 
# Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün.
# Ancak sayı tek sayı ise fonksiyon *raise* ile *ValueError* hatası 
# fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir 
# liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift 
# sayıları bastırın.

def ciftMi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError("Sayı çift değildir hatası alındı.")

liste = [3,4,1,2,6,0,9,7]

for i in liste:
    try:
        print(ciftMi(i))
    except ValueError:
        pass