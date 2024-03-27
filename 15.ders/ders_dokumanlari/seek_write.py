# seek() ve write() fonksiyonları

# with open("bilgiler.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("bilgiler.txt","r+",encoding="utf-8") as file:
#     file.seek(4) # 4. byte (karakter)
#     file.write("DENEME")

# with open("bilgiler.txt","a",encoding="utf-8") as file:
#     file.write("Selçuk Akarın\n")
# # a dosya kipiyle açılan bir dosyanın imleci direkt olarak dosyanın sonunda başlar.

# with open("bilgiler.txt","r",encoding="utf-8")as file:
#     print(file.read())

# with open("bilgiler.txt","r+",encoding="utf-8") as file:
#     icerik = file.read()
#     icerik = "Hülya Hanım\n"+icerik
#     file.seek(0)
#     file.write(icerik)

# with open("bilgiler.txt","r+", encoding="utf-8") as file:
#     print(file.readlines())

# with open("bilgiler.txt","r+", encoding="utf-8") as file:
#     liste = file.readlines()
#     liste.insert(6, "Ahmet\n")
#     file.seek(0)
#     for satir in liste:
#         file.write(satir)

# with open("bilgiler.txt","r+", encoding="utf-8") as file:
#     liste = file.readlines()
#     liste.insert(6, "Nevin\n")
#     file.seek(0)
#     file.writelines(liste)
