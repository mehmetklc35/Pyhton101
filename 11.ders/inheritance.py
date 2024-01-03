class Calısan():
    def __init__(self,isim,maas,departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
        
    def bilgileriGöster(self): 
        print(calısan1.isim)
        print("""
            Çalışan bilgileri:
            
            İsim : {}
            
            Maaş : {}
            
            Departman : {}          
              
             """.format(self.isim, self.maas, self.departman))
        
    def departmanDegistir(self,yeni_departman): 
        print("departman değişiyor")
        self.departman = yeni_departman
        
calısan1 = Calısan("mehmet",80000,"yazılım")

calısan1.bilgileriGöster()

calısan1.departmanDegistir("IT")

calısan1.bilgileriGöster()


class Yonetici(Calısan):    
    pass

class isci(Calısan): 
    pass

yonetici1 = Yonetici("Steve",40000,"Ceo")

print(yonetici1.maas)

yonetici1.bilgileriGöster() 
print("*******")
print(dir(yonetici1))

isci1 = isci("Mark Zuckerberg",40000,"Yazılım")

isci1.bilgileriGöster() 







        
           