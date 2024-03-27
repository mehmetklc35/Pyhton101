# Mantıksal Bağlaçlar
# Mantıksal bağlaçlar daha çok karşılaştırma işlemini kontrol ettiğimiz 
# zamanlarda kullanılır. Bu konuda bunları öğrenmeye çalışacağız.

# and Operatörü
# Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar. 
# Bağlanan karşılaştırma işlemlerinin hepsinin kendi içinde sonucu True ise genel
# sonuç True , diğer durumlarda ise sonuç False çıkar. Kullanımı şu şekildedir.
# and === Hepsi True is True sonucu gelir, en az bir tanesi False ise False sonucu gelir.
# örnek True and True and True = True'dur
# örnek False and True and True = False'dur

# a = 10 > 9      #  true
# b = "Nova" == "Nova"    # true
# c = 5 >= 5   # true

# print(a and b and c and False)

# or Operatörü
# Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonuçlarından en az 
# birinin True olmasına bakar. Bağlanan karşılaştırma işlemlerinin en az 
# birinin True olmasında genel sonuç True , diğer durumlarda ise sonuç False 
# çıkar. Kullanımı şu şekildedir.
# En az bir tanesi True ise sonuc True'dur, ancak hepsi False ise sonuc False'dur
# örnek True or False or False = True'dur
# örnek False or False or False = False'dur

# print(1 < 2 or "Deneme" != "Deneme")

# print(2 > 3 or "Deneme" != "Deneme")

# not operatörü
# not operatörü aslında bir mantıksal bağlaç değildir.
# Bu operatör sadece bir mantıksal değeri veya karşılaştırma işleminini
# tam tersi sonuca çevirir. Yani, not operatörü True olan bir sonucu False , 
# False olan bir sonucu True sonucuna çevirir. Kullanımı şu şekildedir.

# print(not 2 == 2)

# print(not 1>0)

# Operatörleri Beraber Kullanma
# Burada gördüğümüz 3 operatörü beraber kullanmak 
# karmaşıklığa yol açacağı için, parantez kullanabiliriz


# print(not (2.14 > 3.49 or ( 2 != 2 and "Deneme" == "Deneme")))

# print(not 2.14 > 3.49 or 2 != 2 and "Deneme" == "Deneme")
 
# print("Araba" < "Zula" and ( "Bebek" < "Çoçuk" or (not 14 )))

# ogrenci_mi_dict = {"sedat":0,"lale":1,"selcuk":1}
# new_dict = dict()

# for i,j in ogrenci_mi_dict.items():
#     new_dict[i] = int(not j)

# print(new_dict)
