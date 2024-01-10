import time

class Hayvanlar():
    def __init__(self,cinsi,yaş,renk,cinsiyet):
        self.cinsi=cinsi
        self.yaş=yaş
        self.renk=renk
        self.cinsiyet=cinsiyet
        
    def __str__(self):
        return "Cinsi: {}\nYaşı: {}\nRenk: {}\nCinsiyeti: {}\n".format(self.cinsi,self.yaş,self.renk,self.cinsiyet)

class Köpek(Hayvanlar):
    def __init__(self,cinsi,yaş,renk,cinsiyet,menşei,aile):
        super().__init__(cinsi,yaş,renk,cinsiyet)
        self.menşei=menşei
        self.aile=aile        
        
    def __str__(self):
        return "Cinsi: {}\nYaşı: {}\nRenk: {}\nCinsiyeti: {}\nmenşei: {}\naile: {}\n".format(self.cinsi,self.yaş,self.renk,self.cinsiyet,self.menşei,self.aile)

class Kuş(Hayvanlar):
    pass

class At(Hayvanlar):
    def __init__(self,cinsi,yaş,renk,cinsiyet,yasam_süresi,boy):
        super().__init__(cinsi,yaş,renk,cinsiyet)
        self.yasam_süresi=yasam_süresi
        self.boy=boy        
        
    def __str__(self):
        return "Cinsi: {}\nYaşı: {}\nRenk: {}\nCinsiyeti: {}\nYasam_süresi: {}\nBoy: {}\n".format(self.cinsi,self.yaş,self.renk,self.cinsiyet,self.yasam_süresi,self.boy)


köpek=Köpek("Golden",5,"sarı","erkek","England","Retriever")
kuş=Kuş("Kartal",1,"Siyah","erkek")
at=At("Arap",10,"gri","dişi",20,75)

print("""

1- KÖPEK

2-KUŞ

3-AT

çıkış için q' ya basınız.""")

seçim=input("Lütfen seçim yapınız: ")
while True:
    if(seçim == "q"):
        print("Programdan çıktınız.")
        break
    elif(seçim == "1"):
        print("Köpek Bilgileri",köpek)
        time.sleep(1)
        break
    elif (seçim == "2"):
        print("Kuş Bilgileri",kuş)
        time.sleep(1)
        break
    else:
        print("At Bilgileri",at)
        time.sleep(1)
        break
