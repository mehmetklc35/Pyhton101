import time
import random

class Kumanda():

    def __init__(self,tv_durum = "Kapali", tv_ses = 0, kanal_listesi=["Fox"], kanal = "Fox"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    
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
                

kumanda1 = Kumanda("Açık",7,["Trt","Fox","Atv","Show","Cine5"],"Cine5")

print("tv durum: ",kumanda1.tv_durum)
print("tv ses: ",kumanda1.tv_ses)
print("tv kanal listesi: ",kumanda1.kanal_listesi)
print("tv seçili kanal: ",kumanda1.kanal)

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
