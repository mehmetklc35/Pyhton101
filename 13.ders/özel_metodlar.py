# # ozel metodlar - magical methods - dunder methods
# class Kitap(object):    
#     pass

# kitap1 = Kitap()
# print(dir(kitap1))

# print(kitap1)

# class Kitap(object):
#     def __init__(self,isim,yazar,sayfa_sayisi,tur):
#         print("Kitap objesi oluşturuluyor...")
#         self.isim = isim
#         self.yazar = yazar
#         self.sayfa_sayisi = sayfa_sayisi
#         self.tur = tur
    
#     def __str__(self):
#         return f"Kitap ismi : {self.isim}, Kitabın Yazarı:{self.yazar}, Kitabın sayfa sayısı:{self.sayfa_sayisi}, Kitabın turu:{self.tur}"
    
#     def __len__(self):
#         return self.sayfa_sayisi
    
#     def __del__(self):
#         print("Kitap objesi siliniyor...")
    
    
# kitap1 = Kitap("Beyoglu Beyfendisi","Ahmet Ümit",50,"Polisiye")
# # print(kitap1)
# # print(kitap1.__dir__())
# del kitap1
# print(kitap1)
# print(kitap1)
# print(len(kitap1))
# print("Kitabın sayfa sayisi: {}",format(len(kitap1)))




