# Proje 1
#  kalanları 
# "kalanlar.txt" dosyasında 
# ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.

# def notHesapla(satir):
#     # Hatice Günday,70,90,20
#     satir = satir[:-1]
#     liste = satir.split(",")
#     isim = liste[0]
#     not1 = int(liste[1])
#     not2 = int(liste[2])
#     not3 = int(liste[3])
#     toplam_not = not1 * (30/100) + not2 * (30/100) + not3 * (40/100)
#     if toplam_not >= 90:
#         harf = "AA"
#     elif toplam_not >= 85:
#         harf = "BA"
#     elif toplam_not >= 80:
#         harf = "BB"
#     elif toplam_not >= 75:
#         harf = "CB"
#     elif toplam_not >= 70:
#         harf = "CC"
#     elif toplam_not >= 65:
#         harf = "DC"
#     elif toplam_not >= 60:
#         harf = "DD"
#     elif toplam_not >= 55:
#         harf = "FD"
#     else:
#         harf = "FF"
#     return (isim + "-----------> " + harf + "\n",harf)

# # satir = "Selçuk Akyürek,90,80,60\n"
# # print(notHesapla(satir))

# with open("dosya.txt","r",encoding="utf-8") as dosya:
#     for i in dosya:
#         temp = notHesapla(i)
#         if temp[1] == "FF":
#             with open("kalanlar.txt","a",encoding="utf-8") as file2:
#                 file2.write(temp[0])
#         else:
#             with open("gecenler.txt","a",encoding="utf-8") as file1:
#                 file1.write(temp[0])
    
# Proje 2
# "futbolcular.txt" şeklinde bir dosya oluşturun 
# ve içine Galatasaray,Fenerbahçe ve Beşiktaşta 
# oynayan futbolcuları rastgele yerleştirin. 
# Bu dosyadan herbir takımın futbolcularını 
# ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 
# 3 farklı dosyaya yazın.

# "futbolcular.txt" dosyasının başlangıç hali şu 
# şekilde olsun.

#                 Fernando Muslera,Galatasaray
#                 Atiba Hutchinson,Beşiktaş
#                 Simon Kjaer,Fenerbahçe
#                            //
#                            //
#                            //
#                            //
#                            //

with open("futbolcular.txt","r",encoding="utf-8") as file1:
    for satir in file1:
        satir = satir[:-1]
        satir_elemanlari = satir.split(",")
        if satir_elemanlari[1] == "Fenerbahçe":
            with open("fb.txt","a",encoding="utf-8") as file2:
                file2.write(satir_elemanlari[0]+"\n")
        elif satir_elemanlari[1] == "Galatasaray":
            with open("gs.txt","a",encoding="utf-8") as file3:
                file3.write(satir_elemanlari[0]+"\n")
        else:
            with open("bjk.txt","a",encoding="utf-8") as file4:
                file4.write(satir_elemanlari[0]+"\n")
