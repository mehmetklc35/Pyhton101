# Mantıksal Değerler ve Karşılaştırma Operatörleri
# Bu konuda, koşullu durumları incelemeden önce bilmemiz gereken mantıksal 
# değerleri ve karşılaştırma operatörlerini öğrenmeye çalışacağız.

# Mantıksal Değerler (Boolean) - Bool
# Mantıksal değerler ya da ingilizce ismiyle boolean değerler aslında 
# Pythonda bir veri tipidir ve iki değere sahiplerdir: True ve False. 
# Şimdi bu değerlerden değişkenler oluşturalım.

# a = True
# print(a)
# print(type(a))

# b = False
# print(b)

# Pythonda bir sayı değeri eğer 0'dan farklıysa True, 0 ise False olarak anlam kazanır.
# Bunu bool() fonksiyonuyla dönüştürme yaparak görebiliriz.

# print(bool(0))
# print(bool(55))

# print(bool(-1))

# Bool değerleri ayrıca birazdan göreceğimiz 
# bir karşılaştırma operatöründen sonra ortaya çıkan sonuç değeridir

# print(1==2)
# print(1<2)
# print(1>2)

# Ayrıca Pythonda eğer bir değişkenin değerini sonradan belirlemek 
# isterseniz geçici olarak 
# bu değişken None (atanmamış anlamında) değerine eşitleyebilirsiniz.

# a = None
# print(a)

# a=55
# print(a)

# Karşılaştırma Operatörleri
# Operatör	Görevi	Örnek
# ==	İki değer birbirine eşitse True, değilse False değer döner.	2 == 2 (True) , 2 == 3 (False)
# !=	İki değer birbirine eşit değilse True, diğer durumda False döner.	2 != 2 (False), 2 != 3 (True)
# >	Soldaki değer sağdaki değerden büyükse True, değilse False döner.	3 > 2 (True), 2 > 3 (False)
# <	Soldaki değer sağdaki değerden küçükse True, değilse False döner.	2 < 3 (True) , 3 < 2 (False)
# >=	Soldaki değer sağdaki değerden büyükse veya sağdaki değere eşitse True, değilse False döner.	3 >= 2 (True),3 >= 3 (True) , 2 >= 3 (False)
# <=	Soldaki değer sağdaki değerden küçükse veya sağdaki değere eşitse True, değilse False döner.	3 <= 2 (False),3 <= 3 (True) , 2 <= 3 (True)


print(3 <= 2)