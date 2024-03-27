# Döngülerde kullanılan ifadeler : break ve continue
# Bu videoda döngülerde kullanılabilen break ve continue ifadelerini 
# öğrenmeye çalışacağız. Bu ifadeleri kullanarak döngü 
# yapılarını daha efektif kullanabiliriz.

# break ifadesi
# break ifadesi döngülerde programcılar tarafından en çok 
# kullanılan ifadedir. Anlamı şu şekildedir;

# Döngü herhangi bir yerde ve herhangi bir zamanda 
# break ifadesiyle karşılaştığı zaman
# çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula 
# bağlı kalmadan sonlanmış olur.
# break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. 
# Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa 
# sadece içteki döngü sona erer. Örneklerle break ifadesini anlamaya çalışalım.

# i = 0

# while (i<20):
#     print(i)
#     if i == 10:
#         break
#     i += 1

# liste = [1,2,3,4,5,6,7,8]

# for i in liste:
#     if i == 6:
#         break
#     print(i)

# while True:
#     isim = input("İsminiz (çıkmak için q harfine basınız): ")
#     if isim == "q":
#         print("Çıkış yapılıyor...")
#         break
#     print(isim)

# İşte break ifadesi bu kadar ! Şimdi de continue ifadesine bakalım.

# continue ifadesi
# continue ifadesi break'e göre biraz daha az 
# kullanılan bir ifadedir. Anlamı şu şekildedir;

# Döngü herhangi bir yerde ve herhangi bir
# zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
# yapmadan direk bloğunun başına döner.
# continue ifadesini anlamak için örneklerimize bakalım.

# liste = [1,2,3,4,5,6,7,8,9]

# for i in liste:
#     print("i: ", i)

# for i in liste:
#     if i == 5 or i == 8:
#         continue
#     print(i)

# i = 0 # Bu kodda Sonsuz döngü olayı neden oluşur ? Bu kodu çalıştırmayalım.

# # Eğer çalıştırırsak sonsuz döngüyü "Kernel" sekmesinde 

# while (i < 10):
    
#     if (i == 2):
#         continue
        
#     print(i)
#     i += 1

# i = 0

# while(i<10):
#     if (i == 2):
#         i += 1
#         continue
#     print(i)
#     i +=1

# İşte break ve continue ifadeleri bu şekillerde kullanılmaktadır. 
# Kısım sonundaki alıştırmalarla bu konuyu daha iyi kavrayacağız.