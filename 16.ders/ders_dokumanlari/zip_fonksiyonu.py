# liste1 = [1,2,3,4,5]
# liste2 = [6,7,8,9,10]

# sonucu = [(1,6),(2,7),(3,8),(4,9),(5,10)] 

# i = 0
# sonuc = list()
# while (i < len(liste1) and i < len(liste2)):
#     sonuc.append((liste1[i],liste2[i]))
#     i += 1
# print(sonuc)

# zip
# liste1 = [1,2,3,4,5]
# liste2 = [6,7,8,9,10]
# liste3 = [11,12,13,14,15]
# liste4 = [0,0,0,0]
# liste5 = ["Python","Php",".net","c#"]
# print(list(zip(liste1,liste2,liste3,liste4,liste5)))

# liste1 = [1,2,3,4]
# liste2 = ["Python","Java","C#","Php"]

# for i,j in zip(liste1,liste2):
#     print("index: ",i," Programlama Dili: ",j)

# zip vs dictionary

sozluk1 = {"Elma":1,"Armut":2,"Kiraz":3}
sozluk2 = {"Sıfır":0,"Bir":1,"İki":2}
# print(list(zip(sozluk1,sozluk2)))

print(list(zip(sozluk1.values(),sozluk2.values())))