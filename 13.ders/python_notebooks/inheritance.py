class Calisan():
    # Super Class - Base Class
    def __init__(self,isim,maas,departman):
        # properties - özellikler
        print("Çalışan sınıfının init metodu çalıştı")
        self.isim = isim
        self.maas = maas
        self.departman = departman
    
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileriGoster metodu çalıştı")
        print("""
                Çalışan bilgileri:
                
                İsim : {}
                
                Maaş : {}
                
                Departman : {}
            
              """.format(self.isim,self.maas,self.departman))
    
    def departmanDegistir(self,yeni_departman):
        print("Çalışan sınıfının departmanDegistir metodu çalıştı")
        print("departman değişiyor...")
        self.departman = yeni_departman

# calisan1 = Calisan("mehmet",80000,"yazılım")

# calisan1.bilgileriGoster()

# calisan1.departmanDegistir("IT")

# calisan1.bilgileriGoster()
        
class Yonetici(Calisan):
    
    def __init__(self,isim,maas,departman,sorumlu_oldugu_kisi_sayisi):
        pass

# class Isci(Calisan):
#     pass

# class ProjeYoneticisi(Calisan):
#     pass

# yonetici1 = Yonetici("Steve",40000,"Ceo")

# print(yonetici1.maas)

# yonetici1.bilgileriGoster()
# print("*****")
# print(dir(yonetici1))

# isci1 = Isci("Mark Zuckerberg", 40000, "Yazılım")

# isci1.bilgileriGoster()
# print("*****")
# print(dir(isci1))
# isci1.departmanDegistir("İnsan Kaynakları")
# isci1.bilgileriGoster()