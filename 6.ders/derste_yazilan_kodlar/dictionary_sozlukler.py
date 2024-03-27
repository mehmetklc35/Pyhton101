# Sözlükler
# Sözlükler veya İngilizce ismiyle dictionaryler aynı gerçek hayattaki 
# sözlükler gibi davranan bir veritipidir. Bu veritipi, şimdiye kadar 
# gördüğümüz tüm veritiplerinden yapısı gereği farklıdır. Sözlüğün 
# içindeki her bir eleman indeks ile değil, anahtar (key), değer (value) 
# olarak tutulur. Bu anlamda gerçek hayattaki sözlüklere oldukça benzerler.
# Örneğin, elimize bir ingilizce-Türkçe sözlük alıp freedom 
# kelimesini(key ya da anahtar) aradığımız zaman karşılık değer 
# özgürlük (değer ya da value) olarak karşımıza çıkar. 
# Sözlükleri de bu şekilde düşünebiliriz.

# Şimdi isterseniz bir sözlük oluşturarak konumuza başlayalım.

# sozluk = {"freedom":"freedom'ın açıklaması","paint":"paintin açıklaması"}
# print(sozluk)

# bos sozluk tanımı
# sozluk = {}
# print(sozluk)

# sozluk = dict()
# print(sozluk)
# print(type(sozluk))

# Sözlük Değerlerine Erişmek ve Sözlüğe Değer Eklemek
# Sözlük veritipinin gerçek hayattaki sözlüklere çok benzediğini söylemiştik. 
# Öyleyse, bir değeri (value) 
# elde etmek için, indeksleri değil anahtarları (key) kullanacağız.

# ogretmenler = {"selcuk":"05555555","osman":"0333333","gülçin":"022222"}

# print(ogretmenler["gülçin"])
# print(ogretmenler["selcuk"])

# meyveler = ["kivi","mandalina","armut"]
# print(meyveler[2])

# mutable
# a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
# # print(a["iki"][1][0])

# print(a["üç"])
# a["üç"] += 5
# print(a["üç"])

# Bir sözlüğe dinamik olarak da eleman ekleyebiliriz.
# arabalar = {"1":"audi","2":"mercedes","3":"volvo"}

# print(arabalar)
# arabalar["4"] = "mazda"
# print(arabalar)
# arabalar["3"] = "toyota"
# print(arabalar)

# İç içe Sözlükler
# Tıpkı listeler gibi, iç içe sözlükler de oluşturulabilir.

# benim_sozlugum = {
#     "sayılar":{"1":"bir","2":"iki","3":"üç"}, 
#     "harfler":{"a":"a harfi","b":"b harfi"}
#     }

# # print(benim_sozlugum)

# print(benim_sozlugum["harfler"]["b"])

# Temel Sözlük Metodları

yeni_sözlük = {"bir":1,"iki":2,"üç":3}

# print(yeni_sözlük.values())
# print(type(yeni_sözlük.values()))

# print(yeni_sözlük.keys())

print(yeni_sözlük.items())

# for i in yeni_sözlük:
#     print(f"{i} keyine karşılık gelen value değeri = {yeni_sözlük[i]} ")


# for i,j in yeni_sözlük.items():
#     print(f"{i} keyine karşılık gelen value değeri = {j} ")

# Bu konuda sözlüklerin yapısını biraz anladıysak iyi yol katetmişiz demektir.