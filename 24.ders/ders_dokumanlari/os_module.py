# Os Modülü
# Os modülü işletim sisteminde işlemler gerçekleştirebildiğimiz 
# standard bir Python modülüdür. Bu modül çok kapsamlı bir olduğu 
# için bu derste sadece temel fonksiyonlarını kullanmaya çalışacağız. 
# Burada daha sonra çalışmanız için fonksiyonlarımızın açıklaması bulabilirsiniz.

import os
# print(dir(os))

# getcwd() fonksiyonu
# Bu fonksiyon, bulunduğumuz dizinin yolunu söyler.
# print(os.getcwd())

# # chdir() fonksiyonu
# # Bu fonksiyon , bulunduğumuz dizini değiştirmemizi sağlar.

# os.chdir("C:/Users/selcuk/Desktop")
# print(os.getcwd())

# listdir() fonksiyonu
# Bu fonksiyon, bulunduğumuz dizinde klasörleri ve dosyaları listeler.
# os.chdir("C:/Users/selcuk/Desktop/PythonEgitim")
# print(os.listdir())

# mkdir() fonksiyonu
# Bu fonksiyon , "klasör" oluşturmamızı sağlar.
# os.mkdir("deneme1")

# makedirs() fonksiyonu
# Bu fonksiyon iç içe klasör oluşturmamızı sağlar.
# os.makedirs("Deneme3/Deneme2/Deneme1")

# rmdir() fonksiyonu
# Bu fonksiyon, klasör silmemizi sağlar.
# os.rmdir("Deneme2")

# removedirs() fonksiyonu
# Bu fonksiyon, iç içe klasörleri silmemizi sağlar.
# os.removedirs("Deneme3/Deneme2/Deneme0")

# rename() fonksiyonu
# Bu fonksiyon, dosya ve klasörlerin ismini değiştirmemizi sağlar.
# os.rename("nova.txt","AKADEMI.txt")

# stat() fonksiyonu - statistics
# Bu fonksiyon , bir dosyanın değiştirilme zamanı, büyüklüğü 
# gibi özellikleri veren bir stat objesi döner.
# print(os.stat("AKADEMI.txt"))

# walk() fonksiyonu
# Bu fonksiyon belki de os modülünün içindeki en yararlı fonksiyonlardan bir 
# tanesi. Bu fonksiyonumuz içine bir tane dizin (veya klasör) verdiğimizde 
# bunun altındaki tüm dizinleri , dosyaları sıralar ve alt dizinlere gidilecek 
# bir yer kalmayana kadar gider. os.walk() çıktısını görmek için for döngüsü 
# kullanmaya çalışalım.

# for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("C:/Users/selcuk/Desktop/PythonEgitim/24.ders/ders_dokumanlari/test"):
#     print("Şu anki dizin: ",klasor_yolu)
#     print("Klasörler: ",klasor_isimleri)
#     print("Dosyalar: ",dosya_isimleri)
#     print("**********************************")

# for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("C:/Users/selcuk/Desktop/PythonEgitim/24.ders/ders_dokumanlari/test"):
#     for i in klasor_isimleri:
#         if (i.startswith("kr")):
#             print(i)