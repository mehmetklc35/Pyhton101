# For Döngüleri
# Bu konuda Pythondaki for döngülerinin yapısını ve for 
# döngülerinin kullanım alanlarını öğreneceğiz. Ancak ondan
# önce , Pythondaki in operatörünü öğrenmeye çalışalım.

# in Operatörü
# Pythondaki in operatörü , bir elemanın başka bir listede,
# demette (tuple) veya stringte (karakter dizileri) bulunup bulunmadığını 
# kontrol eder. Kullanımı şu şekildedir;

# print("b" in "nova")

# print("academy" in "Nova academy")

# print(9 in [1,2,3,4,5,6,7])

# print("muz" in ("elma","armut","kivi"))

# for Döngüsü
# for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin 
# üzerinde dolaşmamızı sağlayan bir döngü türüdür. Yapısı şu şekildedir.

# for eleman in veri_yapısı(liste,demet vs):
#     Yapılacak İşlemler

# eleman değişkeni her döngünün başında listenin,demetin vs. 
# her bir elemanına eşit olacak ve her döngüde 
# bu elemanla işlem yapılacak.

# Listeler Üzerinde Gezinmek

# liste = [1,2,3,4,5,6,7,8]

# for eleman in liste:
#     print("Eleman: ", eleman)

# liste = [1,2,3,4,5,6,7,8]
# toplam = 0
# for eleman in liste:
#     # toplam = toplam + eleman
#     toplam += eleman
# print("güncel toplam değerimiz: ",toplam)

# liste = [1,2,3,4,5,6,7,8]
# for eleman in liste:
#     if eleman % 2 == 1:
#         print(eleman)

# Karakter Dizileri Üzerinde Gezinmek (Stringler)

# s = "Python Programlama Dili"

# for harf in s:
#     print(harf)

# s = "Nova"
# for harf in s:
#     print(harf*3)

# Demetler üzerinde gezinmek (Demetler - Tuple)

# demet = ("elma","karpuz","portakal","mandalina")
# for eleman in demet:
#     print(eleman)

# Demetlerin üzerinde for döngüsü uygularken aslında
#  çok pratik bir yöntem bulunuyor. Aşağıdaki örneğe bakalım.

# Listelerin için 2 boyutlu demetler

# liste = [(1,2),(3,4),(5,6),(7,8)]

# for eleman in liste:
#     print(eleman) # Herbir elemanın  demet olduğu görebiliyoruz.

# Demet içindeki herbir elemanı almak için pratik yöntem
# liste = [(1,2),(3,4),(5,6),(7,8)]

# for (i,j) in liste:
#     print(f"i'nin değeri :{i}, j'nin değeri {j}")

# liste = [(1,2,3),(4,5,6),(7,8,9)]

# # iteration - iterasyon : döngüler her bir adımı
# for (i,j,k) in liste:
#     print(i*j*k)

# Sözlükler üzerinde gezinmek (Dictionary)
# Hatırlarsanız, sözlükler konusunda 3 adet metod görmüştük. 
# (keys(),values(),items()*). 
# İsterseniz bunları burada hatırlayalım.
# sozluk = {"bir":1,"iki":2,"üç":3}
# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())

# Python sonuçları dict_keys,dict_values,dict_items olarak
# vermesine rağmen , bunlar üzerinde liste veya demet üzerinde
# gezinir gibi for döngüsüyle gezinebiliriz.

# sozluk = {"bir":1,"iki":2,"üç":3}

# # for eleman in sozluk:
# #     print(eleman)

# # keys() metoduyla aynı çalıştı.
# for eleman in sozluk.keys():
#     print(eleman)

# for eleman in sozluk.values():
#     print(eleman)

# for (i,j) in sozluk.items():
#     print(f"key = {i}, value = {j}")
