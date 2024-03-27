# Iteratorların Oluşturulması ve Kullanılması
# Bu konuda iteratorları oluşturmayı, kullanmayı ve kendi objelerimizi iterable 
# (üzerinde gezinilebilecek) olarak nasıl yazarız öğrenmeye çalışacağız. 
# İlk olarak iteratorlar nedir anlamaya çalışalım

# Iteratorlar nedir?
# Iteratorlar aslında Pythonda çoğu yerde biz görmesek de kullanılır. Iteratorlar 
# özellikle for döngülerinde , list comprehensionlarında, ve bir sonraki derste 
# göreceğimiz generatorlarda karşımıza çıkar.

# Iteratorlar en genel anlamıyla üzerinde gezinilebilecek bir objedir ve bu obje 
# her seferinde bir tane eleman döner.

# Pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir.. 
# Örneğin, demetlerden,listelerden ve stringlerden oluşturduğumuz bütün objeler 
# iterable bir objedir.

# dunder methods - magical methods
# Bir iterator objesi oluşturabilmek için hazır metodlar olan __iter()__ ve __next()__ 
# metodlarını mutlaka tanımlaması gerekir.

# Iterator oluşturma
# Bir iterator objesini , iterable bir objeden (liste,demet,string vs) 
# oluşturmak için Pythonda iter() fonksiyonunu kullanıyoruz ve bu objenin 
# bir sonraki elemanını almak için next() fonksiyonu kullanıyoruz.
# liste = [1,2,3,4]
# # print(dir(liste))

# # print("iterator objesinin metodları")
# iterator = iter(liste)
# # print(dir(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)

# liste = [1,2,3,4,5]
# iterator = iter(liste)
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

# Kendi Iterable Objelerimizi Oluşturmak
# Peki biz kendi oluşturduğumuz veritiplerini nasıl iterable yapacağız ? 
# Bunun için oluşturacağımız sınıfların mutlaka __iter()__ ve __next()__ 
# metodlarını tanımlaması gereklidir. Şimdi bir tane kumanda sınıfı oluşturalım 
# ve bu sınıfı iterable yapalım.

class Kumanda:
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi  # kanal listemiz
        self.index = 0 # indeksimiz
    
    def __iter__(self):
        return self # iterator oluşturduğumuz (iter fonksiyonu çağrıldığında) objemizi döneceğiz.

    def __next__(self):
        self.index += 1
        if self.index <= len(self.kanal_listesi):
            return self.kanal_listesi[self.index-1]
        else:
            self.index = 0
            raise StopIteration

kumanda = Kumanda(["Tv8","Atv","Kanal D","Show","Star","Now"])
kumanda.index = 3
# print(next(k))

iterator = iter(kumanda) #Objemiz iterable olduğu için iterator oluşturabiliriz.
print(next(iterator))
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

