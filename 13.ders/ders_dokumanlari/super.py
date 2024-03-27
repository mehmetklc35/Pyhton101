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

class Yonetici(Calisan):
    # Sub class - Alt sınıf
    # override - overriding
    def __init__(self,isim,maas,kisi_sayi,departman="Bilgi Yok"):
        print("Yonetici sınıfının init metodu çalıştı")
        super().__init__(isim,maas,departman)
        self.kisi_sayi = kisi_sayi
    
    # override - overriding
    def bilgileriGoster(self):
        print("Yönetici sınıfının bilgileriGoster metodu çalıştı")
        print("""
                Yöneticinin bilgileri:
                
                İsim : {}
                
                Maaş : {}
                
                Departman : {}
              
                Sorumlu old. kişi sayısı : {}
            
              """.format(self.isim,self.maas,self.departman,self.kisi_sayi))
    
    def zamYap(self,zam_miktari):
        print("Yönetici sınıfının zamYap metodu çalıştı...")
        self.maas += zam_miktari

class Isci(Calisan):
    pass
    
yonetici1 = Yonetici(isim="Steve Wozniak",maas=80000,kisi_sayi=15)
yonetici1.bilgileriGoster()
# yonetici1.departmanDegistir("Muhasebe")
# yonetici1.bilgileriGoster()
# yonetici1.zamYap(5000)
# yonetici1.bilgileriGoster()
# calisan1 = Calisan("Mehmet", 100000,"it")
# calisan1.bilgileriGoster()