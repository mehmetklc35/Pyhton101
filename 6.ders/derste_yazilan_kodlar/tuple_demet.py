# Demetler (Tuplelar)
# Demetler veya İngilizce ismiyle tuplelar listelere oldukça benzer 
# ancak farkları demetlerin değiştirilemez (immutable) oluşudur. 
# Bu yüzden programlarımızda 
# değiştirilmesini istemediğimiz değerleri bir demet içinde depolayabiliriz. 
# İsterseniz konumuza demetlerin oluşturulmasıyla başlayalım.

# Demet Oluşturma
# db_connection = ('163.0.2.32','8000','admin','password123')

# print(type(db_connection))

# Peki tek elemanlı bir demet nasıl tanımlanır ?

# meyveler = ('elma',)
# print(type(meyveler))

# sebzeler = ("soğan","sarımsak", "havuç")

# print(sebzeler[2])

# print(sebzeler[-1])

# print(sebzeler[1:])

# Demetlerin Temel Metodları
# index metoduyla içine verdiğimiz elemanın hangi indekste olduğunu bulabilir

# sebzeler = ("soğan","sarımsak", "havuç", "soğan")

# print(sebzeler.index("havuç"))

# print(sebzeler.index("havuç2"))

# print(sebzeler.index("soğan"))

# count metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.

# sebzeler = ("soğan","sarımsak", "havuç", "soğan", "soğan", "soğan")

# print(sebzeler.count("soğan"))

# print(sebzeler.count("soğan"))

# Değiştirilmeme Özelliği - immutable
# Demetlerin değiştirilemez olduğunu artık biliyoruz. İsterseniz bir deneme yapalım.

# Demet oluşturalım.

# demet = ("Elma","Armut","Muz")
# # demet[0] = "Kiraz"
# demet.remove("Elma")

# Demetleri Ne Zaman Kullanalım ?
# Aslında Python programcıları demetlerden ziyade listeleri daha çok kullanır. 
# Ancak eğer programınızda değiştirilmesini istemediğiniz bilgiler varsa
# (Android uygulama sabitleri gibi) bunları demet içinde depolayabilirsiniz. 
# Aynı zamanda, Read Only(Sadece Okuma) bir veritipi olduğu için listelere göre 
# biraz daha hızlı çalışırlar.