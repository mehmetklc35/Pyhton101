# List Comprehension
# Bu konuda listeleri üretmek ve oluşturmak Pythonda çok pratik bir 
# yöntem olan "List Comprehension" konusunu öğreneceğiz. Biliyorsunuz 
# Pythonda birçok işimizi çok kısa kodlar halledebiliyoruz. 
# Ancak kodları daha da kısaltmak ve pratik yöntemler kullanmak 
# her zaman isteriz. Şimdi örneklerimizle list comprehension'ı 
# anlamaya çalışalım.

# liste = [1,2,3,4]
# liste.append(5)
# print(liste)

# liste = list()
# liste.append(1)
# liste.append(2)
# liste.append(3)
# print(liste)

# Acaba bu kodumuzu list comprehension ile daha kısa yazabilir miyiz ?

# liste1 = [1,2,3,4,5]

# liste2 = [i for i in range(10,60)]
# print(liste2)

# liste = [i*3 for i in range(0,10)]
# print(liste)

# liste = [(1,2),(3,4),(5,6)]
# # print(len(liste))
# # list comprehension
# # liste2 = [i+j for i,j in liste]
# liste2 = list()
# for i,j in liste:
#     liste2.append(i+j)
# print(liste2)

# liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4

# liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension

# print(liste2)

# s = "Python"

# liste = [i*3 for i in s]
# print(liste)

# for i in liste:
#     print(i)

# Peki iç içe listeleri tek bir liste haline list comprehension 
# ile nasıl getirebiliriz ? İlk önce normal yolumuzu görelim.

# liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# for i in liste:
#     print(i) ## Buradaki i değeri de aslında bir liste.

# liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# liste2 = list()
# for i in liste:
#     for x in i:
#         liste2.append(x)
# print(liste2)
    
# List Comprehension 
# 0 0 0
# 1 1 1
# 2 2 2
# matris = [[0,0,0],[1,1,1],[2,2,2]]

# liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# print(liste[0][0])
# liste2 = [x for i in liste for x in i] # Biraz karmaşık
# print(liste2)

# İşte bu kadar ! Eğer "List comprehension" kullanmak 
# istemezseniz, normal bir şekilde
# de listeleri oluşturabilirsiniz. Tamamen size kalmış.