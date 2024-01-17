isimler = ["kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","atatürk","Dikmen","Kaya","Polat"]

isim_soyisim_list = zip (isimler,soyisimler)

for i,j in isim_soyisim_list:
    print(f"isim soyisim: {i} {j}")