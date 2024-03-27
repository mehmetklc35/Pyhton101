# Listeler (mutable)
# Şimdi de yeni bir veritipimiz olan listeleri öğrenmeye çalışalım. 
# Listeler yapıları gereği stringlere oldukça benzerler ve 
# kullanıldıkları yerler de çok yararlı olan bir veritipidir. 
# Tıpkı stringler gibi ,indekslenirler,parçalanırlar ve üzerinde 
# değişik işlemler yapabildiğimiz metodlar bulunur. 
# Ancak listelerin stringlerden önemli farkları da bulunmaktadır. 
# Stringler konusundan bildiğimiz kadarıyla stringler değiştirilemez (immutable)
# bir veri tipidir. Ancak, listelerimiz değiştirilebilir bir veritipidir.

# Bir listede her veritipinden elemanı saklayabiliriz. 
# Bu anlamda sıralı bir diziye benzer. Peki bu konuda ne öğreneceğiz?

# 1.Liste oluşturma
# 2.Indeksleme ve Parçalama
# 3.Temel Liste Metodları ve İşlemleri
# 4.İç içe Listeler  

# Liste Oluşturma
# Listeler bir *[]* köşeli parantez içine veriler 
# veya değerler konarak oluşturulabilir.

# liste1 = [1,2,3,4,5]
# print(liste1)
# print(type(liste1))

# liste2 = [1,"Selcuk",True,2.3242,[1,2,3,4]]
# print(liste2)

# liste = []
# print(liste)

# liste = list()
# print(liste)

# liste = [1,23,4,5,6,7,8,0,0,0,0,0,22,23,2]
# print(len(liste))

# Bir string list() fonksiyonu yardımıyla listeye dönüştürülebilir.
# s = "Merhaba"
# lst = list(s)
# print(lst)

# Listeleri Indeksleme ve Parçalama
# Listeleri indeksleme ve parçalama stringlerle birebir olarak aynıdır.

# liste =[1,2,3,4,5,6,7,8,9]
# print(liste)

# print(liste[0])
# print(liste[8])
# print(liste[-1])
# print(liste[len(liste)-1])
# print(liste[-len(liste)])
# print(liste[:4])
# print(liste[2:4])
# print(liste[5:])
# print(liste[::2])
# print(liste[::-1])

# Temel Liste Metodları ve İşlemleri
# Bu kısımda da listelerde yapabileceğimiz temel işlemleri ve 
# bazı temel metodları öğreneceğiz. Listelerin daha bir çok 
# metodunu kursun ileriki kısımlarında görüyor olacağız.

# Bir listeyi birbirine toplama işlemini stringlerdeki gibi yapabiliriz.

# liste1 = [0,1,2,3]
# liste2 = [4,5,6,7]
# print(liste1+liste2)

# Bir listeye bir tane eleman eklemek içinse aşağıdaki işlemi uygulayabiliriz.

# liste1 = [0,1,2,3]
# liste1 = liste1+["Nova"]
# print(liste1)

# # Hata!
# # string = "Novu"
# # string[-1] = "a"
# # print(string)

# liste1[0] = "Nova Academy"
# print(liste1)

# # print(liste1[-2:])
# liste1[-2:] = [8,9]
# print(liste1)

# Bir listeyi bir tamsayıyla da çarpabiliriz.

# liste1 = [1,2,3]
# liste1 = liste1*5
# print(liste1)


# string = "nova"
# print(string*5)

# Şimdi de isterseniz temel bazı liste metodlarına bakalım. 
# Listeler, diğer programlama dillerindeki arraylere göre oldukça esnektir. 
# Belli bir boyutları yoktur ve ekleme, çıkarma yapmak oldukça kolaydır.

# append metodu
# append metodu, verdiğimiz değeri listeye eklememizi sağlar.

# liste1 = [1,2,3]
# liste1.append(4)
# print(liste1)
# liste1.append(5)
# print(liste1)
# liste1.append("Okyanus")
# print(liste1)

# pop metodu
# Bu metod, içine değer vermezsek listenin son indeksindeki elemanı,
# değer verirsek verdiğimiz değere karşılık gelen indeksteki elemanı 
# listeden atar ve attığı elemanı ekrana basar.

# liste1 = ["Hülya","Mehmet","Ahmet","Sude"]
# print(liste1.pop())
# print(liste1)
# print(liste1.pop())
# print(liste1)
# print(liste1)
# liste1.pop(0)
# print(liste1)

# Aslında zamanı gelmişken söylemekte fayda var. Liste elemanlarına ulaşırken 
# eğer olmayan bir indeksi verirsek Python bizlere hata verecektir.

# print(liste1[10])

# sort metodu
# sort metodu listenin elemanlarını sıralamamızı sağlar. 
# Hemen kullanımına bakalım.

# liste1 = ["Hülya","aehmet","Ahmet","Sude"]
# liste1.sort()
# print(liste1)

# liste2 = [5,2,4,1,7,9,2,2,1]
# liste2.sort()
# print(liste2)

# liste2 = [5,2,4,1,7,9,2,2,1]
# liste2.sort(reverse=True)
# print(liste2)

# İç içe Listeler
# Bir listenin içinde başka bir liste bulundurmak mümkündür. 
# Bunlara Pythonda içiçe listeler denmektedir. 
# Bu tip bir özellik, Pythonda ağaç yapılarında veya 
# matris yapılarında oldukça kullanışlı olmaktadır

# 3 Tane liste oluşturalım.

# liste1 = [1,2,3]
# liste2 = [4,5,6]
# liste3 = [7,8,9]

# yeniliste = [liste1,liste2,liste3]
# yeniliste

# print(yeniliste[1][1])

