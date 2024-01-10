class Bilgisayar:
    def __init__(self,marka,model,ram,depolama):
        self.marka = marka
        self.model = model
        self.ram = ram
        self.depolama = depolama
        
    def bilgileriGöster(self):
        print("Bilgisayar sınıfının bilgileriGoster metodu çalıştı")
        print("""
                Bilgisayar bilgileri:
                
                Marka : {}
                
                Model : {}
                
                Ram : {}
                
                Depolama : {}
            
              """.format(self.marka,self.model,self.ram,self.depolama))
        
    def depolamaDegistir(self,yeni_depolama):
        print("Bilgisayar sınıfının depolamaDegistir metodu çalıştı")
        print("Depolama alanı değişiyor...")
        self.depolama = yeni_depolama

    def uygulama_yukle(self, uygulama):
        print(uygulama, "uygulaması yüklendi.")

class Bilgisayar2:
    def __init__(self,marka,model,ram,depolama,ekran_boyutu):
        print("Bilgisayar2 sınıfının init metodu çalıştı")
        self.marka = marka
        self.model = model
        self.ram = ram
        self.depolama = depolama
        self.ekran_boyutu = ekran_boyutu
    
    def bilgileriGoster(self):
        print("Bilgisayar2 sınıfının bilgileriGoster metodu çalıştı")
        print("""
                Bilgisayar2 bilgileri:
                
                Marka : {}
                
                Model : {}
                
                Ram : {}
                
                Depolama : {}
              
                Ekran_boyutu : {}
            
              """.format(self.marka,self.model,self.ram,self.depolama,self.ekran_boyutu))
        
        


bilgisayar1 = Bilgisayar("Apple", "MacBook Pro", "8 GB", "256 GB SSD")
bilgisayar2 = Bilgisayar2("Apple", "MacBook Pro", "8 GB", "256 GB SSD", "100 px")
bilgisayar1.bilgileriGöster()
bilgisayar1.uygulama_yukle("Chrome")
bilgisayar1.depolamaDegistir("512 GB SSD")
bilgisayar1.bilgileriGöster()
bilgisayar2.bilgileriGoster()



        
        
        
        