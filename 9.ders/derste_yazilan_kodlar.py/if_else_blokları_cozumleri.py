# Problem 1
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

#  Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

#  BKİ 18.5'un altındaysa -------> Zayıf

#  BKİ 18.5 ile 25 arasındaysa ------> Normal

#  BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

#  BKİ 30'un üstündeyse -------------> Obez

# kilo = float(input("Lütfen kilonuzu giriniz: "))
# boy = float(input("Lütfen boyunuzu ondalıklı(metre cinsinden) tipte giriniz."))

# # bki = beden kitle indeksi
# bki = kilo / (boy * boy)

# if (bki < 18.5):
#     print(f"Beden kitle indeks değeriniz zayıf olduğunuzu gösteriyor. BKİ : {bki}")
# elif (bki >=18.5 and bki < 25):
#     print(f"Beden kitle indeks değeriniz normal olduğunuzu gösteriyor. BKİ : {bki}")
# elif (bki >= 25 and bki < 30):
#     print(f"Beden kitle indeks değeriniz Fazla Kilolu olduğunuzu gösteriyor. BKİ : {bki}")
# else:
#     print(f"Beden kitle indeks değeriniz Obez olduğunuzu gösteriyor. BKİ : {bki}")

# Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

# a = int(input("Birinci sayıyı giriniz: "))
# b = int(input("ikinci sayıyı giriniz: "))
# c = int(input("üçüncü sayıyı giriniz: "))

# if (a >= b and a >= c):
#     print(f"en büyük sayı : {a} dır")
# elif (b >= a and b >= c):
#     print(f"en büyük sayı : {b} dır")
# elif (c >= a and c >= b):
#     print(f"en büyük sayı : {c} dır")

# liste = [a,b,c]
# print(f"En büyük sayımız: {max(liste)}")

# eb = 0
# if a >= b and a >= c:
#     eb = a
# elif b >= a and b >= c:
#     eb = b
# elif c >= a and c >= b:
#     eb = c
# print(f"En büyük sayımız {eb} dir")

# Problem 3
# Kullanıcının girdiği vize1,vize2,final notlarına göre harf notunu hesaplayın.

#     Vize1 toplam notun %30'una etki edecek.

#     Vize2 toplam notun %30'una etki edecek.

#     Final toplam notun %40'ına etki edecek.


#     Toplam Not >=  90 -----> AA

#     Toplam Not >=  85 -----> BA

#     Toplam Not >=  80 -----> BB

#     Toplam Not >=  75 -----> CB

#     Toplam Not >=  70 -----> CC

#     Toplam Not >=  65 -----> DC

#     Toplam Not >=  60 -----> DD

#     Toplam Not >=  55 -----> FD

#     Toplam Not <  55 -----> FF

# vize1 = float(input("Vize 1 notunuzu giriniz: "))
# vize2 = float(input("Vize 2 notunuzu giriniz: "))
# final = float(input("Final notunuzu giriniz: "))

# toplam = vize1 * 30 / 100 + vize2 * 30 /100 + final * 40 /100

# if (toplam >= 90):
#     print(f"Toplam notunuz {toplam} olduğu için AA almaya hak kazandınız.")
# elif (toplam >= 85):
#     print(f"Toplam notunuz {toplam} olduğu için BA almaya hak kazandınız.")
# elif (toplam >= 80):
#     print(f"Toplam notunuz {toplam} olduğu için BB almaya hak kazandınız.")
# elif (toplam >= 75):
#     print(f"Toplam notunuz {toplam} olduğu için CB almaya hak kazandınız.")
# elif (toplam >= 70):
#     print(f"Toplam notunuz {toplam} olduğu için CC almaya hak kazandınız.")
# elif (toplam >= 65):
#     print(f"Toplam notunuz {toplam} olduğu için DC almaya hak kazandınız.")
# elif (toplam >= 60):
#     print(f"Toplam notunuz {toplam} olduğu için DD almaya hak kazandınız.")
# elif (toplam >= 55):
#     print(f"Toplam notunuz {toplam} olduğu için FD almaya hak kazandınız.")
# else:
#     print(f"Toplam notunuz {toplam} olduğu için FF almaya hak kazandınız. Kaldınız.")


# Problem 4
# Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

# Eğer kullanıcı "Üçgen" cevabını verirse , 
# 3 tane kenar isteyip bu üçgenin ikizkenar mı , 
# eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya 
# çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa,
# ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

# Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

# Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

# sekil = input("Lütfen şeklinizi giriniz (dörtgen, üçgen): ")

# if sekil == "dörtgen":
#     a = int(input("dörtgenin birinci kenarını giriniz: "))
#     b = int(input("dörtgenin ikinci kenarını giriniz: "))
#     c = int(input("dörtgenin üçüncü kenarını giriniz: "))
#     d = int(input("dörtgenin dördüncü kenarını giriniz: "))
#     if a == b and a == c and a == d:
#         print("Bu dörtgen bir karedir.")
#     elif a == c and b == d:
#         print("Bu şekil bir dikdörtgendir.")
#     else:
#         print("Bu dörtgen normal bir dörtgendir.")

# elif sekil == "üçgen":
#     a = int(input("Üçgenin birinci kenarını giriniz: "))
#     b = int(input("Üçgenin ikinci kenarını giriniz: "))
#     c = int(input("Üçgenin üçüncü kenarını giriniz: "))

#     # |a+b| > |c| and |a+c| > |b| and |b+c| > |a|
#     if (abs(a+b) > abs(c) and abs(a+c) > abs(b) and abs(b+c) > abs(a)):
#         if a == b and a == c:
#             print("Üçgenimiz eşkenardır.")
#         elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
#             print("Üçgenimiz ikizkenardır.")
#         else:
#             print("Üçgenimiz normal bir üçgendir.")
#     else:
#         print("Girilen kenarlarla bir üçgen oluşturulamaz. üçgen belirtmiyor")
# else:
#     print("üçgen veya dörtgen girmediniz.")