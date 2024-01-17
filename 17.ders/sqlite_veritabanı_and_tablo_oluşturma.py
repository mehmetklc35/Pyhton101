
import sqlite3 #- Modülü dahil ediyoruz.
con = sqlite3.connect("kütüphane.db") # - kütüphane.db veritabanı oluşturduk
cursor = con.cursor()
def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitap(isim TEXT, yazar TEXT, yayinevi TEXT, sayfa_sayisi INT)")
    con.commit()
tabloOlustur()
con.close()
