# append() metodu
# append metodu listenin en sonuna eleman eklememizi sağlar.

# liste = [1,2,3,4,5,6,7]
# print(liste)
# liste.append("34")
# print(liste)
# liste.append(35)
# print(liste)
# liste.append([1,2,3])
# print(liste)
# liste.append({"Key":1,"Key2":2})
# print(liste)

# extend() metodu
# extend() metodu bir listeye başka bir listenin elemanları eklememizi sağlar.

# liste1 = [1,2,3,4]
# liste2 = [5,6,7,8]
# liste1.extend(liste2)
# print(liste1)

# xlistesi = ["ali","veli"]
# xlistesi.extend(["zeynep","ayşe"])
# print(xlistesi)

# insert() metodu
# insert() metodu listenin belli bir indeksine bir eleman eklememizi sağlar.

# liste = [1,2,3,4,5,6]

# liste.insert(2,"selcuk")
# print(liste)

# pop() metodu
# pop() metodu içine hiçbir değer vermezsek listenin son elemanını 
# silerek ekrana basar. İçine belli bir indeks değeri verirsek o indeksi 
# siler ve ekrana basar.

# liste = [1,2,3,4,5]
# print(liste.pop())
# print(liste)

# liste = [1,2,3,4,5]
# print(liste.pop(2))
# print(liste)

# remove() metodu
# remove() metodu verdiğimiz değeri listeden çıkarmamızı sağlar.

# liste = [1,2,3,4,5]
# liste.remove(4)
# print(liste)

# liste = ["Python","Php","Java"]
# liste.remove("Python")
# print(liste)

# index() metodu
# index() metodu verilen bir değerin baştan başlayarak hangi indekste 
# olduğunu söyler. Değer listede yoksa hata döner. Eğer ekstra 
# index değeri belirtilirse, index metodu() değeri bu indeksten
# itibaren aramaya çalışır.

# liste = [1,2,3,4,3,3,5,6,7,8,9]

# print(liste.index(3))

# print(liste.index(3,3))

# print(liste.index("Python"))

# count() metodu
# count() metodu verilen bir değerin listede kaç defa geçtiğini sayar.

# liste = [1,2,3,4,3,3,3,3,3,5,6,7,8,9]

# print(liste.count(15))

# sort() metodu
# sort() metodu bir listenin elemanlarını sayıysa küçükten büyüğe , 
# string ise alfabetik olarak sıralar. Eğer özellikle içine 
# reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.

# liste = [22,-1,55,1,5,15]
# liste.sort()
# print(liste)

liste = ["Python","Php","Java","Dart","C"]
# liste.sort()
# print(liste)
liste.sort(reverse=True)
print(liste)
