# # Pythonda Sayılar

# Bu bölümle birlikte artık Python öğrenmeye başlıyoruz. Pythonda temeli sağlam atmamız için öncelikle veri tipleri ve veri yapılarını öğrenmeliyiz.İsterseniz sayıları öğrenerek maratonumuza başlayalım.

# Bu bölümde şunları öğreneceğiz.

#         1. Tamsayı(Integer 0,1,2,10,100) ve Ondalıklı Sayı(Float 1.1, 2.4, 6,78) Veri tipleri
#         2. Basit Matematik İşlemleri 
#         3. Değişken Tanımlama
         


# ### Tamsayılar (Integer)

# Matematikte gördüğümüz tüm sayılar (negatif,pozitif) aslında Python'da bir veri tipidir. Tamsayılar ise ingilizce olarak **Integer** olarak geçmektedir. 

# Örnek olarak, -1000,34,2,0 gibi sayılar Python'da birer tamsayı(integer) değerleridir.

# ### Ondalıklı Sayılar (Float)

# Tamsayılar gibi Ondalıklı sayılar da bizim matematikte gördüğümüz sayı çeşitlerinden bir tanesidir. Ondalıklı sayılar matematikte olduğu gibi, Pythonda da bir veri tipidir.Ondalıklı Sayılar veya diğer adıyla Kayan Sayılar İngilizce olarak **Float** olarak geçmektedir.

# Örnek olarak, 3.14, 3.554546, -13.54 gibi sayılar Python'da birer ondalıklı sayı(float) değerleridir.

# Şimdi de bu Pythondaki basit matematik işlemlerini öğrenelim.


# ### Basit Matematik Operatörleri

# Basit 4 işlemi (Toplama,Çıkarma,Çarpma,Bölme) hepimiz matematikten biliriz. Şimdi bu işlemlerin Pythonda nasıl yapıldığını görmeye çalışalım.


# # Toplama
# print(3 + 4)

# #Çıkarma
# print(5-17)

# #Çarpma
# print(10 * 4)

# #Bölme
# print(4/2)

# Burada basit işlemlerimizi görmüş olduk. Ancak son işlem kafanızı karıştırmış olabilir. Sonuç neden float bir değer olarak karşımıza çıktı? Bunları Matematik Operatörleri bölümünde görmek daha doğru olur diye düşünüyorum.

# Bu basit işlemleri gördüğümüze göre, şimdi de Pythondaki değişken tanımlama işlemlerimizi öğrenmeye çalışalım.

# Değişkenler ve Değişken Tanımlama
# Değişkenler bir programlama dilinde olmazsa olmaz bir kavramdır. Değişkenler aslında bir veri tipinden değer tutan birimlerdir.İsterseniz şimdi de Pythonda bir tane değişken oluşturalım.

# # Değişken ismi ve Değişkenin değeri 
# i = 10

# print(i)


# print(i*i*i)

# # Sonuç, değişkenimizin değerinin 3.kuvveti şeklinde karşımıza çıkmış oldu. 
# # Şimdi de değişkenimizin değerini değiştirelim. 
# # Bunun için , yeni değerimizi "=" operatörüyle değişkenimize atamamız gerekiyor.

# i = 15
# print(i)

# # Şimdi de 3 tane farklı değişken oluşturmaya çalışalım.

# a = 4
# b = 3
# c = a + 2*b

# print(f"a = {a}, b = {b}, c = {c}")

# # İşte bu kadar basit ! Son olarak değişkenlerimize isim verirken dikkat etmemiz gereken noktalardan bahsedelim.

# 1. Değişken isimleri bir sayı ile başlayamaz.
# 2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
# 3. :'",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
# 4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs. )

# 2ogrenci_adi = "Eda Can"
# ogrenci adi = "Eda Can"
# ogrenci+adi = "eda can"
# while = "eda can"

# Son olarak öğrendiklerimizle ilgili bir kaç işlem yapalım. 
# # Sonuçlara bakmadan işlemlerin sonucunu tahmin etmeye çalışın.

# pi_sayısı = 3.14
# çap = 4
# çevre = pi_sayısı * çap
# print(çevre)

# # Python'da iki değişkenin değerini birbiriyle değiştirmek için pratik bir yöntem bulunmaktadır.

# a = 2
# b = 3
# print(f"a = {a}, b = {b}")
# a,b = b,a
# print(f"a = {a}, b = {b}")

# Son olarak bir değişkenin değerini artırma işlemlerinde 
# Pythonda pratik bir yöntem bulunmaktadır. Aşağıdaki koda bakalım.

# a = 10
# a = a + 1
# print(a)

# a = 5
# a += 1
# a += 1
# print(a)

# a = 55
# a -= 1
# a -= 1
# a = a - 1
# print(a)

# a = 100
# a *= 2
# print(a)

# a = 50
# a /= 2
# print(a)


"""
Çoklu Yorum Satır

        Author : Selçuk Akarın

        Version : 1.16

        Notes : 
                - Bu kod dosyası 1000 satırdan oluşur. Pdf dosylarını convert etmeye yarar
"""