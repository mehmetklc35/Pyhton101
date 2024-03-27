# Veri tipi Dönüşümleri - unboxing boxing işlemleri.
# Pythonda ve diğer çoğu programlama dilinde veritiplerinin birbirine 
# dönüştürülmesi oldukça önemlidir. Bazı zaman bir ondalıklı sayıyı 
# tamsayıya dönüştürme, hatta ve hatta bir string'i tamsayıya dönüştürme 
# işlemleri programlarımızı yazarken büyük önem taşır. 
# Bu konuda bu tür dönüşümlerini öğrenmeye çalışacağız.

# Tamsayıyı Ondalıklı Sayıya Çevirme
# Bir tamsayı değeri(integer) ondalıklı sayıya(float) çevirmek için float() 
# fonksiyonunu kullanabiliriz.Örneklere bakalım.

# a = 50
# print(a)
# print(type(a))

# float_a = float(a)
# print(float_a)
# print(type(float_a))

# float_a = float("13asd")
# print(float_a)
# print(type(float_a))

# print(float(-1))

# print(float(9))

# Ondalıklı Sayıyı Tamsayıya Çevirme
# Bir ondalıklı sayıyı tamsayıya çevirmek için int() fonksiyonunu kullanabiliriz.
# Sonuç, ondalıklı sayının tam kısmı olarak karşımıza çıkacak.Örneklere bakalım.

# print(int(10.2))

# print(int(99.34))

# a = 5
# b = 2
# print(a/b)
# print(int(a/b))

# Sayıları Stringlere Çevirme
# Bir sayıyı string'e çevirmek için str() fonksiyonunu kullanabiliriz.
# Sayıyı oluşturan tüm rakamlar veya noktalar birer karaktere dönüşecek.

# a = 25955
# print(type(a))
# b = str(a)
# print(b)
# print(type(b))

# print(len(b))

# x = 34.776688
# y = str(x)
# print(y)
# print(type(y))
# print(len(y))


# Stringleri Tamsayıya Çevirme
# Bir string'i bir tamsayıya çevirmek istediğimiz zaman int() fonksiyonunu 
# kullanabiliriz. Ancak biraz dikkatli olmamızda fayda var. 
# Dönüştürme işlemini yaparken stringin her bir karakterinin bir
# rakam olduğundan emin olmalıyız. Örneklere bakalım.

# yazi = "1ikiüç"
# sayi = int(yazi)
# print(sayi)

# yazi = "123"
# sayi = int(yazi)
# print(sayi)
# print(type(sayi))
# sayi += 1
# print(sayi)

# Stringleri Ondalıklı Sayıya Çevirme
# Bir string'i bir ondalıklı sayıya çevirmek istediğimiz zaman float() 
# fonksiyonunu kullanabiliriz. Ancak biraz dikkatli olmamızda fayda var.
# Dönüştürme işlemini yaparken stringin ondalıklı sayı formatına uygun 
# olduğundan emin olmalıyız. Örneklere bakalım.

# yazi = "89.11"
# sayi = float(yazi)
# print(sayi)
# print(type(sayi))
# sayi += 1.1
# print(sayi)

# yazi = "89.11.12312"
# sayi = float(yazi)
# print(sayi)
# print(type(sayi))
# sayi += 1.1
# print(sayi)