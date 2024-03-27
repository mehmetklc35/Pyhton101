import sqlite3
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()
def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitap(isim TEXT, yazar TEXT, yayinevi TEXT, sayfa_sayisi INT)")
    con.commit()
tabloOlustur()
con.close()