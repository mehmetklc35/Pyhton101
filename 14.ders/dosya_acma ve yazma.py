# w kipi

# open("bilgiler.txt","w")

# file = open("C:/Users/emin/Desktop/REPOS/Pyhton101/14.ders/dosya_acma ve yazma.py""bilgiler.txt","w")

# file = open("bilgiler.txt","w", encoding="utf-8")

# file.write("Nova Academy iğü 1111")

# file.close()

# a kipi - append

# file = open("bilgiler.txt","a",encoding="utf-8")

# file.write("Nova")

# file.close()

# try:
#     file = open("bilgiler.txt","r",encoding="utf-8")
# except FileNotFoundError:
#     print("File not found.....")

# file = open("bilgiler.txt","r",encoding="utf-8")
# for i in file:
#     print(i, end="")
# file.close()

# file = open("bilgiler.txt","r",encoding="utf-8")
# icerik = file.read()
# print("1. okuma : Dosya içeriği:\n",icerik,sep="")
# icerik2 = file.read()
# print("2. okuma : Dosya içeriği\n",icerik2,sep="")
# file.close()

# file = open("bilgiler.txt","r",encoding="utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")

# file = open("bilgiler.txt","r",encoding="utf-8")
# print(file.readlines(), end="")
# file.close()


# import docx 
# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)
# print(getText("test.docx"))