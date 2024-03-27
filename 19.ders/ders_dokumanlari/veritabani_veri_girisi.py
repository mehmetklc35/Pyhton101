import sqlite3
con = sqlite3.connect("kutuphane.db")
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
    yazar = input("Lütfen yazar ismini giriniz: ")
    yayinevi = input("Lütfen yayinevini giriniz: ")
    sayfa_sayisi = int(input("Lütfen sayfa sayısını giriniz: "))
    veriEkle(isim, yazar, yayinevi, sayfa_sayisi)
    print("kitabımız veritabanına başarıyla eklendi.")
# tabloOlustur()
con.close()