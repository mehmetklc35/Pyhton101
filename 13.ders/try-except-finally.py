# # # a = int("12sadas")

# # try:
# #     a = int("12sadas")
# # except: #tüm hatalar için çalışır
# #     print("bir hata yakaladım...")
    
  
# try:
#     a  = int(input("1.sayıyı giriniz:"))
#     b  = int(input("2.sayıyı giriniz:"))
#     print(a/b)
# except ZeroDivisionError: 
#     print("Sıfıra Bölme Hatası")
# except ValueError:
# #     print("ValueError hatası aldın. Girdiğin değerleri kontrol et.")

# finally:
#     print("Her durumda çalışan finally bloğu çalıştı.")
    
    
# Verilen stringi ters çeviren bir fonksiyon yazalım.add()

# def terscevir(yazi):
#     if(type(yazi) != str):
#         raise ValueError("Lütfen doğru bir input giriniz. Girdiğiniz input string değil")
#     else:
#         return yazi[::-1]
    
# print(terscevir("novaAcademy"))   
# print(terscevir(55))  

# # try:
# #     print(terscevir(55))
# # except ValueError:
# #     print("Fonksiyonda bir hata oluştu")

# try:
#     print(terscevir(55))
# except ValueError as error_yazisi:
#     print("Fonksiyonda bir hata oluştu")
#     print("error_yazisi")

# liste = ["11","22a","33"]

# try:
#     for i in liste:
#         print(int(i))
# except:
#     pass

    