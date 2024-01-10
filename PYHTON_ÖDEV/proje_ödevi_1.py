import time
import random

class Kumanda():

    def __init__(self,tv_durum = "Kapali", tv_ses = 0, kanal_listesi=["Fox"], kanal = "Fox", tv_radio_gecis = "tv"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.gecis = tv_radio_gecis
    
    def tvAc(self):
        if self.tv_durum == "Açık":
            print("Tv'niz zaten açık....")
        else:
            print("Tv açılıyor....")
            self.tv_durum = "Açık"

    def tvKapat(self):
        if self.tv_durum == "Kapalı":
            print("Tv zaten kapalı.....")
        else:
            print("Tv kapatılıyor....")
            self.tv_durum = "Kapalı"

    def sesAyarlari(self):
        while(True):
            isaret = input("Sesi Azaltmak için - tuşuna basınız \nSesi arttırmak için + ya basınız \nÇıkış için q'ya basınız:\n")
            if (isaret == "-" and self.tv_ses > 0):
                self.tv_ses -= 1
                print("Ses: ",self.tv_ses)
            elif (isaret == "+" and self.tv_ses < 10):
                self.tv_ses += 1
                print("Ses: ",self.tv_ses)
            elif (isaret == "q"):
                print("Ses güncellendi: ",self.tv_ses)
                break
    
    def kanalEkle(self,yeniKanal):
        print("Kanal ekleniyor......")
        time.sleep(1)
        self.kanal_listesi.append(yeniKanal)
        print("Kanal eklendi.....")

    def rastgeleKanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal: ",self.kanal)
    
    def tv_radio_gecis(self):
        if self.gecis == "Tv":
            print("Zaten Tv modundasınız...")
            time.sleep(1)
        else:
            print("Radio kanalları açılıyor...")
            self.gecis = "Radio kanalları açıldı"
            
        while(True):
            isaret = input("Tv'ye geçmek için w tuşuna basınız \nRadio için p'ye basınız:\n")
            if (isaret == "w"):
                self.gecis = "tv"
                print("Tv'ye geçiliyor....")
                time.sleep(1)
                print("Tv: ",self.gecis)                
            elif (isaret == "p"):
                self.gecis = "radio"
                print("radio'ya geçiliyor...")
                time.sleep(1)
                print("radio: ",self.gecis)                
                break
        

        
                

kumanda1 = Kumanda("Açık",7,["Trt","Fox","Atv","Show","Cine5"],"Cine5")

print("tv durum: ",kumanda1.tv_durum)
print("tv ses: ",kumanda1.tv_ses)
print("tv kanal listesi: ",kumanda1.kanal_listesi)
print("tv seçili kanal: ",kumanda1.kanal)
print("tvradiogecis: ",kumanda1.tv_radio_gecis)

# kumanda1.tvAc()
# print("tv durum: ",kumanda1.tv_durum)
# kumanda1.tvKapat()
# print("tv durum: ",kumanda1.tv_durum)
# kumanda1.sesAyarlari()
kumanda1.kanalEkle("CNBC-e")
kumanda1.kanalEkle("tv8")
kumanda1.kanalEkle("s-sport")
print(kumanda1.kanal_listesi)
kumanda1.rastgeleKanal()
kumanda1.tv_radio_gecis()
