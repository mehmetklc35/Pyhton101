# Generatorların Oluşturulması ve Kullanılması
# Bu derste Pythondaki generatorları anlamaya çalışacağız.

# Generatorlar Pythonda iterable objeler (örnek olarak fonksiyonlar) oluşturmak 
# için kullanılan objelerdir ve bellekte herhangi bir yer kaplamazlar. Örneğin, 
# 100.000 tane değer üretip, bu değerleri bir listede tutmak bellekte oldukça 
# fazla yer kaplayacaktır. O yüzden bu işlemi gerçekleştiren bir fonksiyonu 
# generator fonksiyon şeklinde yazmak oldukça mantıklı olacaktır. Generatorları 
# anlamak için isterseniz bir fonksiyonu ilk olarak generator kullanmadan yazmaya 
# çalışalım.

# def kareleri_al():
#     sonuc = []
#     for i in range(1,6):
#         sonuc.append(i**2)
#     return sonuc

# print(kareleri_al())

# generator fonksiyon
# def kareleri_al2():
#     for i in range(1,10000000):
#         yield i**2

# generator = kareleri_al2()
# print(generator)

# # Yazdığımız ilk fonksiyonda 1'den 6'ya kadar gidip her bir değerin 
# # karesini sonuç isimli listeye atıyoruz ve daha sonra bu listeyi 
# # dönüyoruz.Yani bellekte liste değişkenin içinde 1,4,9,16,25 değerleri tutuluyor.

# # Generatorle yazdığımız 2.fonksiyonda yield anahtar kelimesiyle değerleri 
# # ürettiğimizi sanıyoruz. Ama aslında bu fonksiyonu çağırınca bize sadece 
# # bir tane generator objesi dönüyor ve biz sadece generator objesinin 
# # değerlerine ulaşmaya çalıştığımızda değerler tek tek üretiliyor. 
# # Yani kısacası bellekte değerler tutulmuyor. Bu generator objesinin 
# # üzerinde bir tane iterator oluşturarak durumu daha iyi anlamaya çalışalım.

# iterator = iter(generator)
# for i in range(101):
#     print(next(iterator))

# Aslında generator objesi sadece değerlere ulaşmak istediğimiz 
# zaman yield anahtar kelimesini kullanıp değer üretiyor. Yani 
# generatorler sadece biz değerlere ulaşmak istersek çalışıyor. 
# İşte generatorlerin mantığı tamamıyla bu şekilde ! Şimdi de list 
# comprehensionları generatorlara çevirmeye çalışalım.
    
# liste = [i**3 for i in range(5)]
# print(liste)

generator = (i**3 for i in range(5))
# print(generator)
iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))