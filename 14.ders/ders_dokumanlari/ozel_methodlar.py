# # ozel metodlar - magical methods - dunder methods
# class Kitap():
#     pass

# kitap1 = Kitap()
# print(dir(kitap1))

# print(kitap1)

# # print(len(kitap1))

# del kitap1

# print(kitap1)

class Kitap(object):
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("Kitap objesi oluşturuluyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    
    # override
    def __str__(self):
        return f"Kitap ismi : {self.isim},\n Kitabın Yazarı: {self.yazar},\n Kitabın sayfa sayısı: {self.sayfa_sayisi},\n Kitabın türü: {self.tur}"

    def __len__(self):
        return self.sayfa_sayisi
    
    # override
    def __del__(self):
        print("Kitap objesi siliniyor...")


kitap1 = Kitap("Beyoglu Beyefendisi","Ahmet Ümit",50,"Polisiye")
# print(len(kitap1))
print(kitap1.__dir__())
print(dir(kitap1))
# print(kitap1)
# del kitap1
# print(kitap1)
# print(kitap1)

# print("Kitabın sayfa sayısı: {}".format(len(kitap1)))