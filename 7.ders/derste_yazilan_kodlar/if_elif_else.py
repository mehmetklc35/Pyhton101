# Koşullu Durumlar - if - elif - else koşullu durumları
# Önceki konumuzda koşullu durumlardaki if-else kalıplarımızı öğrendik. 
# Bu bölümde de if-elif-else kalıplarını öğrenmeye çalışacağız.

# if-elif-else Blokları
# Önceki konumuzda koşullu durumlarımızla sadece tek bir koşulu 
# kontrol edebiliyorduk. Ancak programlamada bir durum bir çok koşula
# bağlı olabilir. Örneğin bir hesap makinesi programı yazdığımızda 
# kullanıcının girdiği işlemlere göre koşullarımızı belirleyebiliriz.
# Bu tür durumlar için if-elif-else kalıplarını kullanırız. Kullanımı şu şekildedir;

# if koşul: 
#     Yapılacak İşlemler
# elif başka bir koşul:
#     Yapılacak İşlemler
# elif başka bir koşul:
#     Yapılacak İşlemler

#     //
#     //
# else:
#     Yapılacak İşlemler ,

# Programlarımızda, Kaç tane koşulumuz var ise o kadar elif bloğu oluşturabiliriz.
# Ayrıca else in yazılması zorunlu değildir. if - elif - else kalıplarında,
# hangi koşul sağlanırsa program o bloğu çalıştırır ve if-elif-blokları sona erer.
# Şimdi isterseniz kullanıcıya işlem seçtirdiğimiz bir programla , 
# bu kalıbı öğrenmeye başlayalım.

# islem = int(input("İşlem seçiniz : "))

# if (islem == 1):
#     print("1. işlem seçildi.")
# elif (islem == 2):
#     print("2. işlem seçildi.")
# elif (islem == 3):
#     print("3. işlem seçildi.")
# else:
#     print("İşlem geçersiz.")

# Programlarda else kalıbının kullanılmasına gerek yoktur.
# Buradaki kodda biz diğer durumlar için sadece opsiyonel bir 
# else bloğu koyduk. Kodumuz else bloğu olmadan da çalışabilecektir. 
# Ancak bu durumda yanlış bir işlem girilirse ekrana herhangi bir şeyin 
# yazılmadığını göreceğiz. Yani, else bloğu kullanmak tamamen size bağlı.

# islem = int(input("İşlem seçiniz : "))

# if (islem == 1):
#     print("1. işlem seçildi.")
# elif (islem == 2):
#     print("2. işlem seçildi.")
# elif (islem == 3):
#     print("3. işlem seçildi.")

# *Peki , if koşulu olmadan elif bloklarını yazmak mümkün mü ? *
#  Pythonda böyle bir kullanım hataya yol açacaktır.

# islem = int(input("İşlem seçiniz : "))

# elif (islem == 2):
#     print("2. işlem seçildi.")
# elif (islem == 3):
#     print("3. işlem seçildi.")

# if-if-if Blokları
# Bu blokları öğrenmeden önce isterseniz öğrendiğimiz bilgilerle, 
# bir harf notu hesaplama sistemi yapalım.
# Daha sonra bu kalıpları anlamaya çalışalım.

# note = float(input("Notunuzu giriniz: "))

# if note >= 90:
#     print("AA")
# elif note >= 85:
#     print("BA")
# elif note >= 70:
#     print("BB")
# elif note >= 55:
#     print("CB")
# else:
#     print("dersten kaldınız")

# Burada eğer herhangi bir bloğumuz koşulu sağlarsa print işlemi 
# gerçekleşecek ve programımız sonlanacaktır. Ancak acaba elif 
# bloklarını if bloklarına çevirirsek programımız nasıl çalışacak 
# ? Hemen bakalım.

note = float(input("Notunuzu giriniz: "))

if note >= 90:
    print("AA")

if note >= 85:
    print("BA")

if note >= 70:
    print("BB")

if note >= 55:
    print("CB")

if note < 55:
    print("dersten kaldınız")

# Burada gördüğümüz gibi programımız beklenmedik bir şekilde çalıştı. 
# Çünkü Pythonda programlar her zaman bütün if bloklarını kontrol eder
# ve koşullar doğruysa bu blokları çalıştırır. İşte böyle not 
# hesaplama gibi programlarda elif kullanmamızın sebebi budur.

# Koşullu durumlarımız şimdilik bu kadar ! Kurs boyunca programlarımızda
# birçok yerde koşullu durumları kullanacağız.