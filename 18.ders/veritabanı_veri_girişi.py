import sqlite3 #- Modülü dahil ediyoruz.
con = sqlite3.connect("kütüphane.db") # - kütüphane.db veritabanı oluşturduk
cursor = con.cursor()
def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitap(isim TEXT, yazar TEXT, yayinevi TEXT, sayfa_sayisi INT)")
    con.commit()
def veriEkle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitap VALUES (?, ?, ?, ?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
while True:
    islem = input("Yeni kitap için 1'e, çıkmak için q'ya basınız")
    if islem == "q":
        break
    isim = input("Lütfen kitap ismini giriniz: ")
    yazar = input("Lütfen yazar isimini giriniz: ")
    yayinevi = input("Lütfen yayinevi isimini giriniz: ")
    sayfa_sayisi = int(input("Lütfen sayfa_sayisinı giriniz: "))

    veriEkle(isim,yazar,yayinevi,sayfa_sayisi)
    print("kitabımız veritabanını başarıyla eklendi.")
#tabloOlustur()
con.close()

