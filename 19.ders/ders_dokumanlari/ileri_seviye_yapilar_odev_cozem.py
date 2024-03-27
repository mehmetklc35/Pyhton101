# Problem 1

# Elinizde uzunca bir string olsun.

#             "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


# Bu string içindeki harflerin frekansını 
# (bir harfin kaç defa geçtiği) bulmaya çalışın.

# yazi = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

# # {
# #     "P":2,
# #     "r":5,
# #     "o":7
# # }

# frekans = {}
# for karakter in yazi:
#     # if karakter in frekans:
#     #     frekans[karakter] += 1
#     # else:
#     #     frekans[karakter] = 1
#     frekans[karakter] = yazi.count(karakter)
        
# for i,j in frekans.items():
#     print(i, " ", j)



# Problem 2

# "şiir.txt" şeklinde bir dosya oluşturun ve içinde 
# şu satırlar yer alsın.

# Memlekete sis çökmüş bir gece 
# Usulca yanağıma sen düşüyorsun
# Sabah saat dokuzu beş geçe
# Terk edip bizleri gidiyorsun
# Ayrılık bu kadar yakmamıştı içimizi
# Farkında mısın bilmiyorum
# Aldın beraberinde cumhuriyetimizi
# Korkunç bir veda, sararmıştı her yer
# Ellerini uzat tutmak istiyoruz
# Masmavi gözleri kaybetmiş çocuk
# Aldı bir sabah ruhumuzu
# Lakin nasıl bölmesin yokluğun uykumuzu

# Bu dosyanın herbir satırını okuyun. Satırların baş 
# harflerini birbirine ekleyerek bir string oluşturun 
# ve bu string'i ekrana yazdırın.

# bas_harfler = ""

# with open("siir.txt", "r",encoding="utf-8") as file:
#     for i in file:
#         bas_harfler += i[0]
# print(bas_harfler)



# Problem 3

# Elinizde "mailler.txt" adında , maillerin 
# ve bazı yazıların bulunduğu bir dosya olsun.
# Bu dosyanın her bir satırını okuyun ve sadece 
# mail formatına uygun olanları ekrana yazdırın.

# coskun.m.Deneme@gmail.com
# example@xyz.com
# Selçuk.com
# Selçuk@gmail
# kerim@yahoo.com

#                            //
#                            //
#                            //

# *İpucu: Stringlerde bulunan endswith ve 
# find metodlarını kullanabilirsiniz.*

# with open("mailler.txt","r",encoding="utf-8") as dosya:
#     # for mail in dosya:
#     #     mail = mail[:-1]
#     #     if mail.endswith(".com") and mail.find("@") != -1:
#     #         print(mail)
#     liste = dosya.readlines()
#     for i in liste:
#         if i != liste[len(liste)-1]:
#             i = i[:-1]
#         if i.endswith(".com") and i.find("@") != -1:
#             print(i)


# Problem 4

# Elinizde 2 tane liste bulunsun. Bu listelerden 
# isim ve soyisimleri birleştirerek , ekrana isim 
# ve soyisimleri *isimlere* göre sıralı bir şekilde 
# yazdırmaya çalışın.

# isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

# soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

# isim = ["Kerim","Tarık","Ezgi","Kemal","Alkay","Sükran","Merve"]
# soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

# liste3 = list(zip(isim,soyisim))
# # print(liste3)
# liste3.sort()
# print(liste3)
# for i,j in liste3:
#     print(i,j)
