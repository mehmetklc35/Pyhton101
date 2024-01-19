yazi = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

frekans = dict()

for karakter in yazi:
    if karakter in frekans:
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
        
"************************************"

isimler = ["kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","atatürk","Dikmen","Kaya","Polat"]

liste3 = list(zip(isimler,soyisimler))
print(liste3)
liste3.sort()
print(liste3)

