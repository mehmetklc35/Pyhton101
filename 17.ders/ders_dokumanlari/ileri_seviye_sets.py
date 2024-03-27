# İleri Seviye Kümeler (Sets)
# Bu konuda yeni bir veritipi olan kümeler veya ingilizce 
# adıyla setleri öğreneceğiz.

# Kümeler, matematikte olduğu gibi bir elemandan sadece bir 
# adet tutan bir veritipidir. Bu açıdan kullanıldıkları yerlerde 
# çok önemli bir veritipi olmaktadırlar. İsterseniz hemen bir 
# küme oluşturalım.

# kume = set()
# print(type(kume))

# liste = [1,1,1,2,2,2,3,3,3,4,4,4]
# x = set(liste)
# print(x)

# x = set("Python Programlama Dili")
# print(x)

# x = {"Python","Php","Python"}
# y = {"Bir":1,"İki":2}
# print(x)

# For döngüsüyle Gezinmek
# Kümeler de tıpkı sözlükler gibi sırasız bir veri 
# tipidir. Bunu *for* döngüsüyle görebiliriz.

# x = {"Python","C","Java","Php","Javascript"}
# # for i in x:
# #     print(i)
# # x[0]
# # x["Python"]
# liste = list(x)
# print(liste[1])

# Kümelerin Metodları
# Eleman Eklemek : add() metodu
# Kümeye eleman eklemimizi sağlar. Aynı eleman 
# eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz.
# kume = {1,2,3,4,5}
# print(kume)
# kume.add(6)
# print(kume)
# kume.add(1)
# print(kume)

# İki kümenin farkı : difference() metodu
# Bu metod birinci kümenin ikinci kümeden farkını döner.

# kume1 = {1,2,3,4,5}
# kume2 = {4,5,6,7,8,9}
# print(kume2.difference(kume1))

# İki kümenin farkı ve güncelleme : difference_update() metodu
# Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi 
# bu farka göre günceller.

# küme1.difference_update(küme2) # Küme1'in Küme2'den farkı

# kume1 = {1,2,3,4,5}
# kume2 = {4,5,6,7,8,9}
# print(kume1.difference(kume2))
# print("kume1: ",kume1)
# print("kume2: ",kume2)

# kume1 = {1,2,3,4,5}
# kume2 = {4,5,6,7,8,9}
# kume2.difference_update(kume1)
# print("kume1: ",kume1)
# print("kume2: ",kume2)
# print(kume2)
# print(type(kume2))
# liste = list(kume2)
# print(liste)
# print(type(liste))

# icerik = """
# ali ata bak, ayşe topu tut, bak ali bak 
# ali ata bak, ayşe topu tut, bak ali bak 
# ali ata bak, ayşe topu tut, bak ali bak 
# ali ata bak, ayşe topu tut, bak ali bak 
# ali ata bak, ayşe topu tut, bak ali bak 
# """
# icerik = [x.strip(",").strip("\n").strip(".") for x in icerik.split(' ')]
# kume = set(icerik)
# print(kume)

# Kümeden Eleman Çıkartmak : discard() metodu
# İçine verilen değeri kümeden çıkartır. Eğer 
# kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).

# kume = {1,2,3,4}
# kume.discard(2)
# print(kume)

# kume = {1,2,3,4}
# kume.discard(6)
# print(kume)

# Küme kesişimleri : intersection() metodu
# Bu metod iki kümenin kesişimleri bulmamızı sağlar.

# kume1 = {1,2,3,4,5,6,7,8,9}
# kume2 = {5,6,7,8,9,10,11}
# print(kume1.intersection(kume2))

# Küme kesişimleri ve güncelleme : intersection_update() metodu
# Bu metod birinci kümeyle ikinci kümenin kesişimlerini bulur 
# ve birinci kümeyi bu kesişime göre günceller.
# kume1 = {1,2,3,4,5,6,7,8,9}
# kume2 = {5,6,7,8,9,10,11}
# kume1.intersection_update(kume2)
# print(kume1)

# Kümeler ayrık küme mi ? : isdisjoint() metodu
# Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.

# kume1 = {1,2,3}
# kume2 = {3,4,5,6}
# print(kume1.isdisjoint(kume2))

# Alt kümesi mi ? : issubset() metodu
# Bu metod , birinci küme ikinci kümenin alt 
# kümesiyse True, değilse False döner.

# kume1 = {"Python","C","Php"}
# kume2 = {"C#","Java","Python","C","Php"}
# print(kume1.issubset(kume2))

# # Birleşim Kümesi : union() metodu
# # Bu metod, iki kümenin birleşim kümesini döner.

# kume1 = {1,2,3,4}
# kume2 = {5,6,7,8}
# print(kume1.union(kume2))
# print("kume1: ",kume1)
# print("kume2:",kume2)

# # Birleşim Kümesi ve update : update() metodu
# # Bu birinci kümeyle ikinci kümenin 
# # birleşim kümesini döner ve birinci kümeyi buna göre günceller.

# kume1 = {10,20,30}
# kume2 = {40,50,60}
# kume1.update(kume2)
# print("kume1: ",kume1)
# print("kume2:",kume2)

