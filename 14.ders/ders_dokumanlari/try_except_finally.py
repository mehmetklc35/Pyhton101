# a = int("12sadas")

# try:
#     a = int("12sadas")
# except: # tüm hatalar için çalışır
#     print("bir hata yakalım...")

# try:
#     a = int("12sadas")
#     print("11111111")
# except: # tüm hatalar için çalışır
#     print("bir hata yakalım...")
#     print("22222")
# print("33333")

# a = int("asdas231231")

# print(2/0)

# try:
#     a = int(input("1. sayıyı giriniz: "))
#     b = int(input("2. sayıyı giriniz: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası")
# except ValueError:
#     # handle ettik.
#     print("ValueError hatası aldın. Girdiğin değerleri kontrol et.")



# try:
#     # eval('x === x')
#     print(c)
#     a = int(input("1. sayıyı giriniz: "))
#     b = int(input("2. sayıyı giriniz: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError, SyntaxError):
#     # handle ettik.
#     print("ValueError veya ZeroDivisionError ya da SyntaxError hatası aldın. Girdiğin değerleri kontrol et.")
# except Exception:
#     print("Herhangi bir hata oluştu.")

# try:
#     # eval('x === x')
#     # print(c)
#     a = int(input("1. sayıyı giriniz: "))
#     b = int(input("2. sayıyı giriniz: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError, SyntaxError):
#     # handle ettik.
#     print("ValueError veya ZeroDivisionError ya da SyntaxError hatası aldın. Girdiğin değerleri kontrol et.")
# except Exception:
#     print("Herhangi bir hata oluştu.")
# finally:
#     print("Her durumda çalışan finally bloğu çalıştı.")


# try:
#     # eval('x === x')
    
#     a = int(input("1. sayıyı giriniz: "))
#     b = int(input("2. sayıyı giriniz: "))
#     print(a/b)
#     while(True)
#         with("yazı.txt","w+"):
#             print(c)
#             if (x == y):
#                 break
# except (ValueError, ZeroDivisionError, SyntaxError):
#     # handle ettik.
#     print("ValueError veya ZeroDivisionError ya da SyntaxError hatası aldın. Girdiğin değerleri kontrol et.")
# finally:
#     dosya.close()
#     print("Her durumda çalışan finally bloğu çalıştı.")

# Verilen stringi ters çeviren bir fonksiyon yazalım.
# def terscevir(yazi):
#     if(type(yazi) != str):
#         raise ValueError("Lütfen doğru bir input giriniz. Girdiğiniz input string değil.")
#     else:
#         return yazi[::-1]

# try:
#     print(terscevir(55))
# except ValueError as error_yazisi:
#     print("Fonsiyonda bir hata oluştu")
#     print(error_yazisi)

# print(terscevir("novaAcademy"))
# print(terscevir(55))
    
# try:
#     print(terscevir(55))
# except ValueError:
#     print("Fonsiyonda bir hata oluştu")
    

liste = ["11","22a","33"]

try:
    for i in liste:
        print(int(i))
except:
    pass
