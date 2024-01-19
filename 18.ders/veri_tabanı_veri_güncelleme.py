import sqlite3 #- Modülü dahil ediyoruz.
con = sqlite3.connect("kütüphane.db") # - kütüphane.db veritabanı oluşturduk
cursor = con.cursor()
def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitap(isim TEXT, yazar TEXT, yayinevi TEXT, sayfa_sayisi INT)")
    con.commit()
def veriEkle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitap VALUES (?, ?, ?, ?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def veriCekme():
    cursor.execute("SELECT * FROM kitap")
    data = cursor.fetchall()
    print("kitap tablosu bilgileri.......")
    for i in data:
        print(i)
veriCekme()

def veriGuncelleme(yayinevi):
    cursor.execute("UPDATE kitap SET yayinevi = ? WHERE yayinevi = ?",("Everest", yayinevi))
    con.commit()
# veriGuncelleme("ışık")
def veriSilme(yazar):
    cursor.execute("DELETE FROM kitap WHERE yazar = ?",(yazar,))
    con.commit()
veriSilme("Ahmet Ümit")
