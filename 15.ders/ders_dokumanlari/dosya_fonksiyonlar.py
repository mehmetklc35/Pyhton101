# with context manager'ı

# with open("bilgiler.txt","r",encoding="utf-8") as file:
#     for i in file:
#         print(i, end="")

 # seek(), tell() fonsiyonları
# with open("bilgiler.txt","r",encoding="utf-8") as file:
#     print(file.tell())

# with open("bilgiler.txt","r",encoding="utf-8") as file:
#     file.seek(10)
#     print(file.tell())

with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(4)
    icerik = file.read(4)
    print(icerik)
    print(file.tell())
    file.seek(0)
    print(file.tell())
    icerik = file.read()
    print(icerik)
    print(file.tell())