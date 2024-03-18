# Os modulu işletim sisteminde işlemler gerçekleştirebildiğimiz 
# standart bir pyhton modülüdür.


import os 
print(dir(os))

#getcwd() fonksiyonu bulunduğumuz dizinin yolunu söyler.

print(os.getcwd())

#chdir() fonksiyonu bulunduğumuz dizini değiştirmemezi sağlar

os.chdir("C:/Users")
print(os.getcwd())

# listdir()fonksiyonu bulunduğumuz dizinde klasörleri ve dosyaları listeler.

os.chdir("C:/Users")
print(os.listdir())

# mkdir() klasör oluşturmamazı sağlar

os.mkdir("deneme1")

# makedirs() fonksiyonu iç içe klasör oluşturmamazı sağlar.

os.makedirs("Deneme2/Deneme3/Deneme1")

# rmdir() fonksiyonu klasör silmemezi sağlar

os.rmdir("Deneme2")

# removedirs() fonksiyonu iç içe klasörleri selmemizi sağlar

os.removedirs("Deneme3/Deneme2")

# rename() fonksiyonu dosya veya klasörlerin ismini değiştirmemizi sağlar

os.rename("test.txt","nova.txt")

# stat() fonksiyonu bir dosyanın değiştirilme zamanı, büyüklüğü gibi özellikleri
# görmemizi sağlar.

print(os.stat("Akademi.txt"))

# walk () fonksiyonu içine bir tane dizin veya klasör verdiğimizde 
# bunun altındaki tüm dizinleri, dosyaları sıralar ve alt dizinlere 
# gidilecek bir yer kalmayana kadar gider.

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users"):
    print("Şu anki dizin:", klasor_yolu)
    print("klasörler:",klasor_isimleri)
    print("Dosyalar:",dosya_isimleri)
    print("*******************************")


