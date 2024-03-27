# liste = ["Elma","Armut","Muz","Kiraz"]
# sonuc = list()
# # sonuc = [(0,"Elma"),(1,"Armut"),(2,"Muz"),(3,"Kiraz")]
# i = 0
# for a in liste:
#     sonuc.append((i,a))
#     i += 1
# print(sonuc)


# liste = ["Elma","Armut","Muz","Kiraz"]
# print(tuple(enumerate(liste)))

liste = ["a","b","c","d","e","f"]
print("tip: ",type(enumerate(liste)))
print("enumarate object: ",enumerate(liste))
print("list enumarate object: ",list(enumerate(liste)))
print("tuple enumarate object: ",tuple(enumerate(liste)))

# for index,eleman in enumerate(liste):
#     if index % 2 == 0:
#         print("eleman: ",eleman)
    
