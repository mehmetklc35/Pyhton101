

def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    toplam_not = not1 * (30/100) + not2 * (30/100) + not3 * (40/100)
    if toplam_not >= 90:
        harf = "AA"
    elif toplam_not >= 85:
        harf = "BA"
    elif toplam_not >= 80:
        harf = "BB"
    elif toplam_not >= 75:
        harf = "CB"
    elif toplam_not >= 70:
        harf = "CC"
    elif toplam_not >= 65:
        harf = "BC"
    elif toplam_not >= 60:
        harf = "DD"
    elif toplam_not >= 55:
        harf = "FD"
    else:
        harf = "FF"
    return (isim + "......... " + harf + "\n",harf)

#satir = "Hatice Günday,70,90,20\n"
#print(notHesapla(satir))

# Dosya Açma kodu ==

with open("dosya.txt", "r",endcoming="utf-8") as dosya:
    kalanlar = []
    gecenler = []
    for i in dosya:
        temp = notHesapla(i)
        if temp[1] == "FF":
            kalanlar.append(temp[0])
        else:
            gecenler.append(temp[0])
            
print(gecenler)
print("***************************")
print(kalanlar)

# gecenler ve kalanları farklı dosyalarda açcma metodu

with open("gecenler.txt", "w",encoding="utf-8") as file1:
    for i in gecenler:
        file1.write(i)

with open("gecenler.txt", "w",encoding="utf-8") as file2:
    for i in kalanlar:
        file2.write(i)