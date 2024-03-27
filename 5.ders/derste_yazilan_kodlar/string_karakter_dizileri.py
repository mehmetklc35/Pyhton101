# Karakter Dizileri (Stringler)
# Tekrardan Hoşgeldiniz ! Bu konuda stringleri öğrenmeye 
# çalışacağız.Pythonda bir veri tipi olan Stringler veya 
# Türkçe ismiyle karakter dizileri gerçek hayatta kullandığımız 
# yazıların aynısıdır.Bu veri tipi aslında her biri bir karakter 
# olan bir dizidir. Örnek olarak, "ali" stringi sırasıyla a,l,i 
# harflerinden veya karakterlerden oluşmaktadır. Bu konuda stringleri 
# ve stringlerin özelliklerini görmeye çalışacağız.

# String Oluşturma
# Python'da string oluşturmanın birçok yolu bulunmaktadir.
# Bunların hangisini kullanacağınız tamamıyla size bağlıdır.
# İsterseniz string oluşturma işlemlerini görmeye çalışalım.

# 'Nova Academy'

# "Nova Academy"

# """Nova Academy"""

# Burada dikkat etmemiz gereken nokta, eğer bir çift tırnak ile 
# oluşturacaksak, stringin oluşturulması bitirmeyi yine çift 
# tırnak ile yapmalıyız.

# 'Nova Academy"

# print('Nova Academy\'nin Dersi')

# print("Nova Academy'nin Dersi")

# print("""Nova Academy'nin Dersi""")

# Şimdi de bir tane string veri tipinde değişken oluşturalım. 
# Stringler de bir veri tipi oldukları 
# için bunlardan değişken oluşturup kullanabiliriz.

# cumle = "Ali ata bak."
# print(cumle)

# String Indeksleme ve Parçalama
# Stringler birer karakter dizileri oldukları için her bir karakterin 
# aslında string içinde bir yeri vardır. Örnek olarak "ali" 
# stringinde a,l ve i karakterlerinin yerleri indeks olarak 
# adlandırılır.Pythonda ve genellikle çoğu programlama dilinde 
# (Octave hariç) stringlerin indekslenmesi "0" dan başlamaktadır. 
# Şimdi isterseniz bir string içindeki karakterlere indeks yoluyla 
# nasıl ulaşacağımıza bakalım.

a = "Ali salkfjawskfgaslkfas sdasd"
# print(a[2])
# print(a[-2])

# Peki uzun bir string'in sadece belirli bir kısmını elde etmek 
# için ne yapacağız ? Bunun için indeksleri, : ve [] işaretini 
# kullanacağız. Formülümüz şu şekilde ;

# [başlama indeksi : bitiş indeksi : atlama değeri]

# İsterseniz örneklerimize bakalım.

x = "Python Programlama Dili"

# print(x[0:6:1])
# print(x[7:18:1])
# print(x[19:-1:1])
# print(x[19::1])
# print(x[::1])
# print(x[::3])

# String Özellikleri
# Bir string'in uzunluğunu nasıl buluruz ? Bunun için Python'da 
# len() fonksiyonu bulunmaktadır.
# print(len("Nova Academy"))


# Peki sizce bir string'in belli bir karakterini direkt olarak
# değiştirebilir miyiz ? Hemen bir deneme yapalım.

# a = "Novu Academy"
# print(a)
# a[3] = "a"
# print(a)

# Burada Python bu işleme izin vermedi. 
# Gördüğümüz gibi, bir string'in karakterlerini 
# direkt olarak değiştiremiyoruz.Çünkü stringler böyle bir işlemi desteklemiyor.

# Peki, Pythonda stringler toplanabiliyor mu ?
# Python'da bunu yapmak da mümkündür.

# x = "Python "
# y = "Programlama "
# z = "Dersi"
# a = x+y+z
# print(a)

# Bir string ile bir sayıyı da çarpabiliriz.

# print("Nova "*5)