
# try:
#     file = open("bilgiler.txt","r",encoding="utf-8")
# except FileNotFoundError:
#     print("Dosya Bulunamadı....")


# file = open("bilgiler.txt","r",encoding="utf-8")
# for i in file:
#     print(i, end="")
# file.close()

# file = open("bilgiler.txt","r",encoding="utf-8")
# icerik = file.read()
# print("Dosya içeriği:\n",icerik,sep="")
# file.close()

# file = open("bilgiler.txt","r",encoding="utf-8")
# icerik = file.read()
# print("1. Okuma : Dosya İçeriği:\n",icerik,sep="")
# icerik2 = file.read()
# print("2. Okuma : Dosya İçeriği\n",icerik2,sep="")
# file.close()

# readline() fonksiyonu

# file = open("bilgiler.txt","r",encoding="utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# file.close()

# readlines() fonksiyonu

# file = open("test.docx","r",encoding="utf-8")
# print(file.readlines())
# print("******")
# print(file.readlines())
# file.close()

# import pandas as pd
# dataframe1 = pd.read_excel('test.xlsx')
# print(dataframe1)

# import docx

# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)
# def yazi_ekle(filename):
#     doc = docx.Document(filename)
#     doc.add_paragraph('Lorem ipsum dolor sit amet.')
#     doc.save(filename)
# print(getText("test.docx"))
# yazi_ekle("test.docx")
# print("******")

# print(getText("test.docx"))