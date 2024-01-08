# import time
# import random

# class Kumanda():
    
#     def __init__(self, tv_durum = "Kapali", tv_ses = 0, kanal_listesi=["Fox"], kanal = "Fox"):
#         self.tv_durum = tv_durum
#         self.tv_ses = tv_ses
#         self.kanal_listesi = kanal_listesi
#         self.kanal = kanal
    
#     def tvAc(self):
#         if tv_durum == "Kapalı"
#             print("Tv'niz zaten açık.....")
#         else:
#             print("Tv Açılıyor...")
#             self.tv_durum = "Açık"
    
#     def tvKapat(self):
#         if self.tv_durum == "Kapalı"
#             print("Tv'niz zaten kapalı..")
#         else:
#             print("Tv Kapalıyor...")
#             self.tv_durum = "Kapalı"
        
#     def sesAyarlari(self):
#         while(True):
#             isaret = input("Sesi Azaltmak için - tuşuna basınız \nSesi Arttırmak için + ya basınız \nçıkış için q ya basınız")
#             if (isaret == "-" and tv_ses > 0):
#                 self.tv_ses -= 1
    
#     def kanalEkle(self,yeniKanal):
#         print("Kanal Ekleniyor...")
#         time.sleep(1)
#         self.kanal_listesi.append(yeniKanal)
#         print("Kanal Eklendi...")
    
#     def rastgeleKanal(self):
#         rastgele = random.randint(0,len(self.kanal_listesi)-1)
#         self.kanal = self.kanal_listesi[rastgele]
#         print("Şu anki kanal: ", self.kanal)
              
        
    
            
                  
    
# kumanda1 = Kumanda("Kapalı",7,["Trt","Fox","Ftv","Show","Cine5"],"Cine5"):

# print("tv durum: ", kumanda1.tv_durum)
# print("tv ses: ", kumanda1.tv_ses)
# print("tv kanal listesi: ", kumanda1.kanal_listesi)
# print("tv secili kanal: ", kumanda1.kanal)


# # kumanda1.tvAc()
# # print("tv durum: ", kumanda1.tv_durum)




# kumanda1.kanalEkle("CNBC")
# print("kumanda1.kanal_listesi")
    
